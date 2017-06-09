#!/usr/bin/env python3


import configparser


def load_configuration(filename):

    config = configparser.ConfigParser()
    config.read(filename)

    return config
