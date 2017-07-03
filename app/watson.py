#!/usr/bin/env python3


import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

from aggregator import ApiAggregator

class WatsonConnector():
    """
    Handles the connection to IBM Watson, API calls and whatnot.
    """

    def __init__(self, url, username, password, version):

        self.natural_language_understanding = NaturalLanguageUnderstandingV1(
            url=url,
            version=version,
            username=username,
            password=password)


    def mock_watson(self, data):
        """
        Mocking the IBM Watson Tone Analyzer call for testing.
        """

        with open('response.json.example.2') as data_file:
            data = json.load(data_file)

        return data


    def report(self, text):
        """
        Returns the Watson Data for a specific test.
        """

        # Real Call
        payload = self.natural_language_understanding.analyze(
           text=text,
           features=[features.Entities(), features.Keywords(), features.Emotion()])

        # Fake Call, since we only have limited access to IBM
        # payload = self.mock_watson(text)
        nlu_report = {"nlu": payload}

        return nlu_report
