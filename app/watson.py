#!/usr/bin/env python3


import json
import watson_developer_cloud as wdc

from aggregator import ApiAggregator


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

    def analyze_tone(self, username, date):
        """
        Returns the Tone Analyzer Data for a specific user and date.
        """

        # TODO: Clean up this messy function
        aggregators = []
        texts = []
        feeds = self._get_feeds(username)

        for key, userid in feeds.items():
            feed = db.feeds.find_one({"key": key})
            aggr = ApiAggregator(feed["url"] + userid,
                                 feed["date_field"],
                                 feed["text_field"])

            aggregators.append(aggr)

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
