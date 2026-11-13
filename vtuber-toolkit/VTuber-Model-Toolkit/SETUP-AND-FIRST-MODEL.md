# Setup and your first model

## 1. What you need

- A computer that meets [Live2D Cubism Editor's system requirements](https://www.live2d.com/en/cubism/download/spec/), a ChatGPT account with GPT-Image-2.6 image generation, and Codex with **GPT-6.1 Sol at Medium reasoning or better**. These are this toolkit's requested minimums; account access, model availability and limits can vary. [GPT-6.1 Sol documentation](https://developers.openai.com/api/docs/models/gpt-6.1-sol) · [GPT-Image-2.6 documentation](https://developers.openai.com/api/docs/guides/image-generation).
- Character reference artwork you are allowed to use. A layered PSD is helpful but not essential to start; a flattened image needs extra separation and hidden artwork. If generating or editing art, confirm image generation is actually available in your session.
- Storage for a project folder and time to review and revise. For live use, install a compatible target app such as VTube Studio separately.

## 2. Extract and give it to Codex

1. Extract the ZIP to a normal folder you can find again. Do not delete the extracted `docs` or `engine-setup` folders if you want their setup instructions and patch.
2. Open Codex, open a workspace folder for your new model, and select GPT-6.1 Sol with Medium reasoning or better. Start a chat and give Codex the extracted toolkit folder path, for example: “Read the README and install the skills from this toolkit for my account, then use them to help make my model.” Grant filesystem access if Codex requests it. You can also drag or attach the ZIP/folder if your Codex interface supports it; make sure Codex can actually read and extract the files. Merely mentioning a filename does not install the skills.
3. To install manually on Windows, copy each **whole folder inside** the extracted `skills` folder into `%USERPROFILE%\.codex\skills\`. Create the destination if it does not exist. On macOS or Linux use `~/.codex/skills/`. Do not overwrite an existing skill without reviewing it. Each skill folder must contain `SKILL.md` directly; for example `.codex/skills/live2d-model-production/SKILL.md`. The relevant references are bundled inside the skills.
4. Start a fresh Codex session or restart Codex if the skills do not appear, then ask it to use `live2d-model-production`. You can name `live2d-hair-and-seams`, `live2d-accessories`, or `vrm-avatar-production` when relevant. Verify Codex can find them; copying a ZIP itself into the skills directory does not install it. See [OpenAI's skill overview](https://developers.openai.com/plugins/concepts/skills).

## 3. Install Live2D Cubism Editor

1. Open the official [Cubism Editor download page](https://www.live2d.com/en/cubism/download/editor/) and check system requirements and the current license and plan limitations.
2. Accept the terms only if you agree, download the installer for Windows or your Mac architecture, and run it. Follow the installer prompts; launch Cubism Editor and complete any activation or licensing prompts appropriate to your plan.
3. Follow the official [installation and launch guide](https://docs.live2d.com/en/cubism-editor-manual/cubism-editor-activation/) if needed. The Editor, the separately licensed Cubism Core SDK, and VTube Studio are different components; installing one does not automatically configure all the others. Some features or model complexity may require a particular Editor license.
4. If Codex needs the optional Git-based PSD2Live rigging route, ask it to read `docs/rigging-tools.md`. That document explains Git, Python, JDK 21, pinned versions, the bundled patch, and optional MCP tools. Git setup alone does not create a model, install Cubism, or provide the complete original adapter pipeline. No install has been tested on your computer yet.

## 4. Tell Codex what to make

Share your reference image or layered artwork and describe the character and target app. For a first request you can say:

> Use the Live2D model production skill and these references to create a basic talking head for VTube Studio. Keep the design faithful. Start with blinking, microphone mouth opening, and modest head movement. Show me neutral and movement previews so I can point out seams and request changes. Ask me before adding any major features beyond this starter scope.

The default is only a starter talking head. If you want them, explicitly request full body, body tracking, expressions, outfits, props and accessory toggles, hand gestures, physics or other features. Describe your hair: which sections should move, subtle or strong sway, how quickly they respond, and whether you want them to settle. Your artwork and chosen app may limit what is possible.

## 5. Review and improve it together

Look at the neutral model and moving previews at normal size and zoomed in. Tell Codex exactly where you see a seam, gap, stretching, layer crossing, wrong face, or motion you dislike. For example: “The left side of the hair separates at the temple when the head turns; keep the roots still and make the ends sway gently.” Ask for another preview after each meaningful fix. A human must judge whether the artwork, seams, hair animation and overall design look right; the tool cannot reliably infer your taste from a technical pass.

Before accepting delivery, ask what was actually tested: editable project, exported model, blink, mouth, head tracking, physics, toggles and real target-app playback. A web preview or a valid file does not prove live tracking works. Request an editable backup and runtime ZIP, and keep the original artwork. See `docs/validation.md` and `docs/accessories.md` for details.
