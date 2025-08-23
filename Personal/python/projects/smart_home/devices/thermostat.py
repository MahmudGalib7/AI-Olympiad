from smart_home.core.base import BaseDevice
from smart_home.core.enums import DeviceType


class ThermostatDevice(BaseDevice):
    """Smart thermostat device with temperature and mode control."""
    
    def __init__(self, name: str, room: str, device_id: str = None):
        """Initialize a new thermostat device.
        
        Args:
            name: The human-readable name of the device
            room: The room where the device is located
            device_id: Optional unique identifier (generated if not provided)
        """
        super().__init__(name, room, device_id)
        self.current_temp = 21.0  # Celsius
        self.target_temp = 21.0
        self.humidity = 50.0  # Percentage
        self.mode = "off"  # off, heat, cool, auto
        
    def set_target_temperature(self, temp: float):
        """Set target temperature in Celsius.
        
        Args:
            temp: Target temperature in Celsius
        """
        self.target_temp = temp
        self._update_timestamp()
        self._notify_observers("target_temp_changed", {"target_temp": self.target_temp})
        
    def set_mode(self, mode: str):
        """Set thermostat mode.
        
        Args:
            mode: One of 'off', 'heat', 'cool', or 'auto'
        """
        if mode in ["off", "heat", "cool", "auto"]:
            self.mode = mode
            self._update_timestamp()
            self._notify_observers("mode_changed", {"mode": self.mode})
            
    def update_current_reading(self, temp: float, humidity: float):
        """Update current temperature and humidity readings.
        
        Args:
            temp: Current temperature in Celsius
            humidity: Current humidity percentage
        """
        self.current_temp = temp
        self.humidity = humidity
        self._update_timestamp()
        self._notify_observers("readings_updated", {
            "current_temp": self.current_temp,
            "humidity": self.humidity
        })
        
    def get_type(self) -> DeviceType:
        """Return the device type."""
        return DeviceType.THERMOSTAT
        
    def get_details(self) -> dict:
        """Return a dictionary with the device's details."""
        return {
            "id": self.device_id,
            "name": self.name,
            "room": self.room,
            "type": self.get_type().value,
            "status": self.status.value,
            "current_temp": self.current_temp,
            "target_temp": self.target_temp,
            "humidity": self.humidity,
            "mode": self.mode,
            "last_updated": self.last_updated.isoformat()
        }