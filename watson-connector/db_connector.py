#!/usr/bin/env python3


import pymongo
from bson.json_util import dumps


class MongoDBConnector():
    """
    Handles the MongoDB connection and calls.
    """

    def __init__(self, server="localhost", port=27017):
        self.server = server
        self.port = int(port)
        self.client = pymongo.MongoClient(self.server, self.port)
        self.db = self.client["dr_watson_db"]
        self.reports = self.db['reports']

    def get_reports(self, user):
        """
        Get all reports for a specific user
        """

        try:
            data = self.reports.find({"user": user})
        except KeyError as e:
            data = {}
        finally:
            return dumps(data)

    def get_report(self, user, date):
        """
        Get a specific user report for a day
        """

        try:
            data = self.reports.find({"user": user, "date": date})
        except KeyError as e:
            data = {}
        finally:
            return dumps(data)

    def put_report(self, user, date, payload):
        """
        Store a new user report in database.
        """

        report = {"user": user,
                  "date": date,
                  "payload": payload}

        post_id = self.reports.insert_one(report).inserted_id

        return str(post_id)
