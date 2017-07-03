#!/usr/bin/env python3


username = "18fabe0e-71c2-4620-b56b-50825cf634d1"
password = "0Wa8PgikPkKj"
url = "https://gateway.watsonplatform.net/natural-language-understanding/api"
#    version='2017-02-27',

import json

from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding.features.v1 as \
    features

natural_language_understanding = NaturalLanguageUnderstandingV1(
    url=url,
    version='2017-02-27',
    username=username,
    password=password)

response = natural_language_understanding.analyze(
    text='Bruce Banner is the Hulk and Bruce Wayne is BATMAN! '
         'Superman fears not Banner, but Wayne.',
    features=[features.Entities(), features.Keywords(), features.Emotion()])

print(json.dumps(response, indent=2))
