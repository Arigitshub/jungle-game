# Unreal Setup

## Install locations

Keep project and engine payloads off the system drive.

- Epic Games Launcher: `D:\Program Files\Epic Games\`
- Unreal Engine: `D:\Program Files\Epic Games\UE_5.x`
- Jungle Game project: `D:\Jungle game\game\JungleGame`

## Epic steps

1. Sign in to Epic Games Launcher.
2. Open the Unreal Engine section.
3. Install Unreal Engine 5 to a `D:` path.
4. Confirm the engine version before creating the project.

## Project creation target

- Template: Games
- Base: Third Person or First Person, depending on camera decision
- Blueprint for fastest first slice
- Starter Content: optional
- Ray tracing: enable only if hardware supports it well

## First build objective

Create a minimal prototype map with:

- dense jungle terrain blockout
- one waterfall or river landmark
- fog and rain pass
- one stealth or threat trigger
- one ruin reveal location

## Repo workflow

- Keep source assets organized under `assets/`
- Keep the actual Unreal project under `game/JungleGame/`
- Commit config, content, and source
- Do not commit generated caches covered by `.gitignore`
