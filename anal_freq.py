 # -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:16:21 2020

@author: timot
analyse fréquentielle alphabet
"""


FREQ_FRANCAIS = {
    "A": 8.4,
    "B": 1.06,
    "C": 3.03,
    "D": 4.18,
    "E": 17.26,
    "F": 1.12,
    "G": 1.27,
    "H": 0.92,
    "I": 7.34,
    "J": 0.31,
    "K": 0.05,
    "L": 6.01,
    "M": 2.96,
    "N": 7.12,
    "O": 5.26,
    "P": 3.01,
    "Q": 0.99,
    "R":6.55,
    "S": 8.08,
    "T": 7.74,
    "U": 5.74,
    "V": 1.32,
    "W": 0.04,
    "X": 0.45,
    "Y": 0.30,
    "Z": 0.12
    }


def plus_proche(val1: float, val2: float, val_cible: float) -> float:
    return (val1, val2)[abs(val1 - val_cible) > abs(val2 - val_cible)]



class Texte:
    def __init__(self, text: str) -> None:
        self.text = text
        self.freq = {}
        self.nb_carract = 0
        self.freq2 = {}
        self.freq3 = {}
        self.compteur()
        self.associer(FREQ_FRANCAIS)

    def compteur(self) -> dict:
        self.freq = {chr(i): 0 for i in range(65, 91)}
        self.nb_carract = 0
        for i in self.text:
            self.freq[i] += 1
            self.nb_carract += 1
        for i in list(self.freq.items()):
            self.freq2[i[0]] = i[1] * 100 / self.nb_carract

    def associer(self, langue_frequence: dict) -> dict:
        self.freq3 = {chr(i): chr(i) for i in range(65, 91)}
        for i, j in list(self.freq2.items()):
            for k, l in list(langue_frequence.items()):
                # print(i, round(j, 2), k, l, 0.9 * l <= j <= 1.1 * l, 0.8 * l <= j <= 1.2 * l)
                if 0.9 * l <= j <= 1.1 * l:
                    if plus_proche(langue_frequence[self.freq3[i]], l, j) == l:
                        self.freq3[i] = k
                elif 0.8 * l <= j <= 1.2 * l:
                    print((self.freq2[i], l, j))
                    if plus_proche(langue_frequence[self.freq3[i]], l, j) == l:
                        self.freq3[i] = k
            # del langue_frequence[k]
        print("\n\n\n")

    def new_text(self):
        text = ""
        for i in self.text:
            text += self.freq3.get(i)
        return text


    def __str__(self) -> str:
        return self.text


if __name__ == "__main__":
    text = "WFWKSAKWFIMWDKWFKDWKHZADGKGHZWKGFLKMHHGKWIMWDSESLAWJWWLSALAFVAXXWJWFLWSMEGMNWEWFLWLSMJWHGKUWIMADQSVWTAWFUWJLSAFUWKLIMWLGMKDWKUGJHKYJSNALWFLDWKMFKKMJDWKSMLJWKUWKLIMWLGMLWKDWKHSJLAUMDWKVWKUGJHKYJSNALWFLDWKMFWKKMJDWKSMLJWKUWKLIMWVSFKUWLMFANWJKLGMLWKLWFLJSFKDSLAGFGMAFFAKMGMWFLJSFKDSLAGFWLAFFAKMSDSXGAKUWLLWKMHHGKALAGFVWKHZADGKGHZWKJWKKWETDWHWMLWLJWSUWDDWVWKYWGEWLJWKIMASVEWLLWFLVWKHGAFLKKSFKSMUMFWVAEWFKAGFVWKDAYFWKKSFKDSJYWMJFAHJGXGFVWMJVWKKMJXSUWKKSFKWHSAKKWMJGMHWMLWLJWHSJDWFLADKVMJWHGKJWDSLAXVMFWESKKWSMFWSMLJWLGMLWKLVSFKMFJWHGKJWDSLAXWFMFNSAKKWSMTSLLMHSJDSLWEHWLWJAWFFQWKLWFMFJWHGKSTKGDMHSKEWEWDWKEGDWUMDWKSYJWYSLANWKFAVMNSAKKWSMFAVWKUGJHKIMADJWFXWJEWKADKFWUGFUGANWFLHSKHDMKVWLWFVSFUWSMJWHGKIMSMEGMNWEWFLVSFKMFUGJHKIMWDUGFIMUWKLIMSHHSJWEEWFLADKJWYSJVWFLDSESLAWJWUGEEWZGEGYWFWUWKLIMADKXGFLSTKLJSULAGFVWLGMLWKDWKIMSDALWKIMADMAKGFLWKKWFLAWDDWKUWKLIMADKDSUGFKAVWJWFLUGEEWAFSDLWJSTDWVSFKDAFKLSFLHJWKIMWAFVANAKATDWVWDWMJKHWUMDSLAGFUWKLIMADKJSAKGFFWFLVMJWHGKJWDSLAXVMFSYJWYSLSMFSMLJWSYJWYSLUWKLIMADKGMTDAWFLIMWLSFVAKIMADKJSAKGFFWFLVWDAFVAXXWJWFUWVMUGJHKSMEGMNWEWFLGMSMJWHGKDWTDGUVWESJTJWLWFVSKSVAKKGDMLAGFUWKLIMADKSFWSFLAKKWFLHSJDSHWFKWWWLDWEGMNWEWFLYWFWJSDIMASFAEWLGMKDWKUGJHKWLDWMJSULAGFHSJLAUMDAWJWVWKMFKKMJDWKSMLJWKIMADWKVWLJMALLGMKUWKLIMWUWLLWAFVAXXWJWFUWIMGAIMWXSMKKWWFWDDWEWEWESAKEGEWFLSFWWFWJWFVJSHSKDWKDGAKVMEGMNWEWFLWJJGFWWK"
    print(Texte(text).new_text())
