#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/7/22 10:27
# filename: Cards.py
class Card():
    """
    A playing card.
    """
    # 牌面数字1~13
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    # 梅花、方块、红心、黑桃
    SUITS = ["梅", "方", "红", "黑"]

    def __init__(self, rank, suit, face_up=True):
        self.rank = rank  # 指定牌面数字
        self.suit = suit  # 指定花色
        self.is_face_up = face_up  # 是否显示牌的正面，True为正面，False为背面

    def __str__(self):
        if self.is_face_up:
            rep = self.suit + self.rank
        else:
            rep = "XX"
        return rep

    def pic_order(self):
        if self.rank == "A":
            FaceNum = 1
        elif self.rank == "J":
            FaceNum = 11
        elif self.rank == "Q":
            FaceNum = 12
        elif self.rank == "K":
            FaceNum = 13
        else:
            FaceNum = int(self.rank)

        if self.suit == "梅":
            Suit = 1
        elif self.suit == "方":
            Suit = 2
        elif self.suit == "红":
            Suit = 3
        else:
            Suit = 4
            return (Suit - 1) * 13 + FaceNum

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand():
    """
    A hand of playing cards.
    """

    def __init__(self):
        self.cards = []  # cards 列表变量存储牌手的牌

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "无牌"
        return rep

    def clear(self):
        """
        清空手里的牌
        :return:
        """
        self.cards = []

    def add(self, card):
        """
        增加牌
        :param card:
        :return:
        """
        self.cards.append(card)

    def give(self, card, other_hand):
        """
        把一张牌给其他选手
        :param card: 牌
        :param other_hand: 其他选手
        :return:
        """
        self.cards.remove(card)
        other_hand.add(card)


class Poke(Hand):
    """
    A deck of playing cards.
    """

    def populate(self):
        """
        生成一副牌
        :return:
        """
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        """
        洗牌
        :return:
        """
        import random
        random.shuffle(self.cards)  # 打乱牌的顺序


    def deal(self, hands, per_hand=13):
        """
        发牌，发给玩家，每人默认13张手牌
        :param hands:
        :param per_hand:
        :return:
        """
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.cards.remove(top_card)
                    hand.add(top_card)
                    # self.give(top_card, hand)
                else:
                    print("不能继续发牌了，牌已经发完！")


if __name__ == '__main__':
    print("This is a module with classes for playing cards.")

    # 4个玩家
    players = [Hand(), Hand(), Hand(), Hand()]
    pokel1 = Poke()
    pokel1.populate()  # 生成一副牌
    pokel1.shuffle()  # 洗牌
    pokel1.deal(players, 13)  # k发给玩家每人13张牌

    # 显示4位牌手的牌
    n = 1
    for hand in players:
        print("牌手", n, end=":")
        print(hand)
        n += 1
    input("\n Press the enter key to exit. ")
