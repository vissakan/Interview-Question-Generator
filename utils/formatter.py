from datetime import datetime


def format_output(raw_text: str, job_role: str, experience: str) -> str:
    """Format the LLM output into a clean, well-structured .txt file."""

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    exp_display = f"{experience} year(s)" if experience else "Not specified"

    header = f"""
================================================================================
                     INTERVIEW QUESTION BANK
================================================================================
  Job Role    : {job_role}
  Experience  : {exp_display}
  Generated   : {now}
================================================================================

This document contains 45 tailored interview questions organised by:
  Difficulty  → Easy | Medium | Hard
  Type        → Technical | Behavioural | Situational

--------------------------------------------------------------------------------

"""

    # Clean and section the raw output
    sections = _parse_sections(raw_text)
    body = _render_sections(sections)

    footer = """
--------------------------------------------------------------------------------
                         END OF QUESTION BANK
================================================================================
"""
    return header + body + footer


def _parse_sections(raw_text: str) -> dict:
    """Parse the LLM output into a dict keyed by section headers."""
    import re
    sections = {}
    current_key = None
    current_lines = []

    for line in raw_text.splitlines():
        line = line.strip()
        match = re.match(r'\[(EASY|MEDIUM|HARD)\s*-\s*(TECHNICAL|BEHAVIOURAL|SITUATIONAL)\]', line, re.IGNORECASE)
        if match:
            if current_key:
                sections[current_key] = current_lines
            current_key = f"[{match.group(1).upper()} - {match.group(2).upper()}]"
            current_lines = []
        elif current_key and line:
            current_lines.append(line)

    if current_key:
        sections[current_key] = current_lines

    return sections


def _render_sections(sections: dict) -> str:
    """Render the parsed sections into formatted text."""
    order = [
        "[EASY - TECHNICAL]", "[EASY - BEHAVIOURAL]", "[EASY - SITUATIONAL]",
        "[MEDIUM - TECHNICAL]", "[MEDIUM - BEHAVIOURAL]", "[MEDIUM - SITUATIONAL]",
        "[HARD - TECHNICAL]", "[HARD - BEHAVIOURAL]", "[HARD - SITUATIONAL]",
    ]

    difficulty_banners = {
        "EASY": "▸ DIFFICULTY: EASY",
        "MEDIUM": "▸ DIFFICULTY: MEDIUM",
        "HARD": "▸ DIFFICULTY: HARD",
    }

    output = []
    last_difficulty = None

    for key in order:
        difficulty = key.split(" - ")[0].strip("[")
        q_type = key.split(" - ")[1].strip("]")

        # Print difficulty banner when it changes
        if difficulty != last_difficulty:
            banner = difficulty_banners[difficulty]
            output.append(f"\n{'=' * 64}")
            output.append(f"  {banner}")
            output.append(f"{'=' * 64}\n")
            last_difficulty = difficulty

        output.append(f"  ── {q_type} ──\n")

        questions = sections.get(key, [])
        if questions:
            for q in questions:
                output.append(f"  {q}")
        else:
            output.append("  (No questions generated for this section)")

        output.append("")

    return "\n".join(output)
