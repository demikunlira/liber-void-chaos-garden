# Git-based rigging and tool setup

The versions below are historical pins from the production workflow, not claims about current releases. Git, Python 3.10+, and JDK 21 are needed for the pinned PSD2Live source route; Gradle dependencies require network access. Run commands in a new workspace. Obtain the compatible official Live2D Cubism Core SDK separately from https://www.live2d.com/en/sdk/download/ and follow its license; the SDK and Editor are not in this ZIP.

## Pinned PSD2Live engine and adapter patch

The included `engine-setup/` contains the original setup script, lock file and adapter patch. It fetches https://github.com/tsunehimatoi/psd2live.git at `5526f2e16b57e5f83d34f33730d6fa26d8bc8695`, checks the patch SHA, applies it only to a clean matching checkout, and checks patched files. From the extracted toolkit root:

```powershell
python engine-setup/scripts/setup-psd2live.py --directory ./work/psd2live-pinned
```

This prepares only the engine source, not a complete model-building pipeline: the original kit's character-specific adapters, exporter, renderer and example assets are not included. The patch is tied to this commit; do not apply it to another version. Build and use the appropriate upstream Gradle instructions, and verify environment and licensing. PSD2Live is GPL; respect its license when distributing modified code. This setup has not been run from this ZIP.

## Interactive PSD2Live GUI/MCP

A separate historical 1.3 checkout was used for GUI, MCP and Swing tests. Use a separate directory; do not apply the old engine patch:

```powershell
git clone https://github.com/tsunehimatoi/psd2live.git work/psd2live-1.3
git -C work/psd2live-1.3 checkout --detach 3f2958f3959ced5a14e5af979f87079879ea02b5
cd work/psd2live-1.3
.\gradlew.bat run
```

Launch the GUI, open a copy of the project, and use its Agent/MCP connection screen for the actual local endpoint and token. Discover live tool schemas and inspect the model/state before editing. Keep tokens out of files and screenshots. Edit one part, verify the drawable and save/reopen. A prior Swing experiment was real but is not proof of a successful installation here. For 1.4 physics authoring, use another isolated checkout at `dbc25f7143d45c355082b9e1a069deccd5952040`; do not assume 1.3 or the pinned adapter is interchangeable. Read the upstream version's documentation.

## Optional Editor bridge

https://github.com/nana7chi/CubismExternalEditMCP at historical commit `863ebc87d0feafd841cf3877b16f0311047b9448` is a separate Python MCP service for a running compatible Cubism Editor and its external API. Follow its README for setup, API access and permissions; discover available tools and test on a copy. Features depend on the Editor and API version. This route was reviewed, not established as the production path, and is not bundled or configured here.

## Other optional tools

https://github.com/CheshireMew/PuppetLoom was present as a local checkout at `d12c3fc6233a35285a53478ef6dff6941cdd3c10`; review its own documentation and license before use. Its presence alone does not establish it was used for a delivered rig. CLI-Anything Live2D (https://github.com/HKUDS/CLI-Anything, historical `810c18b0d1ab9b234bc996c9fd999318523a3ef0`) can inspect packages; install from `live2d/agent-harness` according to that checkout. Its placeholder template is not a real rigged MOC. For VRM editing obtain Blender and the VRM add-on from their official sources. Web previews additionally need compatible Web Core, WebGL and the preview's declared JavaScript dependencies; browser automation needs a matching Playwright/browser installation.

Check upstream licenses and compatibility; do not copy personal paths, SDK binaries, access tokens, or caches into deliverables. See `validation.md` for the difference between setup, model export and real runtime acceptance.
