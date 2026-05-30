import os
import json
from datetime import datetime
from dotenv import load_dotenv
from groq import Groq
from tavily import TavilyClient
import streamlit as st

load_dotenv()

# ── PAGE CONFIG ───────────────────────────────────
st.set_page_config(
    page_title="Research Agent",
    page_icon="🔍",
    layout="wide"
)

# ── CONNECT TO AI AND SEARCH ──────────────────────
ai = Groq(api_key=os.getenv("GROQ_API_KEY"))
search = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

MEMORY_FILE = "research_history.json"

# ── MEMORY FUNCTIONS ──────────────────────────────
def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    return []

def save_memory(history):
    with open(MEMORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

# ── RESEARCHER ────────────────────────────────────
def researcher(topic):
    results = search.search(topic, max_results=5)
    web_info = ""
    for r in results["results"]:
        web_info += f"Source: {r['url']}\n"
        web_info += f"Content: {r['content']}\n\n"

    response = ai.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": "You are a research assistant. Extract and organize the most important facts, data, and insights from the web search results. Be thorough and detailed."
            },
            {
                "role": "user",
                "content": f"Topic: {topic}\n\nWeb results:\n{web_info}\n\nExtract all key information."
            }
        ]
    )
    return response.choices[0].message.content, results["results"]

# ── WRITER ────────────────────────────────────────
def writer(topic, findings):
    response = ai.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """You are an expert report writer.
Write clear well structured reports using this format:

# [Topic Title]

## Introduction
[2-3 sentences introducing the topic]

## Key Findings
- [Finding with explanation]
- [Finding with explanation]
- [Finding with explanation]

## Detailed Analysis
[3-4 paragraphs going deep into the topic]

## Conclusion
[2-3 sentences wrapping up]

Keep language clear and easy to understand."""
            },
            {
                "role": "user",
                "content": f"Write a detailed report on: {topic}\n\nBased on:\n{findings}"
            }
        ]
    )
    return response.choices[0].message.content

# ── MAIN APP UI ───────────────────────────────────

# Header
st.title("🔍 Research & Writing Agent")
st.markdown("Type any topic — I'll search the web and write you a full report automatically.")
st.divider()

# Sidebar - History
with st.sidebar:
    st.header("📚 Research History")
    history = load_memory()
    if not history:
        st.info("No research yet. Start by entering a topic!")
    else:
        for item in reversed(history):
            st.markdown(f"**{item['topic']}**")
            st.caption(item['date'])
            st.divider()

# Main input
topic = st.text_input(
    "Enter your research topic:",
    placeholder="e.g. What is quantum computing?"
)

col1, col2 = st.columns([1, 5])
with col1:
    search_btn = st.button("Research!", type="primary", use_container_width=True)

# Run when button clicked
if search_btn and topic:

    # Progress steps
    with st.status("Working on your report...", expanded=True) as status:

        st.write("🔍 Searching the web...")
        findings, sources = researcher(topic)

        st.write("✍️ Writing your report...")
        report = writer(topic, findings)

        st.write("💾 Saving...")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        safe_topic = topic[:30].replace(" ", "_")
        filename = f"report_{safe_topic}_{timestamp}.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report)

        history.append({
            "topic": topic,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "filename": filename
        })
        save_memory(history)

        status.update(label="Report ready!", state="complete")

    st.divider()

    # Show report
    st.subheader("Your Report")
    st.markdown(report)

    st.divider()

    # Download button
    st.download_button(
        label="Download Report as TXT",
        data=report,
        file_name=filename,
        mime="text/plain"
    )

    # Sources used
    with st.expander("View Sources Used"):
        for i, source in enumerate(sources, 1):
            st.markdown(f"**{i}.** [{source['url']}]({source['url']})")

elif search_btn and not topic:
    st.warning("Please enter a topic first!")