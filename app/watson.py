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

    def __init__(self, url, username, password, version):

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


    def ta_report(self, text):
        """
        Returns the Tone Analyzer Data for a specific test.
        """

        # Real Call
        payload = self.tone_analyzer.tone(text=text)
        # Fake Call, since we only have limited access to IBM
        #payload = self.mock_watson_ta(text)
        ta_report = {"ta": payload}

        return ta_report
