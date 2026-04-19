import spacy

nlp = spacy.load("en_core_web_sm")

# Basic skill database (you can expand later)
SKILLS_DB = [
    "python", "java", "c++", "machine learning",
    "deep learning", "sql", "react", "node.js",
    "data analysis", "tensorflow", "pandas"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []

    for skill in SKILLS_DB:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))
