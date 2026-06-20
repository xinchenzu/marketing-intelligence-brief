import streamlit as st

st.set_page_config(
    page_title="Marketing Intelligence Brief",
    page_icon="✨",
    layout="wide"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, rgba(255, 105, 180, 0.28), transparent 30%),
        radial-gradient(circle at top right, rgba(0, 229, 255, 0.25), transparent 28%),
        radial-gradient(circle at bottom left, rgba(255, 214, 10, 0.25), transparent 30%),
        linear-gradient(135deg, #fff7fb 0%, #f5fbff 45%, #fffdf2 100%);
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ffffff 0%, #fff3fb 100%);
    border-right: 1px solid rgba(255, 105, 180, 0.18);
}

.main .block-container {
    padding-top: 2rem;
    max-width: 1180px;
}

.hero {
    position: relative;
    padding: 3rem;
    border-radius: 34px;
    overflow: hidden;
    background:
        linear-gradient(135deg, rgba(255, 94, 174, 0.95), rgba(124, 77, 255, 0.95) 45%, rgba(0, 216, 255, 0.95));
    color: white;
    box-shadow: 0 28px 70px rgba(124, 77, 255, 0.28);
    animation: floatIn 0.9s ease-out;
}

.hero:before {
    content: "";
    position: absolute;
    width: 260px;
    height: 260px;
    right: -60px;
    top: -70px;
    background: rgba(255,255,255,0.25);
    border-radius: 50%;
    filter: blur(2px);
}

.hero:after {
    content: "";
    position: absolute;
    width: 180px;
    height: 180px;
    left: 55%;
    bottom: -90px;
    background: rgba(255, 255, 255, 0.22);
    border-radius: 50%;
}

.hero h1 {
    position: relative;
    font-size: 4.1rem;
    line-height: 1;
    margin-bottom: 1rem;
    font-weight: 850;
    letter-spacing: -0.06em;
}

.hero p {
    position: relative;
    font-size: 1.18rem;
    color: rgba(255,255,255,0.92);
    max-width: 760px;
}

.badge {
    position: relative;
    display: inline-block;
    padding: 0.5rem 0.9rem;
    margin-right: 0.5rem;
    margin-top: 1rem;
    border-radius: 999px;
    background: rgba(255,255,255,0.22);
    backdrop-filter: blur(10px);
    color: white;
    font-weight: 700;
    border: 1px solid rgba(255,255,255,0.35);
}

.glass-card {
    padding: 1.6rem;
    border-radius: 26px;
    background: rgba(255,255,255,0.72);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255,255,255,0.75);
    box-shadow: 0 18px 45px rgba(31, 41, 55, 0.10);
    animation: rise 0.75s ease-out;
}

.feature-card {
    padding: 1.2rem 1.3rem;
    border-radius: 22px;
    background: linear-gradient(135deg, #ffffff, #fff5fd);
    border: 1px solid rgba(255, 105, 180, 0.18);
    box-shadow: 0 12px 30px rgba(255, 105, 180, 0.10);
    margin-bottom: 0.9rem;
}

.output-card {
    padding: 1.4rem 1.5rem;
    border-radius: 24px;
    background: white;
    border: 1px solid rgba(124, 77, 255, 0.18);
    box-shadow: 0 16px 36px rgba(124, 77, 255, 0.12);
    margin-bottom: 1rem;
    animation: rise 0.7s ease-out;
}

.output-card h3 {
    color: #6d28d9;
    margin-bottom: 0.5rem;
}

div.stButton > button {
    border-radius: 999px;
    padding: 0.7rem 1.4rem;
    border: none;
    font-weight: 800;
    color: white;
    background: linear-gradient(90deg, #ff4ecd, #7c3aed, #00c2ff);
    box-shadow: 0 14px 30px rgba(124, 58, 237, 0.28);
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px) scale(1.01);
    box-shadow: 0 18px 40px rgba(124, 58, 237, 0.35);
}

[data-testid="stMetricValue"] {
    color: #7c3aed;
    font-weight: 800;
}

@keyframes floatIn {
    from {opacity: 0; transform: translateY(18px) scale(0.98);}
    to {opacity: 1; transform: translateY(0) scale(1);}
}

@keyframes rise {
    from {opacity: 0; transform: translateY(16px);}
    to {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## ✨ Consultant Toolkit")
    st.write("A fast, polished interface for turning marketing topics into client-ready insights.")
    st.divider()
    st.markdown("### Workflow")
    st.write("① Enter a topic")
    st.write("② Select a source")
    st.write("③ Choose priority")
    st.write("④ Generate a brief")
    st.divider()
    st.info("Built for technology consultants who need clear marketing intelligence without reading every article manually.")

st.markdown("""
<div class="hero">
    <h1>Marketing Intelligence Brief ✨</h1>
    <p>Turn marketing articles into bright, practical, client-ready insights for technology consultants.</p>
    <span class="badge">🌈 Dopamine UI</span>
    <span class="badge">📊 Consultant-Ready</span>
    <span class="badge">⚡ Fast Briefs</span>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

top1, top2, top3 = st.columns(3)
top1.metric("Output Format", "Brief")
top2.metric("Target User", "Consultants")
top3.metric("Style", "Readable")

st.write("")

left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("## Create Your Brief")

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
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("## What You Get")
    st.markdown("""
    <div class="feature-card">💡 <b>Trend Summary</b><br>Simple explanation of the topic.</div>
    <div class="feature-card">🎯 <b>Why It Matters</b><br>Connects the trend to client needs.</div>
    <div class="feature-card">🚀 <b>Consultant Recommendation</b><br>Turns the topic into a next step.</div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

if generate:
    if topic.strip() == "":
        st.error("Please enter a marketing topic or article title before generating the brief.")

    elif source == "Other / Unknown":
        st.warning(
            "The source is unknown. Please verify the original article before using this brief for client recommendations."
        )

    else:
        st.success("✨ Marketing intelligence brief generated successfully.")

        c1, c2, c3 = st.columns(3)
        c1.metric("Source", source)
        c2.metric("Priority", priority)
        c3.metric("Status", "Ready")

        st.markdown(f"""
        <div class="output-card">
            <h3>1. Selected Topic</h3>
            <p>{topic}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="output-card">
            <h3>2. Trend Summary</h3>
            <p><b>{topic}</b> may be relevant to current marketing strategy. 
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
