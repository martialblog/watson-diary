#!/usr/bin/env python3


import json
from aggregator import ApiAggregator


class ReportManager():
    """
    Handles the generation of reports
    """

    def __init__(self, username, watson_manager, personality, db_connector):

        self.username = username
        self.watson = watson_manager
        self.person = personality
        self.db = db_connector
        self.aggregators = []

        self.init_aggregators()

    def get_user_feeds(self):

        user = self.db.users.find_one({"username": self.username})
        # TODO Need to check if feed is available and active

        if not user:
            return {}

        try:
            # TODO for debugging hardcoded, needs to be fixed
            # feeds = user["feeds"]
            feeds = [{'username': 'realsherlock', 'key': 'twitter'}]

            # feeds = [{'username': 'realsherlock', 'key': 'facebook'},
            #          {'username': 'realsherlock', 'key': 'twitter'},
            #          {'username': 'realsherlock', 'key': 'gmail'}]

        except IndexError as e:
            feeds = {}
        finally:
            return feeds

    def init_report(self, date):

        report = self.db.reports.find_one({"username": self.username, "date": date})

        if not report:
            report = { "username": self.username,
                       "date": date,
                       "reports": {}
            }

        return report


    def init_aggregators(self):

        texts = []
        feeds = self.get_user_feeds()

        for userfeed in feeds:
            feed = self.db.feeds.find_one({"key": userfeed['key']})
            aggr = ApiAggregator(feed["url"] + userfeed['username'],
                                 feed["date_field"],
                                 feed["text_field"])

            self.aggregators.append(aggr)


    def get_dates(self):
        """
        Returns all dates for which there's data
        """

        dates = []

        for aggregator in self.aggregators:
            dates += aggregator.get_dates()

        return dates

    def ta_report(self, date):
        """
        Returns the Tone Analyzer Data for a specific user and date.
        Returns the ID of the new database entry.
        """

        report = self.init_report(date)
        texts = []

        for aggregator in self.aggregators:
            text = aggregator.aggregate_date(date)
            if text:
                texts.append(text)

        if not text:
            return

        text = ". ".join(texts)

        payload = self.watson.report(text)

        report["reports"]["nlu"] = payload

        newid = self.db.reports.replace_one(
            {"username": self.username, "date": date},
            report,
            True)

        return newid.raw_result

    def pi_report(self):
        """
        Returns the Personality Insight Data for a specific user and date.
        Returns the ID of the new database entry.
        """

        texts = []

        for date in self.get_dates():

            for aggregator in self.aggregators:
                text = aggregator.aggregate_date(date)
                if text:
                    texts.append(text)

        if not text:
            return

        text = ". ".join(texts)

        payload = self.person.analize(text)
        report = {"username": self.username, "pi": payload}

        print(report)

        newid = self.db.pireports.replace_one(
            {"username": self.username}, report,
            True)

        return newid.raw_result
