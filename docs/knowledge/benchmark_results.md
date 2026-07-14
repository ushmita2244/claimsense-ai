# Retrieval Benchmark Results

## Sprint

Sprint 4 – Advanced Retrieval

---

# Purpose

This document records the performance of every retrieval strategy implemented in the ClaimSense-AI project.

Rather than relying on subjective observations, every retrieval improvement is evaluated using the same benchmark dataset and metrics.

This allows objective comparison between retrieval algorithms and ensures that new features improve retrieval quality instead of introducing regressions.

---

# Evaluation Metrics

Every benchmark run records the following metrics.

| Metric | Description | Target |
|---------|-------------|--------|
| Success Rate | Percentage of benchmark questions answered with the correct knowledge unit retrieved | Higher |
| Precision@K | Percentage of retrieved documents that are relevant | Higher |
| Recall@K | Percentage of relevant knowledge retrieved | Higher |
| Mean Reciprocal Rank (MRR) | Ranking quality of the first relevant result | Higher |
| Average Retrieval Distance | Mean embedding distance of retrieved chunks | Lower |
| Retrieval Quality | DiagnosticsService classification | Excellent |

---

# Benchmark Configuration

Document Corpus

- 2024-guide-to-preventing-cancer-web.pdf

Benchmark Dataset

- Approximately 45–50 benchmark questions

Retriever

- Vector Search (Baseline)

Embedding Model

- Gemini Embedding Model

Vector Database

- ChromaDB

Top-K

- 3

---

# Benchmark History

| Version | Retrieval Strategy | Success Rate | Precision@3 | Recall@3 | MRR | Avg Distance | Notes |
|----------|--------------------|-------------:|------------:|----------:|----:|-------------:|------|
| v1.0 | Dense Vector Search | TBD | TBD | TBD | TBD | TBD | Initial baseline |

---

# Version Details

---

## Version 1.0

### Retrieval Strategy

Dense Vector Search

### Components

- Gemini Embeddings
- ChromaDB
- Cosine Similarity

### Strengths

- Semantic retrieval
- Simple implementation
- Fast retrieval
- Easy to maintain

### Weaknesses

- Weak keyword matching
- Poor performance on ambiguous queries
- Sensitive to embedding quality
- Retrieved incorrect sections for some questions

### Example Observation

Question

> What are the major causes of cancer?

Retrieved

- Prevention
- Exercise
- Alcohol

Expected

- General causes of cancer

Observation

Correct document was retrieved, but incorrect knowledge unit was ranked highest.

Opik classified retrieval quality as **Poor**, indicating that the retrieved chunks were semantically distant from the user's intent.

### Planned Improvements

- Hybrid Search
- BM25
- Cross-Encoder Reranking

---

# Future Benchmark Results

---

## Version 1.1

### Retrieval Strategy

Hybrid Search

Status

Planned

Expected Improvements

- Better keyword matching
- Better handling of exact terminology
- Higher Precision@K
- Lower retrieval distance

Expected Benchmark Changes

| Metric | Expected Trend |
|---------|----------------|
| Success Rate | ↑ |
| Precision@3 | ↑ |
| Recall@3 | ↑ |
| MRR | ↑ |
| Distance | ↓ |

---

## Version 1.2

### Retrieval Strategy

Hybrid Search + Cross Encoder

Status

Planned

Expected Improvements

- Better ranking
- More relevant first result
- Higher MRR

---

## Version 1.3

### Retrieval Strategy

Hybrid Search + Reranking + Query Expansion

Status

Planned

Expected Improvements

- Better handling of natural language
- Improved semantic retrieval
- Better recall

---

## Version 1.4

### Retrieval Strategy

Multi-Query Retrieval

Status

Planned

Expected Improvements

- Better retrieval coverage
- Higher recall
- Improved performance on ambiguous questions

---

## Version 1.5

### Retrieval Strategy

Context Compression

Status

Planned

Expected Improvements

- Smaller prompts
- Reduced token usage
- Improved answer grounding

---

## Version 1.6

### Retrieval Strategy

Parent Document Retrieval

Status

Planned

Expected Improvements

- Richer context
- Better long-form answers
- Reduced context fragmentation

---

# Performance Trend

This section will be updated after every benchmark run.

| Version | Success Rate | Precision@3 | Recall@3 | MRR | Distance |
|----------|-------------:|------------:|----------:|----:|----------:|
| v1.0 | TBD | TBD | TBD | TBD | TBD |
| v1.1 | | | | | |
| v1.2 | | | | | |
| v1.3 | | | | | |
| v1.4 | | | | | |
| v1.5 | | | | | |
| v1.6 | | | | | |

---

# Observations

This section captures qualitative observations from each benchmark run.

## Version 1.0

- Semantic retrieval performs well on direct questions.
- Retrieval quality decreases for broad or ambiguous questions.
- Dense vector search often retrieves the correct document but not the most relevant passage.
- Keyword-heavy queries expose limitations of pure embedding search.
- Opik traces confirmed that retrieval was the weakest stage of the pipeline.

Future versions should reduce these weaknesses.

---

# Opik Evaluation

Every benchmark execution should be logged to Opik.

The following metadata should be attached to each benchmark run.

- Retrieval Strategy
- Benchmark Version
- Success Rate
- Precision@K
- Recall@K
- Mean Reciprocal Rank
- Average Retrieval Distance
- Average Retrieval Time
- Total Benchmark Duration

This enables long-term monitoring and comparison of retrieval quality directly from the Opik dashboard.

---

# Regression Tracking

A new retrieval strategy should only replace the previous implementation if it satisfies the following conditions.

- Success Rate does not decrease.
- Precision@K improves or remains stable.
- Mean Reciprocal Rank improves.
- Retrieval latency remains within acceptable limits.
- No regression is observed in benchmark questions.

If a retrieval strategy fails these conditions, it should not become the default retriever.

---

# Engineering Learnings

This benchmark transforms retrieval optimization from a subjective process into a measurable engineering workflow.

Every retrieval improvement must be supported by benchmark evidence instead of intuition.

The benchmark will serve as the primary validation tool throughout Sprint 4 and future retrieval experiments.
