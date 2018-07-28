# -*- coding: utf-8 -*-
from copy import deepcopy
from typing import Any, Dict

from aiohttp.web import View, json_response, Response

from parkmatte import ParkMatte
from calc_time import calc_start_time
from db_manager import *

PRE_DATA = {'version': '1.0'}


class Analyser(View):
    async def post(self):
        data = await self.request.json()
        user_id = data['session']['user_id']
        session_id = data['session']['session_id']

        db_data = select_all_data(user_id, session_id)

        print('response', data)

        answer: Dict[str, Any] = deepcopy(PRE_DATA)

        answer['session'] = {
            'session_id': data['session']['session_id'],
            'message_id': data['session']['message_id'],
            'user_id': data['session']['user_id'],
        }

        if data['request']['command'] in ('', 'test'):
            answer['response'] = {
                'text': 'Если вы припарковались, скажите мне место парковки.',
                'tts': 'Если вы припарковались, скажите мне место парковки.'
            }

        else:
            parkmatte = ParkMatte()

            name, data = parkmatte.parse(data['request']['command'])

            if name == 'unknown':
                answer['response'] = {
                    'text': 'Что, простите?',
                    'tts': 'Что, простите?'
                }

            elif name == 'start_parking':
                insert(user_id, session_id)

                answer['response'] = {
                    'text': parkmatte.answer(name)
                }

            elif name == 'get_place':
                update_place(data.groupdict()['place'], db_data['id'])

                answer['response'] = {
                    'text': parkmatte.answer(name)
                }

            elif name == 'get_cost':
                update_payment_per_hour(data.groupdict()['place'], db_data['id'])

                answer['response'] = {
                    'text': parkmatte.answer(name)
                }

            elif name == 'get_free_hours':
                update_free_period(data.groupdict()['free_hours'], db_data['id'])

                answer['response'] = {
                    'text': parkmatte.answer(name)
                }

            elif name == 'where_car':
                answer['response'] = {
                    'text': parkmatte.answer(name).format(data=db_data['place'])
                }

            elif name == 'free_hours_left':
                t = calc_free_time(user_id, session_id)

                answer['response'] = {
                    'text': parkmatte.answer(name).format(data=t)
                }

            elif name == 'how_much_pay':
                d = calc_payment(user_id, session_id)

                answer['response'] = {
                    'text': parkmatte.answer(name).format(data=d)
                }

            elif name == 'left_parking':
                update_close_status(db_data['id'])

                answer['response'] = {
                    'text': parkmatte.answer(name)
                }

            elif name == 'get_time':
                d = data.groupdict()
                t = calc_start_time(int(d['digits']), 'hours' if (d['units'] == 'часов') else 'minutes')
                answer['response'] = {
                    'text': parkmatte.answer(name)
                }

        print(answer.keys())
        answer['response']['end_session'] = False

        print('answer', answer)
        return json_response(answer)

    async def get(self):
        return Response(text="Hello pal!")
