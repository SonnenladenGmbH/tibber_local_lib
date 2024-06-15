from tibber_local_lib import SMLDecoder

password = "XXXX-XXXX" # 'XXXX-XXXX' from your QR-Code
url = "http://tibber-host.fritz.box/data.json?node_id=1" # change the hostname or replace it with your IP
auth = ('admin', password)

tibber_pulse = SMLDecoder(url, auth)

meter_id = tibber_pulse.fetch_meter_id()
print(f'Device ID: {meter_id}')

consumption = tibber_pulse.fetch_live_consumption()
print(f'Current Power (W): {consumption}')  # Output: total live power in W

total_consumption = tibber_pulse.fetch_total_consumption()
print(f'Total Consumption (Wh): {total_consumption}')  # Output: total consumption in Wh

tariff1_consumption = tibber_pulse.fetch_tariff1_consumption()
print(f'Tariff 1 Consumption (Wh): {tariff1_consumption}')  # Output: tariff 1 consumption in Wh

tariff2_consumption = tibber_pulse.fetch_tariff2_consumption()
print(f'Tariff 2 Consumption (Wh): {tariff2_consumption}')  # Output: tariff 2 consumption in Wh