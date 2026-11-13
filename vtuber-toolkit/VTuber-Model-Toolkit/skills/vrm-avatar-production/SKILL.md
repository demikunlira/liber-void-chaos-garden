---
name: vrm-avatar-production
description: Create or edit a VRoid/VRM avatar, fit accessories and garments, preserve rig and expression data, and validate export.
---
# VRM avatar production

Inventory the source VRM, editable project, reference images, target runtime and requested changes. Keep source files untouched and make versioned working copies. Obtain Blender and the VRM add-on separately; verify version compatibility and licensing.

Inspect humanoid mappings, bone names and rest transforms, skinning, inverse bind matrices, morph targets, expression bindings, material extensions, spring bones, colliders and VRM metadata before changes. Record a baseline and compare after export. A generic Blender import/export can change orientation, metadata or unsupported extension data: test the actual export path, and where necessary preserve the original GLB structure and patch only the intended data with validated tools.

For clothing and accessories, preserve intended artwork, weights and material settings. Fit across standing, walking, bending and other requested poses; inspect hidden surfaces and body intersections. Make compatible adjustments to morph targets when editing geometry. Treat physics metadata and actual runtime movement as different checks. For face texture work retain UV registration and test lip-sync expressions; inspect shared neck boundaries and color on both sides of seams.

Deliver versioned VRM, editable source where possible, dependencies, textures, preview renders, checksums, results and known limits. Test in the target runtime when available; Blender renders do not establish live tracking or spring behavior. See `references/validation.md`.
