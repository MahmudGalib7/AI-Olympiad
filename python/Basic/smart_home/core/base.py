import abc
import datetime
import uuid
from typing import Dict, List, Optional

from smart_home.core.enums import DeviceStatus, DeviceType


class DeviceObserver(abc.ABC):
    """Abstract base class for observers that react to device events."""
    
    @abc.abstractmethod
    def update(self, device: "BaseDevice", event: str, data: dict):
        """Handle device updates.
        
        Args:
            device: The device that triggered the event
            event: The type of event that occurred
            data: Additional data related to the event
        """
        pass


class BaseDevice(abc.ABC):
    """Abstract base class for all smart home devices."""
    
    def __init__(self, name: str, room: str, device_id: str = None):
        """Initialize a new device.
        
        Args:
            name: The human-readable name of the device
            room: The room where the device is located
            device_id: Optional unique identifier (generated if not provided)
        """
        self.name = name
        self.room = room
        self.device_id = device_id or str(uuid.uuid4())
        self.status = DeviceStatus.OFFLINE
        self.last_updated = datetime.datetime.now()
        self._observers: List[DeviceObserver] = []
        
    def turn_on(self):
        """Turn the device on."""
        self.status = DeviceStatus.ONLINE
        self._update_timestamp()
        self._notify_observers("turned_on")
        
    def turn_off(self):
        """Turn the device off."""
        self.status = DeviceStatus.OFFLINE
        self._update_timestamp()
        self._notify_observers("turned_off")
        
    def _update_timestamp(self):
        """Update the last_updated timestamp to the current time."""
        self.last_updated = datetime.datetime.now()
        
    def add_observer(self, observer: DeviceObserver):
        """Add an observer to this device.
        
        Args:
            observer: The observer to add
        """
        if observer not in self._observers:
            self._observers.append(observer)
            
    def remove_observer(self, observer: DeviceObserver):
        """Remove an observer from this device.
        
        Args:
            observer: The observer to remove
        """
        if observer in self._observers:
            self._observers.remove(observer)
            
    def _notify_observers(self, event: str, data: dict = None):
        """Notify all observers of an event.
        
        Args:
            event: The type of event that occurred
            data: Additional data related to the event
        """
        for observer in self._observers:
            observer.update(self, event, data or {})
            
    @abc.abstractmethod
    def get_details(self) -> dict:
        """Return a dictionary of device details."""
        pass
    
    @abc.abstractmethod
    def get_type(self) -> DeviceType:
        """Return the type of device."""
        pass