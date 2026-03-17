# Interview Question Generator

A web application that generates tailored interview questions based on a candidate's resume and the job role they are applying for. The application uses the Llama 3.3 70B language model via the Groq API to produce relevant, personalised questions and exports them as a downloadable text file.


## What It Does

The application accepts a resume file, a job role, years of experience, an optional job description, and any additional notes. It analyses the resume content alongside the job details and generates 45 interview questions organised by difficulty and type.

Difficulty levels: Easy, Medium, Hard

Question types: Technical, Behavioural, Situational

The output is a structured text file containing 5 questions for each combination of difficulty and type, making a total of 45 questions per generation.


## Sample Output

A full example of the generated output is available in the repo as interview_questions.txt.


    INTERVIEW QUESTION BANK
    Job Role    : Backend Engineer
    Experience  : 0 year(s)
    Generated   : 2026-03-17 21:33:13

    DIFFICULTY: EASY

    TECHNICAL
    1. Can you explain the difference between monolithic and microservice architecture?
    2. How do you use Docker for containerization in a backend environment?
    ...

    BEHAVIOURAL
    1. Can you tell me about a project you are particularly proud of?
    ...

    SITUATIONAL
    1. If you were tasked with deploying a new backend application, what steps would you take?
    ...

    DIFFICULTY: MEDIUM
    ...

    DIFFICULTY: HARD
    ...


## Tech Stack

- Python 3.11
- Flask (web framework)
- Groq API with Llama 3.3 70B (question generation)
- pdfplumber (PDF parsing)
- python-docx (DOCX parsing)


## Supported Resume Formats

- PDF
- DOCX
- TXT

Maximum file size: 5MB


## Prerequisites

- Python 3.9 or higher
- A free Groq API key from console.groq.com
- Conda or any Python virtual environment manager


## Setup and Installation

Clone the repository:

    git clone https://github.com/your-username/interview-gen.git
    cd interview-gen

Create and activate a conda environment:

    conda create -n interview-gen python=3.11
    conda activate interview-gen

Install dependencies:

    pip install -r requirements.txt

Create a .env file in the project root and add your Groq API key:

    GROQ_API_KEY=your_groq_api_key_here

Run the application:

    python app.py

Open your browser and go to http://localhost:5000


## Project Structure

    interview-gen/
    |-- app.py                  Entry point, Flask routes
    |-- utils/
    |   |-- resume_parser.py    Extracts text from resume files
    |   |-- prompt_builder.py   Builds the prompt sent to the LLM
    |   |-- groq_client.py      Handles Groq API communication
    |   |-- formatter.py        Formats the output into a text file
    |-- templates/
    |   |-- index.html          Frontend UI
    
    |-- .env                    API key configuration (not committed)
    |-- .env.example            Example environment file
    |-- requirements.txt        Python dependencies
    |-- .gitignore


## Environment Variables

The application requires one environment variable:

    GROQ_API_KEY    Your API key from console.groq.com

Never commit your .env file. Use .env.example as a reference template.


## Notes

- The Groq free tier is sufficient to run this application

- Questions are tailored based on both the resume content and the job details provided, so more detailed inputs produce more relevant questions
