import streamlit as st
import requests

st.set_page_config(
    page_title="Marketing Intelligence Brief",
    page_icon="✨",
    layout="wide"
)

WEBHOOK_URL = "https://xinchenzu.app.n8n.cloud/webhook/marketing-brief"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

* { font-family: 'Inter', sans-serif; }

.stApp {
    background:
        radial-gradient(circle at 8% 12%, rgba(255, 77, 210, 0.28), transparent 28%),
        radial-gradient(circle at 92% 10%, rgba(0, 209, 255, 0.28), transparent 30%),
        radial-gradient(circle at 50% 95%, rgba(255, 221, 51, 0.26), transparent 35%),
        linear-gradient(135deg, #fff8fc 0%, #f2fbff 46%, #fffdf1 100%);
}

.main .block-container {
    max-width: 1240px;
    padding-top: 1.3rem;
    padding-bottom: 4rem;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, rgba(255,255,255,0.92), rgba(255,244,252,0.95));
    border-right: 1px solid rgba(236, 72, 153, 0.16);
}

.nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0.85rem 1.1rem;
    margin-bottom: 1.1rem;
    border-radius: 999px;
    background: rgba(255,255,255,0.78);
    backdrop-filter: blur(18px);
    box-shadow: 0 18px 45px rgba(17,24,39,0.06);
}

.logo {
    font-weight: 900;
    font-size: 1.05rem;
    color: #111827;
}

.nav-pill {
    display: inline-block;
    margin-left: 0.5rem;
    padding: 0.45rem 0.85rem;
    border-radius: 999px;
    background: #f5f3ff;
    color: #6d28d9;
    font-weight: 750;
    font-size: 0.82rem;
}

.hero {
    position: relative;
    overflow: hidden;
    min-height: 420px;
    padding: 3.7rem 3.5rem;
    border-radius: 38px;
    color: white;
    background: linear-gradient(135deg, #ff4ecd 0%, #7c3aed 44%, #00c2ff 100%);
    box-shadow: 0 34px 80px rgba(124,58,237,0.30);
    animation: heroIn 0.9s ease-out;
}

.hero:before {
    content: "";
    position: absolute;
    width: 360px;
    height: 360px;
    right: -80px;
    top: -110px;
    border-radius: 50%;
    background: rgba(255,255,255,0.25);
}

.hero:after {
    content: "";
    position: absolute;
    width: 230px;
    height: 230px;
    left: 58%;
    bottom: -100px;
    border-radius: 50%;
    background: rgba(255,255,255,0.18);
}

.hero h1 {
    position: relative;
    font-size: 5rem;
    line-height: 0.95;
    letter-spacing: -0.08em;
    font-weight: 950;
    max-width: 900px;
    margin-bottom: 1.3rem;
}

.hero p {
    position: relative;
    font-size: 1.25rem;
    max-width: 760px;
    color: rgba(255,255,255,0.92);
    line-height: 1.65;
}

.badge {
    position: relative;
    display: inline-block;
    margin-top: 1.1rem;
    margin-right: 0.55rem;
    padding: 0.58rem 0.95rem;
    border-radius: 999px;
    background: rgba(255,255,255,0.22);
    border: 1px solid rgba(255,255,255,0.42);
    color: white;
    font-weight: 850;
}

.glow-card {
    padding: 1.5rem;
    border-radius: 28px;
    background: rgba(255,255,255,0.78);
    backdrop-filter: blur(18px);
    box-shadow: 0 22px 48px rgba(17,24,39,0.08);
}

.stat-card {
    padding: 1.25rem 1.35rem;
    border-radius: 26px;
    background: rgba(255,255,255,0.82);
    box-shadow: 0 18px 42px rgba(124,58,237,0.10);
}

.stat-label {
    color: #6b7280;
    font-size: 0.82rem;
    font-weight: 700;
    text-transform: uppercase;
}

.stat-value {
    font-size: 2.1rem;
    font-weight: 950;
    background: linear-gradient(90deg, #ec4899, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.step-card {
    padding: 1.15rem 1.2rem;
    border-radius: 24px;
    background: linear-gradient(135deg, #ffffff, #fff7fd);
    box-shadow: 0 14px 34px rgba(236,72,153,0.08);
    min-height: 128px;
}

.step-number {
    display: inline-flex;
    width: 34px;
    height: 34px;
    align-items: center;
    justify-content: center;
    border-radius: 50%;
    color: white;
    font-weight: 900;
    background: linear-gradient(135deg, #ff4ecd, #7c3aed);
    margin-bottom: 0.6rem;
}

.feature-card {
    padding: 1.15rem 1.25rem;
    border-radius: 24px;
    background: rgba(255,255,255,0.86);
    box-shadow: 0 14px 36px rgba(124,58,237,0.08);
    margin-bottom: 0.9rem;
}

.footer {
    margin-top: 2.5rem;
    padding: 1.3rem;
    border-radius: 28px;
    text-align: center;
    background: rgba(255,255,255,0.68);
    color: #6b7280;
}

div.stButton > button {
    border-radius: 999px;
    padding: 0.85rem 1.55rem;
    border: none;
    font-weight: 900;
    color: white;
    background: linear-gradient(90deg, #ff4ecd, #7c3aed, #00c2ff);
    box-shadow: 0 18px 38px rgba(124,58,237,0.28);
    transition: all 0.25s ease;
}

div.stButton > button:hover {
    transform: translateY(-2px) scale(1.015);
    box-shadow: 0 24px 52px rgba(124,58,237,0.36);
}

@keyframes heroIn {
    from {opacity: 0; transform: translateY(18px) scale(0.985);}
    to {opacity: 1; transform: translateY(0) scale(1);}
}
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("## ✨ Consultant Toolkit")
    st.write("A polished interface for turning marketing topics into client-ready insights.")
    st.divider()
    st.markdown("### Workflow")
    st.write("① Enter a topic")
    st.write("② Select a trusted source")
    st.write("③ Choose priority")
    st.write("④ Generate a live brief")
    st.divider()
    st.success("Connected to n8n Webhook + Gemini workflow.")

st.markdown("""
<div class="nav">
    <div class="logo">✨ Marketing Intelligence Brief</div>
    <div>
        <span class="nav-pill">Consulting</span>
        <span class="nav-pill">n8n Workflow</span>
        <span class="nav-pill">Gemini Analysis</span>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>Turn marketing noise into client-ready insight.</h1>
    <p>
    A colorful intelligence workspace for technology consultants who need to scan marketing topics,
    understand why they matter, and turn them into practical recommendations.
    </p>
    <span class="badge">🌈 Dopamine Design</span>
    <span class="badge">⚡ Live n8n Call</span>
    <span class="badge">🎯 Consultant-Ready</span>
    <span class="badge">💬 Plain English</span>
</div>
""", unsafe_allow_html=True)

st.write("")
st.write("")

s1, s2, s3, s4 = st.columns(4)
with s1:
    st.markdown('<div class="stat-card"><div class="stat-label">Output</div><div class="stat-value">Brief</div></div>', unsafe_allow_html=True)
with s2:
    st.markdown('<div class="stat-card"><div class="stat-label">Audience</div><div class="stat-value">B2B</div></div>', unsafe_allow_html=True)
with s3:
    st.markdown('<div class="stat-card"><div class="stat-label">Engine</div><div class="stat-value">n8n</div></div>', unsafe_allow_html=True)
with s4:
    st.markdown('<div class="stat-card"><div class="stat-label">Use Case</div><div class="stat-value">Strategy</div></div>', unsafe_allow_html=True)

st.write("")

st.markdown("## How it works")
w1, w2, w3 = st.columns(3)
with w1:
    st.markdown('<div class="step-card"><div class="step-number">1</div><h4>Choose a topic</h4><p>Start with a marketing trend, article title, or client question.</p></div>', unsafe_allow_html=True)
with w2:
    st.markdown('<div class="step-card"><div class="step-number">2</div><h4>Send to n8n</h4><p>The interface sends your request to the workflow through a webhook.</p></div>', unsafe_allow_html=True)
with w3:
    st.markdown('<div class="step-card"><div class="step-number">3</div><h4>Get a brief</h4><p>Gemini returns a consultant-ready marketing intelligence brief.</p></div>', unsafe_allow_html=True)

st.write("")

left, right = st.columns([1.05, 0.95], gap="large")

with left:
    st.markdown('<div class="glow-card">', unsafe_allow_html=True)
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

    generate = st.button("✨ Generate Live Marketing Intelligence Brief")
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="glow-card">', unsafe_allow_html=True)
    st.markdown("## What You Get")
    st.markdown("""
    <div class="feature-card">💡 <b>Trend Summary</b><br>Simple explanation of the marketing topic.</div>
    <div class="feature-card">🎯 <b>Why It Matters</b><br>Connects the trend to client needs and business context.</div>
    <div class="feature-card">🚀 <b>Consultant Recommendation</b><br>Turns the topic into a practical next step.</div>
    <div class="feature-card">🧭 <b>Source Context</b><br>Shows where the information came from before it is used.</div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("")

if generate:
    if topic.strip() == "":
        st.error("Please enter a marketing topic or article title before generating the brief.")
    else:
        payload = {
            "topic": topic,
            "source": source,
            "priority": priority
        }

        with st.spinner("Generating live marketing intelligence through n8n..."):
            try:
                response = requests.post(WEBHOOK_URL, json=payload, timeout=60)

                if response.status_code == 200 and response.text.strip():
                    st.success("✨ Live marketing intelligence brief generated successfully.")
                    st.markdown(response.text)
                else:
                    st.warning("The live analysis service did not return a complete response. Showing a safe draft brief instead.")
                    st.markdown(f"""
### Selected Topic
{topic}

### Trend Summary
This topic may be relevant to current marketing strategy. The selected source, {source}, should be reviewed to confirm the original context before using the insight.

### Why It Matters
For technology consultants, this information can help connect marketing trends to client needs, especially when clients are trying to improve digital visibility, content planning, or customer engagement.

### Consultant Recommendation
Use this insight as a starting point for client discussion. Review the original article, identify whether the trend applies to the client’s industry, and decide whether it should influence marketing or technology strategy.
""")

            except requests.exceptions.RequestException:
                st.error("The live analysis service is temporarily unavailable. Please try again later.")

else:
    st.info("Enter a topic, select a source, and click the button to generate a human-readable marketing intelligence brief.")

st.markdown("""
<div class="footer">
    Built as a Streamlit interface for Assignment 5A — connected to an n8n webhook workflow for live marketing intelligence.
</div>
""", unsafe_allow_html=True)
