import streamlit as st
import json
from streamlit_echarts import st_echarts
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

# Function to create a pseudo TOC
def create_toc():
    st.sidebar.title("Table of Contents")
    if st.sidebar.button("Introduction"):
        st.session_state['location'] = 'introduction'
    if st.sidebar.button("Data Overview"):
        st.session_id['location'] = 'data_overview'
    if st.sidebar.button("Analysis"):
        st.session_state['location'] = 'analysis'
    if st.sidebar.button("Conclusion"):
        st.session_state['location'] = 'conclusion'


# Set page config
st.set_page_config(page_title="My Streamlit App with TOC", layout="wide")

# Initialize session state for navigation
if 'location' not in st.session_state:
    st.session_state['location'] = 'introduction'

# Display TOC in sidebar
create_toc()

# Content sections
if st.session_state['location'] == 'introduction':
    st.header("Introduction")
    st.write("This is the introduction section.")

if st.session_state['location'] == 'data_overview':
    st.header("Data Overview")
    st.write("This section provides an overview of the data.")

if st.session_state['location'] == 'analysis':
    st.header("Analysis")
    st.write("This section is for the analysis.")

if st.session_state['location'] == 'conclusion':
    st.header("Conclusion")
    st.write("This is the conclusion section.")
    


# st.set_page_config(layout="wide")
# add_page_title(ayout="wide")

# show_pages(
#     [   
#         Page("dezoomcamp/streamlit_app.py", "NotJustWeb: Fine-Grained Web and Non-Web Dataset in Large Scale", "💻"),

#         # # Web Data
#         Section("Web Data", "📄"),
#         Page("dezoomcamp/2024_cohort/Course_Overview.py", "Course Overview", "📚", in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_1_Introduction_&_Prerequisites.py", "Module 1 Introduction & Prerequisites", "1️⃣", in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_2_Workflow_Orchestration.py", "Module 2 Workflow Orchestration", "2️⃣", in_section=True),
#         Page("dezoomcamp/2024_cohort/Workshop_1_Data_Ingestion.py", "Workshop 1 Data Ingestion", "🛠️", in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_3_Data_Warehouse.py", "Module 3 Data Warehouse and BigQuery", "3️⃣", in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_4_Analytics_Engineering.py", "Module 4 Analytics Engineering", "4️⃣", in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_5_Batch_Processing.py", "Module 5 Batch Processing", "5️⃣", in_section=True),
#         Page("dezoomcamp/2024_cohort/Workshop_2_Stream_Processing_with_SQL.py", "Workshop 2 Stream Processing with SQL", "🛠️", in_section=True),
#         Page("dezoomcamp/2024_cohort/Module_6_Stream_Processing.py", "Module 6 Stream Processing", "6️⃣", in_section=True),
#         Page("dezoomcamp/2024_cohort/Course_Project.py", "Course Project", "🏆", in_section=True),

#         # Non-Web Data
#         Section("Non-Web Data", "📚"),
#         Page("dezoomcamp/2023_cohort/Course_Overview.py", "Course Overview", "📚", in_section=True),
#         Page("dezoomcamp/2023_cohort/Week_1_Introduction_&_Prerequisites.py", "Week 1 Introduction & Prerequisites", "1️⃣", in_section=True),
#         Page("dezoomcamp/2023_cohort/Week_2_Workflow_Orchestration.py", "Week 2 Workflow Orchestration", "2️⃣", in_section=True),
#         Page("dezoomcamp/2023_cohort/Week_3_Data_Warehouse.py", "Week 3 Data Warehouse", "3️⃣", in_section=True),
#         Page("dezoomcamp/2023_cohort/Week_4_Analytics_Engineering.py", "Week 4 Analytics Engineering", "4️⃣", in_section=True),
#         Page("dezoomcamp/2023_cohort/Week_5_Batch_Processing.py", "Week 5 Batch Processing", "5️⃣", in_section=True),
#         Page("dezoomcamp/2023_cohort/Week_6_Stream_Processing.py", "Week 6 Stream Processing", "6️⃣", in_section=True),
#         Page("dezoomcamp/2023_cohort/Week_7_Project.py", "Week 7 Project", "7️⃣", in_section=True),
#         Page("dezoomcamp/2023_cohort/Homework_Quizzes.py", "Homework Quizzes", "📝", in_section=True),
        
#         Page("dezoomcamp/Datasets.py", "Datasets", icon="💾", in_section=False),
#         Page("dezoomcamp/Certificate.py", "Certificate", "📜", in_section=False),
#         Page("dezoomcamp/FAQ.py", "FAQ", "❔", in_section=False),
#         Page("dezoomcamp/Contact.py", "Contact", icon="📩", in_section=False),   
#         Page("dezoomcamp/Contact_thanks.py", "Thank you", icon="💌"),   
#         Page("dezoomcamp/About.py", "About", icon="🖼️", in_section=False) 
#     ]
# )

# hide_pages(["Thank you"])

# st.markdown("### 👨‍🔧 Data Engineering Zoomcamp by [DataTalksClub](https://datatalks.club/)")

# st.image("https://pbs.twimg.com/media/FmmYA2YWYAApPRB.png")

# st.info("Original Course Repository on [Github](https://github.com/DataTalksClub/data-engineering-zoomcamp)")

# st.markdown("---")


# with open("dezoomcamp/data/web_filter_pipeline.json", "r") as f:
#     data = json.loads(f.read())

# option = {
#     "title": {"text": "Web Data Processing Pipeline"},
#     "tooltip": {"trigger": "item", "triggerOn": "mousemove"},
#     "series": [
#         {
#             "type": "sankey",
#             "data": data["nodes"],
#             "links": data["links"],
#             "": {"focus": "adjacency"},
#             "levels": [
#                 {
#                     "depth": 0,
#                     "itemStyle": {"color": "#EE635F"},
#                     "lineStyle": {"color": "source", "opacity": 0.6},
#                 },
#                 {
#                     "depth": 1,
#                     "itemStyle": {"color": "#EE915F"},
#                     "lineStyle": {"color": "source", "opacity": 0.6},
#                 },
#                 {
#                     "depth": 2,
#                     "itemStyle": {"color": "#EEBE5F"},
#                     "lineStyle": {"color": "source", "opacity": 0.6},
#                 },
#                 {
#                     "depth": 3,
#                     "itemStyle": {"color": "#EED65F"},
#                     "lineStyle": {"color": "source", "opacity": 0.6},
#                 },
#                 {
#                     "depth": 4,
#                     "itemStyle": {"color": "#E5EE5F"},
#                     "lineStyle": {"color": "source", "opacity": 0.6},
#                 },
#                 {
#                     "depth": 5,
#                     "itemStyle": {"color": "#C5EE5F"},
#                     "lineStyle": {"color": "source", "opacity": 0.6},
#                 },
#                 {
#                     "depth": 6,
#                     "itemStyle": {"color": "#8CEE5F"},
#                     "lineStyle": {"color": "source", "opacity": 0.6},
#                 },
#                 {
#                     "depth": 7,
#                     "itemStyle": {"color": "#5FEE6C"},
#                     "lineStyle": {"color": "source", "opacity": 0.6},
#                 },
#                 {
#                     "depth": 8,
#                     "itemStyle": {"color": "#5FEEC7"},
#                     "lineStyle": {"color": "source", "opacity": 0.6},
#                 },
#             ],
#             "lineStyle": {"curveness": 0.5},
#             "label": {
#                     "position": 'inside'
#                 }
#         }
#     ],
# }
# st_echarts(option, height="500px")






# st.markdown("---")

# with st.expander("Sign up here for 2024 Cohort"):
#     st.markdown("""
    
#     <a href="https://airtable.com/appzbS8Pkg9PL254a/shr6oVXeQvSI5HuWD"><img src="https://user-images.githubusercontent.com/875246/185755203-17945fd1-6b64-46f2-8377-1011dcb1a444.png" height="50" /></a>

#     #

#     - Register in [DataTalks.Club's Slack](https://datatalks.club/slack.html)
#     - Join the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel
#     - Join the [course Telegram channel with announcements](https://t.me/dezoomcamp)
#     - The videos are published on [DataTalks.Club's YouTube channel](https://www.youtube.com/c/DataTalksClub) in [the course playlist](https://www.youtube.com/playlist?list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
#     - [Frequently asked technical questions](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing)
        
#     #""", unsafe_allow_html=True)

# st.markdown("""
# ### 👨‍🎓 Taking the course

# ##### 👨‍👦‍👦 2024 Cohort

# * **Start**: 15 January 2024 (Monday) at 17:00 CET
# * **Registration link**: https://airtable.com/shr6oVXeQvSI5HuWD
# * [Cohort folder](cohorts/2024/) with homeworks and deadlines 


# ##### 👨‍🔧 Self-paced mode

# All the materials of the course are freely available, so that you
# can take the course at your own pace

# * Follow the suggested syllabus (see below) week by week
# * You don't need to fill in the registration form. Just start watching the videos and join Slack
# * Check [FAQ](https://docs.google.com/document/d/19bnYs80DwuUimHM65UV3sylsCn2j1vziPOwzBwQrebw/edit?usp=sharing) if you have problems
# * If you can't find a solution to your problem in FAQ, ask for help in Slack

# ### 🔎 Overview""", unsafe_allow_html=True)


# st.image("https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/images/architecture/photo1700757552.jpeg")


# st.markdown("""
# ### 📓 Prerequisites

# To get the most out of this course, you should feel comfortable with coding and command line
# and know the basics of SQL. Prior experience with Python will be helpful, but you can pick
# Python relatively fast if you have experience with other programming languages.

# Prior experience with data engineering is not required.

# ### 👨‍🏫 Instructors

# - [Ankush Khanna](https://linkedin.com/in/ankushkhanna2)
# - [Victoria Perez Mola](https://www.linkedin.com/in/victoriaperezmola/)
# - [Alexey Grigorev](https://linkedin.com/in/agrigorev)
# - [Matt Palmer](https://www.linkedin.com/in/matt-palmer/)
# - [Luis Oliveira](https://www.linkedin.com/in/lgsoliveira/)
# - [Michael Shoemaker](https://www.linkedin.com/in/michaelshoemaker1/)

# Past instructors:

# - [Sejal Vaidya](https://www.linkedin.com/in/vaidyasejal/)
# - [Irem Erturk](https://www.linkedin.com/in/iremerturk/)

# ### ❔ Asking for help in Slack

# The best way to get support is to use [DataTalks.Club's Slack](https://datatalks.club/slack.html). Join the [`#course-data-engineering`](https://app.slack.com/client/T01ATQK62F8/C01FABYF2RG) channel.

# To make discussions in Slack more organized:

# * Follow [these recommendations](asking-questions.md) when asking for help
# * Read the [DataTalks.Club community guidelines](https://datatalks.club/slack/guidelines.html)

# ---
            
# ### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=hamagistral&repo=de-zoomcamp-ui&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
            
# ##### 🖼️ Course UI was made by [Hamagistral](https://github.com/Hamagistral) 
# """, unsafe_allow_html=True)

# hide_streamlit_style = """
# <style>
# #MainMenu {visibility: hidden;}
# footer {visibility: hidden;}
# </style>
# """

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 