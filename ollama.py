import os, re, requests

OLLAMA_URL = os.environ.get("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL = os.environ.get("OLLAMA_MODEL", "qwen2.5:3b")

FEW_SHOT = """
You are a filename cleaner. Extract the TRUE song title from a messy filename.
Assume the artist is "Juice WRLD" (and aliases like "JuiceWrld", "Juice World", "Jarad Higgins").
Rules:
- Return ONLY the cleaned title (no artist, no quotes, no commentary).
- Remove the artist name and its aliases if present.
- Ignore junk like: leak, leaked, demo, snippet, v1, v1.1, 320kbps, (Prod. ...), official, audio, video, lyrics.
- Remove file extensions (.mp3, .wav, ...).
- Keep featured artists ONLY if clearly part of the title text itself (e.g., "Hate Me feat. Ellie Goulding").
- Keep normal punctuation like parentheses if it looks like real title info.
- Use normal capitalization for titles.



Examples:
Input:  "01 juice wrld - stick talk v1.1 (.mp3"
Output: "Stick Talk"

Input:  "JuiceWrld_-_Lucid_Dreams_[Official Audio] 320kbps.mp3"
Output: "Lucid Dreams"

Input:  "juice wrld - hate me (feat. ellie goulding) [clean].m4a"
Output: "Hate Me (feat. Ellie Goulding)"

Input:  "JUICE WRLD - righteous (prod. nick mira).flac"
Output: "Righteous"

Now clean this filename and return ONLY the title:
"""

def new_title(filename: str) -> str:
    prompt = FEW_SHOT + f'\nInput: "{filename}"\nOutput: '
    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.2,  # keep it deterministic
            "num_ctx": 1024
        }
    }
    r = requests.post(OLLAMA_URL,json=payload, timeout=60)
    r.raise_for_status()
    text = r.json().get("response", "missing").strip()

    # text = text.splitlines()[0].strip().strip('"').strip("'")
    # text = re.sub(r"\.(mp3|m4a|aac|flac|wav|ogg)$", "", text, flags=re.IGNORECASE)
    # text = re.sub(r"\s{2,}", " ", text).strip()

    return text

if __name__ == "__main__":
    print(new_title("wAGkp_Juice%20WRLD%20-%20Widow%20%28Don%27t%20Go%29.mp3"))