import json

import requests


class DataProducer:

    @staticmethod
    def produce(url: str, payload: dict):
        response = requests.post(url=url, data=json.dumps(payload))

        if response.status_code == 201:
            print(f"[INFO] Data from {payload.get('location')} was produced to the database")
