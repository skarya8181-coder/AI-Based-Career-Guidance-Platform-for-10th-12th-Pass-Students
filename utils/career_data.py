# Sample career data for Career Explorer

CAREERS = [
    {
        'name': 'Software Engineer',
        'overview': 'Build and maintain software applications.',
        'eligibility': '12th + B.Tech/B.E. in CS/IT or BCA',
        'courses': ['B.Tech CS', 'BCA', 'MCA'],
        'entrance_exams': ['JEE', 'University exams'],
        'skills': ['programming', 'algorithms', 'data structures'],
        'salary': {'freshers': 30000, 'avg': 70000, 'experienced': 200000},
        'future': 'High demand across industries',
        'keywords': ['programming', 'coding', 'software'],
        'aptitude_match': ['Technical Problem Solver']
    },
    {
        'name': 'Data Scientist',
        'overview': 'Analyze data to extract insights.',
        'eligibility': '12th + B.Sc/B.Tech/M.Sc in relevant fields',
        'courses': ['B.Sc Statistics', 'B.Tech CS', 'M.Sc Data Science'],
        'entrance_exams': ['University exams'],
        'skills': ['python', 'statistics', 'ml'],
        'salary': {'freshers': 35000, 'avg': 90000, 'experienced': 250000},
        'future': 'Growing demand with AI adoption',
        'keywords': ['data', 'machine learning', 'statistics'],
        'aptitude_match': ['Analytical Thinker']
    },
    {
        'name': 'AI Engineer',
        'overview': 'Build AI systems and ML models.',
        'eligibility': '12th + B.Tech (CS), M.Tech',
        'courses': ['B.Tech CS', 'M.Tech AI'],
        'entrance_exams': ['GATE for Masters'],
        'skills': ['python', 'ml', 'dl'],
        'salary': {'freshers': 40000, 'avg': 120000, 'experienced': 300000},
        'future': 'Excellent growth with specialization',
        'keywords': ['ai', 'machine learning', 'deep learning'],
        'aptitude_match': ['Technical Problem Solver']
    },
    {
        'name': 'Doctor',
        'overview': 'Medical practitioner (MBBS and specializations).',
        'eligibility': '12th (PCB) + NEET',
        'courses': ['MBBS', 'BDS'],
        'entrance_exams': ['NEET'],
        'skills': ['biology', 'empathy', 'diagnosis'],
        'salary': {'freshers': 30000, 'avg': 100000, 'experienced': 400000},
        'future': 'Stable with high trust',
        'keywords': ['medicine', 'health', 'doctor'],
        'aptitude_match': ['Analytical Thinker']
    },
]

# Expand to 30+ by duplicating variants (for demo we keep a concise set)
for i in range(4, 30):
    CAREERS.append({
        'name': f'Career Example {i}',
        'overview': 'Sample career entry for demo.',
        'eligibility': 'Varies',
        'courses': ['Sample Course'],
        'entrance_exams': [],
        'skills': ['communication'],
        'salary': {'freshers': 20000+i*1000, 'avg': 40000+i*2000, 'experienced': 90000+i*3000},
        'future': 'Opportunity varies by field',
        'keywords': ['sample', 'demo'],
        'aptitude_match': ['Creative Designer']
    })
