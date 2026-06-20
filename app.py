import streamlit as st

st.set_page_config(
    page_title="Marketing Intelligence Brief",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8fbff 0%, #eef4ff 45%, #fff7ed 100%);
}

.hero {
    padding: 2.2rem;
    border-radius: 24px;
    background: linear-gradient(135deg, #111827 0%, #1e3a8a 55%, #7c3aed 100%);
    color: white;
    box-shadow: 0 18px 45px rgba(30, 58, 138, 0.25);
    animation: fadeIn 1s ease-in-out;
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}

.hero p {
    font-size: 1.15rem;
    color: #e5e7eb;
}

.card {
    padding: 1.5rem;
    border-radius: 20px;
    background: white;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.08);
    border: 1px solid rgba(148, 163, 184, 0.25);
    margin-bottom: 1rem;
    animation: slideUp 0.7s ease-in-out;
}

.output-card {
    padding: 1.4rem;
    border-radius: 18px;
    background: #ffffff;
    border-left: 6px solid #2563eb;
    box-shadow: 0 10px 25px rgba(37, 99, 235, 0.12);
    margin-bottom: 1rem;
}

.badge {
    display: inline-block;
    padding: 0.35rem 0.7rem;
    border-radius: 999px;
    background: #dbeafe;
    color: #1d4ed8;
    font-weight: 600;
    margin-right: 0.4rem;
}

@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

@keyframes slideUp {
    from {opacity: 0; transform: translateY(18px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🧭 Consultant Toolkit")
    st.write("Use this interface to turn marketing topics into client-ready recommendations.")
    st.divider()
    st.markdown("**Workflow**")
    st.write("1. Enter a topic")
    st.write("2. Select a source")
    st.write("3. Choose priority")
    st.write("4. Generate brief")
    st.divider()
    st.info("Designed for technology consultants who need fast, readable marketing intelligence.")

st.markdown("""
<div class="hero">
    <h1>📈 Marketing Intelligence Brief</h1>
    <p>Turn marketing articles into practical, client-ready insights for technology consultants.</p>
    <span class="badge">Marketing Trends</span>
    <span class="badge">Consulting Insights</span>
    <span class="badge">Human-Readable Output</span>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

left, right = st.columns([1.1, 0.9])

with left:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Input")
    topic = st.text_input(
        "Marketing topic or article title",
        placeholder="Example: AI search optimization, social media strategy, content marketing trends"
    )

    source = st.selectbox(
        "Source",
        [
            "HubSpot",
            "Sprout Social",
            "Hootsuite",
            "Social Media Examiner",
            "Search Engine Journal",
            "Other / Unknown"
        ]
    )

    priority = st.selectbox(
        "Priority level",
        ["High", "Medium", "Low"]
    )

    generate = st.button("✨ Generate Marketing Intelligence Brief")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("What this tool produces")
    st.write("A structured brief that a non-technical user can read and use.")
    st.write("✅ Topic")
    st.write("✅ Source")
    st.write("✅ Priority")
    st.write("✅ Trend Summary")
    st.write("✅ Why It Matters")
    st.write("✅ Consultant Recommendation")
    st.markdown('</div>', unsafe_allow_html=True)

if generate:
    if topic.strip() == "":
        st.error("Please enter a marketing topic or article title before generating the brief.")

    elif source == "Other / Unknown":
        st.warning(
            "The source is unknown. Please verify the original article before using this brief for client recommendations."
        )

    else:
        st.success("Marketing intelligence brief generated successfully.")

        col1, col2, col3 = st.columns(3)
        col1.metric("Source", source)
        col2.metric("Priority", priority)
        col3.metric("Status", "Ready")

        st.markdown(f"""
        <div class="output-card">
            <h3>1. Selected Topic</h3>
            <p>{topic}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="output-card">
            <h3>2. Trend Summary</h3>
            <p>This topic suggests that <b>{topic}</b> may be important for current marketing strategy. 
            The source, <b>{source}</b>, should be reviewed to confirm the original context before using the insight.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="output-card">
            <h3>3. Why It Matters</h3>
            <p>For technology consultants, this information can help connect marketing trends to client needs, 
            especially when clients are trying to improve digital visibility, content planning, or customer engagement.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="output-card">
            <h3>4. Consultant Recommendation</h3>
            <p>Use this insight as a starting point for client discussion. Review the original article, identify whether 
            the trend applies to the client’s industry, and decide whether it should influence marketing or technology strategy.</p>
        </div>
        """, unsafe_allow_html=True)

else:
    st.info("Enter a topic, select a source, and click the button to generate a human-readable marketing intelligence brief.")
