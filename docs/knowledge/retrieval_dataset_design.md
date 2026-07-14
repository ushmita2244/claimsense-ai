# Retrieval Benchmark Dataset Design

## Sprint

Sprint 4 – Advanced Retrieval

---

# Objective

The purpose of the retrieval benchmark is to evaluate how effectively the retrieval pipeline identifies relevant knowledge for a user's question.

This benchmark establishes a measurable baseline before introducing advanced retrieval techniques such as:

- Hybrid Search
- BM25
- Cross-Encoder Reranking
- Query Expansion
- Multi-Query Retrieval
- Context Compression

Every future retrieval strategy will be evaluated using the same benchmark to ensure objective comparison.

---

# Why Build a Retrieval Benchmark?

Without a benchmark, retrieval improvements are subjective.

Example:

> "Hybrid Search seems better."

This is not measurable.

Instead, the benchmark should answer:

- Did retrieval quality improve?
- Did the correct knowledge unit rank higher?
- Did Precision@K improve?
- Did Mean Reciprocal Rank (MRR) improve?
- Did Hybrid Search outperform Vector Search?

---

# Evaluation Levels

The benchmark evaluates retrieval at multiple levels.

---

## Level 1 – Document Match

Question:

Did the retriever return the correct document?

Example

Question:

"What causes lung cancer?"

Expected Document:

2024-guide-to-preventing-cancer-web.pdf

Returned:

2024-guide-to-preventing-cancer-web.pdf

Result:

PASS

---

## Level 2 – Knowledge Unit Match

Question:

Did the retriever return the correct knowledge section?

Example

Question:

"What causes lung cancer?"

Expected Knowledge Unit:

Lung Cancer

Returned:

Lung Cancer

Result:

PASS

This is preferred over evaluating only individual chunks because several adjacent chunks often describe the same concept.

---

## Level 3 – Chunk Match

Question:

Did the retriever return the expected chunk?

Example

Expected:

Chunk 44

Returned:

Chunk 44

PASS

Returned:

Chunk 46

PARTIAL

Returned:

Chunk 18

FAIL

Chunk-level evaluation is useful when answers are localized to a specific passage.

---

## Level 4 – Semantic Match (Future)

Future versions will evaluate semantic relevance using an LLM.

Example

Expected:

"What causes cervical cancer?"

Returned Chunk:

Explains HPV infection

Although the chunk number differs, the semantic content answers the question.

Result:

PASS

This evaluation will be implemented using Gemini or Opik LLM-as-a-Judge.

---

# Difficulty Levels

Questions are categorized by retrieval complexity.

---

## Easy

The answer appears almost verbatim in one chunk.

Examples

- What is HPV?
- What is mammography?
- What is PSA screening?

Purpose

Evaluate exact retrieval.

---

## Medium

Requires understanding synonyms.

Examples

Question

How can cancer be prevented?

Relevant Concepts

- Healthy diet
- Exercise
- Avoid smoking
- Vaccination

Purpose

Evaluate semantic embeddings.

---

## Hard

Requires reasoning across multiple chunks.

Examples

Question

Which lifestyle habits reduce cancer risk?

Relevant Knowledge

Smoking

Alcohol

Diet

Exercise

Vaccination

Purpose

Evaluate multi-concept retrieval.

---

## Ambiguous

Queries intentionally contain ambiguous wording.

Examples

- What causes cancer?
- How do viruses affect cancer?
- What screening should I get?

Purpose

Measure retrieval robustness.

---

## Multi-Hop

Requires combining multiple knowledge units.

Example

Question

How do HPV vaccination and cervical screening work together to reduce cancer risk?

Relevant Knowledge

HPV

Vaccination

Pap Test

Screening Guidelines

Purpose

Evaluate retrieval coverage.

---

# Benchmark Categories

The benchmark will include questions across all knowledge units.

| Knowledge Unit | Approx. Questions |
|---------------|------------------:|
| General Prevention | 6 |
| Breast Cancer | 5 |
| Cervical Cancer | 5 |
| Colorectal Cancer | 4 |
| Liver Cancer | 3 |
| Lung Cancer | 4 |
| Oral Cancer | 2 |
| Prostate Cancer | 3 |
| Skin Cancer | 4 |
| Testicular Cancer | 2 |
| Viruses & Cancer | 4 |
| Screening Summary | 3 |

Target Size

Approximately 45–50 benchmark questions.

---

# Evaluation Metrics

The following metrics will be calculated for every retrieval strategy.

---

## Success Rate

Percentage of questions for which the correct knowledge unit was retrieved.

---

## Precision@K

Measures the proportion of retrieved results that are relevant.

Higher is better.

---

## Recall@K

Measures how many relevant passages were successfully retrieved.

Higher is better.

---

## Mean Reciprocal Rank (MRR)

Measures how early the first correct result appears.

Higher is better.

---

## Average Retrieval Distance

Average embedding distance of retrieved chunks.

Lower is better.

---

## Retrieval Quality

Uses the DiagnosticsService thresholds.

Categories

- Excellent
- Good
- Average
- Poor

---

# Future Metrics

Future versions will also calculate

- Context Precision
- Context Recall
- Groundedness
- Faithfulness
- Hallucination Rate
- Citation Accuracy
- Answer Relevance

These metrics will be integrated with Opik evaluation.

---

# Benchmark Workflow

User Question

↓

Retriever

↓

Retrieved Documents

↓

Document Match

↓

Knowledge Unit Match

↓

Chunk Match

↓

Metric Calculation

↓

Benchmark Report

↓

Comparison Across Retrieval Strategies

---

# Benchmark Rules

Every retrieval strategy must use

- the same document corpus
- the same benchmark dataset
- the same evaluation metrics
- the same Top-K value

This ensures fair comparison.

---

# Expected Retrieval Pipeline Evolution

Baseline

Vector Search

↓

Sprint 4 Story 2

Hybrid Search

↓

Sprint 4 Story 3

Cross-Encoder Reranking

↓

Sprint 4 Story 4

Query Expansion

↓

Sprint 4 Story 5

Multi-Query Retrieval

↓

Sprint 4 Story 6

Context Compression

↓

Sprint 4 Story 7

Parent Document Retrieval

Each stage should improve benchmark metrics while maintaining acceptable latency.

---

# Design Principles

The benchmark should be

- Reproducible
- Deterministic
- Extensible
- Retriever-agnostic
- Independent of the LLM

Only the retrieval component should change between benchmark runs.

This ensures improvements are attributable to retrieval rather than answer generation.

---

# Long-Term Vision

The retrieval benchmark will become the standard evaluation framework for the ClaimSense-AI project.

It will be used to:

- Compare retrieval algorithms
- Detect retrieval regressions
- Validate new retrieval features
- Track retrieval quality over time
- Support production monitoring with Opik
- Provide quantitative evidence of retrieval improvements