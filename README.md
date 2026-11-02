
# 🎓 AI Learning Roadmap Generator

## 📌 Project Overview

AI Learning Roadmap Generator is an AI-powered web application developed using Python, Streamlit, and Groq API.

The application helps students and learners create personalized learning roadmaps for any domain based on their current skill level, available learning duration, daily study hours, and career goals.

## 🎯 Objectives

- Generate personalized learning roadmaps.
- Help beginners learn new technical skills.
- Provide structured weekly learning plans.
- Recommend useful tools and technologies.
- Suggest practical projects and exercises.
- Provide career development guidance.

## 🚀 Features

1. AI-powered roadmap generation.
2. Beginner, Intermediate, and Advanced levels.
3. Custom learning duration.
4. Daily study hour selection.
5. Personalized learning goals.
6. Weekly study plans.
7. Practical projects and exercises.
8. Recommended learning resources.
9. Career guidance.
10. Downloadable roadmaps.
11. Colorful Streamlit dashboard.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web interface |
| Groq API | AI text generation |
| Llama 3.3 70B | Language model |
| GitHub | Project repository |
| Streamlit Cloud | Deployment |

## 📁 Project Structure

```text
AI-Learning-Roadmap-Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## 🔐 API Configuration

The application requires a Groq API key.

For local development, create:

`.streamlit/secrets.toml`

Add:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

Never upload your API key to GitHub.

## ▶️ Run the Application

Execute:

```bash
streamlit run app.py
```

## ☁️ Deployment

1. Upload all three files to GitHub.
2. Open Streamlit Community Cloud.
3. Connect your GitHub account.
4. Select your repository.
5. Select `app.py` as the main file.
6. Open Advanced Settings / Secrets.
7. Add your Groq API key:

```toml
GROQ_API_KEY = "your_groq_api_key"
```

8. Deploy the application.

## 👨‍🎓 Target Users

- University students
- Beginners in technology
- Self-learners
- Programming students
- Career changers
- Technology enthusiasts

## 🔮 Future Improvements

- User authentication
- Roadmap history
- Learning progress tracking
- Interactive quizzes
- AI chatbot mentor
- PDF roadmap export
- Personalized resource recommendations

## 👨‍💻 Conclusion

AI Learning Roadmap Generator makes learning more organized, accessible, and personalized through Artificial Intelligence.

Built with Python, Streamlit, and Groq AI.
