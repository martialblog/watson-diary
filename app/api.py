#!/usr/bin/env python3


from bson import json_util
import argparse
import flask
import flask_cors as cors
import os
import pymongo
import utils
import json

import watson as w
import report as r
import chatbot as c


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

    Watson = w.WatsonConnector(url=conf["watson"]["url"],
                             username=conf["watson"]["username"],
                             password=conf["watson"]["password"],
                             version=conf["watson"]["version"]
    )

    Chatbot = c.Chatbot(url=conf["chatbot"]["url"],
                        username=conf["chatbot"]["username"],
                        password=conf["chatbot"]["password"],
                        version=conf["chatbot"]["version"],
                        workspace_id=conf["chatbot"]["workspace"]
    )

    chatbot_sessions = {}

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
        url = flask.request.json['url']
        name = flask.request.json['name']
        active = flask.request.json['active']
        date_field = flask.request.json['date_field']
        text_field = flask.request.json['text_field']

        new_feed = { "key": key,
                     "url": url,
                     "name": name,
                     "active": active,
                     "date_field": date_field,
                     "text_field": text_field}

        feeds.replace_one({"key": key}, new_feed, True)

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

        return flask.jsonify({}, 200)

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

        output = json_util.dumps(output)

        status = 200
        if output == "[]":
            status = 204

        return output, status

    @app.route('/users/<path:username>', methods=['GET'])
    def get_user(username):
        """
        Returns Profile for specified user.
        """

        user = db.users.find({"username": username})
        user = json_util.dumps(user)

        status = 200
        if user == "[]":
            status = 204

        return user, status

    @app.route('/users/<path:username>/feeds', methods=['GET'])
    def get_feeds_for_user(username):
        """
        Returns all feeds for specified user.
        """

        user = db.users.find_one({"username": username})

        try:
            feeds = user["feeds"]
            status = 200
        except IndexError as e:
            feeds = {}
            status = 204

        feeds = json_util.dumps(feeds)

        return feeds, status

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

        return flask.jsonify({}, 201)

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

        return flask.jsonify({}, 200)

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
        reports = json_util.dumps(reports)

        status = 200
        if reports == "[]":
            status = 204

        return reports, status

    @app.route('/reports/<path:username>/<path:date>', methods=['GET'])
    def get_user_report_date(username, date):
        """
        Returns specified report for specified user.
        """

        report = db.reports.find({"username": username, "date": date})
        report = json_util.dumps(report)

        status = 200
        if report == "[]":
            status = 204

        return report, status

    @app.route('/reports/<path:username>/<path:date>', methods=['PUT'])
    def post_report(username, date):
        """
        Create a new report for a user
        """

        reports = db.reports
        report = reports.find({"username": username, "date": date})

        if not report:
            flask.abort(404)

        rm = r.ReportManager(username, Watson, db)
        rm.ta_report(date)

        return flask.jsonify({}, 201)

    @app.route('/reports/<path:username>/<path:date>', methods=['DELETE'])
    def delete_report(username, date):
        """
        Delete a report
        """
        reports = db.reports
        report = reports.find({"username": username, "date": date})

        if not report:
            flask.abort(404)

        reports.delete_one({"username": username, "date": date})

        return flask.jsonify({}, 200)

    #############
    # Functions #
    #############

    @app.route('/functions/generate/reports/<path:username>', methods=['GET'])
    def generate_all_reports(username):
        """
        Generate all reports for specified user.
        """

        rm = r.ReportManager(username, Watson, db)
        dates = rm.get_dates()

        for date in dates:
           rm.ta_report(date)

        return flask.jsonify({}, 200)

    @app.route('/functions/chatbot', methods=['POST'])
    def chatbot():
        """
        Talk to chatbot.
        """

        # TODO: Validate request data
        chat_input = flask.request.json['input']
        session_id = flask.request.json['sessionid']

        if session_id in chatbot_sessions:
            context = chatbot_sessions[session_id]
        else:
            context = {}

        response = Chatbot.conversate(text=chat_input, context=context)
        chatbot_sessions[session_id] = response['context']
        response_output = response['output']

        return flask.jsonify(response_output, 200)

    return app
