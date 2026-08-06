"""
ui.py

Streamlit UI for Curriculum Designer MVP
"""

import json

import requests
import streamlit as st

# --------------------------------------------------
# Configuration
# --------------------------------------------------

API_URL = "http://127.0.0.1:8000/generate"

st.set_page_config(
    page_title="Curriculum Designer",
    page_icon="🎓",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🎓 Curriculum Designer")
st.caption("Generate industry-ready curricula using LLMs")

st.divider()

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.header("⚙️ Course Details")

    subject = st.text_input(
        "📘 Subject",
        value="AI Mastery"
    )

    target_audience = st.text_input(
        "👨‍🎓 Target Audience",
        value="Third Year Computer Science Engineering Students"
    )

    prerequisites = st.text_area(
        "📚 Prerequisites",
        value="Python, Data Structures, Operating Systems, DBMS"
    )

    duration = st.number_input(
        "⏱️ Duration (Hours)",
        min_value=10,
        max_value=1000,
        value=200,
        step=10,
    )

    st.divider()

    generate = st.button(
        "🚀 Generate Curriculum",
        use_container_width=True,
    )

# --------------------------------------------------
# Main Area
# --------------------------------------------------

if generate:

    payload = {
        "subject": subject,
        "target_audience": target_audience,
        "prerequisites": prerequisites,
        "duration": duration,
    }

    with st.spinner("🤖 Designing curriculum..."):

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=300,
            )

            response.raise_for_status()

            curriculum = response.json()

            st.success("✅ Curriculum generated successfully!")

            st.divider()

            # --------------------------------------------------
            # Course Information
            # --------------------------------------------------

            st.header("📖 Course Information")

            col1, col2 = st.columns(2)

            with col1:
                st.metric(
                    "📘 Course",
                    curriculum.get("course_title", "")
                )

            with col2:
                st.metric(
                    "⏱️ Duration",
                    f"{curriculum.get('duration_hours', 0)} Hours"
                )

            # --------------------------------------------------
            # Modules
            # --------------------------------------------------

            st.divider()

            st.header("🧩 Modules")

            modules = curriculum.get("modules", [])

            for module in modules:

                with st.expander(
                    f"📦 Module {module['module_number']} - {module['module_title']}"
                ):

                    st.subheader("📌 Topics")

                    for topic in module["sub_topics"]:
                        st.write(f"• {topic}")

                    st.subheader("💻 Hands-on")

                    for item in module["hands_on"]:
                        st.write(f"✅ {item}")

            # --------------------------------------------------
            # Daily Plan
            # --------------------------------------------------

            st.divider()

            st.header("🗓️ Daily Plan")

            st.dataframe(
                curriculum.get("daily_plan", []),
                use_container_width=True,
                hide_index=True,
            )

            # --------------------------------------------------
            # Capstone
            # --------------------------------------------------

            capstone = curriculum.get("capstone_project", {})

            st.divider()

            st.header("🏆 Capstone Project")

            st.subheader(capstone.get("title", ""))

            st.write(capstone.get("description", ""))

            st.subheader("🎯 Objective")

            st.write(capstone.get("objective", ""))

            st.subheader("⭐ Features")

            for feature in capstone.get("features", []):

                st.write(f"✅ {feature}")

            st.subheader("📦 Deliverables")

            for item in capstone.get("deliverables", []):

                st.write(f"📄 {item}")

            # --------------------------------------------------
            # Raw JSON
            # --------------------------------------------------

            with st.expander("🔍 View Raw JSON"):

                st.code(
                    json.dumps(curriculum, indent=4),
                    language="json",
                )

        except Exception as ex:

            st.error(str(ex))

else:

    st.info("👈 Enter the course details in the sidebar and click **Generate Curriculum**.")