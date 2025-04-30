import pandas as pd
from collections import Counter
import re

def analyze_skills():
    df = pd.read_csv("data/jobs.csv")
    skills = []
    text_sources = df["Title"].astype(str) + " " + df["Tags"].astype(str)
    for text in text_sources:
        found_skills = re.findall(
            r'\b(data|python|sql|excel|analysis|analytics|machine learning|ml|ai|statistics|powerbi|tableau|r|numpy|pandas|scikit-learn|bi|deep learning)\b',
            text, flags=re.I
        )
        skills.extend(found_skills)
    skill_freq = Counter([s.lower() for s in skills])
    return pd.DataFrame(skill_freq.items(), columns=["Skill", "Frequency"]).sort_values(by="Frequency", ascending=False)
