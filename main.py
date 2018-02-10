# !/usr/bin/python3
# -*- coding: utf-8 -*-
import os

class Person():
    def __init__(self, name, word_file_path):
        self.name = name
        self.word_file_path = word_file_path

    def __repr__(self):
        return self.name

    def say(self, words):
        message = "[{}]:{}".format(self.name, words)
        print(message)

    def find_word(self, start):
        with open(word_file_path, "r") as f:
            for line in f:
                if line.startswith(start):
                    return line.replace("\n", "")
            return "I lose!"

    def fight(self, start):
        resp = self.find_word(start)
        self.say(resp)
        return resp

    def choose_one(self):
        import random
        num = random.choice(range(30000))
        i = 0
        with open(word_file_path, "r") as f:
            for line in f:
                if i == num:
                    resp = line.replace("\n", "")
                    self.say(resp)
                    return resp
                i += 1
            raise KeyError


class Game():
    def __init__(self, memebers):
        self.memebers = memebers
        self.endword = "I lose!"

    def run(self):
        import random
        first = random.choice(self.memebers)
        print("----[{}]先手-----".format(first))
        self.memebers.remove(first)
        sencond = self.memebers[0]
        print("----game start----")
        current_word = first.choose_one()
        for i in range(100):
            if current_word == self.endword: break
            word_tail = current_word[-1]
            current_word = sencond.fight(word_tail)
            if current_word == self.endword: break
            word_tail = current_word[-1]
            current_word = first.fight(word_tail)


if __name__ == "__main__":
    word_file_path = "成语.txt"
    LiMing = Person("LiMing", word_file_path)
    HanMeimei = Person("HanMeimei", word_file_path)
    game = Game([LiMing, HanMeimei])
    game.run()
