#!/usr/bin/env python3


import json
import watson_developer_cloud as wdc


class WatsonConnector():

    def __init__(self, url, username, password, version, db_connector):

        self.db = db_connector
        self.tone_analyzer =  wdc.ToneAnalyzerV3(
            url=url,
            username=username,
            password=password,
            version=version
        )

    def analyze_tone(self, user, date):

        payload = "I'm a new report from watson."

        # TODO: Call aggregator and send text to IBM
        # aggregation = ApiAggregator()
        # Don't wanna waste API calls while testing
        # payload = json.dumps(ta.tone(text=aggregation), indent=2)

        new_id = self.db.put_report(user, date, payload)

        return new_id
