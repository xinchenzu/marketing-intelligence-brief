import streamlit as st

st.set_page_config(page_title="Marketing Intelligence Brief", page_icon="📈")

st.title("📈 Marketing Intelligence Brief")
st.caption("Turn marketing articles into practical insights for technology consultants.")

st.write(
    """
    This interface helps technology consultants review marketing topics, understand why they matter,
    and turn them into client-ready recommendations.
    """
)

st.divider()

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

urgency = st.selectbox(
    "Priority level",
    ["High", "Medium", "Low"]
)

st.divider()

if st.button("Generate Marketing Intelligence Brief"):

    if topic.strip() == "":
        st.error(
            "Please enter a marketing topic or article title before generating the brief."
        )

    elif source == "Other / Unknown":
        st.warning(
            "The source is unknown. Please verify the original article before using this brief for client recommendations."
        )

    else:
        st.success("Marketing intelligence brief generated successfully.")

        st.subheader("1. Selected Topic")
        st.write(topic)

        st.subheader("2. Source")
        st.write(source)

        st.subheader("3. Priority")
        st.write(urgency)

        st.subheader("4. Trend Summary")
        st.write(
            f"This topic suggests that {topic.lower()} may be important for current marketing strategy. "
            f"The source, {source}, should be reviewed to confirm the original context before using the insight."
        )

        st.subheader("5. Why It Matters")
        st.write(
            "For technology consultants, this information can help connect marketing trends to client needs, "
            "especially when clients are trying to improve digital visibility, content planning, or customer engagement."
        )

        st.subheader("6. Consultant Recommendation")
        st.write(
            "Use this insight as a starting point for client discussion. Review the original article, identify whether "
            "the trend applies to the client’s industry, and decide whether it should influence marketing or technology strategy."
        )

else:
    st.info(
        "Enter a topic, select a source, and click the button to generate a human-readable marketing intelligence brief."
    )
