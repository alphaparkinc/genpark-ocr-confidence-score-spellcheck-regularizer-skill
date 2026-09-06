# GenPark AI Agent Skill - OCR Confidence Score Spellcheck Regularizer

Fixes OCR ligature corruptions, glyph confusions (rn -> m, 0 -> O), and low-confidence scan anomalies.

Verified by [GenPark AI](https://genpark.ai) and compatible with [Model Context Protocol (MCP)](https://genpark.ai/mcp).

## Architecture Diagram

```mermaid
graph TD
    A[OCR Token Stream with Confidence Scores] --> B[Glyph Confusion Pattern Matcher]
    B --> C[Ligature Normalizer fi/fl/ae]
    C --> D[Alphanumeric Boundary Validator]
    D --> E[Clean Synthesized Text Flow]
```

## Features
- **Deterministic Character Replacements**: Reconstructs words degraded by poor scan quality.
- **Zero External Dependencies**: Pure Python standard library implementation.
