#!/usr/bin/env python3


from datetime import datetime
import json
import requests


class ApiAggregator():
    """
    Base class for API aggregators. Aggregates an API on a date field.

    params: url - Endpoint for the API.
    params: datefield: Name of the date field within the API.

    Example usage:

    print(twitter.get_for_date("2017-04-03"))

    """

    def __init__(self, url, datefield):

        self.url = url
        self.datefield = datefield
        self.data = {}
        self._initialize_data()

    def _load_api(self):
        """
        Loads the entry API data. Returns JSON object.
        """

        resp = requests.get(self.url)

        if not resp.status_code == 200:
            print("Error Calling API")
            return

        return resp.json()

    def _initialize_data(self):
        """
        Aggregates the the data for this API.
        For different aggregation override this method.

        Default date format: "Mon Apr 04 16:09:50 2017"
        """

        for entry in self._load_api():
            date_obj = datetime.strptime(entry[self.datefield], '%a %b %d %H:%M:%S %Y')
            date = str(date_obj.date())

            if date in self.data:
                self.data[date] = self.data[date] + " - " + entry['text']
            else:
                self.data[date] = entry['text']


    def get_for_date(self, date):
        """
        Returns the aggregated data for a specific date as JSON.
        If no data is available an empty object is returned.

        params: date - date as string (format: YYYY-MM-DD)
        """

        try:
            resp = self.data[date]
        except KeyError as e:
            resp = {}
        finally:
            return resp
