import streamlit as st
import pandas as pd
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Business Reality Assessment Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .metric-card {
        background-color: #f8fafc;
        padding: 1rem;
        border-radius: 0.5rem;
        border: 1px solid #e2e8f0;
    }
    .alert-red { color: #c53030; font-weight: bold; }
    .section-header {
        color: #1a365d;
        border-bottom: 2px solid #2b6cb0;
        padding-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("📊 Business Reality Assessment & Cumulative Net Loss Analysis")
st.caption(f"Internal Planning Dashboard | As of {datetime.now().strftime('%B %d, %Y')} | Confidential")

st.divider()

# ==================== KEY METRICS ====================
st.header("Key Financial Metrics at a Glance")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Total Current Liabilities", value="$313,160", delta="Critical", delta_color="inverse")
with col2:
    st.metric(label="Weekly Burn Rate", value="$6,000", delta="6 people × $1,000", delta_color="off")
with col3:
    st.metric(label="Cumulative Labor Burn", value="$146,580", delta="Jan 1 – Jun 20, 2026", delta_color="off")
with col4:
    st.metric(label="Net Position", value="Deeply Negative", delta="Only Liabilities", delta_color="inverse")

st.caption("All figures reflect current liabilities because no moneys has been paid as agreed for the products produced.")

st.divider()

# ==================== TABS ====================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📋 Executive Overview", 
    "👥 Team Status", 
    "💰 Financial Breakdown", 
    "🚀 Recommended Actions",
    "📄 Source Document"
])

# ==================== TAB 1: EXECUTIVE OVERVIEW ====================
with tab1:
    st.subheader("Current Operational & Leadership Status", divider="blue")
    st.markdown("The business is currently in a **pre-revenue, non-operational distressed state** with significant accumulated liabilities.")
    
    st.markdown("### Key Facts")
    facts = [
        "**Owner (Jason)** — Not actively present or engaged in day-to-day operations.",
        "**No events booked** — Zero pipeline of revenue-generating work.",
        "**Digital presence nonexistent** — Social media accounts, website, and business listing pages are not active or up to date.",
        "**President (Dan)** — Does not have a dedicated office. Has not been running regular meetings or actively meeting/recruiting new talent.",
        "**Studio equipment & engineering** — The studio has been operating with gear and music equipment belonging to Colin (external engineer/producer).",
        "**Colin status** — Not considered a strong long-term cultural or strategic fit with the team. He is completing work on a record and will be parting ways at the end of June 2026.",
        "**Cash flow** — **$0** (no revenue).",
        "**Overall position** — **Only liabilities** on the books with no offsetting assets or revenue streams currently active.",
        "**New team additions** — Tyler (Editor & Audio Technician) and a Social Media Expert (former day laborer) have been added."
    ]
    
    for fact in facts:
        st.markdown(f"• {fact}")
    
    st.warning("**Critical**: The current trajectory is not sustainable. Major decisions regarding leadership, structure, assets (Colin's gear), and go-forward strategy are required immediately.")

# ==================== TAB 2: TEAM STATUS ====================
with tab2:
    st.subheader("Detailed Team Status — June 22, 2026", divider="blue")
    
    team_data = {
        "Name": ["Jason", "Dan", "Ryan", "Zack", "Colin", "Social Media Expert*"],
        "Title": [
            "Owner", "President", "A&R (Artists and Repertoire)", "Videographer",
            "Engineer / Producer", "Social Media Expert (former day laborer)"
        ],
        "Current Status": [
            "Absent / Not Engaged", "Not On-Site", "Available", "Available",
            "Departing June 30", "New Addition"
        ],
        "Key Details": [
            "No active involvement in operations or leadership",
            "No dedicated office; not running meetings; not meeting new talent",
            "Scouting talent & overseeing artistic development of recording artists — vital bridge between creative vision and commercial goals",
            "Core creative role; activity level not detailed",
            "Owns gear & music equipment; not strong team fit; finishing record",
            "*Name placeholder — recently joined to build website, social media presence, and online visibility"
        ]
    }
    
    df_team = pd.DataFrame(team_data)
    
    def color_status(val):
        if "Absent" in str(val) or "Not On-Site" in str(val) or "Departing" in str(val):
            return "background-color: #fed7d7; color: #c53030"
        elif "New Addition" in str(val):
            return "background-color: #c6f6d5; color: #276749"
        else:
            return "background-color: #ebf8ff"
    
    styled_df = df_team.style.map(color_status, subset=["Current Status"])
    st.dataframe(styled_df, use_container_width=True, hide_index=True)
    
    st.caption("* Social Media Expert's actual name is a placeholder. Tyler is accounted for financially but removed from this overview.")

    with st.expander("📖 What is A&R (Artists and Repertoire)?"):
        st.info("""
        **A&R (Artists and Repertoire)** is the department responsible for scouting talent and overseeing the artistic development of recording artists. 
        They act as the vital bridge between creative vision and commercial goals.
        """)

# ==================== TAB 3: FINANCIAL BREAKDOWN ====================
with tab3:
    st.subheader("Financial Reality — Current Liabilities", divider="blue")
    st.error("**Important**: No moneys has been paid as agreed for the products produced. All items below are classified as **current liabilities**.")
    
    st.markdown("### Total Current Liabilities Breakdown")
    liabilities_data = {
        "Item": ["Labor-related accrued liabilities (6 people)", "Tools & equipment unpaid liability",
                 "Amounts due for products produced (sound recordings)", "TOTAL CURRENT LIABILITIES"],
        "Amount": ["$146,580", "$20,000", "$146,580", "$313,160"],
        "Notes": [
            "Unpaid / accrued since Jan 1, 2026 — no cash paid as agreed",
            "Additional current liability — tools/equipment",
            "No payment made as agreed for produced recordings/products — current liability",
            "Labor + tools + unpaid amounts for products produced"
        ]
    }
    
    df_liab = pd.DataFrame(liabilities_data)
    def highlight_total(row):
        if row["Item"] == "TOTAL CURRENT LIABILITIES":
            return ["background-color: #fed7d7; font-weight: bold"] * len(row)
        return [""] * len(row)
    
    styled_liab = df_liab.style.apply(highlight_total, axis=1)
    st.dataframe(styled_liab, use_container_width=True, hide_index=True)
    
    st.divider()
    st.markdown("### Labor Burn Detail (6 People)")
    
    labor_data = {
        "Team Member": ["Dan", "Ryan", "Zack", "Colin", "Tyler", "Social Media Expert (Alex*)"],
        "Role": ["President", "A&R (Artists and Repertoire)", "Videographer", "Engineer / Producer",
                 "Editor & Audio Technician", "Social Media Expert"],
        "Weekly Cost": ["$1,000"] * 6,
        "Weeks": ["24.43"] * 6,
        "Cumulative Cost": ["$24,430"] * 6
    }
    
    df_labor = pd.DataFrame(labor_data)
    st.dataframe(df_labor, use_container_width=True, hide_index=True)
    st.caption("Tyler is included in financial calculations as he is still part of the current labor cost.")

# ==================== TAB 4: RECOMMENDED ACTIONS ====================
with tab4:
    st.subheader("Recommended Immediate Actions", divider="blue")
    
    actions = [
        ("1. Ownership & Leadership Decision", 
         "Jason and Dan must clarify commitment level and presence. Either establish consistent on-site leadership or formally appoint an acting operator."),
        ("2. Colin Transition Plan (Urgent — by June 30)", 
         "Decide whether to purchase Colin's gear/equipment, negotiate transition, or accept loss of studio capability."),
        ("3. Digital Presence Launch (Within 7–14 days)", 
         "Leverage the Social Media Expert to immediately deploy website and active social channels."),
        ("4. Define the Business Clearly", 
         "Write a one-paragraph positioning statement: What do we sell, to whom, and why are we different?"),
        ("5. 90-Day Revenue Plan or Pause Decision", 
         "Create a realistic plan to book paying work within 90 days or consider pause/wind-down."),
        ("6. Financial Cleanup", 
         "Compile full list of liabilities and receivables before any external discussions.")
    ]
    
    for title, desc in actions:
        with st.expander(title, expanded=False):
            st.write(desc)
    
    st.divider()
    st.error("**FINAL NOTE**: The business is accumulating loss. Decisive action is required immediately.")

# ==================== TAB 5: SOURCE DOCUMENT ====================
with tab5:
    st.subheader("📄 Original Source Document", divider="blue")
    st.markdown("### Business Assessment & Net Loss Report – June 2026")
    
    pdf_raw = "https://raw.githubusercontent.com/BurstSoftware/vision-studios/main/Business_Assessment_Net_Loss_Report_June2026.pdf"
    pdf_blob = "https://github.com/BurstSoftware/vision-studios/blob/main/Business_Assessment_Net_Loss_Report_June2026.pdf"
    
    st.markdown(f"""
    **Direct PDF** → [Open / Download]({pdf_raw})  
    **GitHub Page** → [View on GitHub]({pdf_blob})
    """)
    
    st.info("💡 Use the **Direct PDF** link for the best viewing and downloading experience.")
    st.caption("This interactive dashboard was built from the above report.")

# ==================== SIDEBAR ====================
with st.sidebar:
    st.header("Quick Navigation")
    st.markdown("""
    - Executive Overview
    - Team Status
    - Financial Breakdown
    - Recommended Actions
    - Source Document
    """)
    st.divider()
    st.caption("**Data Period**: January 1 – June 20, 2026")
    st.caption("**Rate Used**: $25/person/hour × 40 hrs/week")
    st.caption("**Last Updated**: June 22, 2026")

st.sidebar.info("Run with:\n`streamlit run business_reality_dashboard.py`")
