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
* { font-family: Arial, sans-serif; }

.stApp {
    background: linear-gradient(135deg, #fff7fb 0%, #eef9ff 50%, #fffbe8 100%);
    color: #111827;
}

.main .block-container {
    max-width: 1180px;
    padding-top: 2rem;
    padding-bottom: 4rem;
}

section[data-testid="stSidebar"] {
    background: #fff5fb;
    color: #111827;
}

.hero {
    padding: 3rem;
    border-radius: 32px;
    color: white;
    background: linear-gradient(135deg, #ff4ecd 0%, #7c3aed 45%, #00c2ff 100%);
    box-shadow: 0 25px 60px rgba(124, 58, 237, 0.25);
}

.hero h1 {
    color: white;
    font-size: 4rem;
    line-height: 1;
    font-weight: 900;
    margin-bottom: 1rem;
}

.hero p {
    color: white;
    font-size: 1.2rem;
    max-width: 760px;
}

.badge {
    display: inline-block;
    margin-top: 1rem;
    margin-right: 0.5rem;
    padding: 0.55rem 0.9rem;
    border-radius: 999px;
    background: rgba(255,255,255,0.24);
    border: 1px solid rgba(255,255,255,0.4);
    color: white;
    font-weight: 800;
}

.card {
    padding: 1.5rem;
    border-radius: 26px;
    background: white;
    box-shadow: 0 15px 35px rgba(17,24,39,0.08);
    color: #111827;
}

.stat-card {
    padding: 1.2rem;
    border-radius: 22px;
    background: white;
    box-shadow: 0 12px 28px rgba(124,58,237,0.10);
}

.stat-label {
    color: #6b7280;
    font-size: 0.8rem;
    font-weight: 800;
    text-transform: uppercase;
}

.stat-value {
    font-size: 2rem;
    font-weight: 900;
    color: #7c3aed;
}

.step-card, .feature-card {
    padding: 1.2rem;
    border-radius: 22px;
    background: white;
    border: 1px solid rgba(236,72,153,0.18);
    box-shadow: 0 12px 28px rgba(236,72,153,0.08);
    color: #111827;
    min-height: 120px;
    margin-bottom: 1rem;
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

div.stButton > button {
    border-radius: 999px;
    padding: 0.85rem 1.55rem;
    border: none;
    font-weight: 900;
    color: white;
    background: linear-gradient(90deg, #ff4ecd, #7c3aed, #00c2ff);
}

.footer {
    margin-top: 2rem;
    padding: 1.2rem;
    border-radius: 24px;
    background: white;
    text-align: center;
    color: #4b5563;
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
<div class="hero">
    <h1>Turn marketing noise into client-ready insight.</h1>
    <p>A colorful intelligence workspace for technology consultants who need to scan marketing topics, understand why they matter, and turn them into practical recommendations.</p>
    <span class="badge">🌈 Dopamine Design</span>
    <span class="badge">⚡ Live n8n Call</span>
    <span class="badge">🎯 Consultant-Ready</span>
    <span class="badge">💬 Plain English</span>
</div>
""", unsafe_allow_html=True)

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
    st.markdown('<div class="card">', unsafe_allow_html=True)
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
    st.markdown('<div class="card">', unsafe_allow_html=True)
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

        st.info("Sending request to n8n webhook...")

        try:
            response = requests.post(
                WEBHOOK_URL,
                json=payload,
                timeout=60
            )

            st.write("Webhook status:", response.status_code)

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

        except requests.exceptions.RequestException as e:
            st.error("The live analysis service is temporarily unavailable.")
            st.write("Error details:", str(e))

else:
    st.info("Enter a topic, select a source, and click the button to generate a human-readable marketing intelligence brief.")

st.markdown(
    '<div class="footer">Built as a Streamlit interface for Assignment 5A — connected to an n8n webhook workflow for live marketing intelligence.</div>',
    unsafe_allow_html=True
)
