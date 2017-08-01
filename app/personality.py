#!/usr/bin/python3


import json
from watson_developer_cloud import PersonalityInsightsV3

class Personality:

    def __init__(self, url, username, password, version):

        self.personality_insights = PersonalityInsightsV3(
            url=url,
            version=version,
            username=username,
            password=password,
        )

    def analize(self, text):
        """
        Returns the Watson PI Data for a specific text.
        """

        try:
            profile = self.personality_insights.profile(text,
                                                        raw_scores=True,
                                                        consumption_preferences=True)
        except Exception as e:
            print("Error during API call", e)
            profile = ""

        return profile
