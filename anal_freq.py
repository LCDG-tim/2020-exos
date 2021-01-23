 # -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 15:16:21 2020.

@author: timot
analyse fréquentielle alphabet
"""

from anal_freq2 import get_txt


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
    "Z": 0.12,
    " ": 1000
    }

FREQ_FRANCAIS2 = {
    "A": 7.11,
    "B": 1.14,
    "C": 3.18,
    "D": 3.67,
    "E": 12.10,
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
    "R": 6.55,
    "S": 8.08,
    "T": 7.74,
    "U": 5.74,
    "V": 1.32,
    "W": 0.04,
    "X": 0.45,
    "Y": 0.30,
    "Z": 0.12,
    " ": 1000
    }


def plus_proche(val1: float, val2: float, val_cible: float) -> float:
    """
    Plus proche.

    Parameters
    ----------
    val1 : float
        DESCRIPTION.
    val2 : float
        DESCRIPTION.
    val_cible : float
        DESCRIPTION.

    Returns
    -------
    float
        DESCRIPTION.

    """
    return ((val1, abs(val1 - val_cible)),
            (val2, abs(val2 - val_cible)))[abs(val1 - val_cible) >
                                           abs(val2 - val_cible)]



class Texte:
    """A simple text.

    A other line because kite want it
    """

    def __init__(self, text: str) -> None:
        """
        Builder.

        Parameters
        ----------
        text : str
            DESCRIPTION.

        Returns
        -------
        None
            DESCRIPTION.

        """
        self.text = text
        self.freq = {}
        self.nb_carract = 0
        self.freq2 = {}
        self.freq3 = {}
        self.compteur()
        self.associer(FREQ_FRANCAIS)

    def compteur(self) -> dict:
        """
        Documentation is a documentation.

        Returns
        -------
        dict
            DESCRIPTION.

        """
        self.freq = {chr(i): 0 for i in range(65, 91)}
        self.nb_carract = 0
        for j, i in enumerate(self.text):
            self.freq[i] += 1
            self.nb_carract += 1
        for i in list(self.freq.items()):
            self.freq2[i[0]] = round(i[1] * 100 / self.nb_carract, 2)

    def associer(self, langue_frequence: dict, precision: float = .01) -> dict:
        """
        Documentation is a documentation.

        Returns
        -------
        dict
            DESCRIPTION.

        """
        self.freq3 = {chr(i):" " for i in range(65, 91)}
        for i, j in list(self.freq2.items()):
            if j  > 6:
                for k, l in list(langue_frequence.items()):
                    a = plus_proche(langue_frequence[self.freq3[i]], l, j)
                    print(a)
                    if a[0] == l and a[1] < 1:
                        self.freq3[i] = k
                        print(i, k, a, self.freq3)

    def new_text(self):
        """
        Documentation is a documentation.

        Returns
        -------
        dict
            DESCRIPTION.

        """
        text = ""
        for i in self.text:
            text += self.freq3.get(i)
        return text


    def __str__(self) -> str:
        """
        Documentation is a documentation.

        Returns
        -------
        dict
            DESCRIPTION.

        """
        return self.text


if __name__ == "__main__":
    text = "BWFWKSAKWFIMWDKWFKDWKHZADGKGHZWKGFLKMHHGKWIMWDSESLAWJWWLSALAFVAXXWJWFLWSMEGMNWEWFLWLSMJWHGKUWIMADQSVWTAWFUWJLSAFUWKLIMWLGMKDWKUGJHKYJSNALWFLDWKMFKKMJDWKSMLJWKUWKLIMWLGMLWKDWKHSJLAUMDWKVWKUGJHKYJSNALWFLDWKMFWKKMJDWKSMLJWKUWKLIMWVSFKUWLMFANWJKLGMLWKLWFLJSFKDSLAGFGMAFFAKMGMWFLJSFKDSLAGFWLAFFAKMSDSXGAKUWLLWKMHHGKALAGFVWKHZADGKGHZWKJWKKWETDWHWMLWLJWSUWDDWVWKYWGEWLJWKIMASVEWLLWFLVWKHGAFLKKSFKSMUMFWVAEWFKAGFVWKDAYFWKKSFKDSJYWMJFAHJGXGFVWMJVWKKMJXSUWKKSFKWHSAKKWMJGMHWMLWLJWHSJDWFLADKVMJWHGKJWDSLAXVMFWESKKWSMFWSMLJWLGMLWKLVSFKMFJWHGKJWDSLAXWFMFNSAKKWSMTSLLMHSJDSLWEHWLWJAWFFQWKLWFMFJWHGKSTKGDMHSKEWEWDWKEGDWUMDWKSYJWYSLANWKFAVMNSAKKWSMFAVWKUGJHKIMADJWFXWJEWKADKFWUGFUGANWFLHSKHDMKVWLWFVSFUWSMJWHGKIMSMEGMNWEWFLVSFKMFUGJHKIMWDUGFIMUWKLIMSHHSJWEEWFLADKJWYSJVWFLDSESLAWJWUGEEWZGEGYWFWUWKLIMADKXGFLSTKLJSULAGFVWLGMLWKDWKIMSDALWKIMADMAKGFLWKKWFLAWDDWKUWKLIMADKDSUGFKAVWJWFLUGEEWAFSDLWJSTDWVSFKDAFKLSFLHJWKIMWAFVANAKATDWVWDWMJKHWUMDSLAGFUWKLIMADKJSAKGFFWFLVMJWHGKJWDSLAXVMFSYJWYSLSMFSMLJWSYJWYSLUWKLIMADKGMTDAWFLIMWLSFVAKIMADKJSAKGFFWFLVWDAFVAXXWJWFUWVMUGJHKSMEGMNWEWFLGMSMJWHGKDWTDGUVWESJTJWLWFVSKSVAKKGDMLAGFUWKLIMADKSFWSFLAKKWFLHSJDSHWFKWWWLDWEGMNWEWFLYWFWJSDIMASFAEWLGMKDWKUGJHKWLDWMJSULAGFHSJLAUMDAWJWVWKMFKKMJDWKSMLJWKIMADWKVWLJMALLGMKUWKLIMWUWLLWAFVAXXWJWFUWIMGAIMWXSMKKWWFWDDWEWEWESAKEGEWFLSFWWFWJWFVJSHSKDWKDGAKVMEGMNWEWFLWJJGFWWK"

    a = Texte(get_txt())
