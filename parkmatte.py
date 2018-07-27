# -*- coding: utf-8 -*-
import json
import re
import random


class ParkMatte:
    def __init__(self):
        with open('commands.json', 'r') as fp:
            self.commands_json: dict = json.load(fp)

        with open('answers.json', 'r') as fp:
            self.answer_json = json.load(fp)

    def parse(self, text: str):
        for key, commands in self.commands_json.items():
            for command in commands:
                match = re.match(command, text)

                if match is not None:
                    print('ppp:', key, match)
                    return key, match

        return 'unknown', None

    def answer(self, command):
        return random.choice(self.answer_json[command])
