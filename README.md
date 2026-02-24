# Pracht Alpha Wallbox Integration for Home Assistant

## Installation

Copy the folder `pracht_alpha` into the folder `custom_components` in your HomeAssistant config folder.
If the folder `custom_components` does not exist, create it.

For instance, the structure may look like this:

```
# ls ./homeassistant/config/custom_components/pracht_alpha

api.py              config_flow.py  entity.py    __init__.py    __pycache__  strings.json
binary_sensor.py    const.py        icon@2x.png  manifest.json  select.py    switch.py
brands_fallback.js  coordinator.py  icon.png     number.py      sensor.py    translations
```