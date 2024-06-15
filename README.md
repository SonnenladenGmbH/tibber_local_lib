
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
   - Connect to the bridge's WiFi using the noted password and navigate to the following URL in your browser: `http://tibber_bridge/data.json?node_id=1`. You may need to replace `tibber_bridge` with the correct hostname or IP address.
   - Log in with the username `admin` and the noted password. You will be presented with a web dashboard.
   - Navigate to the `params` page and locate `webserver-force-enable`.
   - Set `webserver-force-enable` to `true` under the `params` tab, then save the changes and click `Store params to flash` at the bottom of the page.
   - Power cycle the bridge.
   - Tibber will still be able to fetch data from the bridge, and now you also have local access 👍.

For more instructions with some pictures, visit [the78mole.de](https://the78mole.de/doing-the-undone-decoding-sml-or-hacking-the-tibber-raw-data).

## Usage

```python
from tibber_local_lib import SMLDecoder

password = "your_password" # 'XXXX-XXXX' from your QR-Code
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
```
```
Device ID: 0901454d41200099e91f
Current Power (W): 1530.2
Total Consumption (Wh): 19311451.7
Tariff 1 Consumption (Wh): 19311451.7
Tariff 2 Consumption (Wh): 0.0

```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.