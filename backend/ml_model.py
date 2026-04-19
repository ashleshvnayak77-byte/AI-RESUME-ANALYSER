from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

def get_similarity(resume_text, job_description):
    resume_emb = model.encode(resume_text)
    jd_emb = model.encode(job_description)

    score = util.cos_sim(resume_emb, jd_emb)

    return float(score[0][0]) * 100
