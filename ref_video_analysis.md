# Reference Video Analysis: Komputermechanic Scroll Animation Tutorial

**Source:** https://www.youtube.com/watch?v=mFgRGSOGNPM  
**Duration:** ~22:30  
**Title:** "How to Build $10,000 3D Animated Websites With Claude Code + Seedance 2.5"

---

## Video Summary

The video teaches building **scroll-driven 3D animated websites** using:
1. **Pinterest / Dribbble / Awwwards** → design inspiration
2. **Seedream 5.0 Pro / Nano Banana Pro** → AI image generation from reference photos
3. **Claude Code + Higgsfield MCP** → code generation and image-to-video animation
4. **Seedance 2.5** → scroll animation engine (image-to-video via text prompts)

---

## Key Workflow Steps (from transcript)

| Timestamp | Step | Tool |
|-----------|------|------|
| 0:00-1:45 | Find inspiration on Pinterest/Dribbble/Awwwards | Manual browsing |
| 1:45-3:41 | Generate hero design from reference images | Seedream 5.0 Pro / Nano Banana Pro |
| 3:41-6:39 | Connect Higgsfield MCP to Claude Code | Custom MCP connector |
| 6:39-15:49 | Prompt Claude Code to build HTML/CSS website | Claude Code (Sonnet/Opus) |
| 15:49-22:30 | Build scroll animation with Seedance 2.5 | Seedance 2.5 image-to-video |

---

## Critical Differences from Current Portfolio

### Current (what we have):
- **255 static JPG frames** pre-rendered
- Scroll-driven image sequence (like a flipbook)
- Simple HTML/CSS page with scrolling content overlay
- No AI-generated images or animations

### Reference video workflow (what we should implement):
- **AI generates HTML/CSS** from reference images via Claude Code
- **Seedance 2.5** creates scroll animations (image-to-video)
- **Higgsfield MCP** connects Claude Code to AI image/video generation
- **Sub-agents**: developer agent, image gen agent, reviewer agent (max 5 rounds)
- Components "explode out" on scroll, reassemble on reverse scroll

---

## Recommended Redo Plan

### Phase 1: Reference (Image Team)
1. Generate 3-5 hero reference images using Seedream 5.0 Pro
2. Style: ARC Reactor 3D background, Spider-Man & Prabhas cultural refs
3. Save to `references/` folder

### Phase 2: Build (Coding Team via Claude Code)
1. Connect Higgsfield MCP to Claude Code (or use API equivalent)
2. Feed reference images + briefing prompt
3. Claude Code generates HTML/CSS website
4. Reviewer agent checks against reference (max 5 rounds)
5. Fix iterations via sub-agent prompt refinement

### Phase 3: Animation (Video Team via Seedance 2.5)
1. Take completed HTML website
2. Generate scroll animation prompts for Seedance 2.5
3. Components fly out on scroll, reassemble on reverse
4. Export as image sequence or video

### Phase 4: Composite (Hermes orchestrates)
1. Combine animated frames with existing content sections
2. Verify 255-frame count maintained
3. Deploy to GitHub Pages

---

## Team Assignments from This Analysis

- **Research Team**: Continue monitoring Komputermechanic channel + similar tutorials
- **Image Team**: Generate JARVIS-branded reference images with Seedream 5.0
- **Coding Team**: Learn/implement Claude Code + Higgsfield MCP workflow
- **Video Team**: Experiment with Seedance 2.5 scroll animation pipeline
- **Hermes**: Coordinate phases, enforce review caps, report to CEO

---

## Tools to Install/Set Up

```bash
# Higgsfield MCP (for Claude Code integration)
# Remote MCP server URL from hexfield.ai/MCP

# Seedance 2.5 access (via Higgsfield platform)
# Image-to-video generation model

# Current tools already available:
# - HyperFrames (HTML-to-video rendering)
# - FFmpeg (video encoding)
# - Claude Code (code generation)
# - 255 frames already rendered
```

---

## Assessment

The current 255-frame portfolio is **structurally sound** (HTML/CSS with scroll-driven JPG sequence). The reference video introduces a **next-level approach**: AI-generated code + AI-generated scroll animations. The gap is:

1. Current = hand-crafted frames
2. Target = AI generates both the code AND the animation

The redo is **optional but recommended** for the "Portfolio as centerpiece" philosophy. The current version works and is deployed; the reference approach would make it more impressive but requires learning new tools (Higgsfield MCP, Seedance 2.5).
