from src.candidate.candidate_info import extract_candidate_info
from src.summary.summary_generator import generate_summary
import streamlit as st
from src.ats.ats_score import calculate_ats_score
import os

# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AI Resume Screening",
    page_icon="🤖",
    layout="wide"
)

# ----------------------------
# CUSTOM CSS
# ----------------------------
st.markdown("""
<style>

.main{
    background-color:#f5f7fa;
}

h1{
    color:#1f4e79;
}

div[data-testid="metric-container"]{
    background-color:white;
    border-radius:12px;
    padding:20px;
    box-shadow:0px 0px 10px rgba(0,0,0,0.1);
}

.skill-box{
    background:#E8F5E9;
    padding:10px;
    border-radius:8px;
    margin-bottom:8px;
    font-size:17px;
}

.missing-box{
    background:#FFEBEE;
    padding:10px;
    border-radius:8px;
    margin-bottom:8px;
    font-size:17px;
}

.status{
    font-size:25px;
    font-weight:bold;
    text-align:center;
    padding:15px;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ----------------------------
# TITLE
# ----------------------------

st.title("🤖 AI Resume Screening & Skill Gap Analyzer")

st.write(
    "Upload your Resume and Job Description to analyze ATS compatibility."
)

st.divider()

# ----------------------------
# FILE UPLOAD
# ----------------------------

col1, col2 = st.columns(2)

with col1:
    resume = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf"]
    )

with col2:
    jd = st.file_uploader(
        "📋 Upload Job Description",
        type=["txt"]
    )

st.write("")

analyze = st.button(
    "🚀 Analyze Resume",
    use_container_width=True
)

# ----------------------------
# ANALYSIS
# ----------------------------

if analyze:

    if resume is None or jd is None:

        st.error("Please upload both Resume and Job Description.")

    else:

        os.makedirs("uploads", exist_ok=True)

        resume_path = os.path.join(
            "uploads",
            resume.name
        )

        with open(resume_path, "wb") as f:
            f.write(resume.getbuffer())

        jd_path = os.path.join(
            "uploads",
            jd.name
        )

        with open(jd_path, "wb") as f:
            f.write(jd.getbuffer())

        result = calculate_ats_score(
            resume_path,
            jd_path
        )
        candidate = extract_candidate_info(
            result["Resume Text"]
    )

        st.success("✅ Resume Analysis Completed")
        st.divider()

        st.subheader("👤 Candidate Information")

        col1, col2 = st.columns(2)

        with col1:

            st.write("### 👤 Name")
            st.success(candidate["Name"])

            st.write("### 📧 Email")
            st.info(candidate["Email"])

            st.write("### 📱 Phone")
            st.info(candidate["Phone"])

        with col2:

            st.write("### 💻 GitHub")
            st.info(candidate["GitHub"])

            st.write("### 🔗 LinkedIn")
            st.info(candidate["LinkedIn"])

        st.divider()

        ats = result["ATS Score"]

        similarity = result["Similarity Score"]

        skill = result["Skill Score"]

        # ----------------------------
        # RESUME STATUS
        # ----------------------------

        if ats >= 85:
            status = "🟢 Excellent Resume"

        elif ats >= 70:
            status = "🟡 Good Resume"

        elif ats >= 50:
            status = "🟠 Average Resume"

        else:
            status = "🔴 Needs Improvement"

        st.markdown(
            f"""
            <div class='status'>
            {status}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        # ----------------------------
        # METRICS
        # ----------------------------

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "🎯 ATS Score",
            f"{ats:.2f}%"
        )

        c2.metric(
            "🤖 Similarity",
            f"{similarity:.2f}%"
        )

        c3.metric(
            "🧠 Skill Match",
            f"{skill:.2f}%"
        )

        st.divider()

        # ----------------------------
        # SKILLS
        # ----------------------------

        left, right = st.columns(2)

        with left:

            st.subheader("✅ Matched Skills")

            for s in result["Matched Skills"]:

                st.markdown(
                    f"""
                    <div class='skill-box'>
                    ✔ {s.title()}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        with right:

            st.subheader("❌ Missing Skills")

            for s in result["Missing Skills"]:

                st.markdown(
                    f"""
                    <div class='missing-box'>
                    ✘ {s.title()}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

        st.divider()

        # ----------------------------
        # SUMMARY
        # ----------------------------

        summary = generate_summary(
            ats,
            similarity,
            skill,
            result["Matched Skills"],
            result["Missing Skills"]
        )

        st.subheader("🧠 AI Resume Summary")

        st.success(summary)