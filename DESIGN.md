---
version: alpha
colors:
  background: "#101327"
  foreground: "#eef3e8"
  primary: "#83efd0"
  danger: "#f18c83"
  muted: "#a4adc5"
typography:
  display:
    fontFamily: "Pygame default sans"
    fontSize: "116px"
  body:
    fontFamily: "Pygame default sans"
    fontSize: "30px"
  utility:
    fontFamily: "monospace"
    fontSize: "20px"
omitted:
  - section: rounded
    reason: "Native vector arcade canvas has no rounded controls."
  - section: spacing
    reason: "Fixed 1280 by 720 game coordinates, not a CSS spacing system."
  - section: components
    reason: "Pygame primitives are documented below instead of web components."
---

## Overview

A keyboard-first vector arcade game for desktop players. Keep the original
wireframe geometry, with the visual language of a deep-space navigation display.
The signature is the mint ship against coral rocks in an ink-indigo starfield.
Avoid dashboard cards, mouse-only menus, and visual clutter during play.

## Colors

Runtime constants in `constants.py` are canonical (ownership model B). The palette
above mirrors BACKGROUND, FOREGROUND, ACCENT, DANGER, and MUTED respectively.
`ui.Renderer`, `Player`, `Shot`, and `Asteroid` consume those shared constants.
The starfield and divider use a quiet secondary shade, #364058. Color never
replaces the textual lives, score, state, and control labels.

## Typography

`ui.Renderer` owns the three fonts. Bundled Pygame sans is used for titles and
body copy; a system monospace face, falling back to Pygame default, carries data.
Keep titles short and centered; keep numeric HUD values aligned.

## Layout

The 1280 by 720 playfield remains the course coordinate system. HUD is above the
82px divider; controls occupy the bottom 38px. Title, pause, and game-over screens
share centered title/detail/action geometry, owned by one renderer. Fullscreen
uses the same logical resolution. Mobile and screen-reader gameplay are not
supported by this native canvas implementation.

## Elevation & Depth

Flat vector outlines. A translucent overlay dims the playfield during menus.
No blur or shadows obscure moving objects.

## Shapes

Preserve the triangular ship, circular collision model, and outlined rocks.
The protection ring communicates temporary invulnerability.

## Components

Canonical owners: Game handles title/playing/paused/game_over transitions,
Renderer owns overlays and HUD, Player owns movement/shooting, and the sprite
classes own object drawing. Enter starts or restarts; P or Enter toggles pause;
Escape exits in every state. Focus loss pauses play without losing progress.
Three lives and two seconds of protection provide recoverable collisions.
Best-score persistence failures show text on menus and preserve the in-memory
best; a later save retries. Reduced motion removes particles and blinking while
keeping the steady protection ring. No forms, async requests, or web primitives
are applicable to this game.

## Do's and Don'ts

Keep all actions keyboard accessible and display controls on every screen.
Keep score and lives readable. Do not add flashing full-screen effects.
Keep menu layout stable and gameplay particle counts bounded.
