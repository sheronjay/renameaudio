# 🎵 renameaudio

A tiny pyhton utility that uses an Ollama language model to turn messy audio filenames into clean titles.

## ✨ Features

- 🧠 AI‑generated titles using your local or remote Ollama server
- 🎶 Supports `.mp3`, `.m4a` and `.wav` files
- 📁 Batch rename entire folders

## 🛠️ Technology Stack

- Python 3.10+
- [requests](https://pypi.org/project/requests/)
- [Ollama](https://ollama.ai) server for running language models (defaults to `qwen2.5:3b`)

## 🚀 Getting Started

Install Ollama:

```bash
yay -S ollama
ollama serve 
```

Pull a model:
Choose a model from the ([Ollama library](https://ollama.com/library)). Example:

```bash
ollama pull qwen2.5:3b 
```

Install dependencies:

```bash
pip install requests
```

## ⚙️ Configuration

Set your preferred model:

```bash
MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5:3b")
```

## 🎚️ Usage

Run the script against a folder of audio files:

```bash
python iterdir.py /path/to/audio/folder
```

The script scans the folder for `.mp3`, `.m4a`, and `.wav` files. For each file, it calls `ollama.new_title` to generate a cleaner title and renames the file.

Example:

![example output](image.png)

## 📝 Notes

- This tool was built for personal use and may need tweaks for your workflow.

- All processing happens locally if you’re running Ollama on your own machine.

- Rename results depend on the model and the prompt — adjust few-shot examples for best results.