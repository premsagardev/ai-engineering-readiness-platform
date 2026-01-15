def sections(raw_text:str) -> list:
    res = []
    SECTION_LIST = ["EXPERIENCE", "SKILLS", "PROJECT", "PROJECTS", "TECH STACK", "SUMMARY", "CERTIFICATIONS", "EDUCATION" ]
    lines = raw_text.splitlines()
    current_header = ""
    current_lines = []
    for line in lines:
        clean_line = line.strip()
        if not clean_line: 
            continue
        elif not any(char.isalnum() for char in clean_line):
            continue
        elif clean_line.upper() in SECTION_LIST:
            new_header = clean_line.upper()
            if len(current_lines) > 0 and current_header:
                res.append({"header" : current_header, "lines" : current_lines});
            current_header = new_header
            current_lines = []
        else:
            current_lines.append(clean_line)
    if len(current_lines) > 0 and current_header:
        res.append({"header" : current_header, "lines" : current_lines});
    return res
