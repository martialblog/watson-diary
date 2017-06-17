#!/usr/bin/env python3


import json
import watson_developer_cloud as wdc

from aggregator import ApiAggregator

# TODO This class is shit... I know.
# TODO All this Feed Stuff should really be in another class

class WatsonConnector():
    """
    Handles the connection to IBM Watson, API calls and whatnot.
    """

    def __init__(self, url, username, password, version, db_connector):

        self.db = db_connector
        self.tone_analyzer =  wdc.ToneAnalyzerV3(
            url=url,
            username=username,
            password=password,
            version=version
        )

    def mock_watson_ta(self, data):
        """
        Mocking the IBM Watson Tone Analyzer call for testing.
        """

        with open('response.json.example') as data_file:
            data = json.load(data_file)

        return data

    def _get_feeds(self, username):

        user = self.db.users.find_one({"username": username})

        if not user:
            return {}

        try:
            feeds = user["feeds"]
        except IndexError as e:
            feeds = {}
        finally:
            return feeds

    def _initialize_aggregators(self, username):

        aggregators = []
        texts = []
        feeds = self._get_feeds(username)

        for userfeed in feeds:
            feed = self.db.feeds.find_one({"key": userfeed['key']})
            aggr = ApiAggregator(feed["url"] + userfeed['username'],
                                 feed["date_field"],
                                 feed["text_field"])

            aggregators.append(aggr)

        return aggregators

    def dates(self, username):

        dates = []
        aggregators = self._initialize_aggregators(username)

        for aggregator in aggregators:
            dates += aggregator.get_dates()

        return dates

    def analyze_tone(self, username, date):
        """
        Returns the Tone Analyzer Data for a specific user and date.
        """

        texts = []
        aggregators = self._initialize_aggregators(username)

        for aggregator in aggregators:

            text = aggregator.aggregate_date(date)
            if text:
                texts.append(text)

        if not text:
            return

        text = ". ".join(texts)

        # Real Call
        # payload = self.tone_analyzer.tone(text=text_aggregation)
        # Fake Call
        payload = self.mock_watson_ta(texts)

        new_report = { "username": username,
                       "date": date,
                       "data": payload,
        }

        new_id = self.db.reports.replace_one(
            {"username": username, "date": date},
            new_report,
            True)

        return new_id.raw_result
