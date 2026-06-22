import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Simple rule-based recommendation: combine marks, interests and aptitude profile

def recommend(career_list, profile, top_k=5):
    # career_list: list of dicts with 'name' and 'keywords' and 'weight' fields
    scores = []
    for c in career_list:
        score = 0.0
        # matches with interests/skills
        for kw in c.get('keywords', []):
            if kw.lower() in profile.get('interests', '').lower():
                score += 30
            if kw.lower() in profile.get('skills', '').lower():
                score += 20
        # marks influence
        marks = profile.get('marks', 0)
        score += min(marks/100 * 30, 30)
        # aptitude mapping
        apt = profile.get('aptitude', {})
        for k,v in apt.items():
            if k in c.get('aptitude_match', []):
                score += v * 2
        scores.append((c['name'], score, c))
    scores.sort(key=lambda x: x[1], reverse=True)
    top = []
    for name, s, c in scores[:top_k]:
        entry = c.copy()
        entry['match_percentage'] = round(min(100, s), 1)
        top.append(entry)
    return top
