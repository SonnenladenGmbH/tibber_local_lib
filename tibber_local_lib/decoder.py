import requests
from smllib import SmlStreamReader


class SMLDecoder:
    def __init__(self, url, auth):
        self.url = url
        self.auth = auth

    def fetch_data(self):
        try:
            response = requests.get(f"http://{self.url}/data.json?node_id=1", auth=self.auth)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data: {e}")
            return None

    def decode_data(self, data):
        if data is None:
            return None

        stream = SmlStreamReader()
        stream.add(data)
        sml_frame = stream.get_frame()
        if sml_frame is None:
            print('Bytes missing')
            return None

        obis_values = sml_frame.get_obis()
        return obis_values

    def fetch_live_consumption(self):
        data = self.fetch_data()
        obis_values = self.decode_data(data)
        if obis_values is None:
            return None

        for entry in obis_values:
            if entry.obis == '0100100700ff':  # OBIS code for current power (W)
                return int(entry.value) / 10

        return None

    def fetch_total_consumption(self):
        data = self.fetch_data()
        obis_values = self.decode_data(data)
        if obis_values is None:
            return None

        for entry in obis_values:
            if entry.obis == '0100010800ff':  # OBIS code for total consumption (Wh)
                return int(entry.value) / 10

        return None

    def fetch_tariff1_consumption(self):
        data = self.fetch_data()
        obis_values = self.decode_data(data)
        if obis_values is None:
            return None

        for entry in obis_values:
            if entry.obis == '0100010801ff':  # OBIS code for tariff 1 consumption (Wh)
                return int(entry.value) / 10

        return None

    def fetch_tariff2_consumption(self):
        data = self.fetch_data()
        obis_values = self.decode_data(data)
        if obis_values is None:
            return None

        for entry in obis_values:
            if entry.obis == '0100010802ff':  # OBIS code for tariff 2 consumption (Wh)
                return int(entry.value) / 10

        return None

    def fetch_meter_id(self):
        data = self.fetch_data()
        obis_values = self.decode_data(data)
        if obis_values is None:
            return None

        for entry in obis_values:
            if entry.obis == '0100000009ff':  # OBIS code for current power (W)
                return entry.value

        return None