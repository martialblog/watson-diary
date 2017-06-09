#!/usr/bin/env python3


import json
import watson_developer_cloud as wdc

from api_aggregator import ApiAggregator


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


    def analyze_tone(self, user, date):
        """
        Returns the Tone Analyzer Data for a specific user and date.
        """

        # TODO: Implement this method
        # TODO: How to handle multiple aggregations?
        # TODO: Call aggregator and send text to IBM
        twitter = ApiAggregator("http://localhost:3000/api/twytta/", "created_at")
        aggregation = twitter.get_for_date(date)

        # Real Call
        # payload = self.tone_analyzer.tone(text=aggregation)

        # Fake Call
        payload = self.mock_watson_ta(aggregation)

        new_id = self.db.put_report(user, date, payload)

        return new_id
