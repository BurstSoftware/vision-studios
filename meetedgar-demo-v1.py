import streamlit as st
import pandas as pd
from datetime import datetime

# ====================== CONFIG ======================
st.set_page_config(
    page_title="MeetEdgar - Social Media Automation",
    page_icon="🚀",
    layout="wide"
)

# ====================== SESSION STATE ======================
if "posts" not in st.session_state:
    st.session_state.posts = pd.DataFrame({
        "id": [1, 2, 3],
        "content": [
            "How to 10x your productivity with automation 🔥",
            "The best marketing tip I learned in 2025",
            "Client success story: +340% engagement"
        ],
        "category": ["Productivity", "Marketing", "Success"],
        "last_posted": ["2025-06-10", "2025-06-05", "2025-05-28"],
        "times_posted": [12, 8, 15]
    })

# ====================== SIDEBAR ======================
st.sidebar.title("🚀 MeetEdgar")
st.sidebar.markdown("### Evergreen Social Media Manager")

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "📚 Content Library",
        "⏰ Scheduling & Queues",
        "🌐 Connected Platforms",
        "🔄 Content Feeds",
        "🤖 AI Assistant",
        "🔀 Variations & A/B Testing",
        "📊 Analytics"
    ]
)

# ====================== PAGES ======================

if page == "🏠 Home":
    st.title("🚀 Welcome to MeetEdgar")
    st.subheader("Set It Once. Post Forever.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Posts in Library", len(st.session_state.posts), "↑14 this month")
    with col2:
        st.metric("Posts Today", "18", "✅ 12 posted")
    with col3:
        st.metric("Active Platforms", "6")

    st.info("""
    **MeetEdgar** automatically recycles your evergreen content across all platforms.
    Build your library once → Let automation do the rest.
    """)
    st.success("✅ All systems running smoothly!")

elif page == "📚 Content Library":
    st.title("📚 Content Library")
    st.markdown("**Unlimited evergreen posts** — never delete anything again.")

    tab1, tab2 = st.tabs(["Browse Library", "➕ Add New Post"])

    with tab1:
        st.dataframe(
            st.session_state.posts,
            use_container_width=True,
            hide_index=True
        )

    with tab2:
        with st.form("new_post_form"):
            content = st.text_area("Post Content *")
            category = st.selectbox("Category", 
                ["Productivity", "Marketing", "Success", "Quotes", "Blog", "Personal"])
            col_a, col_b = st.columns(2)
            with col_a:
                image_url = st.text_input("Image URL (optional)")
            with col_b:
                link = st.text_input("Link (optional)")
            
            if st.form_submit_button("Add to Evergreen Library"):
                if content.strip():
                    new_post = pd.DataFrame([{
                        "id": len(st.session_state.posts) + 1,
                        "content": content,
                        "category": category,
                        "last_posted": "Never",
                        "times_posted": 0
                    }])
                    st.session_state.posts = pd.concat([st.session_state.posts, new_post], ignore_index=True)
                    st.success("✅ Post added to your evergreen library!")
                else:
                    st.error("Please write some content.")

elif page == "⏰ Scheduling & Queues":
    st.title("⏰ Scheduling & Queues")
    st.markdown("Set recurring schedules by category")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("Active Queues")
        queues = [
            "Monday Motivation → Productivity → 9:00 AM",
            "Content Tuesday → Blog → 11:00 AM",
            "Wisdom Wednesday → Quotes → 2:00 PM",
            "Throwback Thursday → Success → 10:00 AM"
        ]
        for q in queues:
            st.success(q)

    with col2:
        st.subheader("Create New Queue")
        category = st.selectbox("Category", ["Productivity", "Marketing", "Quotes", "Success"])
        day = st.selectbox("Day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
        time = st.time_input("Time", value=datetime.strptime("09:00", "%H:%M").time())
        
        if st.button("Create Queue"):
            st.success(f"✅ New queue created: **{day} at {time}** for **{category}**")

    st.info("Next 7 days: **24 posts** scheduled automatically")

elif page == "🌐 Connected Platforms":
    st.title("🌐 Connected Platforms")
    platforms = {
        "Facebook": "✅ Page + Groups",
        "Instagram": "✅ Feed + Stories",
        "LinkedIn": "✅ Profile + Company Page",
        "X (Twitter)": "✅ Connected",
        "Pinterest": "✅ Connected",
        "Bluesky": "✅ Connected"
    }
    for name, status in platforms.items():
        st.success(f"**{name}** — {status}")

elif page == "🔄 Content Feeds":
    st.title("🔄 Content Feeds & Auto Imports")
    st.subheader("Currently Connected Feeds")
    feeds = ["https://yourblog.com/feed", "YouTube Channel: @YourChannel", "Podcast RSS Feed"]
    for feed in feeds:
        st.write(f"✅ {feed}")

    st.subheader("Add New Feed")
    new_feed = st.text_input("RSS / Blog / YouTube / Podcast URL")
    if st.button("Connect Feed"):
        st.success("✅ Feed connected! New content will be automatically imported.")

elif page == "🤖 AI Assistant":
    st.title("🤖 AI Assistant (Inky)")
    prompt = st.text_area("What would you like to post about?", 
                         placeholder="e.g. Productivity tips for entrepreneurs")
    
    if st.button("Generate Post Ideas"):
        st.subheader("Generated Variations")
        st.write("**1.** 🔥 Just discovered a system that saves me 15 hours every week...")
        st.write("**2.** The one productivity hack that changed everything in 2025")
        st.write("**3.** Stop posting every day. Do this instead →")
        st.success("Ready to add any of these to your library?")

elif page == "🔀 Variations & A/B Testing":
    st.title("🔀 Content Variations & A/B Testing")

    original = st.text_input("Original Caption", "How to grow your social media in 2025")
    
    st.subheader("Generated Variations")
    st.write("**A:** The 2025 strategy that grew my account by 340%")
    st.write("**B:** Stop posting daily if you want real growth")
    st.write("**C:** One simple change that 10x’d my engagement")

    if st.button("Simulate A/B Test"):
        data = pd.DataFrame({
            "Variation": ["A", "B", "C"],
            "Engagement": [1240, 1890, 980]
        })
        st.bar_chart(data.set_index("Variation"), use_container_width=True)
        st.success("**Variation B is winning!**")

elif page == "📊 Analytics":
    st.title("📊 Analytics & Insights")

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Reach", "48.2K", "↑18%")
    with col2: st.metric("Avg. Engagement", "1,240", "↑9%")
    with col3: st.metric("Posts Published", "187")
    with col4: st.metric("Best Day", "Wednesday")

    # Engagement by Platform
    data = pd.DataFrame({
        "Platform": ["Instagram", "LinkedIn", "X", "Facebook", "Pinterest"],
        "Engagement": [2450, 1890, 1240, 980, 670]
    })
    
    st.subheader("Engagement by Platform")
    st.bar_chart(data.set_index("Platform"), use_container_width=True)

# ====================== FOOTER ======================
st.sidebar.markdown("---")
st.sidebar.caption("MeetEdgar Demo • Single-file • Streamlit + Pandas only")
