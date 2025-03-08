# 🏠 Smart Home Automation System

![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![GitHub stars](https://img.shields.io/github/stars/yourusername/smart-home-automation?style=social)

A powerful, extensible smart home automation framework built with modern Python and object-oriented principles.

---

## ✨ Features

- 💡 **Multi-Device Support:** Control lights, thermostats, security systems, and various sensors.
- 🎭 **Scenes:** Create and activate preset scenes like "Movie Night" or "Good Morning."
- 🤖 **Automation Rules:** Define custom rules with powerful conditions and actions.
- 🏘️ **Room Organization:** Group devices logically by room or area.
- 👥 **Device Groups:** Create custom device collections for batch control.
- 📊 **Event Logging:** Comprehensive event tracking for all system activities.
- 📱 **Extensible API:** Well-designed architecture ready for UI integration.
- ☁️ **State Persistence:** Save and restore system state between sessions.

---

## 🛠️ Architecture

The project follows a clean OOP design with design patterns like **Observer**, **Command**, and **Strategy**:

```
smart_home/
├── automation/    # Automation rules engine
├── core/          # Core system components and base classes
├── devices/       # Device implementations
├── utils/         # Helper utilities and tools
└── tests/         # Comprehensive test suite
```

---

## 🚀 Getting Started

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-home-automation.git
cd smart-home-automation

# Install dependencies first
pip install -r requirements.txt

# Install the package in editable mode
pip install -e .

```

### Quick Example

```python
from smart_home.core.system import HomeAutomationSystem
from smart_home.devices.light import LightDevice
from smart_home.devices.thermostat import ThermostatDevice

# Create your smart home system
home = HomeAutomationSystem("My Smart Home")

# Add some devices
living_light = LightDevice("Living Room Light", "Living Room")
kitchen_light = LightDevice("Kitchen Light", "Kitchen")
bedroom_thermostat = ThermostatDevice("Bedroom Thermostat", "Bedroom")

home.add_device(living_light)
home.add_device(kitchen_light)
home.add_device(bedroom_thermostat)

# Control your devices
living_light.turn_on()
living_light.set_brightness(75)
bedroom_thermostat.set_target_temperature(22.5)

# Create a scene for movie night
home.create_scene("Movie Night", {
    living_light.device_id: {
        "power": "on",
        "brightness": 30,
        "color": (255, 180, 100)
    },
    kitchen_light.device_id: {
        "power": "off"
    },
    bedroom_thermostat.device_id: {
        "target_temp": 23.0,
        "mode": "auto"
    }
})

# Activate the scene
home.activate_scene("Movie Night")
```

---

## 📋 Advanced Usage

### Creating Automation Rules

```python
from smart_home.automation.rules import Rule, RulesEngine
from smart_home.devices.sensor import SensorDevice

# Add a temperature sensor
temp_sensor = SensorDevice("Living Room Temp", "Living Room", "temperature")
home.add_device(temp_sensor)

# Create a rules engine
rules = RulesEngine(home)

# Define rule condition and action
def temperature_condition(system):
    sensor = next((d for d in system.get_devices_by_room("Living Room")
                   if d.get_type().value == "sensor" and d.sensor_type == "temperature"), None)
    if sensor and sensor.value is not None:
        return sensor.value < 19.0  # Temperature below 19°C
    return False

def heating_action(system):
    thermostat = next((d for d in system.get_devices_by_room("Living Room")
                      if d.get_type().value == "thermostat"), None)
    if thermostat:
        thermostat.turn_on()
        thermostat.set_mode("heat")
        thermostat.set_target_temperature(21.5)

# Add the rule to the engine
rules.add_rule(Rule(
    "Auto Heating",
    temperature_condition,
    heating_action
))

# Update the sensor (which may trigger the rule)
temp_sensor.update_reading(18.5, "C")

# Evaluate rules
rules.evaluate_all_rules()
```

---

## 🧪 Testing

The project comes with comprehensive tests:

```bash
# Run all tests
pytest

# Run a specific test file
pytest smart_home/tests/test_devices.py

# Test with coverage report
pytest --cov=smart_home
```

---

## 📊 Demo Dashboard

Our smart home system integrates perfectly with popular dashboard tools.

![Dashboard Example](https://via.placeholder.com/800x400)

---

## 🗺️ Roadmap

- [ ] Web-based control panel
- [ ] Mobile app integration
- [ ] Voice assistant compatibility
- [ ] Machine learning-based automation
- [ ] IoT device protocol integrations
- [ ] Weather service integration
- [ ] Energy usage analytics
- [ ] Multi-user access control

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository.
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add some amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgements

- Python Architectural Patterns
- *Design Patterns: Elements of Reusable Object-Oriented Software*
- Home Assistant for inspiration

---

<p align="center">Made with ❤️ by <a href="https://github.com/MahmudGalib7">Mahmud Galib</a></p>
<p align="center">
  <a href="https://x.com/MahmudGalib7">Twitter</a> •
  <a href="https://www.reddit.com/user/MahmudGalib7/">Reddit</a> •
</p>