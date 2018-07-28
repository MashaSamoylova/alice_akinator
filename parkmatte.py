# -*- coding: utf-8 -*-
import json
import re


class ParkMatte:
    def __init__(self):
        with open('commands.json', 'r') as fp:
            self.commands_json = json.load(fp)

        with open('answer.json', 'r') as fp:
            self.answer_json = json.load(fp)

    def parse(self, text: str):
        for key, commands in self.commands_json:
            for command in commands:
                match = re.match(command, text)

                if match:
                    return key, match
