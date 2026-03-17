def build_prompt(resume_text: str, job_role: str, experience: str, job_description: str, extra_notes: str) -> str:
    """Build a structured prompt for generating interview questions."""

    experience_line = f"Years of Experience: {experience}" if experience else "Years of Experience: Not specified"
    jd_section = f"\nJob Description:\n{job_description}" if job_description else ""
    notes_section = f"\nAdditional Notes: {extra_notes}" if extra_notes else ""

    prompt = f"""You are an expert technical recruiter and interview coach. Based on the candidate's resume and the job details provided, generate a comprehensive set of interview questions.

--- CANDIDATE RESUME ---
{resume_text}

--- JOB DETAILS ---
Job Role: {job_role}
{experience_line}{jd_section}{notes_section}

--- INSTRUCTIONS ---
Generate exactly 5 questions for each of the 9 combinations below (difficulty × type).
The questions must be tailored to the candidate's resume AND the job role.

Use EXACTLY this format with these exact headers, no extra text before or between sections:

[EASY - TECHNICAL]
1. 
2. 
3. 
4. 
5. 

[EASY - BEHAVIOURAL]
1. 
2. 
3. 
4. 
5. 

[EASY - SITUATIONAL]
1. 
2. 
3. 
4. 
5. 

[MEDIUM - TECHNICAL]
1. 
2. 
3. 
4. 
5. 

[MEDIUM - BEHAVIOURAL]
1. 
2. 
3. 
4. 
5. 

[MEDIUM - SITUATIONAL]
1. 
2. 
3. 
4. 
5. 

[HARD - TECHNICAL]
1. 
2. 
3. 
4. 
5. 

[HARD - BEHAVIOURAL]
1. 
2. 
3. 
4. 
5. 

[HARD - SITUATIONAL]
1. 
2. 
3. 
4. 
5. 

Generate all 45 questions now. Make them specific, insightful, and relevant to the candidate's background and the role.
"""
    return prompt
