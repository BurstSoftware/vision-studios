import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Demo Applications Hub",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for nicer cards
st.markdown("""
    <style>
    .app-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .app-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
    }
    .stButton > button {
        width: 100%;
        height: 50px;
        font-size: 16px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🚀 Demo Applications Hub")
st.markdown("### Click any card below to launch the demo")

st.divider()

# MeetEdgar Demo
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("### 📧")
with col2:
    st.markdown("""
    <div class="app-card">
        <h3>MeetEdgar Demo</h3>
        <p><strong>Social Media Content Scheduling</strong></p>
        <p>Automate your social media posts with smart categorization and evergreen content recycling.</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("Open MeetEdgar Demo →", key="meetedgar", use_container_width=True):
    st.link_button("Open MeetEdgar", "https://meetedgar-demo-v1.streamlit.app/", use_container_width=True)

st.divider()

# Hootsuite Demo
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("### 📱")
with col2:
    st.markdown("""
    <div class="app-card">
        <h3>Hootsuite Demo</h3>
        <p><strong>Social Media Management Dashboard</strong></p>
        <p>Manage multiple social networks, schedule posts, and monitor engagement from one place.</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("Open Hootsuite Demo →", key="hootsuite", use_container_width=True):
    st.link_button("Open Hootsuite", "https://hootsuite-demo-v1.streamlit.app/", use_container_width=True)

st.divider()

# Project Management
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown("### 📋")
with col2:
    st.markdown("""
    <div class="app-card">
        <h3>Project Management Tool</h3>
        <p><strong>Task Tracking & Team Collaboration</strong></p>
        <p>Kanban-style project management with real-time updates, assignees, and progress tracking.</p>
    </div>
    """, unsafe_allow_html=True)

if st.button("Open Project Management →", key="project", use_container_width=True):
    st.link_button("Open Project Management", "https://project-management-v1-1.streamlit.app/", use_container_width=True)

# Footer
st.divider()
st.markdown("""
    <p style="text-align: center; color: #666;">
        Built with ❤️ using Streamlit • All demos are hosted on Streamlit Cloud
    </p>
""", unsafe_allow_html=True)
