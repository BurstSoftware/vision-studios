import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

# ========================= CONFIG =========================
st.set_page_config(
    page_title="Hootsuite Simulator",
    page_icon="🦉",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🦉 Hootsuite Simulator")
st.markdown("### All-in-One Social Media Management Demo")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to Feature",
    [
        "🏠 Home",
        "📅 Publishing & Scheduling",
        "✍️ Content Creation",
        "📊 Analytics & Reporting",
        "🔍 Social Listening",
        "💬 Engagement Inbox",
        "👥 Team Collaboration",
        "📣 Advertising & Integrations"
    ]
)

# ========================= HOME =========================
if page == "🏠 Home":
    st.success("Welcome to the Hootsuite Demo App!")
    st.markdown("""
    This is a **single-file** Streamlit application simulating all major Hootsuite features.
    
    Use the sidebar to navigate between features.
    """)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Posts Scheduled", "47", "↑8")
    with col2:
        st.metric("Total Reach", "184.2K", "↑12%")
    with col3:
        st.metric("Active Campaigns", "6")
    
    st.info("Built with pure Python + Streamlit • One single codebase")

# ========================= PUBLISHING =========================
elif page == "📅 Publishing & Scheduling":
    st.title("📅 Publishing & Scheduling")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.subheader("Social Content Calendar")
        view = st.radio("View Mode", ["Calendar View", "List View"], horizontal=True)
        
        if view == "Calendar View":
            st.info("📆 Interactive Calendar (Demo)")
            dates = pd.date_range(datetime.now(), periods=7)
            for d in dates:
                st.write(f"**{d.strftime('%b %d, %Y')}** — 3 posts scheduled")
        else:
            data = {
                "Platform": ["Instagram", "LinkedIn", "X", "TikTok"],
                "Content": ["Summer Sale Launch", "New Product Update", "Industry Insight", "Behind the Scenes"],
                "Time": ["Jun 19 10:00", "Jun 19 14:30", "Jun 20 09:00", "Jun 21 18:00"],
                "Status": ["Scheduled", "Scheduled", "Draft", "Approved"]
            }
            st.dataframe(pd.DataFrame(data), use_container_width=True)
    
    with col2:
        st.subheader("Quick Schedule Post")
        platforms = st.multiselect("Select Platforms", 
                                  ["Instagram", "LinkedIn", "X (Twitter)", "TikTok", "Facebook"], 
                                  default=["Instagram", "LinkedIn"])
        post_text = st.text_area("Post Content", "Check out our new summer collection! 🌞 #SummerSale")
        post_date = st.date_input("Date", datetime.now())
        post_time = st.time_input("Time", datetime.now().time())
        
        if st.button("Schedule Post", type="primary"):
            st.success(f"✅ Post scheduled on {', '.join(platforms)} for {post_date} at {post_time}")

# ========================= CONTENT CREATION =========================
elif page == "✍️ Content Creation":
    st.title("✍️ Content Creation & OwlyGPT")
    
    st.subheader("AI Caption Generator (OwlyGPT)")
    brand_voice = st.selectbox("Brand Voice", ["Professional", "Fun & Casual", "Luxury", "Tech-Savvy"])
    prompt = st.text_input("What do you want to post about?", "Promote our new eco-friendly product")
    
    if st.button("Generate with OwlyGPT"):
        st.write("**Here are 3 AI-generated options:**")
        st.success("1. Save the planet one sip at a time 🌍 Our new bottle is here!")
        st.success("2. Eco-friendly never looked this good 💧 #GoGreen")
        st.success("3. Hydration with a conscience. Join the movement!")
    
    st.subheader("Media Studio")
    col1, col2 = st.columns(2)
    with col1:
        st.image("https://picsum.photos/600/400", caption="Stock / Canva Integration")
    with col2:
        st.file_uploader("Upload Image or Video", type=["png", "jpg", "mp4", "gif"])

# ========================= ANALYTICS =========================
elif page == "📊 Analytics & Reporting":
    st.title("📊 Analytics & Reporting")
    
    tab1, tab2, tab3 = st.tabs(["Performance Overview", "Best Times", "Competitor Benchmark"])
    
    with tab1:
        df = pd.DataFrame({
            "Platform": ["Instagram", "LinkedIn", "X", "TikTok"],
            "Impressions": [45200, 18900, 67100, 12400],
            "Engagement": [3240, 980, 4520, 1870],
            "Clicks": [890, 420, 1560, 310]
        })
        fig = px.bar(df, x="Platform", y=["Impressions", "Engagement"], barmode="group", title="Performance by Platform")
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.subheader("Best Time to Post")
        best_times = {"Monday": 65, "Tuesday": 78, "Wednesday": 92, "Thursday": 71, "Friday": 88}
        st.bar_chart(best_times)
    
    with tab3:
        st.metric("Your Social Performance Score", "87/100", "↑12")
        st.write("You are outperforming **4 out of 5** tracked competitors this month.")

# ========================= SOCIAL LISTENING =========================
elif page == "🔍 Social Listening":
    st.title("🔍 Social Listening & Monitoring")
    
    query = st.text_input("Search for mentions, keywords, or hashtags", "#YourBrand OR @yourbrand")
    
    if st.button("Search Across Web & Social"):
        st.success("Found **1,248** mentions in the last 7 days")
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Overall Sentiment", "Positive 68%")
            st.image("https://picsum.photos/400/250", caption="Word Cloud")
        with col2:
            st.subheader("Recent Mentions")
            for i in range(3):
                st.info(f"**@user{i+1}** (Instagram): Loving the new feature! 🔥")

# ========================= ENGAGEMENT INBOX =========================
elif page == "💬 Engagement Inbox":
    st.title("💬 Engagement Inbox 2.0")
    
    st.subheader("Unified Messages & Comments")
    
    messages = [
        {"platform": "Instagram", "user": "@jane.design", "text": "When is the next drop? ❤️", "time": "2 min ago"},
        {"platform": "X", "user": "@techguy22", "text": "This thread is gold!", "time": "18 min ago"},
        {"platform": "TikTok", "user": "@lifestylewithmia", "text": "Obsessed with this video 💯", "time": "45 min ago"}
    ]
    
    for msg in messages:
        with st.expander(f"{msg['platform']} • {msg['user']} • {msg['time']}"):
            st.write(msg['text'])
            reply = st.text_input("Your Reply", key=msg['user'])
            if st.button("Send Reply", key=f"reply_{msg['user']}"):
                st.success("Reply sent successfully!")

# ========================= TEAM COLLABORATION =========================
elif page == "👥 Team Collaboration":
    st.title("👥 Team Collaboration")
    
    col1, col2, col3 = st.columns(3)
    with col1: st.metric("Team Members Online", "8", "↑2")
    with col2: st.metric("Posts Pending Approval", "5")
    with col3: st.metric("Total Posts This Week", "47")
    
    st.checkbox("Enable Approval Workflow", value=True)
    st.selectbox("Assign Post for Review", ["Sarah (Designer)", "Mike (Content)", "Alex (Social Manager)"])

# ========================= ADVERTISING =========================
elif page == "📣 Advertising & Integrations":
    st.title("📣 Advertising & Integrations")
    
    st.slider("Monthly Ad Budget", 500, 10000, 2500, step=100)
    
    st.subheader("Connected Platforms")
    integrations = ["Salesforce", "Google Analytics", "Slack", "Zapier", "HubSpot", "Meta Ads", "LinkedIn Ads"]
    for integ in integrations:
        st.toggle(integ, value=True)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Hootsuite Simulator • Single File Streamlit App")
st.sidebar.caption("Built for demonstration purposes")
