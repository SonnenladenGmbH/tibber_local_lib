from tibber_local_lib import SMLDecoder

password = "XXX-XXX" # 'XXXX-XXXX' from your QR-Code
tibber_pulse_host = "tibber-host.fritz.box" # change the hostname or replace it with your IP
nodeId = 1 # find your nodeId: http://tibber-host.fritz.box/nodes/ | default is 1
auth = ('admin', password)

tibber_pulse = SMLDecoder(tibber_pulse_host, auth, nodeId)

meter_id = tibber_pulse.fetch_meter_id()
print(f'Device ID: {meter_id}') # Output: meter ID

consumption = tibber_pulse.fetch_live_consumption()
print(f'Current Power (W): {consumption}')  # Output: total live power in W

total_import = tibber_pulse.fetch_total_energy_import()
print(f'Total Energy Import (Wh): {total_import}')  # Output: total energy imported / consumption in Wh | 1.8.0

total_export = tibber_pulse.fetch_total_energy_export()
print(f'Total Energy Export (Wh): {total_export}')  # Output: total energy exported to the grid in Wh | 2.8.0



# Fetch all data from your SML meter as obis values:
all_meter_data = tibber_pulse.fetch_all_meter_data()
print(f'All meter data: {all_meter_data}') # Output: all obis_values available from the meter