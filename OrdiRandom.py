#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gestion du jeu de l'ordinateur.
"""

from random import choice, sample, randrange
from Ordi import Ordi


class OrdiRandom(Ordi):
    """Concrétisation de choix_coups avec un tirage aléatoire."""
    def choix_coups(self):
        """Choisi un coup parmi l'ensemble des coups possibles.

        * Si la carte à jouer est Liar, num_premise indique le numéro
          du joueur sur lequelle elle doit être jouée.

        * Si la carte est Révolution, num_premise et index sont les
          couples de numéros de prémisses et d'indice des cartes à
          échanger.

        * Dans le cas d'une carte joker, self._hand est modifié.

        :return: Un couple de triplets ((i_hand1, num_premise1, index1),
                 (i_hand2, num_premise2, index2))
        :rtype: tuple
        """
        coups = self.coups_possibles()
        ((i_hand1, num_premise1, index_premise1),
         (i_hand2, num_premise2, index_premise2)) = choice(coups)
        # gestion ddes cartes à jeter
        if i_hand1 == i_hand2 == -1:
            i_hand1, i_hand2 = sample(range(len(self._hand)), 2)
        elif i_hand1 == -1 or i_hand2 == -1:
            if i_hand1 == -1:
                (i_hand1, num_premise1, index_premise1) = (i_hand2,
                                                           num_premise2,
                                                           index_premise2)
            choix = list(range(len(self._hand)))  # choix possibles de carte2
            choix.remove(i_hand1)
            i_hand2 = choice(choix)
        coup = ([i_hand1, num_premise1, index_premise1],
                [i_hand2, num_premise2, index_premise2])
        # gestion des cartes hors prémisses (liar, exchange) et joker
        for i_coup, (i_hand, num_premise, index_premise) in enumerate(coup):
            if num_premise == -1:
                continue
            card = self._hand[i_hand]
            if card.is_liar():
                others = list(range(4))
                others.remove(self._num_player)
                coup[i_coup][1] = choice(others)
            if card.is_exchange():
                i = randrange(len(num_premise))
                coup[i_coup][1] = num_premise[i]
                coup[i_coup][2] = index_premise[i]
            if card.is_joker():
                choices = ("OR", "AND", "THEN") if card.is_jokerop() else "ABCD"
                card.name = choice(choices)
        if i_hand1 < i_hand2:
            coup[1][0] -= 1  # i_hand2 -= 1 en cas de tirages successifs
        return coup
