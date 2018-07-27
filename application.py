 from flask import Flask, request
import logging

application = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@application.route("/", methods=['POST'])
def main():
    logging.info('Request: %r', request.json)
    return "HELLO"

if __name__=="__main__":
    application.run()
