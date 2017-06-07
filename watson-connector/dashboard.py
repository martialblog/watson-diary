#!/usr/bin/env python3


import argparse
import flask
import flask_cors as cors
import os

from db_connector import MongoDBConnector
from watson_connector import WatsonConnector
import utils


def create_app():
    """
    Defines routes and returns a Flask object.
    """

    app = flask.Flask(__name__)
    app.secret_key = os.urandom(128)
    cors.CORS(app)

    conf = utils.load_configuration("drwatson.conf")

    Mongo = MongoDBConnector(server=conf["database"]["server"],
                             port=conf["database"]["port"]
    )

    Watson = WatsonConnector(url=conf["watson"]["url"],
                             username=conf["watson"]["username"],
                             password=conf["watson"]["password"],
                             version=conf["watson"]["version"],
                             db_connector=Mongo
    )

    @app.route('/')
    def show_dashboard():
        return flask.render_template('index.html')


    @app.route('/v1/api/watson/data/<path:user>/reports/<path:date>', methods=['PUT'])
    def update_report(user, date):
        """
        Generates a report for the specified user and date.
        """

        has_entry = Mongo.get_report(user, date)

        # TODO: There's gotta be a better way for this
        if not str(has_entry) == "[]":
            return has_entry

        new_entry = Watson.analyze_tone(user, date)

        return new_entry

    @app.route('/v1/api/watson/data/<path:user>/reports', methods=['GET'])
    def get_reports(user):
        """
        Returns the saved report for the specified user and date as JSON.
        """

        data = Mongo.get_reports(user)

        return data


    @app.route('/v1/api/watson/data/<path:user>/reports/<path:date>', methods=['GET'])
    def get_report_for_date(user, date):
        """
        Returns the saved report for the specified user and date as JSON.
        """

        data = Mongo.get_report(user, date)

        return data


    return app
