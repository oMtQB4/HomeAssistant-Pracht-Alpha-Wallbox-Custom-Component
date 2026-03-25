# Pracht Alpha Wallbox Integration for Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg)](https://hacs.xyz)

Custom [Home Assistant](https://www.home-assistant.io/) integration for the **Pracht Alpha** electric-vehicle wallbox (EV charger).
It communicates with the wallbox over the local network via its built-in HTTP API and exposes charging status, power measurements, current limits, connector lock control, and LED configuration as native Home Assistant entities.

## Supported hardware

| Model | Charging points | Notes |
|---|---|---|
| **Pracht Alpha MONO** | 1 | Single connector |
| **Pracht Alpha DUO** | 2 | Dual connector — second-side entities are created automatically |

The integration uses **local polling** (every 15 seconds) and requires the wallbox password for authentication.
Devices on the network are discovered automatically via **Zeroconf** (`_http._tcp.local.`); you can also add a device manually.

## Entities

### Sensors

| Entity | Device class | Unit | Description |
|---|---|---|---|
| Power (per side) | `power` | W | Real-time charging power |
| Current (per side) | `current` | A | Real-time charging current (diagnostic) |
| Status (per side) | `enum` | — | Connector status: *disconnected*, *connected*, *charging*, *charging with cooling*, *error* |
| Energy (per side) | `energy` | Wh | Total energy delivered (total increasing) |
| Communication PCB temperature | `temperature` | °C | Internal PCB temperature (diagnostic) |
| Box temperature | `temperature` | °C | Enclosure temperature (diagnostic, hidden when unavailable) |
| Uptime | `timestamp` | — | Device boot time (diagnostic, disabled by default) |

### Binary sensors

| Entity | Device class | Description |
|---|---|---|
| Car connected (per side) | `plug` | Whether a vehicle is plugged in |
| Car charging (per side) | `battery_charging` | Whether the vehicle is actively charging |

### Switches

| Entity | Description |
|---|---|
| Lock (per side) | Lock / unlock the charging connector (only on hardware that supports locking) |

### Number

| Entity | Device class | Unit | Description |
|---|---|---|---|
| Max current total | `current` | A | Overall current limit for the wallbox |
| Max current (per side) | `current` | A | Per-connector current limit |

### Select

| Entity | Options | Description |
|---|---|---|
| LED mode | *on*, *on if required*, *off* | Controls the status LED behaviour (only on hardware with LED support) |

> **Note:** For the **Alpha DUO**, entities that are per-side are created for both sides. For the **Alpha MONO**, only single-side entities are created and labelled without a side suffix.

## Installation

### HACS (recommended)

1. Open **HACS** in Home Assistant.
2. Search for *Pracht Alpha* in HACS and install it.
3. Restart Home Assistant.

### HACS (custom repository)

1. Open **HACS** in Home Assistant.
2. Go to **Integrations** and select the three-dot menu → **Custom repositories**.
3. Add the repository URL `https://github.com/oMtQB4/HomeAssistant-Pracht-Alpha-Wallbox-Custom-Component` with category **Integration**.
4. Search for *Pracht Alpha* in HACS and install it.
5. Restart Home Assistant.

### Manual

Copy the `custom_components/pracht_alpha` folder into the `custom_components` directory of your Home Assistant configuration. Create the directory if it does not exist, then restart Home Assistant.

## Configuration

The integration is configured entirely through the Home Assistant UI — no YAML required.

### Automatic discovery

If your wallbox is on the same network, Home Assistant will discover it via Zeroconf and show a notification. Click the notification, enter the **wallbox password**, and confirm.

### Manual setup

1. Go to **Settings → Devices & Services → Add Integration**.
2. Search for **Pracht Alpha**.
3. Enter the **host** (IP address or hostname) of the wallbox.
4. Enter the **password** (the same password used for the wallbox web interface).
5. Click **Submit**.

### Re-authentication

If the password changes, the integration will prompt you to re-authenticate through the UI.