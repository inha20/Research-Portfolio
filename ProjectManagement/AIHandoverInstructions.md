# AI Handover Instructions
## Structure Recognition Research Program

**Version:** 3.1 — Session 25: Branch 8 스테일 ⚠️ 제거 (Part 3 동기화 — MasterHandoverDocument §6 확정 내용 반영); ConsistencyAuditFindings 항목 13 허위 완료 정정  
**Date:** 2026-06-13  
**Supersedes:** Version 2.9

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
  Branch 8: 6BooleanFunctionSpaceTheory (Applied Mathematics Extension — 9번째 저장소, 2026-06-12 정식 지정)
  Branch 9 (potential): Post Lattice × KMap 시각화 ← ⚠️ 탐색 단계
  Branch 10 (potential): Boolean Function Space Topology ← ⚠️ 탐색 단계
  Branch 11 (potential): 구조 인식 실험 및 계산 모델 ← ⚠️ 탐색 단계
  세부내용: MasterHandoverDocument §6 Branch 표 참조
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

## Part 5: The Hypotheses of SRT (H1–H10)

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
| **H8** | **Concept-as-Lens** | **Concepts function as observation lenses — changing what is visible** *(통합 확장 가설 — SRT v0.3 승격)* |
| **H9** | **Concept Evolution** | **Research generates concepts; concepts generate further research** *(통합 확장 가설 — SRT v0.3 승격)* |
| **H10** | **Generative Concept** | **Concepts differ in their generativity — some open more research than others** *(통합 확장 가설 — SRT v0.3 승격)* |

**Current SRT version:** v0.3 (as of Session 12, 2026-06-06). See `4StructureRecognitionTheory-main/theory/StructureRecognitionTheory_v0.3.md`.

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

## Part 7: Repository Status (as of 2026-06-12)

| Repository | Health | Status Summary |
|---|---|---|
| 1KMapStructureInvariance | Stable | README 표준화 완료 (Phase 5 ✅) |
| 2SymmetricBooleanFunctionMinorThesis | Stable | README 표준화 완료; images/ 중복 파일 연구자 직접 정리 필요 |
| 3VariableRearrangementInvarianceMinorThesis | Active | README Abstract 추가 완료; 그림 25개 연구자 직접 제작 필요 |
| 4StructureRecognitionTheory | Active | SRT v0.3 + H1–H10 + OpenProblems v1.1 (OP-01–09) + CoreQuestions v2.0 완료 |
| **5HumanAIResearchCollaboration** | **Complete** | **paper.md Session 17 대규모 확장; GitHub Pages 배포 완료** |
| Research-Portfolio | Active | GitHub Pages 배포 완료 (Session 16) |
| ANTIGRAVITY | Monitoring | Session continuity maintenance |
| inha20 | Active | README Abstract 추가 완료; GitHub Pages 배포 완료 |
| **6BooleanFunctionSpaceTheory** | **Active** | **9번째 저장소 (2026-06-12) — Branch 8 정식 지정 완료 (2026-06-12); Research-Portfolio·inha20 역방향 링크 추가 완료 (Session 23)** |

---

## Part 8: Summer 2026 Priority Queue

Handle in this order:

1. ✅ Repository stabilization (verify completeness, update READMEs) — Phase 1 완료
2. ✅ Research-Portfolio development (timeline, concept genealogy, research log) — Phase 2 진행 중
3. ✅ GitHub Pages construction — Phase 3 완료 (2026-06-07, Session 16)
4. 🔴 Image/figure standardization (연구자 직접 Paper 3 그림 25개) — Phase 2 잔여
5. 🟠 Repository content improvement — Phase 4 활성 (June–July)
6. 🟠 Search discoverability improvements — Phase 5 활성 (SEO 메타태그 AI 실행 가능)
7. Future project exploration (math ed, Human-AI collaboration formal track) — Phase 6

---

## Part 9: Key Documents by Category

### For Understanding the Program
- `Research-Portfolio-main/ProjectManagement/MasterHandoverDocument.md` ← Start here
- `Research-Portfolio-main/ResearchProgramMap.md`
- `Research-Portfolio-main/ConceptGenealogy.md`

### For Understanding the Theory
- `4StructureRecognitionTheory-main/theory/StructureRecognitionTheory_v0.3.md` ← **현재 최신 버전**
- `4StructureRecognitionTheory-main/theory/Hypotheses.md` ← H1–H10 포함
- `4StructureRecognitionTheory-main/theory/CoreQuestions.md` ← v2.0 (Level 0–8, Q1–Q15)
- `4StructureRecognitionTheory-main/theory/OpenProblems.md` ← OP-01–OP-09
- `4StructureRecognitionTheory-main/theory/CaseStudyConnections.md` ← Papers 1–3 → H1–H7 mapping

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
5. Check `ConsistencyAuditFindings_20260612.md` for any unresolved audit items
6. 다중 파일 편집이 예정된 경우, **Part 11을 먼저 읽는다** (Multi-File Editing 계획 구조 — 헤더/풋터 불일치 재발 방지)
7. Prefer clarifying questions over confident assumptions

---

## Part 11: Multi-File Editing — 검증된 계획 구조 (2026-06-12)

> 반복적 세션 강제 종료 분석에서 도출한 구조. 다수 파일을 수정하는 모든 세션에서 적용할 것.

**0단계 — 사전 읽기 (Pre-flight)**

편집 대상 파일 전부를 순서대로 읽는다. 각 파일에서 기록할 항목: (a) 헤더 버전 번호, (b) 풋터 버전 번호, (c) Change Log 마지막 항목. 한국어 파일은 인코딩 확인 포함. 헤더≠풋터일 경우 시작전에 메모.

**1단계 — 중요도 역순 편집 (이 파일 먼저)**

편집 순서: `AIHandoverInstructions.md` → `MasterHandoverDocument.md` → 기타. 갑작스런 종료 시 가장 많이 참조되는 파일이 최신 상태로 남도록 한다. 광범위하게 참조되는 문서가 먼저, 좌폼 범위가 마지막.

**2단계 — 원자적 단위 편집 + 즉시 검증**

파일 하나 편집 완료 직후 해당 파일을 다시 읽는다. 확인 체크리스트:
- 헤더 버전 = 풋터 버전?
- 자기참조 문구(⚠️ 알림, "v?.? 에서 멈춥있음" 등) 읽었다면 해당 문구도 갱신했는가?
- Change Log에 현재 수정 반영 항목 존재?

공통 오류 패턴 주의: 한국어 파일에서 `str_replace` 실패 시 유니코드 코드포인트 직접 확인.

**3단계 — 교차 문서 일관성 점검**

- 버전 번호: 헤더·풋터 동시 업데이트. 한 쪽만 수정하지 말 것.
- Session History: MasterHandoverDocument에 해당 세션 행 있는가?
- ✅ 이미지 규칙 충돌 해소 완료 (Session 21, 2026-06-13): `MasterHandoverDocument.md` §8이 이 문서 Part 2와 일치 — AI 코드 기반 그림 생성 모두 ❌ 금지로 통일됨.

**4단계 — ConsistencyAuditFindings 증분 갱신**

작업 완료된 항목은 즉시 감사 보고서에 체크 표시. 미점검사항 12개 중 AI 실행 가능 항목(1·2·4·7·8·9·10번)을 우선 처리.

이 구조를 무시하는 것이 헤더/풋터 버전 재발의 주원인입니다.

---

## Change Log

| Version | Date | Change |
|---|---|---|
| 3.1 | 2026-06-13 | **Session 25 정정**: Part 3 Branch 8 스테일 ⚠️ 제거 (MasterHandoverDocument §6 확정 내용 동기화; "9번째 저장소" → "Branch 8" 명시); Part 7 6BoolFuncSpace ⚠️ Active → Active, 번호 충돌 표기 제거; ConsistencyAuditFindings 항목 13 허위 완료 정정 (INTEGRATION_DIRECTIVE.md 실제 미수정, 13-C 결정 대기), 항목 14 ✅ 완료 반영 |
| 3.0 | 2026-06-13 | **Session 24 연구자 결정 실행**: 항목 13 (C: 전면 수정) — INTEGRATION_DIRECTIVE.md Architecture B 번호 체계로 전면 수정 완료; 항목 14 (탐색적 등록) — MasterHandoverDocument §6 Branch 9–11 ⚠️ 탐색 단계 등록; ConsistencyAuditFindings 항목 13·14 완료 처리; AIHandoverInstructions v3.0 |
| 2.9 | 2026-06-13 | **Session 23 연구자 결정 반영**: Finding 1 원칙(폴더 내용 문서 반영) 적용 — Research-Portfolio·inha20 README Repo 6 역방향 링크 추가 완료; Finding 2 해결(inha20 HANDOVER.md 구버전 지시서 → 인간 삭제); Finding 3·6·7 현행 유지; 미문서화 항목 13(INTEGRATION_DIRECTIVE 번호 충돌)·14(후보 저장소 3개 미등록) ConsistencyAuditFindings에 등록; Part 7 Repo 6 상태 업데이트 |
| 1.0 | Prior | Initial handover document |
| 2.0 | 2026-06-05 | Full expansion: Architecture B adopted, Human-AI protocol, hypothesis table, repository status, priority queue |
| 2.1 | 2026-06-05 | **Human-Created Style Standard added**: All figures must be created by human tools (Python/LaTeX/drawing apps); AI image generation explicitly prohibited |
| 2.2 | 2026-06-05 | **Image Rule Unified**: AI code-based figure generation also prohibited; spec-based workflow adopted |
| 2.3 | 2026-06-06 | **inha20 7번째 저장소 전면 통합**: Part 7 표에 inha20 행 추가; 6→7 전환 완료 |
| 2.4 | 2026-06-06 | **5HumanAIResearchCollaboration 8번째 저장소 전면 통합**: Part 3 아키텍쳐 Paper 5 추가; Part 7 표에 행 추가; 7→8 전환 완료 |
| 2.5 | 2026-06-12 | **Session 18 대폭 업데이트 (ConsistencyAuditFindings 반영)**: H8–H10 가설 Part 5 추가; SRT v0.3 + Phase 3 완료 반영; 6BooleanFunctionSpaceTheory 9번째 저장소 Part 3/7 등록; 번호 충돌 주석 추가; 감사 알림 포인터 추가 |
| 2.6 | 2026-06-12 | **Session 19 교정**: 감사 알림 ⚠️ (v2.4 스테일 경고) 제거; Part 7 표 Session 18 기준으로 전면 갱신; Part 8 Priority Queue 현행화; Part 9 SRT 참조 v0.1→v0.3 교정; OpenProblems + CaseStudyConnections + CoreQuestions v2.0 링크 추가; Part 10 ConsistencyAuditFindings 점검 단계 추가; Change Log v2.5/v2.6 정식 기록 |
| 2.7 | 2026-06-12 | **Session 19 계획 구조 추가**: Part 11 (Multi-File Editing 검증된 계획 구조 — 0~4단계) 신설; ConsistencyAuditFindings Recommended Action Plan 완료 현황 반영 (Step 6 ✅, 나머지 상태 명시) |
| 2.8 | 2026-06-13 | **Session 21 미완성 수정 처리 (Session 22)**: Part 10 항목 6 추가 (Part 11 진입점 연결 — Session 21에서 기록만 남기고 파일 미수정이었던 부분 실제 반영); Part 11 Step 3 이미지 규칙 충돌 해소 반영 (충돌은 Session 21에서 해결됐으나 이 문서에 잔존 문구 수정); ConsistencyAuditFindings Step 2 완료 처리 |

---

*Maintained in: Research-Portfolio-main/ProjectManagement/*  
*Cross-reference: ANTIGRAVITY-main/RESEARCH_STATUS.md*  
*Last Updated: 2026-06-13 (v3.1 — Session 25: Part 3 Branch 8 스테일 ⚠️ 제거; ConsistencyAuditFindings 항목 13 허위 완료 정정)*
