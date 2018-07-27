# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import Any, Dict

from aiohttp.web import View, json_response, Response

from parkmatte import ParkMatte
from calc_time import calc_start_time

PRE_DATA = {'version': '1.0'}


class Analyser(View):
    async def post(self):
        data = await self.request.json()
        print('response', data)

        answer: Dict[str, Any] = deepcopy(PRE_DATA)

        answer['session'] = {
            'session_id': data['session']['session_id'],
            'message_id': data['session']['message_id'],
            'user_id': data['session']['user_id'],
        }

        if data['request']['command'] in ('', 'test'):
            print('1 way')

            answer['response'] = {
                'text': 'Если вы припарковались, скажите мне место парковки.',
                'tts': 'Если вы припарковались, скажите мне место парковки.'
            }

        else:
            print('2 way')

            parkmatte = ParkMatte()
            name, data = parkmatte.parse(data['request']['command'])

            if name == 'get_time':
                d = data.groupdict()
                calc_start_time(int(d['digits']), 'hours' if (d['units'] == 'часов') else 'minutes')
                answer['response'] = {
                    'text': parkmatte.answer(name)
                }

        print(answer.keys())
        answer['response']['end_session'] = False

        print('answer', answer)
        return json_response(answer)

    async def get(self):
        return Response(text="Hello pal!")
