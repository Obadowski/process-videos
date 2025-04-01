# Process Videos

CLI tool for batch processing narrated videos: extracts audio, applies loudness normalization using `ffmpeg`, and recompresses using H.264 or H.265. Great for presentations, voice-over recordings, and tutorials.

## Installation

```bash
pip install process-videos
```

## Usage

```bash
process-videos --dir ./videos
```

Optional parameters:
- `--codec`: libx264 or libx265
- `--crf`: Compression factor (default: 28)
- `--preset`: Encoder preset (default: veryfast)
- `--audio-bitrate`: e.g. 128k
