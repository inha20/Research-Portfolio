# Concept Genealogy

**Last Updated:** 2026-06-06
**Purpose:** Record the evolutionary history of concepts developed throughout the research program.
The goal is not merely to define concepts, but to document how one concept generated another.

> **Rule:** This genealogy must be preserved verbatim. The sequence of development is itself a research finding.
> Do not summarize, flatten, or reorder the lineages.

---

## Introduction

Concepts in this research program are not stable definitions imposed from outside. They are tools that emerged through observation, proved useful for a while, and then generated new tools that made new observations possible.

This document records that generative history. Each lineage is a chain of concepts where each step *enabled* the next.

---

# Primary Lineage: Boolean Structure → Research Theory

## Step 1: Pattern

*First appearance: Karnaugh map observations (Paper 1)*

Patterns are the starting points of observation. They are not yet structures — they are repeated, symmetric, or anomalous features that catch attention before being understood.

Examples in this program:
- Checkerboard patterns in XOR/XNOR K-maps
- Ring and corner forms in symmetric function K-maps
- Preservation of certain properties under variable rearrangement

At this stage, the researcher does not yet know *why* the pattern appears. The pattern is a datum — a signal that something may be worth investigating.

↓ *What happened: Pattern prompted the question "why?"*

---

## Step 2: Layer Structure

*First appearance: Paper 2 (Symmetric Boolean Functions)*

The concept of Hamming Weight Layer (L₀, L₁, ..., Lₙ) explained why symmetric functions produce specific visual patterns. Functions that select odd layers produce checkerboard patterns; functions that select specific single layers produce ring/corner/point patterns.

Layer Structure was not derived mathematically before the pattern was noticed. The pattern was seen first; the layer structure was discovered as the explanation.

**New observation that Layer Structure enabled:**
- "What does it mean for a function to 'select' certain layers?"
- "Are there other functions that select layers in interesting combinations?"
- "Does the same layer structure appear across different representation arrangements?"

↓ *What happened: Layer Structure generated the question about invariance*

---

## Step 3: Equivalence

*First appearance: Variable rearrangement observations (Paper 3)*

Under variable rearrangement, the same Boolean function can look visually different on a Karnaugh map. But certain functions that looked different turned out to produce the same *type* of pattern under the right arrangement. This generated the concept of equivalence — two visual presentations are equivalent if they represent the same logical structure.

Equivalence shifted attention from specific patterns to the *class* of patterns that share an underlying structure.

↓ *What happened: Equivalence generated the question "what makes things equivalent?"*

---

## Step 4: Structural Invariance

*First appearance: Core research question of Paper 3*

If equivalence classes exist, there must be something that is *preserved* across equivalent arrangements. That preserved something is structural invariance.

Structural invariance is what survives transformation. The 1-cell count survives rearrangement. The XOR structure survives variable permutation. Invariance is what cannot be removed by a surface-level representation change.

**This concept changed the research question:**
- Before: "How do patterns change under rearrangement?"
- After: "What is preserved under rearrangement?"

The focus shifted from change to invariance.

↓ *What happened: Structural Invariance generated a meta-question about structure itself*

---

## Step 5: Structure Recognition Theory

*First appearance: Paper 4 framework development (2025-2026)*

After three papers about Boolean structures, a new kind of question emerged:
- Not "what is the structure?"
- But: "why did humans find these structures interesting?"
- And: "how do structures become research questions?"

Structure Recognition Theory is the concept that *the recognition of structure is itself worth studying*. This required seeing the research program not just as a source of Boolean function results, but as a case study in how humans generate research.

**New observations this concept enabled:**
- H1–H7 hypotheses about research generation
- The connection between representation, attention, and research worthiness
- The distinction between pattern, structure, and explanatory significance

↓ *What happened: SRT generated the question about the collaboration process itself*

---

## Step 6: Human-AI Collaboration Model

*First appearance: Paper 5 (HARCT) — 2026*

Developing Papers 1–4 required collaboration between a human researcher and multiple AI systems. This collaboration process became visible as an object of study when Paper 5 asked:

> "What made this research program sustainable over time despite memory limitations, AI transitions, and context loss?"

The answer: not intelligence alone, but research continuity — the ability to preserve, restore, and transfer research context across time.

**New concepts generated by Human-AI Collaboration Model:**
- Goal Preservation Theory (goals > information)
- Reconstruction Cost Theory (documentation = economic variable)
- Future-Self Collaboration (temporal collaboration with a future version of the researcher)
- Externalized Memory (context preserved outside active participants)

↓ *What happened: The collaboration model itself required a concept for how collaboration sustains concept evolution*

---

## Step 7: Concept-as-Lens (Emerging — 2026)

*First appearance: SRT v0.2 (H8, candidate hypothesis), CoreQuestions.md v2.0 Level 6*

> **Status:** Candidate hypothesis (H8). Not yet confirmed. Recorded here as an emerging conceptual direction.

After documenting the six steps above, a meta-level observation became available:

Each step in this lineage was not merely a discovery. Each concept *changed what could be observed next.* "Hamming Weight Layer" made the invariance question askable. "Structural Invariance" made the SRT question askable. "Structure Recognition Theory" made the HARCT question askable.

The concept of Concept-as-Lens — the idea that concepts function as observation lenses — makes this pattern itself visible and potentially deliberate.

**What the lineage reveals about the lens mechanism:**

Looking back over Steps 1–6, each concept transition followed the same three-stage pattern:

1. *Observation without concept:* Phenomena existed but could not be precisely named or investigated (checkerboard was visible; layer structure was not yet thinkable).
2. *Concept emergence:* Through investigation, a new concept crystallized (Hamming Weight Layer).
3. *Expanded perception:* With the concept available, phenomena previously invisible became observable (invariance across arrangements was now an askable question).

If this pattern holds, then the genealogy above is not merely a history of discoveries. It is a history of how each concept *created the conditions* for the next discovery.

**Why this matters for the research program:**

The program-level question — "How do humans come to see something new?" — cannot be fully answered without the Concept-as-Lens concept itself. Seeing something new often means first acquiring a concept that makes the new thing seeable.

This is why Level 6–8 of CoreQuestions.md ask not "what is observed?" but "what determines what *can* be observed?":
- Level 6: What makes a concept effective as an observation lens?
- Level 7: How does concept acquisition change what is observable?
- Level 8: How does the concept evolution cycle generate new discovery cycles?

**Connection to formal definitions (SRT v0.3):**

The Concept-as-Lens hypothesis is directly related to the formal definition of *structure* under development in SRT v0.3: structure is defined in part as a configuration that is *recognized holistically* — and what can be recognized holistically depends on what concepts the observer has available. The formal definition of *explanatory significance* similarly depends on the observer's conceptual repertoire: a structure can only be detected as having explanatory significance if the observer has concepts that make the structure's non-randomness visible.

**New question this concept enables:**
- "Can concept evolution be used deliberately rather than only recognized in retrospect?"
- "What makes a concept generative?" (H10)
- "How do humans come to see something new?" (program-level question)

**Significance for the program:**
The program-level question "How do humans come to see something new?" requires the Concept-as-Lens concept to be fully askable — because seeing something new often requires a new concept first.

↓ *What may come next: SRT v0.3 formal definitions / AI Collaboration Education / Structure-Based Mathematics*

---

## Secondary Lineages

---

# Lineage: Difference → Attention → Meaning

## Difference

Certain features stand out against a background. They are not randomly distributed — they form patterns of symmetry, contrast, repetition, or anomaly.

Examples:
- The checkerboard stands out from all-zero or random Boolean functions
- Ring patterns stand out as globally regular
- Invariance stands out because *most* properties do not survive rearrangement

↓

## Attention

Differences attract attention. Not uniformly — some differences attract intense investigation, most are ignored.

Hypothesis (H3): A prior selection process governs which differences receive investigative attention.

↓

## Meaning

Attended differences become meaningful when they are perceived as non-random — as if "there must be a reason for this."

Meaning is not computation. Meaning is the judgment that a pattern *demands* an explanation.

---

# Lineage: Structure Discovery → Research Question Generation

## Structure Discovery

Structures are discovered — not computed. In all three case studies (Papers 1–3), the structure was perceived before it was analyzed.

Key feature: Structure discovery is holistic. The whole pattern is recognized before the parts are computed.

↓

## Research Worthiness

Not every discovered structure generates a research question. A significance filter operates between structure discovery and research question generation.

Candidate criteria: compression, prediction, generalization, explanation pull.

↓

## Research Question Generation

Research questions emerge when a structure is perceived as having explanatory potential — when the researcher feels "this structure should have a deeper explanation."

The question is not "what is this pattern?" but "why does this structure exist?"

---

# Lineage: Research → Concept → Expanded Perception

## Research

Research generates concepts as its output — not just facts.

↓

## Concept

Concepts are not merely labels for existing observations. They function as lenses (H8) that make new observations possible.

Examples:
- "Hamming Weight Layer" as concept → made symmetric function patterns legible
- "Structural invariance" as concept → made the question "what is preserved?" formulable
- "Explanatory significance" as concept → made the distinction between noticing and researching visible
- "Concept-as-Lens" as concept → made the question "how do humans come to see something new?" fully formulable

↓

## Expanded Perception

A concept expands what can be observed. After "Hamming Weight Layer" was available as a concept, researchers could see things in symmetric functions that were previously invisible.

↓

## New Observations

Expanded perception generates new observations — phenomena that could not have been noticed before the concept existed.

↓

*The cycle repeats.*

---

# Lineage: Memory → Externalized Memory → Context Transfer

*This lineage emerged from Paper 5 (HARCT)*

## Memory (Biological and AI)

Both human memory and AI context windows are finite and fragile. Human researchers forget details; AI systems lose context at session boundaries.

↓

## Externalized Memory

Research context can be moved *outside* both human memory and AI context windows — into repositories, documents, handover files, reminder systems.

Externalized Memory is not merely storage. It is memory designed for recoverability.

↓

## Context Transfer

Stored context must be transferred across time, participants, and AI systems. The goal is not preservation alone but *successful restoration*.

Context Transfer is the mechanism by which externalized memory becomes useful.

↓

## Research Continuity

When goal preservation, externalized memory, and context transfer operate together, research continuity emerges — the ability to sustain a research program despite memory limitations, AI transitions, and interruptions.

---

# Concept Map: Current Program

```
Pattern (observation)
  ↓
Layer Structure (first explanation)
  ↓
Equivalence (same structure, different representations)
  ↓
Structural Invariance (what is preserved?)
  ↓
Structure Recognition Theory (why do humans see structure?)
  ↓
Human-AI Collaboration Model (how does collaboration sustain research?)
  ↓
Concept-as-Lens [candidate] (how do concepts change what can be observed?)
  ↓
[Program-level question: "How do humans come to see something new?"]
[Future: AI Collaboration Education]
[Future: Structure-Based Mathematics]
```

*Parallel thread:*
```
Memory → Externalized Memory → Context Transfer → Research Continuity (HARCT)
```

---

# AI Collaboration and Agency Branch (2026)

*Exploratory — documents an emerging parallel thread in the research program history*

This branch traces a distinct lineage: not the conceptual development of the research questions, but the technological development of the *collaborators* through which the research was conducted.

```
Physical AI (early robotics / automation)
  ↓
OpenClaw (Claude-native interaction paradigm)
  ↓
GitHub Collaboration (repository-mediated AI workspace)
  ↓
Content Generation (AI as co-author, not just assistant)
  ↓
File/Output Management (AI managing the research artifact layer)
  ↓
Edit/Observation Cycle (iterative human–AI refinement of research objects)
  ↓
Second AI Industrial Revolution [emerging concept]
```

This branch represents an empirical observation that runs in parallel to the primary lineage: as AI became capable of acting in the digital world (not merely conversing), the nature of Human-AI collaboration research changed qualitatively.

Paper 5 studied one slice of this — long-term textual research collaboration. But the broader territory visible from this branch is:
- AI as agent in file systems, repositories, and research workflows
- The question of what "research collaboration" means when one collaborator has no persistent memory
- The documentation burden created by AI context boundaries, and how it reshapes what research can be sustained

**Connection to primary lineage:**
This branch converges with Step 6 (Human-AI Collaboration Model) of the primary lineage. Where Step 6 asks *what kind of cognitive division of labor sustains research*, this branch asks *what kind of infrastructure does it require*.

**Open:** The relationship between this branch and the primary lineage is not yet formally theorized. It is recorded here because the research program itself was made possible by this technological evolution, and future papers may need to make this explicit.

---

*Preserved verbatim per MasterHandoverDocument.md — this sequence is itself a research finding.*
*Updated: 2026-06-06*
*Cross-reference: ResearchTimeline.md, ResearchProgramMap.md, 4SRT/theory/ConceptEvolution.md*
