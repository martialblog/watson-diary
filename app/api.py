#!/usr/bin/env python3


from bson import json_util
import argparse
import flask
import flask_cors as cors
import os
import pymongo
import utils


def create_app():
    """
    Defines routes and returns a Flask object.
    """

    conf = utils.load_configuration("drwatson.conf")

    app = flask.Flask(__name__)
    app.secret_key = os.urandom(128)
    cors.CORS(app)

    mongo = pymongo.MongoClient("localhost", 27017)
    db = mongo.drwatson

    # Watson = WatsonConnector(url=conf["watson"]["url"],
    #                          username=conf["watson"]["username"],
    #                          password=conf["watson"]["password"],
    #                          version=conf["watson"]["version"],
    #                          db_connector=db
    # )

    #########
    # Feeds #
    #########

    @app.route('/feeds', methods=['GET'])
    def get_feeds():
        """
        Returns all available feeds.
        """

        feeds = db.feeds
        output = []

        for s in feeds.find():
            output.append(s)

        return json_util.dumps(output)

    @app.route('/feeds/<path:feed>', methods=['GET'])
    def get_feed(feed):
        """
        Returns info for specified feed.
        """

        feed = db.feeds.find({"key": feed})

        return json_util.dumps(feed)

    @app.route('/feeds/<path:key>', methods=['PUT'])
    def post_feed(key):
        """
        Post new feed
        """

        feeds = db.feeds
        feed = feeds.find({"key": key})


        # TODO: Validate request data
        key = flask.request.json['key']
        name = flask.request.json['name']
        active = flask.request.json['active']
        date_field = flask.request.json['date_field']
        text_field = flask.request.json['text_field']

        new_feed = { "key": key,
                     "name": name,
                     "active": active,
                     "date_field": date_field,
                     "text_field": text_field}

        feeds.replace_one({"key": key}, new_feed, True)

        # TODO: Proper Return value
        return flask.jsonify({"result": []}, 201)

    @app.route('/feeds/<path:key>', methods=['DELETE'])
    def delete_feed(key):
        """
        Delete a feed.
        """
        feeds = db.feeds
        feed = feeds.find({"key": key})

        if not feed:
            flask.abort(404)

        feeds.delete_one({"key": key})

        # TODO: Proper Return value
        return flask.jsonify({"result": []}, 200)

    #########
    # Users #
    #########

    @app.route('/users', methods=['GET'])
    def get_users():
        """
        Returns all users.
        """

        users = db.users
        output = []

        for s in users.find():
            output.append(s)

        return json_util.dumps(output)

    @app.route('/users/<path:username>', methods=['GET'])
    def get_user(username):
        """
        Returns Profile for specified user.
        """

        user = db.users.find({"username": username})

        return json_util.dumps(user)

    @app.route('/users/<path:username>/feeds', methods=['GET'])
    def get_feeds_for_user(username):
        """
        Returns all feeds for specified user.
        """

        user = db.users.find({"username": username})
        u = list(user)

        try:
            feeds = u[0]["feeds"]
        except IndexError as e:
            feeds = {}

        return json_util.dumps(feeds)

    @app.route('/users/<path:username>', methods=['PUT'])
    def post_user(username):
        """
        Create a new user profile.
        """
        users = db.users

        # TODO: Validate request data
        username = flask.request.json['username']
        password = flask.request.json['password']
        mail = flask.request.json['mail']
        feeds = flask.request.json['feeds']

        new_user = { "username": username,
                     "mail": mail,
                     "password": password,
                     "feeds": feeds}

        users.replace_one({"username": username}, new_user, True)

        # TODO: Proper Return value
        return flask.jsonify({"result": []}, 201)

    @app.route('/users/<path:username>', methods=['DELETE'])
    def delete_user(username):
        """
        Delete a user profile.
        """
        users = db.users
        user = users.find({"username": username})

        if not user:
            flask.abort(404)

        users.delete_one({"username": username})

        # TODO: Proper Return value
        return flask.jsonify({"result": []}, 200)

    ###########
    # Reports #
    ###########

    @app.route('/reports/<path:username>', methods=['GET'])
    @app.route('/users/<path:username>/reports', methods=['GET'])
    def get_user_reports(username):
        """
        Returns all reports for specified user.
        """

        reports = db.reports.find({"username": username})

        return json_util.dumps(reports)

    @app.route('/reports/<path:username>/<path:date>', methods=['GET'])
    def get_user_report_date(username, date):
        """
        Returns specified report for specified user.
        """

        report = db.reports.find({"username": username, "date": date})

        return json_util.dumps(report)

    @app.route('/reports/<path:username>/<path:date>', methods=['PUT'])
    def post_report(username, date):
        """
        Create a new report for a user
        """

        reports = db.reports
        report = report.find({"username": username, "date": date})

        if not report:
            flask.abort(404)

        # TODO: Call IBM Watson Connector
        # Watson.create_report(username, date)

        # For testing:
        username = username
        date = date
        data = "TEST PAYLOAD"

        new_report = { "username": username,
                       "date": date,
                       "data": data,
        }

        reports.insert_one(new_report)

        # TODO: Proper Return value
        return flask.jsonify({"result": []}, 201)

    @app.route('/reports/<path:username>/<path:date>', methods=['DELETE'])
    def delete_report(username, date):
        """
        Delete a report
        """
        reports = db.reports
        report = report.find({"username": username, "date": date})

        if not report:
            flask.abort(404)

        reports.delete_one({"username": username, "date": date})

        # TODO: Proper Return value
        return flask.jsonify({"result": []}, 200)

    return app
