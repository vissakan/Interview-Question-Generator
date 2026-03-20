import os
import uuid
import io
import json
import traceback
from flask import Flask, request, render_template, send_file, jsonify
from dotenv import load_dotenv

load_dotenv()

from utils.resume_parser import extract_text
from utils.prompt_builder import build_prompt
from utils.groq_client import generate_questions
from utils.formatter import format_output, format_output_json

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5MB limit
UPLOAD_FOLDER = 'outputs'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    try:
        # Get form fields
        job_role = request.form.get('job_role', '').strip()
        experience = request.form.get('experience', '').strip()
        job_description = request.form.get('job_description', '').strip()
        extra_notes = request.form.get('extra_notes', '').strip()
        resume_file = request.files.get('resume')

        if not job_role:
            return jsonify({'error': 'Job role is required.'}), 400
        if not resume_file or resume_file.filename == '':
            return jsonify({'error': 'Please upload a resume file.'}), 400

        # Validate API key is set
        if not os.environ.get("GROQ_API_KEY"):
            return jsonify({'error': 'GROQ_API_KEY is not set in your .env file.'}), 500

        # Extract resume text
        filename = resume_file.filename.lower()
        if not (filename.endswith('.pdf') or filename.endswith('.docx') or filename.endswith('.txt')):
            return jsonify({'error': 'Only PDF, DOCX, or TXT files are supported.'}), 400

        app.logger.info(f"Parsing resume: {filename}")
        resume_text = extract_text(resume_file, filename)
        if not resume_text or not resume_text.strip():
            return jsonify({'error': 'Could not extract text from the resume. Please try a different file.'}), 400

        app.logger.info(f"Resume extracted. Characters: {len(resume_text)}")

        # Build prompt and call Groq
        prompt = build_prompt(resume_text, job_role, experience, job_description, extra_notes)
        app.logger.info("Calling Groq API...")
        raw_output = generate_questions(prompt)
        app.logger.info("Groq API responded successfully.")
        # Get requested output format (default: txt)
        output_format = request.form.get('format', 'txt').strip().lower()
        unique_id = uuid.uuid4().hex[:8]

        if output_format == 'json':
            data = format_output_json(raw_output, job_role, experience)
            buffer = io.BytesIO()
            buffer.write(json.dumps(data, indent=2).encode('utf-8'))
            buffer.seek(0)
            output_filename = f"interview_questions_{unique_id}.json"
            return send_file(
                buffer,
                as_attachment=True,
                download_name=output_filename,
                mimetype='application/json'
            )

        # Default: existing .txt path — unchanged

        # Format output
        formatted = format_output(raw_output, job_role, experience)

        # Send as in-memory file — no disk permission issues
        buffer = io.BytesIO()
        buffer.write(formatted.encode('utf-8'))
        buffer.seek(0)

        output_filename = f"interview_questions_{uuid.uuid4().hex[:8]}.txt"
        return send_file(
            buffer,
            as_attachment=True,
            download_name=output_filename,
            mimetype='text/plain'
        )

    except Exception as e:
        # Print full traceback to terminal
        traceback.print_exc()
        return jsonify({'error': f'Error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True)
