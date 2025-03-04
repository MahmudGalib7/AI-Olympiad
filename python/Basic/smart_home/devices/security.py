from smart_home.core.base import BaseDevice
from smart_home.core.enums import DeviceType


class SecurityDevice(BaseDevice):
    """Smart security device with armed status and alarm functionality."""
    
    def __init__(self, name: str, room: str, device_id: str = None):
        """Initialize a new security device.
        
        Args:
            name: The human-readable name of the device
            room: The room where the device is located
            device_id: Optional unique identifier (generated if not provided)
        """
        super().__init__(name, room, device_id)
        self.armed = False
        self.alarm_triggered = False
        self.sensor_data = {}
        
    def arm(self):
        """Arm the security system."""
        self.armed = True
        self._update_timestamp()
        self._notify_observers("armed", {})
        
    def disarm(self):
        """Disarm the security system."""
        self.armed = False
        if self.alarm_triggered:
            self.reset_alarm()
        self._update_timestamp()
        self._notify_observers("disarmed", {})
        
    def trigger_alarm(self, reason: str):
        """Trigger the alarm.
        
        Args:
            reason: The reason for triggering the alarm
        """
        self.alarm_triggered = True
        self._update_timestamp()
        self._notify_observers("alarm_triggered", {"reason": reason})
        
    def reset_alarm(self):
        """Reset the alarm."""
        self.alarm_triggered = False
        self._update_timestamp()
        self._notify_observers("alarm_reset", {})
        
    def update_sensor_data(self, sensor_type: str, data: dict):
        """Update sensor data.
        
        Args:
            sensor_type: Type of sensor data to update
            data: The new sensor data
        """
        self.sensor_data[sensor_type] = data
        self._update_timestamp()
        self._notify_observers("sensor_updated", {"sensor": sensor_type, "data": data})
        
    def get_type(self) -> DeviceType:
        """Return the device type."""
        return DeviceType.SECURITY
        
    def get_details(self) -> dict:
        """Return a dictionary with the device's details."""
        return {
            "id": self.device_id,
            "name": self.name,
            "room": self.room,
            "type": self.get_type().value,
            "status": self.status.value,
            "armed": self.armed,
            "alarm_triggered": self.alarm_triggered,
            "sensor_data": self.sensor_data,
            "last_updated": self.last_updated.isoformat()
        }