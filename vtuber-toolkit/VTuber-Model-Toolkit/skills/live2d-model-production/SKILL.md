---
name: live2d-model-production
description: Create, repair, rig, validate and package a Live2D VTuber model from supplied artwork or a layered project, including hair, expressions and accessories.
---
# Live2D model production

Read `references/rigging-tools.md`, `references/accessories.md`, and `references/validation.md`. Inventory the reference artwork, approved design, existing editable project, runtime and target features. Preserve originals and work in versioned copies. Establish the neutral image and desired range of motion before designing the rig.

1. Separate face, eyes, eyelids, brows, mouth, jaw, hair groups, body, clothing and accessories according to intended motion and occlusion. Preserve original visible pixels where possible; paint hidden coverage under moving overlaps. Keep coordinates, transforms, canvas dimensions and layer ordering. Reassemble and compare to reference before rigging.
2. Set parents and meshes deliberately: face features follow the face, head follows body, and hair locks have anchored roots and independently deformable tips. Do not assign clothing pixels to hair. Record intended motion ownership and pivot locations. Examine alpha on light and dark backgrounds and inspect exposed opaque gaps as well as transparency.
3. Rig and test one parameter at a time: independent blinks, eye direction, mouth form and open, head and body rotation, breathing and requested gestures. Check midpoints and combinations as well as extrema; avoid deformation that loses the approved likeness. Physics drives authored shapes; tune sway, damping and settling after static poses work. Keep physics outputs under the solver.
4. Add requested props and outfit toggles using the accessory reference. Check every relevant pose and outfit, including visibility, draw order, framing and independent controls.
5. Export actual runtime resources and retain editable sources. Follow validation guidance; distinguish Core load, visual review, editor reopening and actual VTube Studio playback. Record which checks were performed and any limitations.

A single flattened illustration cannot automatically supply hidden artwork or a finished professional rig. A project file, runtime MOC, JSON parse, and visual acceptance are distinct deliverables. Verify all referenced files, atlas versions, physics, motions and expressions match the exported model.

## Default scope and feedback

If no broader scope is requested, make a starter talking-head model with a neutral face, basic blink, microphone-driven mouth opening and modest head movement when the artwork and runtime permit. Explain which features actually work and which need target-app testing. Ask the user what hair motion, physics, accessories, toggles, expressions, outfits or full-body features they want; do not assume these extras are included. Continue independent preparation while awaiting preferences.

Show the user neutral and motion previews and ask for specific visual feedback about seams, exposed gaps, face likeness, hair sway, timing and preferred features. Iterate based on the user's observations; technical checks cannot replace visual acceptance. Do not imply that a model is approved or live-tested without evidence.
