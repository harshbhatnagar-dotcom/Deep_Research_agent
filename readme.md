# 🔍 Deep Research Agent

An AI-powered Deep Research system that automatically plans research, performs multiple web searches, synthesizes findings into a comprehensive report, and delivers the final report via email using Resend.

Built using:

- OpenAI Agents SDK
- GPT-OSS 120B (via Groq)
- Tavily Search API
- Resend Email API
- Gradio UI

---

## 🚀 Features

- Multi-step agentic research workflow
- Automatic research planning
- Parallel web searching
- Report synthesis from multiple sources
- Professional report generation in Markdown
- Email delivery using Resend
- Interactive Gradio interface

---

## 🏗️ Architecture

```text
User Query
     │
     ▼
Planner Agent
     │
     ▼
Search Plan
     │
     ▼
Search Agent(s)
     │
     ▼
Search Summaries
     │
     ▼
Writer Agent
     │
     ▼
Research Report
     │
     ▼
Email Agent
     │
     ▼
Resend Email Delivery
```

---

## 📂 Project Structure

```text
.
├── deep_research.py
├── research_manager.py
├── planner_agent.py
├── search_agent.py
├── writer_agent.py
├── email_agent.py
├── .env
├── requirements.txt
└── README.md
```