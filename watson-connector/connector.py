#!/usr/bin/env python3


import configparser
import json
import watson_developer_cloud as wdc


def load_configuration(filename):

    config = configparser.ConfigParser()
    config.read(filename)

    return config


def tone_analyser(config):

    analyzer = wdc.ToneAnalyzerV3(
        url=config["watson"]["url"],
        username=config["watson"]["username"],
        password=config["watson"]["password"],
        version=config["watson"]["version"]
    )

    return analyzer


def main():

    cf = load_configuration("credentials.conf")
    ta = tone_analyser(cf)

    print(json.dumps(ta.tone(text='I am very happy'), indent=2))


if __name__ == "__main__":
    main()
