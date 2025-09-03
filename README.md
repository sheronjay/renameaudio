# 🎵 renameaudio

A tiny utility that uses an Ollama language model to turn messy audio filenames into clean titles.

## ✨ Features

- 🧠 AI‑generated titles using your local or remote Ollama server
- 🎶 Supports `.mp3`, `.m4a` and `.wav` files
- 📁 Batch rename entire folders

## 🛠️ Technology Stack

- Python 3.10+
- [requests](https://pypi.org/project/requests/)
- [Ollama](https://ollama.ai) server for running language models (defaults to `qwen2.5:3b`)

## 🚀 Getting Started

Install dependencies:

```bash
pip install requests
```

## ⚙️ Configuration

Optional environment variables:

```bash
export OLLAMA_URL=http://localhost:11434/api/generate
export OLLAMA_MODEL=qwen2.5:3b
```

## 🎚️ Usage

Run the script against a folder of audio files:

```bash
python iterdir.py /path/to/audio/folder
```

The script scans the folder for `.mp3`, `.m4a`, and `.wav` files. For each file, it calls `ollama.new_title` to generate a cleaner title and renames the file.

## 📝 Notes

This tool was built for personal use and may require tweaks for other setups.