import pytest
import datetime
from unittest.mock import MagicMock

from smart_home.core.enums import DeviceStatus, DeviceType
from smart_home.devices.light import LightDevice
from smart_home.devices.thermostat import ThermostatDevice
from smart_home.devices.security import SecurityDevice
from smart_home.devices.sensor import SensorDevice


class TestLightDevice:
    def test_initialization(self):
        light = LightDevice("Test Light", "Living Room", "light-123")
        assert light.name == "Test Light"
        assert light.room == "Living Room"
        assert light.device_id == "light-123"
        assert light.status == DeviceStatus.OFFLINE
        assert light.brightness == 0
        assert light.color == (255, 255, 255)
        
    def test_turn_on_off(self):
        light = LightDevice("Test Light", "Living Room")
        
        light.turn_on()
        assert light.status == DeviceStatus.ONLINE
        
        light.turn_off()
        assert light.status == DeviceStatus.OFFLINE
        
    def test_set_brightness(self):
        light = LightDevice("Test Light", "Living Room")
        observer = MagicMock()
        light.add_observer(observer)
        
        light.set_brightness(75)
        assert light.brightness == 75
        observer.update.assert_called_once()
        
        # Test bounds
        light.set_brightness(150)
        assert light.brightness == 100
        
        light.set_brightness(-10)
        assert light.brightness == 0
        
    def test_set_color(self):
        light = LightDevice("Test Light", "Living Room")
        observer = MagicMock()
        light.add_observer(observer)
        
        light.set_color(100, 150, 200)
        assert light.color == (100, 150, 200)
        observer.update.assert_called_once()
        
        # Test bounds
        light.set_color(300, -50, 1000)
        assert light.color == (255, 0, 255)
        
    def test_get_type(self):
        light = LightDevice("Test Light", "Living Room")
        assert light.get_type() == DeviceType.LIGHT
        
    def test_get_details(self):
        light = LightDevice("Test Light", "Living Room", "light-123")
        light.set_brightness(50)
        light.set_color(100, 100, 100)
        
        details = light.get_details()
        assert details["id"] == "light-123"
        assert details["name"] == "Test Light"
        assert details["room"] == "Living Room"
        assert details["type"] == "light"
        assert details["brightness"] == 50
        assert details["color"] == (100, 100, 100)


class TestThermostatDevice:
    def test_initialization(self):
        thermo = ThermostatDevice("Test Thermostat", "Bedroom", "thermo-123")
        assert thermo.name == "Test Thermostat"
        assert thermo.room == "Bedroom"
        assert thermo.device_id == "thermo-123"
        assert thermo.status == DeviceStatus.OFFLINE
        assert thermo.current_temp == 21.0
        assert thermo.target_temp == 21.0
        assert thermo.humidity == 50.0
        assert thermo.mode == "off"
        
    def test_set_target_temperature(self):
        thermo = ThermostatDevice("Test Thermostat", "Bedroom")
        observer = MagicMock()
        thermo.add_observer(observer)
        
        thermo.set_target_temperature(23.5)
        assert thermo.target_temp == 23.5
        observer.update.assert_called_once()
        
    def test_set_mode(self):
        thermo = ThermostatDevice("Test Thermostat", "Bedroom")
        observer = MagicMock()
        thermo.add_observer(observer)
        
        thermo.set_mode("heat")
        assert thermo.mode == "heat"
        observer.update.assert_called_once()
        
        # Invalid mode
        thermo.set_mode("invalid_mode")
        assert thermo.mode == "heat"  # Should not change
        
    def test_update_current_reading(self):
        thermo = ThermostatDevice("Test Thermostat", "Bedroom")
        observer = MagicMock()
        thermo.add_observer(observer)
        
        thermo.update_current_reading(22.5, 45.0)
        assert thermo.current_temp == 22.5
        assert thermo.humidity == 45.0
        observer.update.assert_called_once()
        
    def test_get_type(self):
        thermo = ThermostatDevice("Test Thermostat", "Bedroom")
        assert thermo.get_type() == DeviceType.THERMOSTAT


class TestSecurityDevice:
    def test_initialization(self):
        security = SecurityDevice("Test Security", "Entrance", "sec-123")
        assert security.name == "Test Security"
        assert security.room == "Entrance"
        assert security.device_id == "sec-123"
        assert security.status == DeviceStatus.OFFLINE
        assert security.armed is False
        assert security.alarm_triggered is False
        
    def test_arm_disarm(self):
        security = SecurityDevice("Test Security", "Entrance")
        observer = MagicMock()
        security.add_observer(observer)
        
        security.arm()
        assert security.armed is True
        observer.update.assert_called_once()
        
        security.disarm()
        assert security.armed is False
        
    def test_trigger_reset_alarm(self):
        security = SecurityDevice("Test Security", "Entrance")
        observer = MagicMock()
        security.add_observer(observer)
        
        security.trigger_alarm("Motion detected")
        assert security.alarm_triggered is True
        observer.update.assert_called_once()
        
        security.reset_alarm()
        assert security.alarm_triggered is False
        
    def test_update_sensor_data(self):
        security = SecurityDevice("Test Security", "Entrance")
        observer = MagicMock()
        security.add_observer(observer)
        
        security.update_sensor_data("motion", {"detected": True, "location": "front"})
        assert security.sensor_data["motion"] == {"detected": True, "location": "front"}
        observer.update.assert_called_once()
        
    def test_get_type(self):
        security = SecurityDevice("Test Security", "Entrance")
        assert security.get_type() == DeviceType.SECURITY


class TestSensorDevice:
    def test_initialization(self):
        sensor = SensorDevice("Test Sensor", "Kitchen", "temperature", "sensor-123")
        assert sensor.name == "Test Sensor"
        assert sensor.room == "Kitchen"
        assert sensor.device_id == "sensor-123"
        assert sensor.status == DeviceStatus.OFFLINE
        assert sensor.sensor_type == "temperature"
        assert sensor.value is None
        assert sensor.unit == ""
        
    def test_update_reading(self):
        sensor = SensorDevice("Test Sensor", "Kitchen", "temperature")
        observer = MagicMock()
        sensor.add_observer(observer)
        
        sensor.update_reading(22.5, "C")
        assert sensor.value == 22.5
        assert sensor.unit == "C"
        observer.update.assert_called_once()
        
    def test_get_type(self):
        sensor = SensorDevice("Test Sensor", "Kitchen", "temperature")
        assert sensor.get_type() == DeviceType.SENSOR