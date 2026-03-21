from flask import Flask, request, jsonify
import PyPDF2

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['resume']

    reader = PyPDF2.PdfReader(file)
    text = ""

    for page in reader.pages:
        text += page.extract_text()

    skills = ["python","c++","sql","java","machine learning","data analysis","html","css","javascript","docker","aws"]

    detected_skills = []
    for skill in skills:
        if skill in text.lower():
            detected_skills.append(skill)

    job_skills = ["python","sql","docker","aws","machine learning"]

    matched = []
    missing = []

    for skill in job_skills:
        if skill in detected_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (len(matched)/len(job_skills))*100

    return jsonify({
        "score": score,
        "matched": matched,
        "missing": missing
    })

app.run()
