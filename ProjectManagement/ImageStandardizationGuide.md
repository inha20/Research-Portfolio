# Image Standardization Guide
## Structure Recognition Research Program

**Version:** 2.1 — Spec-Based Workflow & Placeholder Notation Added  
**Date:** 2026-06-05  
**Scope:** Papers 1–4 and all related research assets

---

## Purpose

Establish a unified visual style across all papers so that any figure can be placed into any paper in the program while appearing to belong to the same research program.

**Core Question:**
> Can this figure be placed into Papers 1, 2, 3, or 4 while still appearing to belong to the same research program?

---

## Figure Naming Convention

**Standard format:** `FigureNN_description.png`

| Rule | Example |
|---|---|
| Two-digit zero-padded number | `Figure01_`, `Figure09_`, `Figure13_` |
| Lowercase description, underscores only | `kmap_4variable_gray_code` |
| No spaces, no special characters | ✅ `Figure03_exactly0_point_pattern` |
| Originals preserved before renaming | `figures/originals/01.png` |

**Full example:** `Figure01_kmap_4variable_gray_code.png`

---

## Caption Format Standard

**Format:**
```
Figure N. [Descriptive title]. [One sentence explaining what the figure shows and why it matters.]
```

**Examples:**
```
Figure 1. 4-variable Karnaugh map with Gray code arrangement. The variable ordering
(ABCD) in Gray code sequence produces the checkerboard pattern characteristic of
XOR and XNOR functions.

Figure 8. XOR checkerboard pattern under 0132 variable ordering. The diagonal
alternation of 0s and 1s is invariant under this arrangement, demonstrating that
the checkerboard structure survives certain variable rearrangements.
```

**Rules:**
- Caption always ends with a period
- Do not use "As shown above" or "The figure below"
- Explain significance, not just appearance

---

## Technical Standards

### Resolution
| Use Case | Minimum DPI |
|---|---|
| Screen / GitHub display | 96 DPI |
| Print-ready submission | 300 DPI |
| Standard working resolution | 150 DPI |

### Dimensions
- All K-map figures: consistent cell size (e.g., 60×60px per cell)
- Consistent canvas margins across all figures in a paper
- Portrait or landscape orientation declared consistently per paper

### File Format
| Content Type | Format |
|---|---|
| K-map diagrams | PNG (lossless) |
| Pattern illustrations | PNG |
| Photographs (if any) | JPG |
| Vector diagrams | SVG + PNG export |

---

## Color Convention (STRICT)

All papers must use the **same** cell color convention:

| Cell Value | Color |
|---|---|
| 0 (minterm = 0) | White `#FFFFFF` |
| 1 (minterm = 1) | Black `#000000` or Dark Gray `#333333` |

**Prohibited:**
- Mixing White/Black with White/Gray in the same program
- Using color (red, blue, green) for cell values without explicit justification
- Different color meanings in different figures within the same paper

**Highlight/Annotation Colors** (consistent across all papers):
- Group boxes: Blue `#2563EB` with 2px border
- Important regions: Orange `#F59E0B` background highlight
- Labels: Same font color as body text (`#111111`)

---

## Typography Standard

| Element | Specification |
|---|---|
| Figure labels (0, 1, A, B) | Same font as thesis body; size 10–12pt |
| Variable names (A, B, C, D) | Same font, italic or bold consistent per paper |
| Axis labels | Same font, regular weight |
| Figure caption | Same font, 1pt smaller than body |

**Rule:** Do not use system default fonts. Use the same font family across all figures in all papers.

---

## Line Style Standard

| Element | Style |
|---|---|
| K-map grid lines | 1px solid, `#888888` |
| Group box borders | 2px solid, group color |
| Arrows | 1.5px, arrowhead style consistent |
| Highlight boxes | 2px border, 10% opacity fill |

---

## Figure Inventory Requirement

Each paper repository must maintain a `figures/figure_inventory.md`:

```markdown
# Figure Inventory — [Paper Name]

| # | Filename (Current) | Filename (Standard) | Caption | Status |
|---|---|---|---|---|
| 1 | 01.png | Figure01_kmap_gray_code.png | Figure 1. ... | ✅ Renamed |
| 2 | 02.png | Figure02_boolean_layer.png | Figure 2. ... | ⬜ Pending |
```

---

## Workflow for Figure Standardization Day

1. **Backup first:** Copy entire `figures/` to `figures/originals/`
2. **Create inventory:** Fill in `figure_inventory.md` with current state
3. **Rename copies:** Apply standard naming to copies (do not delete originals)
4. **Update captions:** Edit paper text to match new standard captions
5. **Verify:** Confirm all in-text figure references resolve correctly
6. **Review question:** Could this figure appear in another paper without looking out of place?

---

## Human-Created Style Standard (연구 프로그램 이미지 통일 원칙)

**원칙:** 이 연구 프로그램의 모든 이미지 파일은 **사람이 생성한 스타일**로 통일한다.

### 정의

"사람이 생성한 스타일"이란, **연구자가 직접** 그리기 도구를 조작하여 만든 그림을 의미한다.  
AI는 그림 생성 과정에 어떤 방식으로도 관여해서는 안 된다.

| 허용 방법 | 설명 |
|---|---|
| 그리기 도구 (PowerPoint, Keynote, Draw.io) | 연구자 직접 제작 |
| 손 그림 스캔 | 연구자 직접 작성 후 디지털화 |
| 그림 편집 소프트웨어 (Inkscape, GIMP 등) | 연구자 직접 조작 |

### 금지 방법 (HARD RULE — 전면 금지)

| ❌ 금지 방법 | 이유 |
|---|---|
| AI 이미지 생성 (DALL-E, Midjourney, Stable Diffusion 등) | 스타일 불일치; 재현성 없음 |
| **AI가 코드(Python, LaTeX 등)를 작성하여 그림을 생성** | **동일한 이유: AI가 최종 이미지 결정에 관여함** |
| 텍스트-to-이미지 모델 | 수치 정확도 보장 불가 |
| AI가 생성한 코드 기반 자동 그림 | 사람이 그린 스타일과 불일치 |

> **핵심 원칙:**  
> 최종 이미지의 픽셀을 **연구자**가 직접 결정해야 한다.  
> AI가 코드를 작성하고 그 코드가 그림을 출력하는 것도 **금지** — 스타일 통일이 목적이기 때문.  
>
> **AI의 허용 역할:** 그림 *설명 작성*, *배치 위치 표시*, *명세서 작성*에 한함.  
> **AI의 금지 역할:** 그림을 직접 만들거나, 그림 생성 코드를 작성하는 것.

### AI 협업 워크플로: 명세서 기반 방식 (2026-06-05 채택)

그림이 필요할 때 AI는 다음 두 가지 방식으로만 기여한다.

#### 방식 1 — 본문에 `[간단한 설명]` 플레이스홀더 삽입

논문/문서 본문 작성 시 이미지가 들어갈 자리에 다음 형식으로 표기한다:

```
[그림: 4변수 카르노맵 AB/CD 배열의 XOR 체커보드 패턴]
[그림: NAND 게이트만을 사용한 XOR 회로도]
[그림: 변수 재배열 AB/CD → AC/BD 패턴 변환 비교]
```

**규칙:**
- 대괄호 `[` `]` 사용 (꺾쇠 아님)
- "그림:" 접두사 포함
- 내용이 무엇인지 연구자가 바로 파악할 수 있을 정도로 명확하게 기술
- 플레이스홀더는 나중에 연구자가 삭제하고 실제 `![그림 N](images/...)` Markdown 이미지 링크로 교체

#### 방식 2 — 그림 명세서 작성

연구자가 그림을 직접 제작할 수 있도록 별도 명세서를 작성한다.  
명세서에 포함할 내용:

| 항목 | 설명 | 예시 |
|---|---|---|
| 그림 번호 | 논문 내 순서 | Figure 08 |
| 표준 파일명 | 명명 규칙 준수 | `Figure08_xor_checker_ABCD.png` |
| 그림 제목 | 논문 캡션용 | XOR Checkerboard Pattern (AB/CD) |
| 격자 구조 | 행/열 레이블, 셀 수 | 4×4, 행: AB (00/01/11/10), 열: CD (00/01/11/10) |
| 셀 값 | 각 셀의 0/1 값 | (0,0)=0, (0,1)=1, (0,2)=0, ... |
| 색상 | 0=흰색, 1=검정 (표준 준수) | #FFFFFF / #000000 |
| 강조 표시 | 그룹 박스, 화살표 등 | 없음 / 파란 테두리 그룹 박스 |
| 캡션 | 표준 형식 1문장 | Figure 8. XOR checkerboard pattern... |
| 저장 경로 | 리포지토리 내 경로 | `figures/Figure08_xor_checker_ABCD.png` |
| 본문 참조 위치 | 어느 절에서 참조하는지 | 5.7.1절 "XOR 체커보드 패턴 분석" |

### 스타일 기준점 (Style Baseline)

신규 그림은 아래 기존 그림들의 시각 스타일을 기준으로 삼는다:

- **Paper 1 기준:** `images/ABCDXOR.png`, `images/ABCDXNOR.png` (격자 스타일, 폰트, 여백)
- **Paper 2 기준:** `images/01.png` ~ `images/13.png` (셀 크기, 색상, 레이블 방식)
- **Paper 3 신규 그림:** 위 두 기준점과 시각적으로 구별 불가능한 수준을 목표

### 검증 질문 (생성 전 확인)

> Paper 2의 기존 그림(01.png~13.png) 옆에 놓았을 때, 같은 연구자가 만든 것처럼 보이는가?

이 질문에 "예"가 아닌 경우 해당 그림은 재작성이 필요하다.

---

## Prohibited

- ❌ Different cell color conventions within the same program
- ❌ Inconsistent fonts across figures in the same paper
- ❌ Renaming originals without backup
- ❌ **AI 이미지 생성 도구(DALL-E, Midjourney, SD 등)로 만든 그림** — 절대 금지
- ❌ Missing captions on any figure
- ❌ Caption-less figures committed to repository

---

*Last Updated: 2026-06-05 (Rev. 2.1 — Spec-Based Workflow & `[간단한 설명]` Placeholder 추가)*  
*Cross-reference: Expand_Summer2026_ResearchMaintenancePlan.md Phase 2*
*Trigger: 이미지 생성 스타일 통일 지침 (2026-06-05 결정)*
