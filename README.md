
# Tibber Pulse Local Library

`tibber_local_lib` is a Python library designed to fetch and decode SML data from Tibber Pulse / your SML energy meter locally.

Key Features:
- Operates entirely locally without relying on the Tibber Cloud API.
- No data fetching limitations, even if your internet service provider (ISP) is down.
- Developed quickly, so it may require enhancements. However, it works flawlessly for me with polling rates greater than 3 seconds (this is a limitation of the SML energy meter and may vary depending on the manufacturer).

Contributions are welcome! Feel free to enhance and improve this library.

## Installation

```sh
pip install tibber_local_lib
```

## Setting Up Tibber Pulse for Local Access

### Initial Setup:

1. **Pre-requisites**:
   - Ensure your Tibber Pulse is already connected to Tibber and you can see data on your Tibber App.
   - Note the password on the socket of your Tibber bridge (visible when unplugged, beneath the QR code).
   - Plug in the bridge and wait for the LED to light up again.
   - Verify that you are still receiving data on your Tibber App.

### Enable Web Server:

1. **Configure the Bridge**:
   - Power off the bridge twice in 2-second intervals and wait for the LED to light up green.
   - Connect to the bridge's WiFi using the noted password and navigate to the following URL in your browser: `http://tibber-host.fritz.box/`. You need to replace `tibber-host.fritz.box` with the correct hostname or IP address.
   - Log in with the username `admin` and the noted password. You will be presented with a web dashboard.
   - Navigate to the `params` page and locate `webserver-force-enable`.
   - Set `webserver-force-enable` to `true` under the `params` tab, then save the changes and click `Store params to flash` at the bottom of the page.
   - Remember your nodeId: `http://tibber-host.fritz.box/nodes/` | default is 1
   - Power cycle the bridge.
   - Tibber will still be able to fetch data from the bridge, and now you also have local access 👍.

For more instructions with some pictures, visit [the78mole.de](https://the78mole.de/doing-the-undone-decoding-sml-or-hacking-the-tibber-raw-data).

## Usage | Examples:

```python
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
```
```
Device ID: 0a01454d4800009f3XXX
Current Power (W): 50
Total Energy Import (Wh): 3983179.1
Total Energy Export (Wh): 4814912.100000001
```

## Handling Different Meter Data Reports

Meters can vary significantly in the types of data they report. Some meters provide extensive details such as phase voltage, current, and more. To accommodate these variations and help you discover the specific data your meter can report, we have added a function called fetch_all_meter_data().

```python
from tibber_local_lib import SMLDecoder

password = "XXX-XXX" # 'XXXX-XXXX' from your QR-Code
tibber_pulse_host = "tibber-host.fritz.box" # change the hostname or replace it with your IP
nodeId = 1 # find your nodeId: http://tibber-host.fritz.box/nodes/ | default is 1
auth = ('admin', password)

tibber_pulse = SMLDecoder(tibber_pulse_host, auth, nodeId)

# Fetch all data from your SML meter as obis values:
all_meter_data = tibber_pulse.fetch_all_meter_data()
print(f'All meter data: {all_meter_data}') # Output: all obis_values available from the meter
```
```
All meter data: [<obis: 010060320101, value: EMH>, <obis: 0100600100ff, value: 0a01454d4800009f3XXX>, <obis: 0100010800ff, status: 1839364, val_time: 56769492, unit: 30, scaler: -1, value: 39831791>, <obis: 0100020800ff, val_time: 56769492, unit: 30, scaler: -1, value: 48149121>, <obis: 0100100700ff, unit: 27, scaler: 0, value: 50>]
```

This function retrieves and decodes the complete set of data from your meter, giving you a comprehensive view of all the available metrics. This enables you to explore and utilize the full capabilities of your specific meter.

## Contributing to Meter Data Decoding

We strive to continuously improve our library and accommodate the diverse range of meters available. If you discover new values or metrics reported by your meter that are not currently decoded by our functions, we welcome your contributions! Sharing these insights helps us enhance the library for everyone. Feel free to submit a pull request or open an issue on our GitHub repository with the details of the new values you have identified. Together, we can make this tool even more powerful and versatile.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.