# Gera as 5 trilhas ambiente do Nallon: instrumentais, sem bateria, estéreo, com reverb.
# Uso: python trilhas.py <pasta> [segundos=30] [n]
#   -> <pasta>/1-aurora.wav ... 5-horizonte.wav (ou só a trilha n)
# Toda trilha resolve na tônica nos últimos segundos, onde cai a assinatura do vídeo.
# Sintetizadas aqui, sem licença de terceiros. Dependência: numpy.
import sys
import wave
import numpy as np

sr = 44100
out_dir = sys.argv[1]
dur = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0
so = sys.argv[3] if len(sys.argv) > 3 else None
n = int(sr * dur)
t = np.arange(n) / sr


def hz(m): return 440 * 2 ** ((m - 69) / 12)


def corte(passo):  # começo do acorde final (tônica): última troca de acorde antes de dur - 4,5 s
    return passo * ((dur - 4.5) // passo)


def nova(semente):  # buffer estéreo vazio; a semente fixa deixa cada trilha igual a cada geração
    global rng
    rng = np.random.default_rng(semente)
    return np.zeros((2, n))


def pad(buf, notas, ini, fim, amp, brilho=.55, borda=2.4):
    i0, i1 = max(int(ini * sr), 0), min(int(fim * sr), n)
    if i1 <= i0: return
    tt = t[i0:i1]
    env = (np.sin(np.pi / 2 * np.clip((tt - ini) / borda, 0, 1))
           * np.sin(np.pi / 2 * np.clip((fim - tt) / borda, 0, 1))) ** 2
    for m in notas:
        for canal in (0, 1):  # desafinação e fase diferentes por canal: largura estéreo
            x = 0
            for det in rng.uniform(-.004, .004, 3):
                fase = rng.uniform(0, 2 * np.pi)
                x = x + sum(brilho ** k / (k + 1) * np.sin((k + 1) * (2 * np.pi * hz(m) * (1 + det) * tt + fase))
                            for k in range(6))
            buf[canal, i0:i1] += amp * (1.1 if m < 48 else 1) * x * env


def cama(buf, prog, passo, amp, **kw):  # pad contínuo: um acorde a cada `passo` s, tônica (prog[0]) no fim
    c = corte(passo)
    for i in range(round(c / passo)):
        pad(buf, prog[i % len(prog)], i * passo - 1.2, (i + 1) * passo + 1.2, amp, **kw)
    pad(buf, prog[0], c - 1.2, dur + 3, amp, **kw)


def nota(buf, m, ini, amp, tipo, p=.5):  # p: 0 esquerda, 1 direita
    i0 = int(ini * sr); k = min(sr * 5, n - i0)
    if k <= 0: return
    tt = np.arange(k) / sr; w = 2 * np.pi * hz(m) * tt
    if tipo == 'ep':       # piano elétrico FM
        x = np.sin(w + (1.4 * np.exp(-tt / .45) + .2) * np.sin(w)) + .12 * np.sin(4 * w) * np.exp(-tt / .1)
        env = np.minimum(tt / .004, 1) * np.exp(-tt / 1.8)
    elif tipo == 'piano':  # piano de feltro: parciais um pouco inarmônicos, agudos morrem antes
        x = sum(np.sin(w * h * np.sqrt(1 + 4e-4 * h * h)) * np.exp(-tt * h ** .8 / 2.2) / h ** 1.4
                for h in range(1, 8))
        env = np.minimum(tt / .012, 1)
    elif tipo == 'pluck':
        x = np.sin(w) + .3 * np.sin(2 * w) + .08 * np.sin(3 * w)
        env = np.minimum(tt / .003, 1) * np.exp(-tt / .28)
    else:                  # 'sub': pulso grave macio
        x = np.sin(w)
        env = np.minimum(tt / .03, 1) * np.exp(-tt / .4)
    x = amp * x * env
    buf[:, i0:i0 + k] += np.stack([x * np.cos(p * np.pi / 2), x * np.sin(p * np.pi / 2)])


def eco(buf, d, ganhos=(.38, .24, .14, .08)):  # pingue-pongue: cada repetição troca de lado
    out = buf.copy()
    for i, g in enumerate(ganhos):
        k = int((i + 1) * d * sr)
        out[:, k:] += g * (buf[::-1] if i % 2 == 0 else buf)[:, :-k]
    return out


def filtra(y, lo, hi):  # passa-faixa de 2ª ordem, fase zero
    f = np.fft.rfftfreq(y.shape[-1], 1 / sr) + 1e-9
    return np.fft.irfft(np.fft.rfft(y) / np.sqrt(1 + (lo / f) ** 4) / np.sqrt(1 + (f / hi) ** 4), y.shape[-1])


def reverb(y, decay, mix):  # convolução com ruído estéreo em decaimento exponencial
    m = int(3.5 * sr)
    ir = rng.standard_normal((2, m)) * np.exp(-np.arange(m) / sr / decay)
    ir[:, :int(.02 * sr)] = 0
    tam = 1 << (n + m).bit_length()
    wet = filtra(np.fft.irfft(np.fft.rfft(y, tam) * np.fft.rfft(ir, tam), tam)[:, :n], 200, 5000)
    return y + mix * wet * np.sqrt(np.mean(y ** 2) / np.mean(wet ** 2))


def finaliza(buf, nome, decay=1.0, mix=.35):
    y = filtra(reverb(buf, decay, mix), 35, 9000)
    y = y.mean(0) + .6 * (y - y.mean(0))  # estreita o estéreo: soa bem também no alto-falante mono do celular
    y *= (np.sin(np.pi / 2 * np.clip(t / 1.0, 0, 1)) * np.sin(np.pi / 2 * np.clip((dur - t) / 2.0, 0, 1))) ** 2
    y *= .7 / np.max(np.abs(y))
    assert np.isfinite(y).all()
    with wave.open(f'{out_dir}/{nome}.wav', 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((y.T * 32767).astype('<i2').tobytes())


def aurora():  # 1. Pad quente em Ré maior com notas esparsas de piano elétrico: calmo e confiante
    b, m = nova(1), np.zeros((2, n))
    prog = [[38, 45, 54, 57, 61, 64], [35, 47, 54, 57, 62, 66], [43, 50, 54, 57, 59, 66], [45, 52, 57, 62, 64, 69]]
    cama(b, prog, 6, .05)
    ini = 1.5
    while ini < dur - 2:
        ac = prog[0] if ini >= corte(6) else prog[int(ini // 6) % 4]
        nota(m, rng.choice(ac[3:]) + 12, ini, .15, 'ep', rng.uniform(.25, .75))
        ini += rng.choice([1.5, 2.25, 3.0])
    finaliza(b + eco(m, .75, (.3, .18, .1)), '1-aurora', decay=1.2, mix=.45)


def vidro():  # 2. Piano elétrico em Fá maior, 76 BPM: quente, cara de produto bem-acabado
    b, m = nova(2), np.zeros((2, n))
    prog = [[41, 48, 57, 60, 64, 67], [38, 50, 53, 57, 60, 64], [46, 53, 57, 60, 62, 65], [48, 55, 58, 62, 65]]
    tempo = 60 / 76; passo = tempo * 4
    cama(b, [a[:2] for a in prog], passo, .05, brilho=.3)
    for i in range(int((dur - 1) / (tempo * 2))):
        ini = i * tempo * 2
        ac = prog[0] if ini >= corte(passo) - .01 else prog[(i // 2) % 4]
        for j, nt in enumerate(ac if i % 2 == 0 else ac[2:]):  # acorde cheio, depois só as vozes de cima
            nota(m, nt, ini + j * .018 + rng.uniform(0, .008),
                 (.2 if i % 2 == 0 else .13) * rng.uniform(.85, 1.1), 'ep', .3 + .08 * j)
    finaliza(b + eco(m, tempo * .75, (.22, .12)), '2-vidro', decay=.8, mix=.3)


def pulso():  # 3. Arpejo em colcheias com eco e pulso grave macio, 100 BPM: movimento, tecnologia
    b, m = nova(3), np.zeros((2, n))
    prog = [[48, 55, 60, 64, 67, 72], [45, 57, 60, 64, 67, 72], [41, 53, 57, 60, 65, 69], [43, 55, 59, 62, 67, 71]]
    tempo = 60 / 100; passo = tempo * 8
    cama(b, [a[:4] for a in prog], passo, .045, brilho=.35)
    for i in range(int((dur - .5) / (tempo / 2))):
        ini = i * tempo / 2
        ac = prog[0] if ini >= corte(passo) - .01 else prog[(i // 16) % 4]
        nota(m, ac[[2, 4, 3, 5, 4, 3, 5, 4][i % 8]] + 12, ini, .17 if i % 2 == 0 else .11, 'pluck', .35 + .3 * (i % 2))
        if i % 2 == 0: nota(b, ac[0], ini, .16, 'sub')
    finaliza(b + eco(m, tempo * .75), '3-pulso', decay=.7, mix=.28)


def manha():  # 4. Piano de feltro em Dó maior, 66 BPM: acolhedor, loja de bairro
    b, m = nova(4), np.zeros((2, n))
    prog = [[48, 55, 64, 67, 74, 76], [45, 52, 60, 64, 67, 72], [41, 53, 57, 64, 69, 72], [43, 55, 59, 62, 67, 74]]
    tempo = 60 / 66; passo = tempo * 4
    cama(b, [a[:3] for a in prog], passo, .03, brilho=.3)
    for comp in range(int(dur / passo) + 1):
        ac = prog[0] if comp * passo >= corte(passo) - .01 else prog[comp % 4]
        for batida, idx, forca in ((0, 0, .9), (0, 2, .7), (1, 3, .55), (2, 5, .8), (2.5, 4, .5), (3, 3, .6)):
            ini = comp * passo + batida * tempo + rng.uniform(0, .015)
            if ini < dur - 1: nota(m, ac[idx], ini, .26 * forca * rng.uniform(.85, 1.1), 'piano', .35 + .05 * idx)
    finaliza(b + m, '4-manha', decay=1.1, mix=.4)


def horizonte():  # 5. Crescendo em Sol maior, 90 BPM: sobe até a assinatura e resolve nela
    b, m = nova(5), np.zeros((2, n))
    prog = [[43, 50, 55, 59, 62, 67], [40, 52, 55, 59, 64, 67], [36, 48, 55, 60, 64, 67], [38, 50, 57, 62, 66, 69]]
    tempo = 60 / 90; passo = tempo * 8; c = corte(passo)
    cama(b, prog, passo, .05, brilho=.4)
    b *= .35 + .65 * np.clip(t / c, 0, 1) ** 1.5
    for i in range(round(c / (tempo / 2))):
        ini = i * tempo / 2; sobe = ini / c
        if sobe > .2:   # ostinato na quinta, entra aos poucos
            nota(m, 74, ini, .17 * (sobe - .2) * (1 if i % 2 == 0 else .6), 'pluck', .4 + .2 * (i % 2))
        if sobe > .5 and i % 4 == 0:
            nota(m, prog[(i // 16) % 4][3 + (i // 4) % 3] + 12, ini, .16 * sobe, 'ep', .6)
    for j, nt in enumerate(prog[0] + [79, 83, 86]):  # acorde de chegada, arpejado
        nota(m, nt, c + j * .03, .2, 'ep', .2 + .07 * j)
    finaliza(b + eco(m, tempo * .75), '5-horizonte', decay=1.2, mix=.4)


for i, trilha in enumerate((aurora, vidro, pulso, manha, horizonte), 1):
    if so in (None, str(i)): trilha()
