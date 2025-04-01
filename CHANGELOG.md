# Changelog

## [0.2.2] - 2025-04-01
### Added
- Fallback to `imageio-ffmpeg` when `ffmpeg` is not available in system PATH
- Automatic CLI setup via setuptools entry_points
- Makefile and publish.sh for simplified publishing workflow

### Changed
- All CLI messages and structure translated to English
- Improved error handling and tool suggestions

---

## [0.2.1] - 2025-03-31
### Fixed
- Audio normalization artifacts from previous version

### Changed
- Switched to `ffmpeg loudnorm` filter for better voice quality

---

## [0.2.0] - 2025-03-30
### Added
- Batch video/audio processing tool using `click`
- ffmpeg-based audio normalization
- Video compression with CRF and preset options
