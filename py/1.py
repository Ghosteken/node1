import json

# The given JSON content with quiz questions for multiple categories
quiz_data = {
    "Math": [
        {"question": "What is Math question 1?", "options": ["Math Option A 1", "Math Option B 1", "Math Option C 1", "Math Option D 1"], "answer": "Math Option A 1"},
        {"question": "What is Math question 2?", "options": ["Math Option A 2", "Math Option B 2", "Math Option C 2", "Math Option D 2"], "answer": "Math Option A 2"},
        {"question": "What is Math question 3?", "options": ["Math Option A 3", "Math Option B 3", "Math Option C 3", "Math Option D 3"], "answer": "Math Option A 3"},
        {"question": "What is Math question 4?", "options": ["Math Option A 4", "Math Option B 4", "Math Option C 4", "Math Option D 4"], "answer": "Math Option A 4"},
        {"question": "What is Math question 5?", "options": ["Math Option A 5", "Math Option B 5", "Math Option C 5", "Math Option D 5"], "answer": "Math Option A 5"},
        {"question": "What is Math question 6?", "options": ["Math Option A 6", "Math Option B 6", "Math Option C 6", "Math Option D 6"], "answer": "Math Option A 6"},
        {"question": "What is Math question 7?", "options": ["Math Option A 7", "Math Option B 7", "Math Option C 7", "Math Option D 7"], "answer": "Math Option A 7"},
        {"question": "What is Math question 8?", "options": ["Math Option A 8", "Math Option B 8", "Math Option C 8", "Math Option D 8"], "answer": "Math Option A 8"},
        {"question": "What is Math question 9?", "options": ["Math Option A 9", "Math Option B 9", "Math Option C 9", "Math Option D 9"], "answer": "Math Option A 9"},
        {"question": "What is Math question 10?", "options": ["Math Option A 10", "Math Option B 10", "Math Option C 10", "Math Option D 10"], "answer": "Math Option A 10"}
    ],
    "Science": [
        {"question": "What is Science question 1?", "options": ["Science Option A 1", "Science Option B 1", "Science Option C 1", "Science Option D 1"], "answer": "Science Option A 1"},
        {"question": "What is Science question 2?", "options": ["Science Option A 2", "Science Option B 2", "Science Option C 2", "Science Option D 2"], "answer": "Science Option A 2"},
        {"question": "What is Science question 3?", "options": ["Science Option A 3", "Science Option B 3", "Science Option C 3", "Science Option D 3"], "answer": "Science Option A 3"},
        {"question": "What is Science question 4?", "options": ["Science Option A 4", "Science Option B 4", "Science Option C 4", "Science Option D 4"], "answer": "Science Option A 4"},
        {"question": "What is Science question 5?", "options": ["Science Option A 5", "Science Option B 5", "Science Option C 5", "Science Option D 5"], "answer": "Science Option A 5"},
        {"question": "What is Science question 6?", "options": ["Science Option A 6", "Science Option B 6", "Science Option C 6", "Science Option D 6"], "answer": "Science Option A 6"},
        {"question": "What is Science question 7?", "options": ["Science Option A 7", "Science Option B 7", "Science Option C 7", "Science Option D 7"], "answer": "Science Option A 7"},
        {"question": "What is Science question 8?", "options": ["Science Option A 8", "Science Option B 8", "Science Option C 8", "Science Option D 8"], "answer": "Science Option A 8"},
        {"question": "What is Science question 9?", "options": ["Science Option A 9", "Science Option B 9", "Science Option C 9", "Science Option D 9"], "answer": "Science Option A 9"},
        {"question": "What is Science question 10?", "options": ["Science Option A 10", "Science Option B 10", "Science Option C 10", "Science Option D 10"], "answer": "Science Option A 10"}
    ]
}

# Convert the quiz data to JSON format and save it as a file
file_path = '/mnt/data/quiz_data.json'

with open(file_path, 'w') as f:
    json.dump(quiz_data, f)

file_path
