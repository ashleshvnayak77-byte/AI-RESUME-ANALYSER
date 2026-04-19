from flask import Flask, request, jsonify
from parser import extract_text
from ml_model import get_similarity
from skill_extractor import extract_skills

app = Flask(__name__)

@app.route('/')
def home():
    return "AI Resume Analyzer Running 🚀"

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']
    job_description = request.form['job_description']

    file_path = "resumes/" + file.filename
    file.save(file_path)

    # Extract text
    resume_text = extract_text(file_path)

    # ML similarity score
    score = get_similarity(resume_text, job_description)

    # Extract skills
    skills = extract_skills(resume_text)

    return jsonify({
        "match_score": round(score, 2),
        "skills": skills
    })

if __name__ == '__main__':
    app.run(debug=True)
