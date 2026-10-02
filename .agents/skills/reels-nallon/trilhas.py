# Gera as 5 trilhas ambiente do Nallon (30 s, instrumentais, sem bateria).
# Uso: python trilhas.py <pasta> [segundos=30]  ->  <pasta>/1-pad-atual.wav ... 5-minimal-tech.wav
# Sintetizadas aqui, sem licença de terceiros. Dependência: numpy.
import sys
import wave
import numpy as np

sr = 44100; dur = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
t = np.arange(int(sr * dur)) / sr
out_dir = sys.argv[1]
rng = np.random.default_rng(3)

def hz(m): return 440 * 2 ** ((m - 69) / 12)

def pad(freqs, ini, fim, amp, atk=3.0, rel=3.5, brilho=(1, .35, .12)):
    env = np.clip((t - ini) / atk, 0, 1) * np.clip((fim - t) / rel, 0, 1)
    x = 0
    for f in freqs:
        for det, a in ((0, 1), (.0035, .6), (-.0035, .6)):
            ff = f * (1 + det)
            x = x + a * sum(b * np.sin(2 * np.pi * (k + 1) * ff * t) for k, b in enumerate(brilho))
    return amp * x * env * (1 + .1 * np.sin(2 * np.pi * .12 * t))

def nota_curta(f, ini, amp, decay=.9, harm=(1, .5, .25, .1), trem=0):
    n0 = int(ini * sr); n = min(int(sr * 3), len(t) - n0)
    if n <= 0: return
    tt = np.arange(n) / sr
    env = np.minimum(tt / .005, 1) * np.exp(-tt / decay)
    x = sum(b * np.sin(2 * np.pi * (k + 1) * f * tt) for k, b in enumerate(harm))
    if trem: x *= 1 + .25 * np.sin(2 * np.pi * trem * tt)
    buf[n0:n0 + n] += amp * x * env

def ar(g):
    r = rng.standard_normal(len(t)); r = np.convolve(r, np.ones(400) / 400, 'same')
    return r * g * np.clip(t / 3, 0, 1)

def finaliza(y, nome, eco=((.29, .35), (.53, .25), (.97, .18), (1.6, .12))):
    out = y.copy()
    for d, g in eco:
        k = int(d * sr); out[k:] += g * y[:-k]
    out /= np.max(np.abs(out)); out *= .7
    out *= np.clip(t / 1.2, 0, 1) * np.clip((dur - t) / 1.2, 0, 1)
    with wave.open(f'{out_dir}/{nome}.wav', 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.stack([out, out * .97], 1) * 32767).astype('<i2').tobytes())

def acordes(seq, amp_grave=.16, amp=.09, **kw):
    y = 0
    for notas, ini, fim in seq:
        for m in notas: y = y + pad([hz(m)], ini, fim, amp_grave if m < 50 else amp, **kw)
    return y

# 1. Pad calmo: Am9 - Fmaj7 - Cadd9 (o dos vídeos Lilo e Agenda, 2026-09-30)
finaliza(acordes([([45, 52, 57, 60, 64, 71], 0, 12), ([41, 53, 57, 60, 64, 69], 9, 22),
                  ([48, 55, 60, 64, 67, 74], 19, 30)]) + ar(.6), '1-pad-atual')

# 2. Pad claro e otimista: Cmaj7 - G6 - Am7 - Fmaj9
finaliza(acordes([([48, 55, 64, 67, 71], 0, 9.5), ([43, 55, 59, 64, 67], 7, 17),
                  ([45, 57, 60, 64, 67], 14.5, 24), ([41, 57, 60, 64, 67], 21.5, 30)],
                 brilho=(1, .45, .2, .08)) + ar(.4), '2-pad-claro')

# 3. Marimba leve sobre pad: arpejo a 92 BPM, sem bateria (movimento de loja)
buf = np.zeros(len(t))
prog = [[57, 60, 64, 67], [53, 57, 60, 64], [48, 55, 60, 64], [55, 59, 62, 67]]
passo = 60 / 92 / 2
for i in range(int(dur / passo)):
    ini = i * passo; acorde = prog[int(ini // (passo * 16)) % 4]
    padrao = [0, 2, 1, 3, 2, 1, 3, 2][i % 8]
    nota_curta(hz(acorde[padrao] + 12), ini, .22 if i % 2 == 0 else .14, decay=.35, harm=(1, .1, .3, .02))
base = acordes([([45, 57], 0, 11), ([41, 53], 10.4, 21.5), ([48, 55], 20.9, 30)], amp_grave=.12, amp=.07)
finaliza(buf + base + ar(.3), '3-marimba-leve', eco=((.33, .25), (.65, .15)))

# 4. Piano elétrico lo-fi: Dmaj7 - Bm7 - Gmaj7 - A6, acordes tocados a cada 2 tempos (76 BPM)
buf = np.zeros(len(t))
prog = [[50, 57, 61, 64, 66], [47, 54, 57, 62, 66], [43, 54, 59, 62, 66], [45, 52, 57, 61, 66]]
tempo = 60 / 76
for i in range(int(dur / (tempo * 2))):
    ini = i * tempo * 2; acorde = prog[(i // 2) % 4]
    for j, m in enumerate(acorde):
        nota_curta(hz(m), ini + j * .012, .16 if m < 50 else .1, decay=1.6, harm=(1, .3, .05), trem=4.5)
finaliza(buf + ar(.5), '4-piano-lofi', eco=((.21, .3), (.43, .2), (.8, .12)))

# 5. Minimal moderno: pulso grave suave + brilho agudo (tech, limpo)
buf = np.zeros(len(t))
tempo = 60 / 100
for i in range(int(dur / tempo)):
    nota_curta(hz([38, 38, 34, 36][int(i // 8) % 4]), i * tempo, .35, decay=.25, harm=(1, .15))
brilho = acordes([([74, 78, 81], 0, 15.5), ([72, 76, 79], 14.5, 30)], amp=.05, atk=4, rel=4, brilho=(1, .1))
finaliza(buf + brilho + ar(.25), '5-minimal-tech', eco=((.3, .3), (.6, .2), (1.2, .12)))
