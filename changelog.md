# inotia00/revanced-patches

***Release Version: [v4.14.1](https://github.com/inotia00/revanced-patches/releases/tag/v4.14.1)***  
***Release Date: September 28, 2024, 15:28:48 UTC***  
<details>
<summary><b><i>Changelog:</i></b></summary>

YouTube
==
- chore(YouTube): no longer checks `PlayerType` or `VideoInformation` to determine if it is Shorts or not
- chore(YouTube): remove outated patches
- chore(YouTube): replace with a fingerprint that supports a wider range of versions
- chore(YouTube/Change start page): hook a more appropriate Intent
- chore(YouTube/Hide ads): clean up duplicate or unused filters
- feat(YouTube): add `Hide shortcuts` patch https://github.com/ReVanced/revanced-patches/pull/3699
- feat(YouTube): add `Hook YouTube Music actions` patch
- feat(YouTube): rename `Visual preferences icons` to `Visual preferences icons for YouTube`
- feat(YouTube/Change start page): add `Change start page type` setting https://github.com/inotia00/ReVanced_Extended/issues/2395#issuecomment-2368848355
- feat(YouTube/Custom branding icon): add patch option `YouTube (Minimal header)` https://github.com/inotia00/revanced-patches/pull/83
- feat(YouTube/Hide feed components): add `Hide UPCOMING video` setting
- feat(YouTube/Hide feed components): add `Hide expandable shelves` setting
- feat(YouTube/Hide feed components): add `Hide related videos` setting
- feat(YouTube/Hide feed components): remove `Duration filter` setting as it no longer works due to server side changes https://github.com/inotia00/ReVanced_Extended/issues/2389
- feat(YouTube/Hide feed components): selectively hide video by views for Home / Subscription / Search
- feat(YouTube/Navigation bar components): add `Hide navigation bar` setting
- feat(YouTube/PlayerTypeHook): add hooking on Shorts state (whether Shorts is open or not)
- feat(YouTube/Shorts Component): add `Disable Like button animation` setting https://github.com/inotia00/ReVanced_Extended/issues/2407#issuecomment-2380597800
- feat(YouTube/Shorts Component): always hide suggested actions if all sub-settings of the suggested actions category are enabled https://github.com/inotia00/ReVanced_Extended/issues/2407
- feat(YouTube/Shorts components): add `Height percentage of empty space` setting
- feat(YouTube/Spoof streaming data): match with ReVanced
- feat(YouTube/Video playback): add `Disable VP9 codec` setting https://github.com/inotia00/ReVanced_Extended/issues/2384
- feat(YouTube/Visual preferences icons for YouTube): add the patch option `ApplyToAll` that do not apply to sub-settings https://github.com/inotia00/ReVanced_Extended/issues/2392
- fix(YouTube/Change start page): change the actual start page instead of redirecting the Url https://github.com/inotia00/ReVanced_Extended/issues/2395
- fix(YouTube/Hide ads): ads are not hidden from feed (A/B tests)
- fix(YouTube/Hide comments components): `Hide Comments by members banner` setting hides Channel guidelines
- fix(YouTube/Hide feed components): `Hide carousel shelf` setting sometimes hides the library shelf
- fix(YouTube/Hide feed components): `Hide expandable chip under videos` setting does not work https://github.com/inotia00/ReVanced_Extended/issues/2376
- fix(YouTube/Hide feed components): `Hide recommended videos` setting does not work https://github.com/inotia00/ReVanced_Extended/issues/2402
- fix(YouTube/Hide feed components): `Hide related videos` setting hides the player flyout component
- fix(YouTube/Hide feed components): new kind of community posts are not hidden
- fix(YouTube/Hide feed components): new kind of survey shelves are not hidden
- fix(YouTube/Hide feed components): slightly reduced the height of the empty space left behind by the `Hide expandable chip under videos` setting
- fix(YouTube/Integrations): skip patches even in versions where fingerprints are still used
- fix(YouTube/Navigation bar components): Library button is not hidden when `Cairo navigation bar` is applied (A/B tests)
- fix(YouTube/Player components): `Disable player popup panels` setting disables the engagement panel in Mix playlists on certain YouTube version
- fix(YouTube/Player components): patch is broken in certain versions
- fix(YouTube/Return YouTube Dislike): show correct value when swiping back to prior Short and disliking https://github.com/ReVanced/revanced-integrations/commit/2eb5e3afebe374a86e9da521d6441402130f0fd0 https://github.com/inotia00/ReVanced_Extended/issues/668
- fix(YouTube/Settings): `Search bar in settings` can't find certain settings https://github.com/inotia00/ReVanced_Extended/issues/2136
- fix(YouTube/Settings): `Swap Create and Notifications button` description cuts off https://github.com/inotia00/ReVanced_Extended/issues/2373
- fix(YouTube/Settings): app crashes due to exception caused by initialization failure
- fix(YouTube/Settings): clarify the description of some settings https://github.com/inotia00/ReVanced_Extended/issues/2393
- fix(YouTube/Settings): some settings are disabled on tablets or tablet layouts https://github.com/inotia00/ReVanced_Extended/issues/2383
- fix(YouTube/Shorts components): `Hide Save sound button` setting does not work https://github.com/inotia00/ReVanced_Extended/issues/2397
- fix(YouTube/Shorts components): even if `Hide navigation bar` is turned on, the navigation bar will reappear when the user opens the comments or description panel in Shorts
- fix(YouTube/SponsorBlock): add summary text to 'view my segments' button https://github.com/ReVanced/revanced-patches/commit/df80b9f92f0d981b9a40b7756d74f8ccc3dcb1e9
- fix(YouTube/Spoof streaming data): reduce response timeout and cache size
- fix(YouTube/Theme): revert `reverts background color of More comments icon in live chats` https://github.com/inotia00/ReVanced_Extended/issues/2197#issuecomment-2351306813
- feat(YouTube/Translations): update translation


YouTube Music
==
- feat(YouTube Music): add `Visual preferences icons for YouTube Music` patch https://github.com/inotia00/ReVanced_Extended/issues/2216
- feat(YouTube Music): add support version `6.20.51` (Android 5.0+) https://github.com/inotia00/revanced-patches/pull/81
- feat(YouTube Music): changes to supported versions - changed `6.29.58` to `6.29.59`, changed `7.16.52` to `7.16.53`, removed `6.33.52` (as it is almost the same as `6.29.59`)
- feat(YouTube Music): drop support version `7.17.51` https://github.com/inotia00/ReVanced_Extended/issues/2382
- feat(YouTube Music): replace with a fingerprint that supports a wider range of versions
- feat(YouTube Music/Custom branding icon): update monochrome icon for `afn_red` & `afn_blue` https://github.com/inotia00/revanced-patches/pull/82
- feat(YouTube Music/Settings): add `Open default app settings` setting https://github.com/inotia00/ReVanced_Extended/issues/1861
- fix(YouTube Music/Disable Cairo splash animation): some versions are recognized as unpatchable even though they can be patched
- fix(YouTube Music/Disable auto captions): captions cannot be changed when `Disable forced auto captions` is turned on
- fix(YouTube Music/Flyout menu components): `Hide 3-column component` setting does not work
- fix(YouTube Music/Flyout menu components): unable to patch due to incorrect format
- fix(YouTube Music/GmsCore support): can't share the stories to Facebook, Instagram and Snapchat https://github.com/inotia00/ReVanced_Extended/issues/1830
- fix(YouTube Music/Player components): crash at first launch on old clients https://github.com/inotia00/ReVanced_Extended/issues/2377
- fix(YouTube Music/SponsorBlock): SponsorBlock does not skip segment at the beginning when in background https://github.com/inotia00/ReVanced_Extended/issues/2396
- fix(YouTube Music/SponsorBlock): SponsorBlock skips entire song when in background https://github.com/inotia00/ReVanced_Extended/issues/2379
- feat(YouTube Music/Translations): update translation


Shared
==
- build: bump dependencies
- chore(LithoFilterPatch): add compatibility with older versions of AGP
- chore(Settings): separate `Reset to default` part from toasts https://github.com/inotia00/ReVanced_Extended/issues/1839
- chore: remove obsolete code
- feat(Hide ads): remove `Close fullscreen ads` setting https://github.com/inotia00/ReVanced_Extended/issues/2017#issuecomment-2351327068


Announcement
==
- **There is a change in `options.json`. If you see warnings related to patch options, remove the `options.json` file or `Patch options`.**
- YouTube Music's support version has been rolled back to **7.16.53** for the following reasons: https://github.com/inotia00/ReVanced_Extended/issues/2382
- Reddit 2024.18.0+ can only be patched via [CLI](https://github.com/inotia00/revanced-documentation/blob/main/docs/latest-reddit-patch-info.md) or rvx-builder.
- Compatible ReVanced Manager: [RVX Manager v1.22.2 (fork)](https://github.com/inotia00/revanced-manager/releases/tag/v1.22.2).


Contribute to translation
==
- [YouTube](https://crowdin.com/project/revancedextended)
- [YT Music](https://crowdin.com/project/revancedmusicextended)</details>

# ReVanced/revanced-patches

***Release Version: [v4.16.0](https://github.com/ReVanced/revanced-patches/releases/tag/v4.16.0)***  
***Release Date: September 30, 2024, 19:16:41 UTC***  
<details>
<summary><b><i>Changelog:</i></b></summary>

# [4.16.0](https://github.com/ReVanced/revanced-patches/compare/v4.15.0...v4.16.0) (2024-09-30)


### Bug Fixes

* **Soundcloud:** Support latest versions ([#3702](https://github.com/ReVanced/revanced-patches/issues/3702)) ([099ac5e](https://github.com/ReVanced/revanced-patches/commit/099ac5ea2cf55633a7c6a7e6f8e963599bcd5784))
* **Twitter - Open links with app chooser:** Fix incorrect version in compatibility list ([#3683](https://github.com/ReVanced/revanced-patches/issues/3683)) ([adafe85](https://github.com/ReVanced/revanced-patches/commit/adafe85d77f6a0031a5523b9b7da69475959d78d))
* **YouTube - SponsorBlock:** Fade out SB buttons without overlapping other buttons ([#3719](https://github.com/ReVanced/revanced-patches/issues/3719)) ([bf96108](https://github.com/ReVanced/revanced-patches/commit/bf9610894f0a9f9e751e2eed5b825c5d327a722c))
* **YouTube:** Show video chapter titles without clipping when overlay buttons are enabled ([#3674](https://github.com/ReVanced/revanced-patches/issues/3674)) ([4b88c31](https://github.com/ReVanced/revanced-patches/commit/4b88c316ed90c56e83e2aee266561833b36fc37d))


### Features

* **Google Photos:** Restore hidden 'Back up while charging' toggle ([#3678](https://github.com/ReVanced/revanced-patches/issues/3678)) ([f9e19ce](https://github.com/ReVanced/revanced-patches/commit/f9e19ce6e9185fdf31b2b0d5f2934f6e8a544b8e))
* **YouTube - Disable precise seeking gesture:** Hide "pull up" label that shows up when swiping ([#3668](https://github.com/ReVanced/revanced-patches/issues/3668)) ([3fa8af9](https://github.com/ReVanced/revanced-patches/commit/3fa8af9fe534b59ad093c36f1927f56f549a330d))
* **YouTube - Hide Shorts components:** Add `Hide save music`, `Hide stickers` ([#3710](https://github.com/ReVanced/revanced-patches/issues/3710)) ([8c99321](https://github.com/ReVanced/revanced-patches/commit/8c99321df4db696156330fc90dd547c1345d880e))
* **YouTube - Hide Shorts components:** Add patch option to hide Shorts app shortcut (long press app icon) ([#3699](https://github.com/ReVanced/revanced-patches/issues/3699)) ([0d4e1f5](https://github.com/ReVanced/revanced-patches/commit/0d4e1f5d03cf3dcc06fd41165e26a1ce901b976b))
* **YouTube - Hide Shorts components:** Add patch option to hide Shorts from app launcher widget ([#3707](https://github.com/ReVanced/revanced-patches/issues/3707)) ([838f183](https://github.com/ReVanced/revanced-patches/commit/838f1834a5df547ce2c3217b874c0594b6878a67))



</details>

