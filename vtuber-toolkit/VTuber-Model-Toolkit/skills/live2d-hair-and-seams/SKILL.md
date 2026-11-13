---
name: live2d-hair-and-seams
description: Separate and rig Live2D hair, repair exposed seams, and review motion with human feedback.
---
# Live2D hair and seams

Ask the user what hair motion they want: subtle or pronounced, independent locks, response speed and settling. Start from the approved character art. Split hair by logical root-to-tip moving volumes; keep front, side and rear sections independent where the design calls for it. Record layer placement, occlusion and movement ownership. Paint sufficient hidden coverage beneath overlapping locks, the scalp and face for relative movement. Preserve intentional partings, highlights and original visible pixels; avoid assigning clothing or face pixels to a hair layer.

Parent shared head motion to the head and independent sway to child deformers. Pin roots, author neutral and controlled sway shapes, then tune physics and damping. Check neutral, intermediate and extreme head/body combinations, repeated motion, reversal and settling. Inspect composited alpha on contrasting backgrounds and look for exposed opaque scalp as well as transparent gaps. Fix missing underpainting, placement, draw order or deformation instead of masking a faulty seam with extra motion.

Show stills and actual motion previews to the user, identify the regions tested and invite feedback about visible seams and the desired look. Iterate until the user accepts the appearance or explicitly report what remains unresolved; parameter movement or a clean automated report alone is not visual acceptance.
