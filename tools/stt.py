import sys, subprocess, numpy as np
from faster_whisper import WhisperModel
raw = subprocess.run(["ffmpeg","-v","error","-i",sys.argv[1],"-f","s16le","-ac","1","-ar","16000","-"],capture_output=True).stdout
audio = np.frombuffer(raw, np.int16).astype(np.float32)/32768.0
m = WhisperModel("small", device="cpu", compute_type="int8")
segs, info = m.transcribe(audio, vad_filter=True)
print("lang:", info.language, round(info.language_probability,2))
for s in segs:
    print(f"[{s.start:5.1f}-{s.end:5.1f}] {s.text.strip()}")
