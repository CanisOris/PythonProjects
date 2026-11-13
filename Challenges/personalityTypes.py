
communication_levers_dict = {
    "I": {"lever": "Pace", "need": "Time to process; prefers written or delayed responses over on-the-spot reactions"},
    "E": {"lever": "Pace", "need": "Thinks out loud; processes externally and matches energetic, immediate pacing"},
    "S": {"lever": "Specificity", "need": "Concrete examples, factual data, and a linear, sequential conversation format"},
    "N": {"lever": "Specificity", "need": "Abstract framing, inferences, brainstorming, and circular or out-of-order conversation"},
    "T": {"lever": "Warmth", "need": "Direct, straightforward logic; needs objective reasoning and cause-and-effect named explicitly"},
    "F": {"lever": "Warmth", "need": "Emotional context named; appreciates good manners, tactfulness, and a harmonious tone"},
    "J": {"lever": "Structure", "need": "Bullet points, timelines, decisive conclusions, and clear expectations; vagueness reads as unreliability"},
    "P": {"lever": "Structure", "need": "Exploration, flexibility, and spontaneous brainstorming over immediate conclusions"}
}

process_pairs_dict = {
    "ST": {
        "title": "Bottom-line",
        "focus": "Realities and practical applications",
        "communication_style": "Practical, straightforward, fact-oriented, and logical. Wants to cut to the chase and have step-by-step directions."
    },
    "SF": {
        "title": "Customer Service",
        "focus": "Realities in the here and now",
        "communication_style": "Warm, friendly, sympathetic, and people-oriented. Values friendly interactions, positive feedback, and practical support."
    },
    "NF": {
        "title": "Possibilities for People",
        "focus": "Ideas, possibilities, and empowerment",
        "communication_style": "Enthusiastic, insightful, and encouraging. Needs freedom, imagination, and a warm environment."
    },
    "NT": {
        "title": "Logical Possibilities",
        "focus": "Systems, frameworks, and objective analysis",
        "communication_style": "Analytical, objective, and theoretical. Needs logical explanations, competence, and debate without personal offense."
    }
}

interaction_styles_dict = {
    "Get-Things-Going": {
        "types": ["ENFP", "ENTP", "ESFJ", "ESFP"],
        "vibe": "Energetic, expressive, and persuasive",
        "tips": "Ask open-ended questions, be responsive, allow time for plenty of conversation, and use friendly banter."
    },
    "Behind-the-Scenes": {
        "types": ["INFP", "INTP", "ISFJ", "ISFP"],
        "vibe": "Quiet, friendly, and accommodating",
        "tips": "Use a quiet tone, be laid-back, maintain a steady calm pace, and give them processing time without rushing."
    },
    "Chart-the-Course": {
        "types": ["INFJ", "INTJ", "ISTJ", "ISTP"],
        "vibe": "Grounded, focused, and matter-of-fact",
        "tips": "Be detailed, pause for questions, avoid excessive small talk, and do not ramble when you need something from them."
    },
    "In-Charge": {
        "types": ["ENFJ", "ENTJ", "ESTJ", "ESTP"],
        "vibe": "Direct, action-oriented, and decisive",
        "tips": "Lead with conclusions, be precise, time-bound your asks, and remember that directness lands as respect."
    }
}

mbti_types_dict = {
    "INTJ": {"title": "Architect", "temperament": "Analyst", "functions": ["Ni", "Te", "Fi", "Se"]},
    "INTP": {"title": "Logician", "temperament": "Analyst", "functions": ["Ti", "Ne", "Si", "Fe"]},
    "ENTJ": {"title": "Commander", "temperament": "Analyst", "functions": ["Te", "Ni", "Se", "Fi"]},
    "ENTP": {"title": "Debater", "temperament": "Analyst", "functions": ["Ne", "Ti", "Fe", "Si"]},
    "INFJ": {"title": "Advocate", "temperament": "Diplomat", "functions": ["Ni", "Fe", "Ti", "Se"]},
    "INFP": {"title": "Mediator", "temperament": "Diplomat", "functions": ["Fi", "Ne", "Si", "Te"]},
    "ENFJ": {"title": "Protagonist", "temperament": "Diplomat", "functions": ["Fe", "Ni", "Se", "Ti"]},
    "ENFP": {"title": "Campaigner", "temperament": "Diplomat", "functions": ["Ne", "Fi", "Te", "Si"]},
    "ISTJ": {"title": "Logistician", "temperament": "Sentinel", "functions": ["Si", "Te", "Fi", "Ne"]},
    "ISFJ": {"title": "Defender", "temperament": "Sentinel", "functions": ["Si", "Fe", "Ti", "Ne"]},
    "ESTJ": {"title": "Executive", "temperament": "Sentinel", "functions": ["Te", "Si", "Ne", "Fi"]},
    "ESFJ": {"title": "Consul", "temperament": "Sentinel", "functions": ["Fe", "Si", "Ne", "Ti"]},
    "ISTP": {"title": "Virtuoso", "temperament": "Explorer", "functions": ["Ti", "Se", "Ni", "Fe"]},
    "ISFP": {"title": "Adventurer", "temperament": "Explorer", "functions": ["Fi", "Se", "Ni", "Te"]},
    "ESTP": {"title": "Entrepreneur", "temperament": "Explorer", "functions": ["Se", "Ti", "Fe", "Ni"]},
    "ESFP": {"title": "Entertainer", "temperament": "Explorer", "functions": ["Se", "Fi", "Te", "Ni"]}
}

cognitive_functions_dict = {
    "Ni": {"name": "Introverted Intuition", "focus": "Internal visions, patterns, and insights"},
    "Ne": {"name": "Extraverted Intuition", "focus": "External possibilities, brainstorming, and connections"},
    "Ti": {"name": "Introverted Thinking", "focus": "Internal logic, frameworks, and accuracy"},
    "Te": {"name": "Extraverted Thinking", "focus": "External organization, efficiency, and metrics"},
    "Fi": {"name": "Introverted Feeling", "focus": "Internal values, authenticity, and individuality"},
    "Fe": {"name": "Extraverted Feeling", "focus": "External harmony, empathy, and social dynamics"},
    "Si": {"name": "Introverted Sensing", "focus": "Internal memory, traditions, and past experiences"},
    "Se": {"name": "Extraverted Sensing", "focus": "External reality, present moment, and action"}
}

subdivisions_dict = {
    "Introversion": {"code": "I", "preference": "Internal"},
    "Extraversion": {"code": "E", "preference": "External"},
    "Sensing": {"code": "S", "preference": "Concrete"},
    "Intuition": {"code": "N", "preference": "Abstract"},
    "Thinking": {"code": "T", "preference": "Logic"},
    "Feeling": {"code": "F", "preference": "Values"},
    "Judging": {"code": "J", "preference": "Structure"},
    "Perceiving": {"code": "P", "preference": "Flexible"}
}

test_info = {
    "name": "Myers-Briggs Type Indicator",
    "abbreviation": "MBTI",
    "category": "Typology",
    "popular": True,
    "type_classification": 16,  # Fixed the incomplete string syntax here
    "subdivisions": subdivisions_dict,
    "myrating": 7
}