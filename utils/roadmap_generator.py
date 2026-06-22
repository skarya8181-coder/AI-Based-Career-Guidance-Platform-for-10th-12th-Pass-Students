# Generates simple roadmap steps for a career

SAMPLE_ROADMAPS = {
    "AI Engineer": [
        "Complete 12th (PCM)",
        "B.Tech in CSE / B.E.",
        "Learn Python",
        "Study ML fundamentals",
        "Deep Learning and NLP",
        "Build projects",
        "Internships",
    ],
    "Data Scientist": [
        "Complete 12th (PCM/PCB/Commerce)",
        "B.Sc / B.Tech / BCA",
        "Learn Python and Statistics",
        "Machine Learning",
        "Projects and Kaggle",
        "Internships",
    ],
}


def get_roadmap(career):
    return SAMPLE_ROADMAPS.get(career, [
        "Finish 12th",
        "Pursue relevant undergraduate degree",
        "Acquire necessary skills",
        "Build projects",
        "Apply for internships",
    ])
