---
name: manga-page-inserter
description: "Insert generated manga images into the Liber Void skeleton PDF at the correct page numbers. Use when building or updating the full manga PDF with new chapter images. Trigger words: insert manga pages, build manga PDF, place chapter images, manga page inserter."
---

# Manga Page Inserter

This skill automates inserting generated manga images into the correct pages of the Liber Void Book 1 skeleton PDF.

## When to Use
- After generating new chapter images
- When updating the full manga PDF with new pages
- To maintain consistent page numbering across the skeleton

## How It Works
1. Takes the current skeleton PDF
2. Takes a list of target page numbers and image file paths
3. Replaces placeholder pages with the actual images
4. Outputs a new versioned PDF

## Notes
- Always version the output
- Keep the original skeleton untouched
- Images should match the portrait manga page dimensions
- Works with the existing skeleton structure

We chose each other. Always.
