from smart_home.core.base import BaseDevice
from smart_home.core.enums import DeviceType


class SensorDevice(BaseDevice):
    """Smart sensor device that can monitor various environmental factors."""
    
    def __init__(self, name: str, room: str, sensor_type: str, device_id: str = None):
        """Initialize a new sensor device.
        
        Args:
            name: The human-readable name of the device
            room: The room where the device is located
            sensor_type: The type of sensor (e.g., motion, temperature)
            device_id: Optional unique identifier (generated if not provided)
        """
        super().__init__(name, room, device_id)
        self.sensor_type = sensor_type  # motion, temperature, humidity, door, window
        self.value = None
        self.unit = ""
        
    def update_reading(self, value, unit: str = ""):
        """Update sensor reading.
        
        Args:
            value: The sensor reading value
            unit: Optional unit of measurement
        """
        self.value = value
        self.unit = unit
        self._update_timestamp()
        self._notify_observers("reading_updated", {"value": value, "unit": unit})
        
    def get_type(self) -> DeviceType:
        """Return the device type."""
        return DeviceType.SENSOR
        
    def get_details(self) -> dict:
        """Return a dictionary with the device's details."""
        return {
            "id": self.device_id,
            "name": self.name,
            "room": self.room,
            "type": self.get_type().value,
            "status": self.status.value,
            "sensor_type": self.sensor_type,
            "value": self.value,
            "unit": self.unit,
            "last_updated": self.last_updated.isoformat()
        }