<div align="center">

# 🏥 ClaimSense AI
### Enterprise Healthcare Intelligence Platform

An enterprise-grade AI platform that combines Retrieval-Augmented Generation (RAG), AI Agents, Long-Term Memory, Medical Web Search, and Intelligent Tool Routing to deliver grounded, explainable healthcare responses.

Built with **LangGraph**, **FastAPI**, **Google Gemini**, **ChromaDB**, **Hybrid Search**, and **Streamlit**.

---

![Python](https://img.shields.io/badge/Python-3.13-blue)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic_AI-green)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688)
![Gemini](https://img.shields.io/badge/Google-Gemini-orange)
![RAG](https://img.shields.io/badge/RAG-Hybrid_Search-purple)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

</div>

---

# Overview

ClaimSense AI is an enterprise healthcare intelligence platform designed to answer complex healthcare questions using grounded retrieval instead of relying solely on LLM reasoning.

Unlike traditional chatbots, ClaimSense AI plans every request, retrieves trusted medical knowledge, selects appropriate tools, remembers previous conversations, evaluates retrieval quality, and generates explainable responses backed by citations.

The project demonstrates production-oriented AI engineering patterns including:

- Agentic AI
- Hybrid RAG
- Semantic Memory
- Intelligent Tool Routing
- Medical Web Search
- Guardrails
- Retrieval Evaluation
- Production Observability

---

# Features

## Agentic Workflow

- LangGraph based multi-step reasoning
- Planner-driven tool selection
- Dynamic execution graph
- Multi-turn conversations

---

## Retrieval-Augmented Generation

- Dense Vector Search
- BM25 Sparse Search
- Reciprocal Rank Fusion (RRF)
- Reranking
- Explainable citations

---

## AI Memory

- Long-term semantic memory
- Context-aware conversations
- Personalized follow-up questions

---

## Intelligent Tool Calling

ClaimSense AI automatically chooses between:

- Enterprise Knowledge Base
- Medical Web Search
- Clinical Calculators
- Future enterprise tools

---

## Medical Web Search

- Live healthcare search
- Trusted medical sources
- AI-generated summaries
- Source attribution

---

## Healthcare Guardrails

- Prompt Injection Detection
- Healthcare Domain Validation
- Safe Response Generation
- Output Validation

---

## Evaluation Framework

Every response is automatically evaluated.

Metrics include:

- Retrieval Quality
- Performance Metrics
- Answer Statistics
- Source Attribution
- Latency Analysis

---

## Observability

- Opik Tracing
- Pipeline Metrics
- LLM Latency
- Retrieval Diagnostics

---

# Architecture

```text
┌──────────────────────────────────────────────────────────────┐
│                     Streamlit Frontend                       │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                  LangGraph Agent Workflow                    │
│                                                              │
│ Query Rewrite                                                │
│ Conversation History                                         │
│ Semantic Memory                                              │
│ Agent Guardrails                                             │
│ Planner                                                      │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                     Intelligent Tool Layer                   │
│                                                              │
│ 📚 Knowledge Base                                             │
│ 🌐 Medical Web Search                                         │
│ 🗄 SQL Analytics                                               │
│ 🧮 Clinical Calculator                                        │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│                   AI Generation Layer                        │
│                                                              │
│ Hybrid Retrieval                                              │
│ Google Gemini                                                 │
│ Tool Calling                                                  │
│ Source Attribution                                            │
│ Evaluation                                                    │
└──────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌──────────────────────────────────────────────────────────────┐
│              Observability & Performance                     │
│                                                              │
│ Opik Tracing                                                  │
│ Retrieval Metrics                                             │
│ Latency                                                       │
│ Evaluation Reports                                            │
└──────────────────────────────────────────────────────────────┘
```

---

# Technology Stack

## AI

- Google Gemini
- LangGraph
- LangChain
- RAG
- AI Agents
- Tool Calling
- Prompt Engineering
- Conversational Memory

---

## Retrieval

- ChromaDB
- Dense Embeddings
- BM25
- Hybrid Search
- Reciprocal Rank Fusion
- Semantic Search
- Reranking

---

## Backend

- FastAPI
- Python
- Pydantic
- Dependency Injection
- Modular Service Architecture

---

## Observability

- Opik
- Logging
- Performance Metrics
- Retrieval Diagnostics

---

## Frontend

- Streamlit
- Custom UI Components
- Interactive Chat Interface

---

# Project Structure

```
claimsense-ai/

├── graph/
│   ├── graph_builder.py
│   ├── nodes.py
│   └── graph_service.py
|   |__state.py
│
├── services/
│   ├── rag/
|   |__ agent/
│   ├── planner/
│   ├── memory/
│   ├── guardrails/
│   ├── web_search/
│   ├── attribution/
│   ├── evaluation/
│   └── llm/
|   |__ ingestion/
|   |__ prompts/
|   |__ reranker/
|   |__ retrieval/
|   |__ tools/
|   |__ sql/
|   |__ validation/
|   |__ rewriting/
|   |__ utilities/
|   |__ embeddings/
|   |__ answer_generation/
│
├── models/
│
├── ui/
│
├── data/
│   |__ vector_db/
|   |__ raw/
|   |__ chroma/
|
|
├── tests/
│
└── streamlit_app.py
|
|__ api/
|   |__ app.py
|
|__ core/
|   |__ service_container.py
|   |
|   |__ utils/
|   |   |__timer.py
|   |
|   |__ config/
        |__ settings.py


```

---

# AI Pipeline

Every question follows this workflow.

1. Rewrite Query
2. Retrieve Conversation History
3. Retrieve Long-Term Memory
4. Validate Input
5. Retrieve Knowledge Base
6. Evaluate Retrieval Quality
7. Plan Execution Strategy
8. Execute Required Tool
9. Generate Grounded Response
10. Validate Output
11. Store Conversation Memory

---

# Example Capabilities

### Disease Intelligence

- Explain diabetes
- Disease progression
- Symptoms
- Treatments

---

### Drug Interaction

- Medication compatibility
- Contraindications
- Side effects

---

### Healthcare Claims

- Insurance policies
- Prior authorization
- Claims explanation

---

### Clinical Calculations

- BMI
- Dosage calculations
- Medical formulas

---

### Medical Research

- Latest WHO guidelines
- Clinical evidence
- Medical literature

---

# Screenshots

## Landing Page

> Add screenshot here

---

## AI Chat

> Add screenshot here

---

## AI Insights

> Add screenshot here

---

## Source Attribution

> Add screenshot here

---

# Performance

| Component | Description |
|------------|-------------|
| Hybrid Retrieval | Dense + BM25 |
| Memory | Semantic Vector Memory |
| Tool Routing | Planner Based |
| Observability | Opik |
| Backend | FastAPI |
| Frontend | Streamlit |

---

# Future Improvements

- PDF Chat
- Multi-document Retrieval
- Knowledge Graph Integration
- Voice Assistant
- Streaming Responses
- Authentication
- Feedback Learning
- Multi-Agent Collaboration

---

# Running Locally

```bash
git clone https://github.com/YOUR_USERNAME/claimsense-ai.git

cd claimsense-ai

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

streamlit run streamlit_app.py

uvicorn api.app:app --reload
```

---

# Author

**Ushmita Marwah**

LinkedIn: https://linkedin.com/in/ushmita-marwaha24

GitHub: https://github.com/ushmita2244

---

# License

MIT License