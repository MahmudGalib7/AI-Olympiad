from smart_home.core.base import BaseDevice
from smart_home.core.enums import DeviceType


class LightDevice(BaseDevice):
    """Smart light device with brightness and color control."""
    
    def __init__(self, name: str, room: str, device_id: str = None):
        """Initialize a new light device.
        
        Args:
            name: The human-readable name of the device
            room: The room where the device is located
            device_id: Optional unique identifier (generated if not provided)
        """
        super().__init__(name, room, device_id)
        self.brightness = 0  # 0-100
        self.color = (255, 255, 255)  # RGB
        
    def set_brightness(self, level: int):
        """Set brightness level (0-100).
        
        Args:
            level: Brightness level between 0 and 100
        """
        self.brightness = max(0, min(100, level))
        self._update_timestamp()
        self._notify_observers("brightness_changed", {"brightness": self.brightness})
        
    def set_color(self, r: int, g: int, b: int):
        """Set RGB color.
        
        Args:
            r: Red component (0-255)
            g: Green component (0-255)
            b: Blue component (0-255)
        """
        self.color = (
            max(0, min(255, r)),
            max(0, min(255, g)),
            max(0, min(255, b))
        )
        self._update_timestamp()
        self._notify_observers("color_changed", {"color": self.color})
        
    def get_type(self) -> DeviceType:
        """Return the device type."""
        return DeviceType.LIGHT
        
    def get_details(self) -> dict:
        """Return a dictionary with the device's details."""
        return {
            "id": self.device_id,
            "name": self.name,
            "room": self.room,
            "type": self.get_type().value,
            "status": self.status.value,
            "brightness": self.brightness,
            "color": self.color,
            "last_updated": self.last_updated.isoformat()
        }