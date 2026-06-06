# Expand Summer 2026 Research Maintenance Plan
## Complete Execution Document

**Version:** 3.0 — 7th Repository (inha20) Integrated  
**Date:** 2026-06-06  
**Scope:** All 7 repositories  
**Horizon:** June–August 2026

---

## Executive Summary

This document transforms the Summer 2026 maintenance plan from a high-level outline into a **fully actionable project management document** with specific tasks, timelines, risk assessments, and measurable completion criteria.

**Program Goal:**  
Transform 7 individual repositories into a coherent, publicly discoverable, long-term-preserved research program.

**Evaluation Standard:**  
> How can the Summer 2026 maintenance project maximize the long-term value, visibility, and preservation of the research program?

---

## Phase 0: Research Asset Audit (Week 1 — June 5–11)

### 0.1 Repository Inventory Checklist

For each repository, verify:

| Item | 1KMap | 2Symmetric | 3Variable | 4SRT | Portfolio | ANTIGRAVITY | **inha20** |
|---|---|---|---|---|---|---|---|
| README.md exists | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Main paper/thesis file | ✓ | ✓ | ✓ | ✓ | — | — | — |
| Figure/images directory | ✓ | ✓ | pending | — | — | — | — |
| References section | ? | ? | ✓ | ✓ | — | — | — |
| Cross-repository links | partial | partial | partial | ✓ | partial | partial | partial |
| Handover document | ? | ? | ✓ | pending | ✓ | partial | ✓ |
| GitHub Pages enabled | ? | ✓ | ? | ? | ? | — | ? |

**Action:** Complete all cells above. Missing items become Phase 1 tasks.

### 0.2 Backup Verification

Before any modification:

- [ ] Download latest version of all 7 repositories from GitHub
- [ ] Create timestamped local backup (YYYYMMDD_backup/)
- [ ] Verify main paper files are readable and complete
- [ ] Record current commit hashes for all repositories

**Risk:** Losing work during standardization  
**Mitigation:** Backup before every modification session

### 0.3 File Naming Audit

- [ ] List all figure/image files across Papers 1–3
- [ ] Identify naming inconsistencies
- [ ] Document current state before standardization

---

## Phase 1: Repository Stabilization (Weeks 1–2 — June 5–18)

### 1.1 README Quality Review

**Standard README structure (required for all repositories):**

```markdown
# [Repository Name]
## [Subtitle]

> [One-sentence research question]

## Abstract
[3–5 sentence summary suitable for a researcher in a related field]

## Keywords
[5–10 searchable keywords]

## Research Context
[Where this repository fits in the 4-paper program]

## Key Findings
[3–5 bullet points]

## Repository Structure
[File tree with descriptions]

## Related Repositories
[Links to Papers 1–4, Research-Portfolio]

## Status
[Current completion state]

## Author
[Name, institution]
```

**Tasks:**
- [ ] Paper 1 README — add Abstract, Keywords, Research Context sections
- [ ] Paper 2 README — add Abstract, Keywords sections
- [ ] Paper 3 README — verify all sections complete
- [ ] Paper 4 README — verify research branch table accurate
- [ ] Research-Portfolio README — add current research status section
- [ ] ANTIGRAVITY README — expand from single line to full description
- [ ] **inha20 README** — verify Summer 2026 status section is current; confirm GitHub Pages deployment

### 1.2 File Organization Review

For each paper repository:

- [ ] Verify `paper/` or equivalent directory exists and contains main thesis
- [ ] Verify `images/` or `figures/` directory is organized
- [ ] Remove any duplicate files
- [ ] Verify `.gitignore` is appropriate

### 1.3 Cross-Repository Linking

Every repository README must link to:
- [ ] Research-Portfolio (program hub)
- [ ] Paper 4 SRT (theoretical framework)
- [ ] Directly related papers (e.g., Paper 2 links to Papers 1 and 3)

**Standard link block:**
```markdown
## Research Program
This repository is part of the Structure Recognition Research Program.
- [Research Portfolio](https://github.com/inha20/Research-Portfolio) — Program Hub
- [Structure Recognition Theory](https://github.com/inha20/4StructureRecognitionTheory) — Theoretical Framework
- [All Papers](https://github.com/inha20/Research-Portfolio#papers)
```

---

## Phase 2: Figure and Image Standardization (One Dedicated Day — Target: June 20)

### 2.1 Unified Figure Naming Convention

**Standard:** `FigureNN_description.png`

Examples:
- `Figure01_kmap_4variable_gray_code.png`
- `Figure02_exactly0_point_pattern.png`
- `Figure08_xor_checkerboard_0132.png`

**Rules:**
- Two-digit figure number (01, 02, ..., 13)
- Lowercase, underscores only
- Descriptive but concise
- Original files preserved in `figures/originals/` before renaming

### 2.2 Caption Format Standard

```
Figure N. [Descriptive title]. [One-sentence explanation of what the figure shows and why it matters.]
```

Example:
```
Figure 1. 4-variable Karnaugh map with Gray code arrangement. The variable order 
(ABCD → rows: 00,01,11,10; columns: 00,01,11,10) produces checkerboard patterns 
for XOR/XNOR functions.
```

### 2.3 Technical Standards

| Property | Standard |
|---|---|
| Resolution | Minimum 150 DPI (screen); 300 DPI (print-ready) |
| Format | PNG for diagrams; PNG/JPG for photographs |
| Background | White or transparent |
| Font | Consistent across all figures (recommend: same as thesis body) |
| Line weight | Consistent across figures in same paper |
| Color | Consistent scheme across papers in same program |

### 2.4 Figure Inventory Task

For each paper:
- [ ] Create `figures/figure_inventory.md` listing all figures with current filename, new standard filename, caption status
- [ ] Identify figures missing from `figures/` directory
- [ ] Identify figures referenced in text but not present

**Risk:** Destroying original figure metadata  
**Mitigation:** Never delete originals. Move to `figures/originals/`. Rename copies only.

---

## Phase 3: GitHub Pages Development (Weeks 3–6 — June 21 – July 17)

### 3.1 Site Architecture

```
cjh3c.github.io (Research-Portfolio Hub)
├── index.html — Program overview
├── papers/
│   ├── paper1.html — KMap Structure Invariance
│   ├── paper2.html — Symmetric Boolean Functions
│   ├── paper3.html — Variable Rearrangement Invariance
│   └── paper4.html — Structure Recognition Theory
├── theory/
│   └── srt.html — SRT Framework
├── roadmap.html — Research roadmap visualization
└── about.html — Researcher profile
```

### 3.2 Individual Repository Pages

Each paper repository should have a self-contained GitHub Pages site:

- `cjh3c.github.io/2SymmetricBooleanFunctionMinorThesis-main/` — already exists
- `cjh3c.github.io/1KMapStructureInvariance/` — needs setup
- `cjh3c.github.io/3VariableRearrangementInvarianceMinorThesis-main/` — needs setup
- `cjh3c.github.io/4StructureRecognitionTheory/` — needs setup
- `inha20.github.io/inha20/` — index.html 이미 존재; Settings → Pages → Source 설정만으로 즉시 배포 가능

### 3.3 Navigation Design

Every page must have:
- Header: Program name + navigation bar
- Footer: Link to Research-Portfolio hub
- Sidebar (desktop): Research program tree
- "You are here" indicator

### 3.4 Research Roadmap Visualization

Create a visual diagram showing:
```
Boolean Structure Studies (Papers 1–3)
         ↓
Structure Recognition Theory (Paper 4)
         ↓
Human-AI Collaboration Research
         ↓
AI Collaboration Education
```

**Priority:** Papers 1 → 2 → 3 → 4 → Hub (in this order)  
**Completion criteria:** All 5 sites publicly accessible and cross-linked

---

## Phase 4: Repository Content Improvement (Weeks 5–7 — July 1–21)

### 4.1 Paper 3 Completion Tasks

Paper 3 is the most incomplete:
- [ ] Generate and place figures in `figures/` directory
- [ ] Format references in `references/references.md`
- [ ] Complete HANDOVER.md review
- [ ] Verify FUTURE_IDEAS.md is current

### 4.2 Paper 4 Theory Development

Active development tasks for SRT:
- [ ] Expand `theory/CoreQuestions.md` with Q1–Q7 analysis
- [ ] Add `theory/OpenProblems.md` documenting unresolved questions
- [ ] Create `theory/FutureHypotheses.md` for post-H7 directions
- [ ] Draft case study connections (Papers 1–3 → H1–H7 mapping table)

### 4.3 Research-Portfolio Content

- [ ] Complete `ResearchTimeline.md` with all major development dates
- [ ] Finalize `ConceptGenealogy.md` narrative
- [ ] Add `ResearchLog` entries regularly (minimum: one per work session)
- [ ] Create `ProjectManagement/MeetingNotes.md` for documenting decisions

---

## Phase 5: Search Discoverability (Weeks 7–9 — July 14 – July 31)

### 5.1 GitHub Repository Metadata

For each repository:
- [ ] Add descriptive repository description (appears in GitHub search)
- [ ] Add relevant topic tags: `boolean-functions`, `karnaugh-map`, `structure-recognition`, `human-ai-collaboration`, `research-program`
- [ ] Verify repository names are search-friendly
- [ ] Add website link to GitHub Pages

### 5.2 README SEO Optimization

Each README should contain (for search visibility):

**Keywords section:**
```markdown
## Keywords
Karnaugh map, Boolean function, structural invariance, 
structure recognition, human-AI collaboration, visual pattern analysis,
symmetric Boolean function, variable rearrangement, Hamming weight
```

**Abstract section:**
- 100–200 word academic abstract
- Mention key concepts in first paragraph

### 5.3 Cross-Repository Linking Matrix

| From | Links to |
|---|---|
| Paper 1 | Paper 2, Research-Portfolio, Paper 4 |
| Paper 2 | Paper 1, Paper 3, Research-Portfolio, Paper 4 |
| Paper 3 | Paper 2, Research-Portfolio, Paper 4 |
| Paper 4 | All papers, Research-Portfolio |
| Research-Portfolio | All repositories |
| ANTIGRAVITY | Research-Portfolio, Paper 4 |
| **inha20** | **Research-Portfolio, Papers 1–4** (외부 진입점 → 내부 탐색 경로) |

**Completion criteria:** Every repository has working links to all repositories in its row.

---

## Phase 6: Future Projects (August — Exploratory)

### 6.1 Structure-Based Elementary Mathematics for Adults

**Core Idea:**  
Reinterpret elementary mathematics through pattern, structure, symmetry, and meaning.

**Candidate Topics:**
- Multiplication Tables as pattern systems
- Fractions as structural relationships
- Geometry as symmetry analysis
- Number patterns as structure discovery exercises

**Proposed Repository:** `StructureBasedMathematics` (new)  
**Entry Point:** Create concept document before building repository

**Action:** Draft `Research-Portfolio-main/FutureProjects/StructureBasedMathematics_Concept.md`

### 6.2 Human-AI Collaboration Research (Formal Track)

**Transition:** Move from exploratory hypothesis to systematic research design

**Milestones:**
- [ ] Formalize H1–H7 into testable propositions
- [ ] Design a study comparing human vs. AI structure discovery
- [ ] Identify relevant literature (cognitive science, HCI)
- [ ] Draft research proposal

### 6.3 AI Collaboration Education

**Core Question:** How should human-AI collaboration be taught?

**Initial Product:** A short educational framework document  
**Target Audience:** University students learning with AI tools  
**Action:** Create `Research-Portfolio-main/FutureProjects/AICollaborationEducation_Concept.md`

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| Figure files corrupted or lost during standardization | Low | High | Always backup before renaming; keep originals |
| GitHub Pages deployment fails | Medium | Medium | Test each page locally first |
| Theory development stalls | Low | Medium | Return to empirical observations for new questions |
| Cross-repository links break after GitHub changes | Low | Medium | Use full URL links, not relative paths |
| AI session loses context | High | Medium | MasterHandoverDocument.md solves this |
| Paper 3 figures never generated | Medium | High | Set explicit deadline; use existing figure list |

---

## Completion Criteria

The Summer 2026 maintenance project is complete when:

- [ ] All 7 repositories have complete, standard-format READMEs
- [ ] All repositories are backed up
- [ ] Figure naming is unified across Papers 1–3
- [ ] All 5 GitHub Pages sites are publicly accessible
- [ ] Cross-repository linking is complete (linking matrix verified)
- [ ] Research-Portfolio serves as functional navigation hub
- [ ] `MasterHandoverDocument.md` is up-to-date
- [ ] `ProjectStatus.md` reflects final state
- [ ] At least one future project has a concept document

---

## Progress Tracking

Update `ProjectManagement/ProjectStatus.md` after each work session.  
Record significant decisions in CHANGELOG or session notes.

---

*Last Updated: 2026-06-06 (v3.0 — inha20 7번째 저장소 정식 편입)*  
*Owner: Choi Jonghun / ANTIGRAVITY*  
*Review trigger: GitHub Pages deployment complete*
