import pytest
from unittest.mock import MagicMock

from smart_home.core.system import HomeAutomationSystem, SystemObserver
from smart_home.core.enums import DeviceType
from smart_home.devices.light import LightDevice
from smart_home.devices.thermostat import ThermostatDevice
from smart_home.automation.rules import Rule, RulesEngine


class TestHomeAutomationSystem:
    def test_initialization(self):
        system = HomeAutomationSystem("Test Home")
        assert system.name == "Test Home"
        assert len(system.devices) == 0
        assert len(system.rooms) == 0
        assert len(system.device_groups) == 0
        assert len(system.scenes) == 0
        assert len(system.event_log) == 0

    def test_add_remove_device(self):
        system = HomeAutomationSystem("Test Home")
        light = LightDevice("Test Light", "Living Room")
        
        device_id = system.add_device(light)
        assert device_id == light.device_id
        assert system.devices[device_id] == light
        assert "Living Room" in system.rooms
        
        # Test observer was added
        assert len(light._observers) == 1
        assert isinstance(light._observers[0], SystemObserver)
        
        # Test removal
        assert system.remove_device(device_id) is True
        assert device_id not in system.devices
        
        # Test removing non-existent device
        assert system.remove_device("nonexistent-id") is False

    def test_get_device(self):
        system = HomeAutomationSystem("Test Home")
        light = LightDevice("Test Light", "Living Room")
        device_id = system.add_device(light)
        
        # Test retrieving device
        retrieved_device = system.get_device(device_id)
        assert retrieved_device == light
        
        # Test retrieving non-existent device
        assert system.get_device("nonexistent-id") is None

    def test_get_devices_by_room(self):
        system = HomeAutomationSystem("Test Home")
        light1 = LightDevice("Light 1", "Living Room")
        light2 = LightDevice("Light 2", "Living Room")
        thermostat = ThermostatDevice("Thermostat", "Bedroom")
        
        system.add_device(light1)
        system.add_device(light2)
        system.add_device(thermostat)
        
        living_room_devices = system.get_devices_by_room("Living Room")
        assert len(living_room_devices) == 2
        assert light1 in living_room_devices
        assert light2 in living_room_devices
        
        bedroom_devices = system.get_devices_by_room("Bedroom")
        assert len(bedroom_devices) == 1
        assert thermostat in bedroom_devices
        
        # Test non-existent room
        kitchen_devices = system.get_devices_by_room("Kitchen")
        assert len(kitchen_devices) == 0

    def test_get_devices_by_type(self):
        system = HomeAutomationSystem("Test Home")
        light1 = LightDevice("Light 1", "Living Room")
        light2 = LightDevice("Light 2", "Bedroom")
        thermostat = ThermostatDevice("Thermostat", "Living Room")
        
        system.add_device(light1)
        system.add_device(light2)
        system.add_device(thermostat)
        
        lights = system.get_devices_by_type(DeviceType.LIGHT)
        assert len(lights) == 2
        assert light1 in lights
        assert light2 in lights
        
        thermostats = system.get_devices_by_type(DeviceType.THERMOSTAT)
        assert len(thermostats) == 1
        assert thermostat in thermostats

    def test_create_device_group(self):
        system = HomeAutomationSystem("Test Home")
        light1 = LightDevice("Light 1", "Living Room")
        light2 = LightDevice("Light 2", "Bedroom")
        
        light1_id = system.add_device(light1)
        light2_id = system.add_device(light2)
        
        # Create valid group
        assert system.create_device_group("All Lights", [light1_id, light2_id]) is True
        assert "All Lights" in system.device_groups
        assert len(system.device_groups["All Lights"]) == 2
        
        # Create group with some invalid IDs
        assert system.create_device_group("Some Lights", [light1_id, "invalid-id"]) is True
        assert "Some Lights" in system.device_groups
        assert len(system.device_groups["Some Lights"]) == 1
        
        # Create group with all invalid IDs
        assert system.create_device_group("No Lights", ["invalid-id1", "invalid-id2"]) is False
        assert "No Lights" not in system.device_groups

    def test_create_activate_scene(self):
        system = HomeAutomationSystem("Test Home")
        light = LightDevice("Test Light", "Living Room")
        thermostat = ThermostatDevice("Test Thermostat", "Living Room")
        
        light_id = system.add_device(light)
        thermostat_id = system.add_device(thermostat)
        
        # Create scene
        scene_data = {
            light_id: {
                "power": "on",
                "brightness": 75,
                "color": (255, 200, 150)
            },
            thermostat_id: {
                "power": "on",
                "target_temp": 22.5,
                "mode": "heat"
            }
        }
        
        assert system.create_scene("Evening Mode", scene_data) is True
        assert "Evening Mode" in system.scenes
        
        # Activate scene
        light.turn_off()  # Make sure devices are in a different state
        thermostat.turn_off()
        
        assert system.activate_scene("Evening Mode") is True
        
        # Verify devices were updated
        assert light.status == "ONLINE"
        assert light.brightness == 75
        assert light.color == (255, 200, 150)
        
        assert thermostat.status == "ONLINE"
        assert thermostat.target_temp == 22.5
        assert thermostat.mode == "heat"
        
        # Test activating non-existent scene
        assert system.activate_scene("Nonexistent Scene") is False

    def test_log_event(self):
        system = HomeAutomationSystem("Test Home")
        
        system.log_event("test_event", {"key": "value"})
        
        assert len(system.event_log) == 1
        event = system.event_log[0]
        assert event["type"] == "test_event"
        assert event["data"] == {"key": "value"}
        assert "timestamp" in event

    def test_get_system_status(self):
        system = HomeAutomationSystem("Test Home")
        light = LightDevice("Test Light", "Living Room")
        thermostat = ThermostatDevice("Test Thermostat", "Bedroom")
        
        system.add_device(light)
        system.add_device(thermostat)
        
        light.turn_on()
        
        system.create_device_group("Lights", [light.device_id])
        system.create_scene("Night Mode", {light.device_id: {"power": "off"}})
        
        status = system.get_system_status()
        
        assert status["name"] == "Test Home"
        assert status["device_count"] == 2
        assert set(status["rooms"]) == {"Living Room", "Bedroom"}
        assert status["groups"] == ["Lights"]
        assert status["scenes"] == ["Night Mode"]
        assert status["devices_by_status"]["online"] == 1
        assert status["devices_by_status"]["offline"] == 1
        assert status["devices_by_type"]["light"] == 1
        assert status["devices_by_type"]["thermostat"] == 1


class TestRulesEngine:
    def test_rules_engine(self):
        system = HomeAutomationSystem("Test Home")
        light = LightDevice("Test Light", "Living Room")
        system.add_device(light)
        
        engine = RulesEngine(system)
        
        # Create a simple rule
        condition_fn = MagicMock(return_value=True)  # Always trigger
        action_fn = MagicMock()
        
        rule = Rule("Test Rule", condition_fn, action_fn)
        
        # Add rule
        rule_id = engine.add_rule(rule)
        assert rule_id in engine.rules
        
        # Evaluate rules
        engine.evaluate_all_rules()
        
        # Check if rule was triggered
        condition_fn.assert_called_once_with(system)
        action_fn.assert_called_once_with(system)
        assert rule.last_triggered is not None
        
        # Test disabling rule
        engine.disable_rule(rule_id)
        assert engine.rules[rule_id].enabled is False
        
        # Reset mocks
        condition_fn.reset_mock()
        action_fn.reset_mock()
        
        # Evaluate rules again - should not trigger
        engine.evaluate_all_rules()
        condition_fn.assert_not_called()
        action_fn.assert_not_called()
        
        # Test enabling rule
        engine.enable_rule(rule_id)
        assert engine.rules[rule_id].enabled is True
        
        # Test removing rule
        assert engine.remove_rule(rule_id) is True
        assert rule_id not in engine.rules