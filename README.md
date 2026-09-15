# Memora

> A local-first, RAG-based personal knowledge retrieval system for searching and understanding documents using natural language.

## Overview

Memora is a learning-focused software project that explores how modern Retrieval-Augmented Generation (RAG) systems work.

The goal is to build a system that can automatically ingest documents from selected local folders, understand their content, retrieve relevant information, and provide source-grounded answers to natural-language questions.

Instead of requiring users to manually organize information into notes or links, Memora is designed to work on top of existing documents and make their contents easier to retrieve and understand.

## Problem

Personal information is often scattered across:

- PDF files
- Word documents
- Text files
- Markdown notes
- Research papers
- College documents
- Project documentation
- Other local files

Traditional keyword search works well for finding exact words, but it is less effective for questions involving context, meaning, or relationships between pieces of information.

For example:

> "What did I write about vector databases in my research notes?"

Memora aims to retrieve the relevant content and generate an answer based on those sources.

## Core Idea

The planned architecture is:

```text
Local Documents
      |
      v
Document Ingestion
      |
      v
Text Extraction
      |
      v
Chunking
      |
      v
Embeddings
      |
      v
PostgreSQL + pgvector
      |
      v
Semantic Retrieval
      |
      v
LLM
      |
      v
Answer + Sources
