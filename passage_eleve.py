# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 09:24:35 2021.

@author: Lebobe Timothe and Nicotte Loann
"""

import tkinter as tk
import random as rdm


def get_eleves() -> dict:
    """
    Read csv.

    Returns
    -------
    dict
        DESCRIPTION.

    """
    return_val = {}
    with open("passage_eleve.txt", "r") as f:
        for i in f.readlines()[1:]:
            i: str
            i = i.strip().split(";")
            key, val = tuple(i[1:3]), i[3]
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
    with open("passage_eleve.txt", "w") as f:
        f.write("classe;nom;prenom;passages\n")
        for key, val in dct.items():
            f.write("{};{};{};{};\n".format("TCurie", key[0], key[1], val))



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
        self.window.geometry("600x300+300+250")
        self.window.maxsize(self.window.winfo_screenwidth(),
                       self.window.winfo_screenheight())
        self.window.minsize(600, 300)

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
                  command=self.save).grid(row=0,
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
        self.result["text"]= "Résultat : " + " ".join(rdm.choice(eleve_lst))


    def save(self) -> None:
        """
        Save.

        Returns
        -------
        None
            DESCRIPTION.

        """
        eleve = tuple(self.result["text"].split(" ")[2:5])
        self.dict[eleve] += 1
        save(self.dict)

    def options(self) -> None:
        """
        Options.

        Parameters
        ----------
        *args : TYPE
            DESCRIPTION.
        **kwargs : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        owindow = tk.Tk()
        owindow.geometry("600x300+300+250")
        owindow.maxsize(owindow.winfo_screenwidth(),
                       owindow.winfo_screenheight())
        owindow.minsize(600, 300)

        omaster = tk.Frame()

        switch_button = tk.Button(omaster,
                                  text)

        pass



e = {("PARS", "Théo"): 0, ("PARS", "Patrick"): 0,
     ("PARS", "Albert"): 0, ("PARS", "Camus"): 0}

save(e)

App(e)
