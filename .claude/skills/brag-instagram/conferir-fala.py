# Transcreve cada WAV com o Whisper: imprime o texto para conferir a fala
# gerada e grava ao lado <arquivo>.json com o tempo de cada palavra, no
# formato de transcrição das legendas ([{"id", "text", "start", "end"}]).
# Uso: python conferir-fala.py assets/vo-*.wav
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")

import soundfile as sf
from transformers import pipeline

asr = pipeline("automatic-speech-recognition", "openai/whisper-large-v3-turbo", device="cuda:0")
for arquivo in sys.argv[1:]:
    audio, sr = sf.read(arquivo)
    saida = asr(
        {"raw": audio, "sampling_rate": sr},
        return_timestamps="word",
        generate_kwargs={"language": "pt"},
    )
    palavras = [
        {"id": f"w{i}", "text": c["text"].strip(), "start": round(c["timestamp"][0], 3), "end": round(c["timestamp"][1], 3)}
        for i, c in enumerate(saida["chunks"])
    ]
    Path(arquivo).with_suffix(".json").write_text(json.dumps(palavras, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{arquivo} ({len(audio) / sr:.1f}s): {saida['text'].strip()}")
