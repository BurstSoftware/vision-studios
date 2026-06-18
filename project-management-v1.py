import streamlit as st
import pandas as pd
from datetime import date
import uuid

# ====================== CONFIG ======================
st.set_page_config(
    page_title="Vision Studios • Project Hub",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CUSTOM CSS ======================
st.markdown("""
<style>
    .main { background-color: #0f0f1a; color: #e0e0ff; }
    .stButton>button {
        background-color: #6366f1;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        font-weight: 600;
    }
    .metric-card {
        background-color: #1a1a2e;
        padding: 1.2rem;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
    }
    h1, h2, h3 { color: #c4c4ff; }
</style>
""", unsafe_allow_html=True)

# ====================== SESSION STATE ======================
if 'projects' not in st.session_state:
    st.session_state.projects = pd.DataFrame({
        'id': ['P001', 'P002', 'P003'],
        'name': ['CyberForge Trailer', 'Neon Realms Game', 'Echoes of Eternity'],
        'description': ['Cinematic trailer for upcoming AAA title', 
                       'Open-world cyberpunk RPG', 
                       'Sci-fi narrative adventure'],
        'start_date': ['2025-11-01', '2025-09-15', '2026-01-10'],
        'end_date': ['2026-02-28', '2026-06-30', '2026-08-15'],
        'status': ['In Progress', 'Planning', 'In Progress'],
        'progress': [65, 25, 40]
    })

if 'tasks' not in st.session_state:
    st.session_state.tasks = pd.DataFrame({
        'id': ['T001', 'T002', 'T003', 'T004'],
        'project_id': ['P001', 'P001', 'P002', 'P003'],
        'title': ['Storyboard finalization', 'Voice-over recording', 
                 'Character concept art', 'Level design doc'],
        'assignee': ['Alex Rivera', 'Jordan Kim', 'Sam Chen', 'Taylor Brooks'],
        'status': ['Done', 'In Progress', 'To Do', 'In Progress'],
        'due_date': ['2025-12-15', '2026-01-10', '2025-12-20', '2026-02-05']
    })

if 'team' not in st.session_state:
    st.session_state.team = pd.DataFrame({
        'id': ['E001', 'E002', 'E003', 'E004'],
        'name': ['Alex Rivera', 'Jordan Kim', 'Sam Chen', 'Taylor Brooks'],
        'role': ['Creative Director', 'Sound Designer', 
                'Concept Artist', 'Lead Game Designer'],
        'email': ['alex@visionstudios.com', 'jordan@visionstudios.com',
                 'sam@visionstudios.com', 'taylor@visionstudios.com']
    })

# ====================== SIDEBAR ======================
st.sidebar.image("https://via.placeholder.com/180x180/6366f1/ffffff?text=VISION", width=180)
st.sidebar.title("Vision Studios")
st.sidebar.markdown("### Project Management")

page = st.sidebar.selectbox(
    "Navigate",
    ["Dashboard", "Projects", "Tasks", "Team", "Reports"]
)

st.sidebar.markdown("---")
st.sidebar.caption("Vision Studios PM v2.0")

# ====================== DASHBOARD ======================
if page == "Dashboard":
    st.title("🌟 Project Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Active Projects", len(st.session_state.projects))
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Total Tasks", len(st.session_state.tasks))
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        completed = len(st.session_state.tasks[st.session_state.tasks['status'] == 'Done'])
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Completed Tasks", completed)
        st.markdown('</div>', unsafe_allow_html=True)

    with col4:
        avg_progress = round(st.session_state.projects['progress'].mean(), 1)
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Average Progress", f"{avg_progress}%")
        st.markdown('</div>', unsafe_allow_html=True)

    st.subheader("Current Projects")
    display_df = st.session_state.projects[['name', 'status', 'progress', 'end_date']].copy()
    st.dataframe(display_df, use_container_width=True, hide_index=True)

    st.subheader("Upcoming Deadlines")
    upcoming = st.session_state.tasks[st.session_state.tasks['status'] != 'Done'].sort_values('due_date').head(6)
    st.dataframe(upcoming[['title', 'assignee', 'due_date', 'status']], 
                use_container_width=True, hide_index=True)

# ====================== PROJECTS ======================
elif page == "Projects":
    st.title("📁 All Projects")

    tab1, tab2 = st.tabs(["📋 Project List", "➕ New Project"])

    with tab1:
        st.dataframe(st.session_state.projects, use_container_width=True, hide_index=True)

    with tab2:
        with st.form("new_project_form"):
            st.subheader("Create New Project")
            name = st.text_input("Project Name *")
            desc = st.text_area("Description")
            col_a, col_b = st.columns(2)
            with col_a:
                start_date = st.date_input("Start Date", date.today())
            with col_b:
                end_date = st.date_input("Target End Date")
            
            status = st.selectbox("Status", ["Planning", "In Progress", "Completed"])
            progress = st.slider("Progress (%)", 0, 100, 10)

            if st.form_submit_button("Create Project"):
                if name:
                    new_id = f"P{100 + len(st.session_state.projects):03d}"
                    new_project = pd.DataFrame([{
                        'id': new_id,
                        'name': name,
                        'description': desc,
                        'start_date': start_date.strftime("%Y-%m-%d"),
                        'end_date': end_date.strftime("%Y-%m-%d"),
                        'status': status,
                        'progress': progress
                    }])
                    st.session_state.projects = pd.concat([st.session_state.projects, new_project], 
                                                        ignore_index=True)
                    st.success(f"✅ Project **{name}** created successfully!")
                    st.rerun()
                else:
                    st.error("Project name is required")

# ====================== TASKS ======================
elif page == "Tasks":
    st.title("✅ Tasks & Assignments")

    # Filter
    project_names = ["All Projects"] + list(st.session_state.projects['name'])
    selected_project = st.selectbox("Filter by Project", project_names)

    if selected_project != "All Projects":
        pid = st.session_state.projects[st.session_state.projects['name'] == selected_project]['id'].iloc[0]
        filtered_tasks = st.session_state.tasks[st.session_state.tasks['project_id'] == pid]
    else:
        filtered_tasks = st.session_state.tasks

    st.dataframe(filtered_tasks, use_container_width=True, hide_index=True)

    with st.expander("➕ Add New Task"):
        with st.form("new_task_form"):
            proj_name = st.selectbox("Project", st.session_state.projects['name'])
            proj_id = st.session_state.projects[st.session_state.projects['name'] == proj_name]['id'].iloc[0]

            title = st.text_input("Task Title")
            assignee = st.selectbox("Assignee", st.session_state.team['name'])
            due_date = st.date_input("Due Date")
            task_status = st.selectbox("Status", ["To Do", "In Progress", "Review", "Done"])

            if st.form_submit_button("Add Task"):
                new_task = pd.DataFrame([{
                    'id': f"T{1000 + len(st.session_state.tasks)}",
                    'project_id': proj_id,
                    'title': title,
                    'assignee': assignee,
                    'status': task_status,
                    'due_date': due_date.strftime("%Y-%m-%d")
                }])
                st.session_state.tasks = pd.concat([st.session_state.tasks, new_task], ignore_index=True)
                st.success("Task added successfully!")
                st.rerun()

# ====================== TEAM ======================
elif page == "Team":
    st.title("👥 Studio Team")

    st.dataframe(st.session_state.team, use_container_width=True, hide_index=True)

    with st.expander("➕ Add New Team Member"):
        with st.form("new_member_form"):
            name = st.text_input("Full Name")
            role = st.text_input("Role / Position")
            email = st.text_input("Email Address")
            
            if st.form_submit_button("Add Member"):
                new_member = pd.DataFrame([{
                    'id': f"E{100 + len(st.session_state.team)}",
                    'name': name,
                    'role': role,
                    'email': email
                }])
                st.session_state.team = pd.concat([st.session_state.team, new_member], ignore_index=True)
                st.success(f"{name} added to the team!")
                st.rerun()

# ====================== REPORTS ======================
elif page == "Reports":
    st.title("📊 Reports & Analytics")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Project Progress")
        st.bar_chart(st.session_state.projects.set_index('name')['progress'])

    with col2:
        st.subheader("Task Status Distribution")
        status_counts = st.session_state.tasks['status'].value_counts()
        st.bar_chart(status_counts)

    st.subheader("Workload by Team Member")
    workload = st.session_state.tasks['assignee'].value_counts()
    st.bar_chart(workload)

# Footer
st.markdown("---")
st.caption("© 2026 Vision Studios • Project Management System built with Streamlit")
