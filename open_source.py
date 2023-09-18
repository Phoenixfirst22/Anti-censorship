import random

# Made by Phoenixfirst22
# https://github.com/Phoenixfirst22


mode = input("Easy read mode?(y/n): ")


while mode.lower() != "y" and mode.lower() != "n":
    print(mode + " is not an option ")
    mode = input("please select a valid option(y/n): ")
if mode.lower() == "y":
    print("Easy read mode enabled")
    a = ["α"]
    b = ["b"]
    c = ["ç"]
    d = ["Ð"]
    e = ["℮"]
    f = ["℉"]
    g = ["ğ"]
    h = ["Ἠ", "Ἡ", "Ἢ", "Ἣ", "Ἤ", "Ἥ", "Ἦ", "Ἧ", "ᾘ", "ᾙ", "ᾚ", "ᾛ", "ᾜ", "ᾝ", "ᾞ", "ᾟ", "Ὴ"]
    i = ["í", "Ī", "ī", "Ĭ", "ỉ"]
    j = ["ȷ"]
    k = ["Ķ", "ķ"]
    l = ["Ļ", "L̂"]
    m = ["m", "м"]
    n = ["ņ", "Ñ"]
    o = ["ó", "ó"]
    p = ["р́"]
    q = ["q"]
    r = ["Ř"]
    s = ["Š", "š", "ŝ"]
    t = ["Τ", "t", "т"]
    u = ["Ū", "ū", "ú", "ü"]
    v = ["v"]
    w = ["Ш"]
    x = ["×"]
    y = ["Ý", 'ý']
    z = ['Ž', 'ž']
else:
    a = ["ά", "α", "á", "ã", "ą", "Å"]
    b = ["ß", "b"]
    c = ["℃", "ç"]
    d = ["Ð"]
    e = ["℮", "ë", "ê", "é"]
    f = ["℉", "ƒ"]
    g = ["Ğ", "ğ"]
    h = ["Ἠ", "Ἡ", "Ἢ", "Ἣ", "Ἤ", "Ἥ", "Ἦ", "Ἧ", "ᾘ", "ᾙ", "ᾚ", "ᾛ", "ᾜ", "ᾝ", "ᾞ", "ᾟ", "Ὴ"]
    i = ["í", "Ī", "ī", "Ĭ", "ỉ"]
    j = ["ȷ"]
    k = ["Ķ", "ķ"]
    l = ["Ļ", "L̂"]
    m = ["m", "м"]
    n = ["Ņ", "ņ", "И", "ŋ", "Ñ", "ñ"]
    o = ["ó", "ó", "0", "ø"]
    p = ["Ⓟ", "р́"]
    q = ["Q", "q"]
    r = ["Я", "Ř"]
    s = ["Š", "š", "$", "ŝ"]
    t = ["Τ", "t", "т"]
    u = ["Ū", "ū", "ú", "ü"]
    v = ["v"]
    w = ["Ш"]
    x = ["×"]
    y = ["Ý", 'ý']
    z = ['Ž', 'ž']
    print("normal mode")
zzz = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
zzz2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
print("Made by Phoenixfirst22")
print("https://github.com/Phoenixfirst22")
#input
while True:
    eingabe = input("Enter text: ")
    # array aus input
    bl_count = len(eingabe)
    bl = list(eingabe)


    # ausgebe liste
    def l(bl):
        zähler2 = 0
        nl = []
        while bl_count != zähler2:
            if bl[zähler2] in zzz2:
                nl.append(random.choice(zzz[zzz2.index(bl[zähler2])]))
            else:
                nl.append(bl[zähler2])
            zähler2 += 1
        print(''.join(nl))


    l(bl)











