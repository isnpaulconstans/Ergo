#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Interface graphique."""

import tkinter as tk
from Constantes import Constantes as Cst


class PryeIntro(tk.Toplevel):
    """Interface graphique fenetre acceuil avec animation
    et choix du mode de jeu"""
    # definition du chemin des lettres de l'animation
    LETWAY = [
                (1,15),(1,14),(1,13),(2,13),(3,13),(3,14),(3,15),(4,13),
                (5,13),(5,14),(5,15), #E
                (1,9),(2,9),(3,10),(4,10),(5,10),(2,11),(1,11), #Y
                (5,5),(4,5),(3,6),(3,7), #r
                (5,1),(4,1),(3,1),(2,1),(1,1),(1,2),(1,3),(2,3),(3,3),(3,2) #P
                   ]

    def __init__(self):
        """Constructeur de la classe

        :return: Objet PryeIntro
        :rtype: PryeIntro
        """
        super().__init__()
        self.title("PrYE acceuil")
        self.grab_set()
        self.transient(self.master)
        self.resizable(width=False, height=False)
        self.__init_intro__()
        self.button_choice()
        self.cheat = tk.BooleanVar()
        tk.Checkbutton(self, text="cheat mode",
                       variable=self.cheat
                       ).grid(column=0, row=2, columnspan=4)
        self.flag = 1
        self.pause = 150
        self.animate_letter(len(self.LETWAY), self.LETWAY)

    def __init_intro__(self):
        """ Creation de la fenetre d'animation """
        self.can = tk.Canvas(self, height=7*Cst.CARD_HEIGHT,
                             width=17*Cst.CARD_WIDTH,
                             bg="skyblue")
        self.can.grid(column=0, row=0, columnspan=5)
        self.img = tk.PhotoImage(file="images/carteBack.png")
        self.id_img = self.can.create_image(425, 465, image=self.img)

    def rectangle(self, x, y):
        """ création d'un rectangle trace du passage de la carte.

        :param x: abscisse du coin supérieur gauche
        :type x: int
        :param y: ordonnée du coin inférieur droit
        :type y: int
        """
        self.can.create_rectangle(x, y, x+Cst.CARD_WIDTH, y+Cst.CARD_HEIGHT,
                                  fill="ivory")

    def animate_letter(self, nb_cards, l_way):
        """ deplace la carte sur le canvas en suivant un chemin defini ,
        de façon récursive et laisse la trace du parcours

        :param nb_cards: nombre de cartes à afficher
        :type nb_cards: int

        :param l_way: le chemin à suivre par la carte PrYE
        :type l_way: list
        """
        if self.flag != 1:
            return
        if nb_cards == 0:
            self.flag = 0
            return
        self.can.coords(self.id_img,
                        Cst.CARD_WIDTH*(l_way[nb_cards-1][1]+1)
                        - Cst.CARD_WIDTH/2,
                        Cst.CARD_HEIGHT*l_way[nb_cards-1][0]
                        + Cst.CARD_HEIGHT/2)
        self.rectangle(Cst.CARD_WIDTH*l_way[nb_cards-1][1],
                       Cst.CARD_HEIGHT*l_way[nb_cards-1][0])
        self.can.tag_raise(self.id_img)
        self.after(self.pause, lambda: self.animate_letter(nb_cards-1, l_way))

    def button_choice(self):
        """ Creation des boutons de choix du mode de jeu """
        for nb_player in range(1, 5):
            pluriel = "s" if nb_player >= 2 else ""
            tk.Button(self, text="{} joueur{}".format(nb_player, pluriel),
                      bd=7, font="Arial 16",
                      command=lambda x=nb_player: self.destroy(x)
                      ).grid(column=nb_player-1, row=1)

    def destroy(self, nb_player=1):
        """Ferme la fenêtre d'introduction et lance le jeu.

        :param nb_player: le nombre de joueurs humains
        :type nb_player: int
        """
        self.master.start(nb_player, self.cheat.get())
        super().destroy()
