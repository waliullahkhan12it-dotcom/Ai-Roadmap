import os
import streamlit as st
from groq import Groq

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Learning Roadmap Generator",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #10172a, #172554, #312e81);
    color: #ffffff;
}

.main .block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.hero {
    background: linear-gradient(120deg, #2563eb, #7c3aed, #9333ea);
    padding: 38px 30px;
    border-radius: 22px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 10px 35px rgba(0,0,0,0.3);
}

.hero h1 {
    color: white;
    font-size: 38px;
    font-weight: 800;
}

.hero p {
    color: #e0e7ff;
    font-size: 17px;
}

.section-card {
    background: rgba(255,255,255,0.08);
    border: 1px solid rgba(255,255,255,0.15);
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 18px;
}

.feature-card {
    background: linear-gradient(145deg, #1e3a8a, #4338ca);
    padding: 22px;
    border-radius: 17px;
    text-align: center;
    min-height: 140px;
    border: 1px solid rgba(255,255,255,0.15);
}

.feature-card h3 {
    color: white;
    font-size: 19px;
}

.feature-card p {
    color: #dbeafe;
    font-size: 14px;
}

.result-card {
    background: rgba(255,255,255,0.08);
    border-left: 5px solid #38bdf8;
    border-radius: 12px;
    padding: 18px;
    margin: 12px 0;
}

div[data-testid="stForm"] {
    background: rgba(255,255,255,0.07);
    padding: 25px;
    border: 1px solid rgba(255,255,255,0.15);
    border-radius: 18px;
}

.stButton > button {
    background: linear-gradient(90deg, #2563eb, #9333ea);
    color: white;
    border: none;
    border-radius: 12px;
    font-weight: 700;
    padding: 12px;
    min-height: 48px;
    width: 100%;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #7c3aed, #2563eb);
    color: white;
    border: 1px solid #ffffff;
}

.stDownloadButton > button {
    background: #059669;
    color: white;
    border-radius: 10px;
    border: none;
}

label, .stMarkdown, p, li {
    color: #f1f5f9 !important;
}

h1, h2, h3 {
    color: #ffffff !important;
}

[data-testid="stSidebar"] {
    background: #111827;
}

hr {
    border-color: rgba(255,255,255,0.2);
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# GROQ API CONFIGURATION
# --------------------------------------------------

def get_api_key():
    try:
        return st.secrets.get("GROQ_API_KEY", "")
    except Exception:
        return os.getenv("GROQ_API_KEY", "")


def generate_roadmap(field, level, duration, hours, goal):

    api_key = get_api_key()

    if not api_key:
        st.error(
            "Groq API key is missing. Add GROQ_API_KEY "
            "in Streamlit App Settings → Secrets."
        )
        return None

    client = Groq(api_key=api_key)

    system_prompt = """
    You are an expert AI learning advisor, professional educator,
    technical mentor and career roadmap designer.

    Your responsibility is to create detailed, realistic,
    practical and personalized learning roadmaps.

    Follow these rules:
    1. Adapt everything to the student's selected skill level.
    2. Divide the roadmap into logical phases or weeks.
    3. Explain what the learner should study in each phase.
    4. Include practical exercises and hands-on activities.
    5. Recommend relevant tools and technologies.
    6. Include projects after appropriate learning phases.
    7. Recommend learning resources and documentation.
    8. Include a final capstone project.
    9. Provide career opportunities and next steps.
    10. Avoid unrealistic promises and unnecessary topics.
    11. Use clear headings, bullet points and numbered steps.
    12. Make the roadmap achievable within the given duration.
    13. Explain technical concepts in understandable language.
    """

    user_prompt = f"""
    Create a complete personalized learning roadmap.

    LEARNING DOMAIN: {field}
    CURRENT SKILL LEVEL: {level}
    AVAILABLE LEARNING TIME: {duration}
    DAILY STUDY HOURS: {hours}
    LEARNING GOAL: {goal}

    Organize the response using these sections:

    1. PERSONALIZED LEARNING OVERVIEW
    - Introduction to the domain
    - Expected outcome
    - Required prerequisites

    2. COMPLETE LEARNING ROADMAP
    - Divide the duration into appropriate weeks or phases.
    - Topics to learn in each week.
    - Explanation of each topic.
    - Practical exercises.
    - Expected weekly results.

    3. TOOLS AND TECHNOLOGIES
    - Important tools
    - Programming languages if required
    - Software and platforms

    4. PRACTICAL PROJECTS
    - Beginner-friendly projects
    - Intermediate projects
    - Advanced projects
    - Explain what each project teaches.

    5. LEARNING RESOURCES
    - Official documentation
    - Recommended websites
    - Courses and tutorials
    - Books where relevant

    6. FINAL CAPSTONE PROJECT
    - Project idea
    - Main features
    - Implementation steps

    7. CAREER ROADMAP
    - Relevant job roles
    - Skills required
    - Portfolio recommendations
    - Suggested next steps

    8. WEEKLY STUDY STRATEGY
    - How to distribute study hours
    - Revision strategy
    - Practice strategy

    Make the response detailed, realistic and specific
    to the selected domain and learning duration.
    """

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.6,
            max_tokens=6500
        )

        return response.choices[0].message.content

    except Exception as e:
        st.error(f"Roadmap generation failed: {str(e)}")
        return None


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.markdown("## 🎓 Roadmap AI")
    st.markdown("---")

    st.markdown("### Navigation")
    st.markdown("""
    - 🏠 Home Dashboard
    - 🧠 Generate Roadmap
    - 📚 Learning Resources
    - 🚀 Career Guidance
    """)

    st.markdown("---")

    st.markdown("### About Project")
    st.write(
        "An AI-powered learning assistant that creates "
        "personalized learning plans using Groq LLM."
    )

    st.markdown("---")
    st.caption("Powered by Python + Streamlit + Groq AI")

# --------------------------------------------------
# HERO SECTION
# --------------------------------------------------

st.markdown("""
<div class="hero">
    <h1>🎓 AI Learning Roadmap Generator</h1>
    <p>Your Personal AI Mentor for Learning Any Skill</p>
    <p>Discover • Learn • Practice • Build • Achieve</p>
</div>
""", unsafe_allow_html=True)

# --------------------------------------------------
# DASHBOARD FEATURES
# --------------------------------------------------

st.markdown("## 🌟 Welcome to Your Learning Journey")

st.write(
    "Turn your learning goals into a structured, "
    "personalized roadmap with the power of Artificial Intelligence."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>🧠 AI Powered</h3>
        <p>Intelligent roadmaps generated by Groq AI.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>📅 Structured Plans</h3>
        <p>Organized weekly learning and practice schedules.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🚀 Career Focused</h3>
        <p>Projects, tools and career development guidance.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --------------------------------------------------
# ROADMAP GENERATOR INPUTS
# --------------------------------------------------

st.markdown("## 🚀 Generate Your Personalized Roadmap")

with st.form("roadmap_form"):

    field = st.text_input(
        "🎯 What do you want to learn?",
        placeholder="Example: Cybersecurity, Python, AI, Data Science..."
    )

    col1, col2 = st.columns(2)

    with col1:
        level = st.selectbox(
            "📊 Select Your Current Skill Level",
            ["Beginner", "Intermediate", "Advanced"]
        )

    with col2:
        duration = st.selectbox(
            "⏳ How much time do you have?",
            [
                "2 Weeks",
                "1 Month",
                "2 Months",
                "3 Months",
                "6 Months",
                "1 Year",
                "2 Years"
            ]
        )

    hours = st.selectbox(
        "⏰ Daily Study Hours",
        [
            "1 Hour",
            "2 Hours",
            "3 Hours",
            "4 Hours",
            "5 Hours",
            "6+ Hours"
        ]
    )

    goal = st.text_area(
        "🏆 What is your learning goal?",
        placeholder="Example: I want to become a professional cybersecurity analyst.",
        height=100
    )

    submitted = st.form_submit_button(
        "✨ Generate My AI Learning Roadmap",
        use_container_width=True
    )

# --------------------------------------------------
# GENERATE AND DISPLAY ROADMAP
# --------------------------------------------------

if submitted:

    if not field.strip():
        st.warning("Please enter a learning domain.")

    elif not goal.strip():
        st.warning("Please describe your learning goal.")

    else:
        with st.spinner(
            "🤖 AI is analyzing your goals and creating your roadmap..."
        ):
            roadmap = generate_roadmap(
                field,
                level,
                duration,
                hours,
                goal
            )

        if roadmap:
            st.session_state["roadmap"] = roadmap
            st.session_state["roadmap_field"] = field

# --------------------------------------------------
# ROADMAP RESULTS
# --------------------------------------------------

if st.session_state.get("roadmap"):

    st.markdown("---")

    st.markdown("## 📚 Your Personalized Learning Roadmap")

    st.success(
        f"Your {st.session_state['roadmap_field']} roadmap is ready!"
    )

    st.markdown(
        '<div class="result-card">Your AI-generated learning plan is below. '
        'Follow the phases and complete the practical exercises.</div>',
        unsafe_allow_html=True
    )

    st.markdown(st.session_state["roadmap"])

    st.markdown("---")

    st.download_button(
        label="📥 Download Your Roadmap",
        data=st.session_state["roadmap"],
        file_name="AI_Learning_Roadmap.txt",
        mime="text/plain",
        use_container_width=True
    )

    if st.button("🔄 Generate Another Roadmap"):
        st.session_state.pop("roadmap", None)
        st.session_state.pop("roadmap_field", None)
        st.rerun()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.markdown("""
<div style="text-align:center; padding:20px;">
    <h3>🎓 Learn Smarter with AI</h3>
    <p>Built with Python | Streamlit | Groq AI</p>
    <p>Turn Your Ambition Into Achievement 🚀</p>
</div>
""", unsafe_allow_html=True)
