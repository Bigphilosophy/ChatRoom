# -*- coding: utf-8 -*-
import os

def prepare_file():
    with open("成语.txt", "w+") as to_file:
        with open("成语大全.txt", "r") as f:
            for line in f:
                if line.find("拼音") != -1:
                    strip_line = line.replace(" ", "")
                    split_line = strip_line.split("拼音")[0] + "\n"
                    to_file.write(split_line)


class Person():
    def __init__(self, name, word_file_path):
        self.name = name,
        self.word_file_path = word_file_path

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


if __name__ == "__main__":
    prepare_file()
    word_file_path = "成语.txt"
    LiMing = Person("LiMing", word_file_path)
    HanMeimei = Person("HanMeimei", word_file_path)
    print(LiMing.name)
    # ----start
    print("-----game begin------")
    current_word = "为所欲为"
    for i in range(10000):
        if current_word == "I lose!": break
        word_tail = current_word[-1]
        current_word = HanMeimei.fight(word_tail)
        if current_word == "I lose!": break
        word_tail = current_word[-1]
        current_word = LiMing.fight(word_tail)
