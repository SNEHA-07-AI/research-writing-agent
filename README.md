# research-writing-agent
Agentic AI system that performs web research, information synthesis, and report generation using Groq LLMs, LangGraph workflows, and Tavily Search.


# Agentic AI Research & Writing Assistant

## Overview

The Agentic AI Research & Writing Assistant is an AI-powered application that automates the entire research and content generation process. Instead of manually searching multiple websites, reading articles, collecting information, and writing summaries, users simply enter a topic and the system performs the complete workflow automatically.

The agent researches the topic, gathers relevant information from the web, analyzes the collected content, and generates a well-structured report within minutes.

---

## Problem Statement

Traditional research is time-consuming and often involves:

* Searching across multiple websites
* Reading lengthy articles
* Identifying relevant information
* Taking notes
* Organizing findings
* Writing a final report

This project simplifies the process by automating research and report generation using AI agents.

---

## Features

* Automated web research
* AI-powered content analysis
* Information summarization
* Structured report generation
* Fast response using Groq LLMs
* Agent-based workflow architecture
* Easy-to-use command-line interface

---

## Tech Stack

* Python
* Groq API
* LangGraph
* Tavily Search API
* AI Agents
* Large Language Models (LLMs)

---

## Architecture

The system consists of three major components:

### 1. User Input

The user provides a research topic such as:

"What is Machine Learning?"

### 2. Research Agent

The Research Agent searches the web using Tavily Search API and gathers relevant information from trusted sources.

Responsibilities:

* Search the web
* Collect research data
* Filter relevant information
* Prepare research notes

### 3. Writing Agent

The Writing Agent receives the research notes and generates a professional report.

Responsibilities:

* Analyze collected information
* Organize content logically
* Generate summaries
* Create structured reports

### 4. LangGraph Workflow

LangGraph manages the execution flow between the agents.

Workflow:

User Query → Research Agent → Writing Agent → Final Report

LangGraph ensures that each step is executed in the correct sequence.

---

## What is Groq?

Groq provides ultra-fast inference for Large Language Models (LLMs).

In this project, Groq acts as the AI engine responsible for:

* Understanding user queries
* Analyzing research data
* Extracting key insights
* Generating human-like reports

Its high-speed inference significantly reduces report generation time.

---

## What is Tavily?

Tavily is a search engine designed specifically for AI applications.

It provides:

* Clean search results
* Relevant information
* AI-friendly content retrieval

This allows the Research Agent to access reliable information efficiently.

---

## What is LangGraph?

LangGraph is a framework for building agentic workflows.

It helps:

* Define agent interactions
* Manage execution flow
* Coordinate multiple AI agents
* Build scalable AI systems

In this project, LangGraph orchestrates the collaboration between the Research Agent and the Writing Agent.

---

## Project Workflow

1. User enters a topic.
2. Research Agent searches the web using Tavily.
3. Relevant information is collected and summarized.
4. Writing Agent processes the research data.
5. A structured report is generated.
6. The final report is presented to the user.

---

## Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/agentic-ai-research-writing-assistant.git
cd agentic-ai-research-writing-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Run the Project

```bash
python main.py
```

Enter a topic when prompted and the agent will automatically research and generate a report.

---

## Future Enhancements

* Multi-agent collaboration
* Citation and reference generation
* PDF export functionality
* Web-based user interface
* Research memory and knowledge storage
* Multi-language report generation
* Advanced source verification

---

## Learning Outcomes

This project demonstrates:

* Agentic AI Systems
* LLM Integration
* Web Search Tool Integration
* Workflow Orchestration using LangGraph
* Prompt Engineering
* Python Application Development

---

## Author

Developed as an Agentic AI project using Groq, LangGraph, and Tavily to automate research and report generation.

