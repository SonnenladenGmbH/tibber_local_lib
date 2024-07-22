import requests
from smllib import SmlStreamReader


class SMLDecoder:
    def __init__(self, url, auth, nodeID=1):
        self.url = url
        self.auth = auth
        self.nodeId = nodeID

    def fetch_data(self):
        try:
            response = requests.get(f"http://{self.url}/data.json?node_id={self.nodeId}", auth=self.auth)
            response.raise_for_status()
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch data: {e}")
            return None

    def decode_sml_data(self, data):
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

    def fetch_all_meter_data(self):
        data = self.fetch_data()
        obis_values = self.decode_sml_data(data)
        if obis_values is None:
            return None
        return obis_values # returns all available meter data

    def fetch_live_consumption(self):
        data = self.fetch_data()
        obis_values = self.decode_sml_data(data)
        if obis_values is None:
            return None

        for entry in obis_values:
            if entry.obis == '0100100700ff':  # OBIS code for current power (W)
                scaler = getattr(entry, 'scaler', 0)  # Default scaler is 0 if not provided
                return int(entry.value) * (10 ** scaler)

        return None

    def fetch_total_energy_import(self):
        data = self.fetch_data()
        obis_values = self.decode_sml_data(data)
        if obis_values is None:
            return None

        for entry in obis_values:
            if entry.obis == '0100010800ff':  # OBIS code for total consumption (Wh)
                scaler = getattr(entry, 'scaler', 0)  # Default scaler is 0 if not provided
                return int(entry.value) * (10 ** scaler)

        return None

    def fetch_total_energy_export(self):
        data = self.fetch_data()
        obis_values = self.decode_sml_data(data)
        if obis_values is None:
            return None

        for entry in obis_values:
            if entry.obis == '0100020800ff':  # OBIS code for total consumption (Wh)
                scaler = getattr(entry, 'scaler', 0)  # Default scaler is 0 if not provided
                return int(entry.value) * (10 ** scaler)

        return None


    def fetch_meter_id(self):
        data = self.fetch_data()
        obis_values = self.decode_sml_data(data)
        if obis_values is None:
            return None

        for entry in obis_values:
            if entry.obis == '0100000009ff':  # OBIS code for meter ID
                return entry.value

            elif entry.obis == '0100600100ff':  # alternative OBIS code for meter ID
                return entry.value

        return None