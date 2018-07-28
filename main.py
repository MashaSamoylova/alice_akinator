# -*- coding: utf-8 -*-

from aiohttp.web import Application, run_app, post, view
from analyser import Analyser
from db_manager import *


HANDLERS = [
    view('/', Analyser),
]


def main():
    application = Application()
    application.router.add_routes(HANDLERS)
    run_app(application, host='127.0.0.1', port=5000, access_log=None)


if __name__ == '__main__':
    prepare_db()
    main()
