# -*- coding: utf-8 -*-

from aiohttp.web import Application, run_app, post, view

from analyser import Analyser

HANDLERS = [
    view('/', Analyser),
]


def main():
    application = Application()
    application.router.add_routes(HANDLERS)
    run_app(application, host='127.0.0.1', port=1496, access_log=None)


if __name__ == '__main__':
    main()
