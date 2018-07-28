from flask import Flask, request
from aiohttp import web
from aioalice import Dispatcher, get_new_configured_app
import logging

application = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
dp = Dispatcher()

@application.route("/", methods=['POST'])
@dp.request_handler()
async def handle_all_requests(alice_request):
    return alice_request.response('Привет этому миру!')

if __name__=="__main__":
    application.run(port='5000')
