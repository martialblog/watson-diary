#!/usr/bin/env python3


import json
from aggregator import ApiAggregator


class ReportManager():
    """
    Handles the generation of reports
    """

    def __init__(self, username, watson_manager, db_connector):

        self.username = username
        self.watson = watson_manager
        self.db = db_connector
        self.aggregators = []

        self.init_aggregators()

    def get_user_feeds(self):

        user = self.db.users.find_one({"username": self.username})

        if not user:
            return {}

        try:
            feeds = user["feeds"]
        except IndexError as e:
            feeds = {}
        finally:
            return feeds

    def init_report(self, date):

        init_report = { "username": self.username,
                        "date": date,
        }

        if "reports" in init_report.keys():
            pass
        else:
            init_report["reports"] = []

        return init_report


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

        payload = self.watson.ta_report(text)
        report["reports"].append(payload)

        newid = self.db.reports.replace_one(
            {"username": self.username, "date": date},
            report,
            True)

        return newid.raw_result
