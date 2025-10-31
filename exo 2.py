def compter_mots(t):
    return t.split()


def frequence_mots(m):
    f = {}
    for x in m: f[x] = f.get(x, 0) + 1
    return f


def longueur_moyenne_mots(m):
    return sum(len(x) for x in m) / len(m) if m else 0


def mot_plus_moins(f):
    p, m = max(f, key=f.get), min(f, key=f.get)
    return p, f[p], m, f[m]


def detecter_palindromes(f):
    return [x for x in f if x == x[::-1] and len(x) > 1]


def separer_phrases(t):
    p, s = [], ""
    for c in t:
        s += c
        if c in ".!?": p.append(s.strip()); s = ""
    if s: p.append(s.strip())
    return p


def longueur_moyenne_phrases(p):
    return sum(len(x.split()) for x in p) / len(p) if p else 0


def ponctuation_utilisee(t):
    return {c for c in t if c in ".!,?;:"}


def statistiques_mots(m):
    s = {"courts": 0, "moyens": 0, "longs": 0}
    for x in m:
        if len(x) <= 3:
            s["courts"] += 1
        elif len(x) <= 6:
            s["moyens"] += 1
        else:
            s["longs"] += 1
    return s


def top_10(f):
    return sorted(f.items(), key=lambda x: x[1], reverse=True)[:10]


def phrases_longues(p):
    return sorted(p, key=len, reverse=True)[:3]


def diversite(m):
    return len(set(m)) / len(m) * 100 if m else 0


def patterns(m):
    return [m[i] for i in range(len(m) - 1) if m[i] == m[i + 1]]


def analyse():
    with open("data.txt", "r") as f:
        t = f.read()

    m, freq, p = compter_mots(t), frequence_mots(compter_mots(t)), separer_phrases(t)
    a, b, c, d = mot_plus_moins(freq)
    print("Nombre de mots :", len(m))
    print("Longueur moyenne des mots :", round(longueur_moyenne_mots(m), 2))
    print("Mot le plus utilisé :", a, b)
    print("Mot le moins utilisé :", c, d)
    print("Palindromes :", detecter_palindromes(freq))
    print("Nombre de phrases :", len(p))
    print("Longueur moyenne des phrases :", round(longueur_moyenne_phrases(p), 2))
    print("Ponctuations utilisées :", ponctuation_utilisee(t))
    print("Statistiques des mots :", statistiques_mots(m))
    print("Top 10 :", top_10(freq))
    print("Phrases les plus longues :", phrases_longues(p))
    print("Diversité du vocabulaire :", round(diversite(m), 2), "%")
    print("Patterns répétitifs :", patterns(m))


analyse()