#!/usr/bin/env python3


import api
import utils


def main():

    conf = utils.load_configuration("drwatson.conf")
    app = api.create_app()

    # TODO: Commandline or Config Args
    app.run(host='0.0.0.0',
            debug=conf.getboolean('app', 'Debug'),
            port=int(conf["app"]["port"]))

if __name__ == "__main__":
    main()
