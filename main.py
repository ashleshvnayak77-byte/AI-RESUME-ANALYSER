print("AI Resume Analyzer Started")
import PyPDF2
file = open("resumes/Software_Engineering_2.pdf","rb")
reader = PyPDF2.PdfReader(file)
text= ""
for page in reader.pages:
    text += page.extract_text()
print(text)
skills = ["python","c++","sql","java","machine learning","data analysis","html","css","javascript","docker","aws"]
detected_skills=[]
for skill in skills:
    if skill in text.lower():
        detected_skills.append(skill)
print("detected skills:")
for skill in detected_skills:
    print(skill)
job_skills=["python","sql","docker","aws","machine learning"]
matched=[]
for skill in job_skills:
    if skill in detected_skills:
        matched.append(skill)
missing=[]
for skill in job_skills:
    if skill not in detected_skills:
        missing.append(skill)
score=(len(matched)/len(job_skills))*100
print("Job Matching Results:")
print("Matched Skills:",matched)
print("Missing Skills:",missing)
print("Match score:",score,"%")
