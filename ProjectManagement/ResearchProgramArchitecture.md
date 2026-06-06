# Research Program Architecture

**Version:** 2.1  
**Date:** 2026-06-06  
**Status:** Architecture B — Officially Adopted (8개 저장소 반영)

---

## Purpose

Define the overall structure, design principles, concept genealogy, and repository roles of the research program.  
This document serves as the architectural specification — the blueprint against which all changes should be evaluated.

---

## Program Structure

```
Paper 1: KMap Structure Invariance
 ↓
Paper 2: Symmetric Boolean Function Visual Patterns
 ↓
Paper 3: Variable Rearrangement Invariance
 ↓
Paper 4: Structure Recognition Theory (SRT)   ← Theoretical Hub
 ↓
Paper 5: Human-AI Research Collaboration      ← Methodological Meta-layer

Research-Portfolio   ← Program Navigation Hub
inha20               ← GitHub Public Entry Point
ANTIGRAVITY          ← AI Collaboration Workspace
```

---

## Architecture Decision: Architecture B Adopted

**Decision Date:** 2026-06-05  
**Decision:** Architecture B (Empirical Foundation Model) is the official program architecture.

### Architecture B — Empirical Foundation Model

```
Empirical Observations (Papers 1–3)
         ↓
  ┌──────────────────────────────────┐
  │   Structure Recognition Theory   │
  │        (Paper 4 — Hub)           │
  └──────────────────────────────────┘
         ↓
  ┌─────────────────┐  ┌──────────────────────┐  ┌────────────────────────┐
  │ Human-AI Collab │  │ AI Collab Education  │  │ Structure-Based Math   │
  └─────────────────┘  └──────────────────────┘  └────────────────────────┘
```

**Rationale for choosing Architecture B:**
1. Papers 1–3 all contribute empirical phenomena that Paper 4 theorizes about
2. The conceptual connections across papers are real and documented
3. Architecture B provides a unified research narrative without sacrificing paper independence
4. It accurately reflects the historical development of the researcher's thinking

**Architecture A (rejected):** Independent projects model. Rejected because it misrepresents the actual conceptual relationships.

---

## Concept Genealogy (Preservation Required)

```
Pattern
 ↓ (first observation: KMap checkerboards)
Layer Structure
 ↓ (discovery: Hamming Weight layers explain pattern positions)
Equivalence
 ↓ (observation: functions with same pattern despite different arrangements)
Structural Invariance
 ↓ (question: what is preserved across transformations?)
Structure Recognition Theory
 ↓ (meta-question: why do certain structures become research-worthy?)
Human-AI Collaboration Model
 ↓ (observation: humans discover, AI expands explanation space)
[Future: AI Collaboration Education / Structure-Based Mathematics]
```

This genealogy must be preserved verbatim in `Research-Portfolio/ConceptGenealogy.md`.

---

## Repository Roles (Strict Definitions)

| Repository | Role | Type | Independence |
|---|---|---|---|
| 1KMapStructureInvariance | Empirical Case Study 1 | Paper repository | Full — independent publication path |
| 2SymmetricBooleanFunctionMinorThesis | Empirical Case Study 2 | Paper repository | Full — independent publication path |
| 3VariableRearrangementInvarianceMinorThesis | Empirical Case Study 3 | Paper repository | Full — independent publication path |
| 4StructureRecognitionTheory | Theoretical Hub | Theory repository | Central — integrates all others |
| **5HumanAIResearchCollaboration** | **Paper 5 — Methodological Study** | **Paper repository** | **Meta-layer — 연구 과정 자체가 연구 대상** |
| Research-Portfolio | Program Hub | Navigation/planning | Central — entry point for program |
| ANTIGRAVITY | AI Workspace | Operational | Supporting — continuity maintenance |
| inha20 | GitHub Profile Repository | Public entry point | 연구 프로그램 외부 진입점 |

---

## Research Branches

| # | Branch Name | Repositories | Status |
|---|---|---|---|
| 1 | Karnaugh Map Visual Pattern Analysis | Paper 1 | Papers written |
| 2 | Symmetric Boolean Function Visual Patterns | Paper 2 | Papers written |
| 3 | Variable Rearrangement Invariance | Paper 3 | Papers written |
| 4 | Structure Recognition Theory | Paper 4 | Framework in development |
| **5** | **Human-AI Research Collaboration** | **Paper 5** | **Active — 이론 압축 단계** |
| 6 | AI Collaboration Education | Future repo | Exploratory |
| 7 | Structure-Based Elementary Mathematics | Future repo | Exploratory |

---

## Design Principles

1. **Preserve independent papers.** Papers 1–3 must remain independently publishable.
2. **Preserve discovery history.** The sequence of discovery is itself research data.
3. **Preserve concept genealogy.** The development from Pattern to SRT must be traceable.
4. **Integrate theory through Paper 4.** SRT is the theoretical integration layer — not the papers themselves.
5. **Maintain clear repository roles.** No repository should serve a role already occupied by another.
6. **Prefer preservation over efficiency.** When in doubt, preserve more rather than less.
7. **Document architectural decisions.** Every significant structural decision goes in CHANGELOG or this document.

---

## Prohibited Actions

- ❌ Merge Papers 1–3 into a single paper
- ❌ Remove discovery history documents
- ❌ Flatten the concept hierarchy into a simple list
- ❌ Treat any two repositories as duplicates
- ❌ Revert from Architecture B to Architecture A without documented justification
- ❌ Add new repositories without defining their role relative to this architecture

---

## Evaluation Question

Before any proposed change, ask:

> **Does this change strengthen or weaken the long-term architecture of the research program?**

Secondary question:

> **Does this change preserve or reduce the discoverability of the research program's intellectual development?**

---

## Architecture Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | Prior | Initial architecture document |
| 2.0 | 2026-06-05 | Architecture B formally adopted; prohibition list added; rationale documented |
| 2.1 | 2026-06-06 | 5HumanAIResearchCollaboration (Paper 5) 정식 편입; inha20 행 추가; 프로그램 구조도에 Paper 5 Meta-layer 반영; Branch 5 실질 저장소로 업데이트; 저장소 수 6→8 |

---

*Next review: Before adding any new repository to the program*
