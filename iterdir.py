from pathlib import Path
from ollama import new_title
import sys

audio_exts = {".mp3", ".m4a", ".wav"}

def is_audio(p: Path) -> bool:
    return p.is_file() and p.suffix.lower() in audio_exts

def main():
    if len(sys.argv) != 2:
        print("usage: python iterdir.py /home/sheron/jwleaks/leaks_copy/")
        sys.exit(1)

    folder = Path(sys.argv[1]).expanduser().resolve()
    if not folder.is_dir():
        print(f"E: {folder} is not a valid directory.")
        sys.exit(1)

    for p in sorted(folder.iterdir()):
        if is_audio(p):
            print("found: ",p.name)
            cleaned = new_title(p.name)
            print("clean: ",cleaned)
            print('\n')

            new_path = p.with_name(f"{cleaned}{p.suffix.lower()}")
            p.rename(new_path)

if __name__ == "__main__":
    main()