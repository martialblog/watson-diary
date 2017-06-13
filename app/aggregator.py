#!/usr/bin/env python3


from datetime import datetime
import requests


class ApiAggregator():
    """
    Base class for API aggregators. Aggregates an API on a date field.

    params: url - Endpoint for the API.
    params: datefield: Name of the date field within the API.

    Example usage:

    print(twitter.get_for_date("2017-04-03"))

    """

    def __init__(self, url, date_field, text_field, date_format='%a %b %d %H:%M:%S %Y'):

        self.url = url
        self.date_format = date_format
        self.date_field = date_field
        self.text_field = text_field
        self.data = {}
        self._initialize_data()

    def _load_api(self):
        """
        Loads the entry API data. Returns JSON object.
        """

        try:
            resp = requests.get(self.url)
        except Exception:
            print("Error Calling API")
            return {}

        return resp.json()

    def _initialize_data(self):
        """
        Aggregates the the data for this API.
        For different aggregation override this method.

        Default date format: "Mon Apr 04 16:09:50 2017"
        """

        for entry in self._load_api():
            date_obj = datetime.strptime(entry[self.date_field], self.date_format)
            date = str(date_obj.date())

            if date in self.data:
                self.data[date] = self.data[date] + ". " + entry[self.text_field]
            else:
                self.data[date] = entry[self.text_field]


    def aggregate_date(self, date):
        """
        Returns the aggregated data for a specific date.
        If no data is available an empty object is returned.

        params: date - date as string (format: YYYY-MM-DD)
        """

        try:
            resp = self.data[date]
        except KeyError as e:
            resp = None
        finally:
            return resp


# aggr = ApiAggregator("http://localhost:3000/api/twytta/realsherlock",
#                      "created_at",
#                      "text")
