# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:24:35 2021.

@author: Lebobe Timothe and Nicotte Loann
"""


import re


import tkinter as tk
import random as rdm


from list_pile import ListFile


def get_eleves(path: str = "NSI_eleves.csv") -> dict:
    """
    Read csv.

    Returns
    -------
    dict
        DESCRIPTION.

    """
    return_val = {}
    with open(path, "r") as f:
        for i in f.readlines()[1:]:
            i: str
            i = i.strip().split(";")
            key, val = tuple(i[:2]), i[2]
            return_val[key] = int(val)

    return return_val


def save(dct: dict) -> None:
    """
    Save a csv.

    Parameters
    ----------
    dct : dict
        DESCRIPTION.

    Returns
    -------
    None
        DESCRIPTION.

    """
    with open("passage_eleve.csv", "w") as f:
        f.write("nom;prenom;passages;\n")
        for key, val in dct.items():
            f.write("{};{};{};\n".format(key[0], key[1], val))



class App:
    """
    App.

    Returns
    -------
    TYPE
        DESCRIPTION.

    """

    def __init__(self, dct: dict = get_eleves()) -> None:
        """
        Buider.

        Returns
        -------
        None
            DESCRIPTION.

        """
        self.dict = dct
        self.window = tk.Tk()
        self.window.title("Interrogation Arbitraire")
        self.window.geometry("600x300+300+250")
        self.window.maxsize(self.window.winfo_screenwidth(),
                       self.window.winfo_screenheight())
        self.window.minsize(600, 300)

        self.auto_save = True
        self.omaster, self.switch_button = [None] * 2
        self.tirages = ListFile()

        bg = "#777777"
        font = (None, 20)

        self.window.config(bg=bg)

        master_frame = tk.Frame(self.window, bg=bg)
        tk.Label(master_frame,
                 text="Qui va être interrogé ?",
                 font=(None, 40),
                 bg=bg).pack(expand=True)

        but_frame = tk.Frame(master_frame, bg=bg)

        tk.Button(but_frame,
                  text="tirer au sort",
                  font=font,
                  command=self.get_rdm_eleve).grid(row=0,
                                                   column=0,
                                                   sticky=tk.W,
                                                   padx=10)

        tk.Button(but_frame,
                  text="Enregistrer",
                  font=font,
                  command=self.call_save).grid(row=0,
                                          column=1,
                                          sticky=tk.W,
                                          padx=10)

        tk.Button(but_frame,
                  text="Option",
                  font=font,
                  command=self.options).grid(row=0,
                                          column=2,
                                          sticky=tk.W,
                                          padx=10)

        but_frame.pack(expand=True)

        self.result = tk.Label(master_frame,
                          text="Résultat : ",
                          font=font,
                          bg=bg)
        self.result.pack(expand=True)

        master_frame.pack(expand=True)
        self.window.mainloop()

    def get_rdm_eleve(self, dct: dict = get_eleves()) -> str:
        """
        Get a students.

        Parameters
        ----------
        dct : dict, optional
            DESCRIPTION. The default is get_eleves().

        Returns
        -------
        str
            DESCRIPTION.

        """
        somme = 0
        for val in dct.values():
            somme += val
        nb_eleve = len(dct)

        prob = {}
        for key, val in dct.items():
            try:
                val = round(somme * 10 / (nb_eleve * val))
            except ZeroDivisionError:
                val = round(somme * 10 / nb_eleve)
            if val == 0:
                val = 1

            prob[key] = val
        eleve_lst = [key for key, val in prob.items() for i in range(val)]
        eleve = " ".join(rdm.choice(eleve_lst))
        self.result["text"]= "Résultat : " + eleve
        if len(self.tirages) <= 10:
            self.tirages.add(eleve)
            self.tirages.delete_start()
        else:
            self.tirages.add(eleve)

        if self.auto_save:
            self.save()


    def save(self) -> None:
        """
        Save.

        Returns
        -------
        None
            DESCRIPTION.

        """
        if re.findall("^Résultat : \\w+ \\w+$", self.result["text"]):
            eleve = tuple(self.result["text"].split(" ")[2:5])
            self.dict[eleve] += 1
            save(self.dict)
        else:
            tk.messagebox.showerror("Enregistrement", "L'enregistrement est"
                                    "impossible car aucun tirage n'a été "
                                    "fait.")

    def call_save(self)-> None:
        """
        Call save.

        Returns
        -------
        None.

        """
        if self.auto_save:
            tk.messagebox.showinfo("Enregistrer", "Ce résultat a déja été "
                                   "enregistré si vous voulez désactiver "
                                   "l'enregistrement automatique aller dans"
                                   " Option>Enregistrement auto. ",
                                   parent=self.window)
        else:
            self.save()

    def options(self) -> None:
        """
        Options.

        Returns
        -------
        None.

        """
        owindow = tk.Tk()
        owindow.title('Options')
        owindow.geometry("600x300+300+250")
        owindow.maxsize(owindow.winfo_screenwidth(),
                        owindow.winfo_screenheight())
        owindow.minsize(600, 300)

        bg = "#777777"

        owindow.config(bg=bg)


        omaster = tk.Frame(owindow, bg=bg)

        tk.Label(omaster, text="Options", bg=bg)

        self.switch_button = tk.Button(omaster,
                                  text="Enregistrement auto. : {}"
                                  .format(("Désactivé",
                                           "Activé")[self.auto_save]),
                                  command=self.switch,
                                  font=(None, 20))
        self.switch_button.pack(expand=True)

        buth = tk.Button(omaster,
                         text="Historique des tirages",
                         font=(None, 20),
                         command=self.history)
        buth.pack(expand=True)

        omaster.pack(expand=True)

        owindow.mainloop()

    def history(self) -> None:
        """
        History.

        Returns
        -------
        None.

        """
        win = tk.Tk()
        win.title("historique")
        win.geometry("500x500+400+50")
        win.config(bg="#777777")
        hmaster = tk.Frame(win, bg="#777777")
        print(len(self.tirages))
        if len(self.tirages):
            for i in range(len(self.tirages)):
                tk.Label(hmaster,
                         text=self.tirages.get_maillon_indice(i),
                         bg="#777777",
                         font=(None, 20)).pack(expand=True)
        else:
            tk.Label(hmaster,
                     text="pas de tirages",
                     bg="#777777",
                     font=(None, 30)).pack(expand=True)
            tk.Label(hmaster,
                     text="enrgistrés sur cette session",
                     bg="#777777",
                     font=(None, 30)).pack(expand=True)
        hmaster.pack(expand=True)

    def switch(self) -> None:
        """
        Switch.

        Returns
        -------
        None.

        """
        self.auto_save = not self.auto_save
        self.switch_button["text"] = "Enregistrement auto. : {}" \
                                      .format(("Désactivé",
                                               "Activé")[self.auto_save])


NSI = {("LEBOBE", "Timothé"): 0, ("NICOTTE", "Loann"): 0,
     ("BAILLET", "Maxime"): 0, ("OUDIN", "Clement"): 0,
     ("JONQUET", "Logan"): 0, ("ROYER", "Lucas"): 0, ("ARNOUD", "Florian"): 0,
     ("POLYCARPE", "Guillaume"): 0, ("MAGINOT", "Louen"): 0,
     ("DUPONT", "Alexis"): 0, ("LE MANS", "Léo"): 0,
     ("PERRETANT", "Mallory"): 0, ("GIRAULT", "Lucas"): 0,
     ("LOGEROT", "Alexis"): 0, ("TETVUIDE", "Yanis"): 0,
     }

App(get_eleves())
