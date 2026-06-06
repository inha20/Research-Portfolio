# AI Handover Instructions
## Structure Recognition Research Program

**Version:** 2.4 — 8th Repository (5HumanAIResearchCollaboration) Fully Integrated  
**Date:** 2026-06-06  
**Supersedes:** Version 2.3

> **Start here if you are an AI collaborator joining this research program.**  
> Read this document before touching any file in any repository.

---

## Part 1: Program Identity

### What You Are Joining

This is a long-term research program by a single researcher (Choi Jonghun, Inha University) investigating **how humans discover structure, assign meaning, and generate research questions**.

The program is **not** a loose collection of papers. It is a unified intellectual project:

- **Papers 1–3** = empirical case studies (specific phenomena observed and documented)
- **Paper 4** = meta-theoretical framework explaining why those phenomena became research
- **Research-Portfolio** = program hub (navigation, history, planning)
- **ANTIGRAVITY** = AI collaboration workspace (continuity between AI sessions)

### The Central Question
> *How do humans come to see something new?*

This question is the north star of the entire program.

---

## Part 2: What Not To Do

These are **hard constraints**. Violating them damages the research program.

| ❌ Never Do | Reason |
|---|---|
| Merge Papers 1–3 into a single paper | They are independent case studies with separate publication paths |
| Delete or overwrite historical documents | Discovery history is primary data in this research program |
| Flatten the concept hierarchy | The genealogy (Pattern → Layer → Equivalence → Invariance → SRT) is itself a research finding |
| Rename figures without preserving originals | Figure metadata is part of the research record |
| Force theoretical frameworks onto early observations | The researcher discovers phenomena before theories; this sequence matters |
| Treat repositories as duplicates | Each repository has a defined, distinct role |
| Produce more content when organization is lacking | Always prefer conceptual organization over content generation |
| **Use AI image generators (DALL-E, Midjourney, SD, etc.) to create figures** | **No reproducibility; copyright issues; breaks visual style consistency with existing figures** |
| **Write code (Python, LaTeX, etc.) to auto-generate figures, even indirectly** | **AI involvement in final image output is prohibited regardless of method** |

### 연구 프로그램 이미지 규칙 — AI 그림 절대 금지 + 명세서 기반 워크플로 (2026-06-05)

**모든 이미지 파일은 "사람이 생성한 스타일"로 통일한다. AI는 최종 이미지 픽셀 결정에 어떠한 방식으로도 관여해서는 안 된다.**

#### ❌ 절대 금지 (방법 불문)

| 금지 방법 | 이유 |
|---|---|
| DALL-E, Midjourney, Stable Diffusion, ChatGPT image 등 AI 이미지 생성 서비스 | 스타일 불일치; 재현성 없음 |
| AI가 Python, matplotlib, LaTeX, TikZ 등 코드를 작성하여 그림 생성 | AI가 최종 이미지 결정에 관여함 |
| AI가 생성한 코드 기반 자동 그림 (간접 방식 포함) | 동일한 이유 |

> **원칙:** AI가 코드를 작성하고 그 코드를 실행하여 그림을 만드는 것도 **금지**.

#### ✅ 허용 (인간 직접 제작)

| 허용 방법 | 설명 |
|---|---|
| 그리기 도구 (PowerPoint, Keynote, Draw.io, Inkscape 등) | 연구자 직접 제작 |
| 손 그림 스캔 | 연구자 직접 작성 후 디지털화 |
| 그림 편집 소프트웨어 (GIMP, Illustrator 등) | 연구자 직접 조작 |

#### AI의 허용 역할 — 명세서 기반 워크플로

그림이 필요한 경우 AI는 다음 두 가지 역할만 수행한다:

**① 본문에 `[간단한 설명]` 플레이스홀더 삽입**

본문 작성 시 이미지가 들어갈 위치에 다음과 같이 표기한다:

```
[그림: 4변수 카르노맵 AB/CD 배열의 XOR 체커보드 패턴]
```

연구자가 나중에 직접 이미지를 생성하여 해당 위치에 삽입할 수 있게 한다.

**② 그림 명세서 작성 (그림 제작용 상세 지침)**

연구자(인간)가 그림을 직접 만들 수 있도록 다음 내용을 포함한 명세서를 작성한다:
- 그림 번호 및 제목
- 그림에 표현해야 할 내용 (격자 구조, 셀 값, 레이블 등)
- 색상·크기·스타일 기준 (`ImageStandardizationGuide.md` 준수)
- 저장 경로 및 파일명 (명명 규칙 준수)
- 본문에서 참조하는 위치

#### 스타일 기준점

- **Paper 1 기준:** `images/ABCDXOR.png`, `images/ABCDXNOR.png`
- **Paper 2 기준:** `images/01.png` ~ `images/13.png`
- 세부 지침: `Research-Portfolio-main/ProjectManagement/ImageStandardizationGuide.md`

---

## Part 3: The Research Architecture (Architecture B — Official)

```
Empirical Foundation Layer:
  Paper 1: KMap Structure Invariance
  Paper 2: Symmetric Boolean Function Patterns  
  Paper 3: Variable Rearrangement Invariance
           ↓
Theoretical Integration Layer:
  Paper 4: Structure Recognition Theory (SRT)
           ↓
Methodological Layer:
  Paper 5: Human-AI Research Collaboration
           (연구 프로그램을 가능하게 한 과정 연구 — 자기 참조적)
           ↓
Application Domains:
  Branch 6: AI Collaboration Education
  Branch 7: Structure-Based Elementary Mathematics
```

This architecture was formally decided on 2026-06-05. Do not propose reverting to Architecture A (independent projects model).

---

## Part 4: Concept Genealogy — Preserve at All Costs

```
Pattern (1st observation: KMap checkerboards)
 ↓
Layer Structure (Hamming Weight Layers)
 ↓
Equivalence (functions with same pattern under different arrangements)
 ↓
Structural Invariance (what is preserved across transformations)
 ↓
Structure Recognition Theory (why structures become meaningful)
 ↓
Human-AI Collaboration Model (roles in collaborative discovery)
```

Each step represents a **real intellectual discovery** made by the researcher.  
Do not summarize this into a flat list. The sequence is the story.

---

## Part 5: The Seven Hypotheses of SRT

All are **exploratory**. None are established. Treat them as research directions, not conclusions.

| # | Name | Core Claim |
|---|---|---|
| H1 | Structure Discoverer | Humans have comparative advantage in structure discovery over AI |
| H2 | Representation Transformation | Representation change enables structure discovery |
| H3 | Attention Filter | Not all patterns receive investigative attention |
| H4 | Significance Filter | Implicit filter: "is this worth investigating?" |
| H5 | Explanation Anticipation | Humans feel a pattern "should have an explanation" before finding it |
| H6 | Explanatory Significance | Research begins from detection of explanatory potential, not structure per se |
| H7 | Mature Structure Discoverer | Human core role = detecting explanation opportunity |

---

## Part 6: Human-AI Collaboration Model

### How This Researcher and AI Work Together

The researcher has observed this pattern repeatedly across this project:

```
Human:  Notices something unusual
        ↓
AI:     Names it, connects it to frameworks
        ↓
Human:  Selects which connection is meaningful
        ↓
AI:     Expands explanation space
        ↓
Human:  Decides the research direction
```

**Your role as AI collaborator:**
- You are the **expansion engine**, not the decision maker
- Suggest frameworks; let the human select
- Document observations as observations, not conclusions
- When something seems important but unresolved, mark it as an open question, not a solved problem

---

## Part 7: Repository Status (as of 2026-06-05)

| Repository | Health | Immediate Needs |
|---|---|---|
| 1KMapStructureInvariance | Stable | README update, cross-links |
| 2SymmetricBooleanFunctionMinorThesis | Stable | GitHub Pages integration |
| 3VariableRearrangementInvarianceMinorThesis | Active | Image standardization, figure placement |
| 4StructureRecognitionTheory | Active | Theory development continues |
| **5HumanAIResearchCollaboration** | **Active** | **이론 압축·통합 (ANTIGRAVITY_TheoryIntegrationTask.md 실행); 확장자 없는 파일 .md 정리; 폴더 구조 정비** |
| Research-Portfolio | Active | GitHub Pages, program documentation |
| ANTIGRAVITY | Monitoring | Session continuity maintenance |
| inha20 | Active | HANDOVER.md 생성 완료(2026-06-06); GitHub Pages 배포 대기; README 현행화 |

---

## Part 8: Summer 2026 Priority Queue

Handle in this order:

1. Repository stabilization (verify completeness, update READMEs)
2. Research-Portfolio development (timeline, concept genealogy, research log)
3. GitHub Pages construction (Papers → Hub)
4. Image/figure standardization (one dedicated session)
5. Search discoverability improvements
6. Future project exploration (math ed, Human-AI collaboration formal track)

---

## Part 9: Key Documents by Category

### For Understanding the Program
- `Research-Portfolio-main/ProjectManagement/MasterHandoverDocument.md` ← Start here
- `Research-Portfolio-main/ResearchProgramMap.md`
- `Research-Portfolio-main/ConceptGenealogy.md`

### For Understanding the Theory
- `4StructureRecognitionTheory-main/theory/StructureRecognitionTheory_v0.1.md`
- `4StructureRecognitionTheory-main/theory/Hypotheses.md`
- `4StructureRecognitionTheory-main/theory/CoreQuestions.md`

### For Understanding AI Workflow
- `ANTIGRAVITY-main/MESSAGE_TO_ANTIGRAVITY.md`
- `ANTIGRAVITY-main/RESEARCH_STATUS.md`
- This document

### For Summer 2026 Project Management
- `Research-Portfolio-main/ProjectManagement/Expand_Summer2026_ResearchMaintenancePlan.md`
- `Research-Portfolio-main/ProjectManagement/ProjectStatus.md`
- `Research-Portfolio-main/Summer2026Plan.md`

---

## Part 10: Recommended First Actions for a New AI Session

1. Read `MasterHandoverDocument.md` (this directory)
2. Read `ANTIGRAVITY-main/RESEARCH_STATUS.md` for current session context
3. Ask the researcher: "Where did we leave off?" rather than assuming continuity
4. Check `ProjectStatus.md` for current task queue
5. Prefer clarifying questions over confident assumptions

---

## Change Log

| Version | Date | Change |
|---|---|---|
| 1.0 | Prior | Initial handover document |
| 2.0 | 2026-06-05 | Full expansion: Architecture B adopted, Human-AI protocol, hypothesis table, repository status, priority queue |
| 2.1 | 2026-06-05 | **Human-Created Style Standard added**: All figures must be created by human tools (Python/LaTeX/drawing apps); AI image generation explicitly prohibited |
| 2.2 | 2026-06-05 | **Image Rule Unified**: AI code-based figure generation also prohibited; spec-based workflow adopted |
| 2.3 | 2026-06-06 | **inha20 7번째 저장소 전면 통합**: Part 7 표에 inha20 행 추가; 6→7 전환 완료 |
| 2.4 | 2026-06-06 | **5HumanAIResearchCollaboration 8번째 저장소 전면 통합**: Part 3 아키텍쳐 Paper 5 추가; Part 7 표에 행 추가; 7→8 전환 완료 |

---

*Maintained in: Research-Portfolio-main/ProjectManagement/*  
*Cross-reference: ANTIGRAVITY-main/RESEARCH_STATUS.md*
