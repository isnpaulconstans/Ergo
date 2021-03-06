#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Le paquet de cartes."""

from random import shuffle
from Card import Card
from Constantes import Constantes as Cst


class Deck(list):
    """Le paquet de cartes."""
    def __init__(self):
        """Constructeur de la classe

        :return: un paquet de cartes mélangées
        :rtype: Deck
        """
        super().__init__()
        for carte, number in Cst.NUMBER.items():
            super().extend([Card(carte) for _ in range(number)])
        shuffle(self)

    def draw(self, number):
        """Tire number cartes

        :param number: le nombre de cartes à tirer
        :type number: int

        :return: number cartes du paquet s'il en reste assez, la fin du
                 paquet ou une liste vide sinon.
        :rtype: list
        """
        res = []
        while len(res) < number and self != []:
            res.append(super().pop())
        return res

    def append(self, card):
        """Ajoute une carte à la fin du paquet (possible avec Tabula Rasa).

        :param card: la carte à ajouter
        :type card: Card"""
        super().insert(0, card)

    def pop(self):
        """Récupère la dernière carte (pour annuler un Tabula Rasa).

        :return: la dernière carte du paquet
        :type card: Card"""
        return super().pop(0)

    def is_finished(self):
        """Indique si la paquet est terminé.

        :return: True si la paquet est terminé, False sinon
        :rtype: bool"""
        return self == []
