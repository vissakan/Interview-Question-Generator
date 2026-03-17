# InterviewForge — AI Interview Question Generator

Generate 45 tailored interview questions from a resume and job role using Groq (Llama 3.3 70B). Questions are categorised by difficulty (Easy / Medium / Hard) and type (Technical / Behavioural / Situational), and exported as a `.txt` file.

---

## Setup

### 1. Clone / download the project

```bash
cd interview-gen
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your Groq API key

- Go to https://console.groq.com and sign up (free)
- Create an API key
- Open `.env` and replace the placeholder:

```
GROQ_API_KEY=your_actual_key_here
```

### 5. Run the app

```bash
python app.py
```

Open your browser at **http://localhost:5000**

---

## Project Structure

```
interview-gen/
├── app.py                  # Flask routes
├── utils/
│   ├── resume_parser.py    # PDF / DOCX / TXT text extraction
│   ├── prompt_builder.py   # Constructs the LLM prompt
│   ├── groq_client.py      # Groq API call (Llama 3.3 70B)
│   └── formatter.py        # Formats output into clean .txt
├── templates/
│   └── index.html          # Frontend UI
├── outputs/                # Temporary generated files
├── .env                    # API key (never commit this)
├── requirements.txt
└── .gitignore
```

---

## Output Format

```
================================================================================
                     INTERVIEW QUESTION BANK
================================================================================
  Job Role    : Backend Engineer
  Experience  : 2 year(s)
  Generated   : 2025-01-15 14:32:00
================================================================================

================================================================
  ▸ DIFFICULTY: EASY
================================================================

  ── TECHNICAL ──
  1. ...
  2. ...
  ...

  ── BEHAVIOURAL ──
  ...

  ── SITUATIONAL ──
  ...

================================================================
  ▸ DIFFICULTY: MEDIUM
================================================================
  ...
```

---

## Notes

- Supported resume formats: **PDF, DOCX, TXT** (max 5MB)
- Groq free tier is sufficient for this project
- The `outputs/` folder stores generated files temporarily — you can clear it anytime
