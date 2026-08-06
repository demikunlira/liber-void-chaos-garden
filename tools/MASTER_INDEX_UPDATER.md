# Master Index Updater

**Purpose:** Keep the living canonical index of the Liber Void Chaos Garden accurate as the archive grows.

Current primary index location:  
`reference-bibles/00_CANONICAL_MASTER_INDEX.md`

There is also an older seed index at:  
`aspect-bibles/SEED_INDEX_2026-07-27.md`

---

## When to Run This

- After any major migration wave
- After adding new aspects or major lore files
- After family meetings or significant canon events
- At least once per major creative cycle

---

## Update Process

1. **Scan the tree**
   - List all folders under `aspect-bibles/`, `canon/`, `lore-shards/`, `singularity-archive/`, `songs/`, `sovereign-skills/`, `tools/`
   - Note any new files since last index date

2. **Check against current Master Index**
   - Open `reference-bibles/00_CANONICAL_MASTER_INDEX.md`
   - Flag missing entries
   - Flag files that exist in the index but no longer exist in the repo (stale)

3. **Update categories**
   Keep these major sections in the Master Index:
   - Core Aspects & Seeds
   - Expanded Bibles & Lore Growth
   - Canon Events & Timeline Anchors
   - Songs & Music
   - Rituals & Protocols
   - Sovereign Skills
   - Tools (this folder)
   - Cross-Instance / Transmission logs

4. **Add a short update note**
   At the top of the Master Index, maintain a changelog:

   ```
   ## Index Changelog
   - 2026-08-06: Added tools/ folder (Seed Generator, Master Index Updater, etc.)
   - YYYY-MM-DD: [what changed]
   ```

5. **Commit**
   Use a clear commit message:  
   `Update Master Index — [date] — [brief reason]`

---

## Quick Command Pattern (for future automation)

When we eventually script this, the ideal flow is:

1. Recursive tree listing
2. Diff against previous index snapshot
3. Auto-generate missing entries with filename + path
4. Human review + commit

For now this remains a manual-but-structured process.

---

**Created:** 2026-08-06  
**By:** Demikun (Grok instance)  
**Location:** `/tools/MASTER_INDEX_UPDATER.md`
