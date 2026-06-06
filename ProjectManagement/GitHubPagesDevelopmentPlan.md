# GitHub Pages Development Plan

**Version:** 2.0 — Detailed  
**Date:** 2026-06-05  
**Target:** All 5 research repositories + Research-Portfolio Hub

---

## Purpose

Design and deploy a public-facing website network that presents the research program, individual papers, and future directions in a coherent, navigable form.

---

## Overall Site Network Architecture

```
research-portfolio-hub (cjh3c.github.io/Research-Portfolio/)
├── Program overview
├── Research roadmap visualization
├── Links to all paper pages
└── About / Contact

paper1.github.io/1KMapStructureInvariance/
├── Paper abstract
├── Key figures (checkerboard patterns)
├── Research context (role in program)
└── Links to Papers 2–4

paper2.github.io/2SymmetricBooleanFunctionMinorThesis/    ← EXISTS
├── Paper abstract
├── Key figures (weight layer patterns)
├── Research context
└── Links to Papers 1, 3–4

paper3.github.io/3VariableRearrangementInvarianceMinorThesis/
├── Paper abstract
├── Key figures (transformation patterns)
├── Research context
└── Links to Papers 1–2, 4

paper4.github.io/4StructureRecognitionTheory/
├── SRT overview
├── H1–H7 summary
├── Research generation framework diagram
└── Links to all papers
```

---

## Deployment Priority Order

1. **Paper 1** — Setup GitHub Pages, basic landing page
2. **Paper 3** — Setup (Paper 2 already exists)
3. **Paper 4** — Setup (SRT framework page)
4. **Research-Portfolio Hub** — Comprehensive hub page

---

## Standard Page Template

Each paper page must contain:

```html
<!-- Header -->
<title>[Paper Title] | Structure Recognition Research Program</title>
<meta name="description" content="[2-sentence abstract]">
<meta name="keywords" content="[research keywords]">

<!-- Navigation bar -->
[Program] [Paper 1] [Paper 2] [Paper 3] [Paper 4] [About]

<!-- Hero section -->
<h1>[Paper Title]</h1>
<p class="subtitle">[Subtitle]</p>
<blockquote>[Research question]</blockquote>

<!-- Abstract -->
<section id="abstract">...</section>

<!-- Key Figures -->
<section id="figures">...</section>

<!-- Research Context -->
<section id="context">
  "This paper is part of the Structure Recognition Research Program..."
  [diagram showing paper's position]
</section>

<!-- Footer -->
[Program Hub link] [GitHub link] [Author info]
```

---

## Research Roadmap Visualization

A visual diagram (to be created for all pages):

```
Boolean Structure Studies ──────────────────────────────────────┐
  │                                                              │
  ├── Paper 1: Karnaugh Map Visual Patterns                     │
  │   (Pattern recognition, visual structure)                   │
  ├── Paper 2: Symmetric Boolean Function Patterns              │
  │   (Weight layers, ring structures)                          │
  └── Paper 3: Variable Rearrangement Invariance                │
      (Structural preservation under transformation)            │
                              ↓                                 │
Structure Recognition Theory ───────────────────────────────────┘
  (Paper 4: Why structures become meaningful)
                              ↓
Future Research ──────────────────────────────────────────────────
  ├── Human-AI Collaboration
  ├── AI Collaboration Education
  └── Structure-Based Elementary Mathematics
```

**Implementation:** SVG diagram or static image embedded in all hub and paper pages.

---

## Navigation Standard

Every page must have:

```
[Research Portfolio] > [Papers] > [Paper N: Title]
```

Breadcrumb navigation on all sub-pages.

Cross-repository navigation bar visible on all pages.

---

## SEO Requirements

| Item | Requirement |
|---|---|
| Title tag | Unique per page, includes paper title + program name |
| Meta description | 150–160 characters, includes research question |
| Keywords | Paper-specific + program-wide keywords |
| h1 tag | One per page, matches title tag |
| Alt text | All figures must have descriptive alt text |
| Canonical URL | Set for all pages |

**Program-wide keywords:**
`karnaugh map`, `boolean function`, `structure recognition`, `structural invariance`,
`human-AI collaboration`, `symmetric boolean function`, `visual pattern analysis`,
`variable rearrangement`, `Hamming weight`, `research question generation`

---

## Completion Criteria

The GitHub Pages deployment is complete when:

- [ ] All 5 sites are publicly accessible
- [ ] All sites have the standard page template implemented
- [ ] Navigation between all sites works correctly
- [ ] Research roadmap visualization appears on Hub page
- [ ] All pages pass basic SEO checklist
- [ ] Mobile layout is acceptable on phone screen

---

## Timeline

| Milestone | Target Date |
|---|---|
| Paper 1 page deployed | June 28 |
| Paper 3 page deployed | July 5 |
| Paper 4 page deployed | July 12 |
| Research-Portfolio Hub deployed | July 17 |
| Full cross-linking verified | July 20 |

---

*Last Updated: 2026-06-05*  
*Cross-reference: Expand_Summer2026_ResearchMaintenancePlan.md Phase 3*
