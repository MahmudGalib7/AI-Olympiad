import datetime
from typing import Dict, List, Optional, Set

from smart_home.core.base import BaseDevice, DeviceObserver
from smart_home.core.enums import DeviceStatus, DeviceType


class SystemObserver(DeviceObserver):
    """Observer that logs all device events into the home system."""
    
    def __init__(self, home_system: "HomeAutomationSystem"):
        """Initialize with a reference to the home automation system.
        
        Args:
            home_system: The home automation system that will log events
        """
        self.home_system = home_system
        
    def update(self, device: BaseDevice, event: str, data: dict):
        """Handle device updates by logging them in the system.
        
        Args:
            device: The device that triggered the event
            event: The type of event that occurred
            data: Additional data related to the event
        """
        self.home_system.log_event(f"device_{event}", {
            "device_id": device.device_id,
            "device_name": device.name,
            "room": device.room,
            **data
        })


class HomeAutomationSystem:
    """Central system that manages all smart home devices and features."""
    
    def __init__(self, name: str):
        """Initialize a new home automation system.
        
        Args:
            name: The name of this home automation system
        """
        self.name = name
        self.devices: Dict[str, BaseDevice] = {}
        self.rooms: Set[str] = set()
        self.device_groups: Dict[str, List[str]] = {}
        self.scenes: Dict[str, Dict[str, dict]] = {}
        self.event_log = []
        
    def add_device(self, device: BaseDevice) -> str:
        """Add a device to the system.
        
        Args:
            device: The device to add
            
        Returns:
            The device ID
        """
        self.devices[device.device_id] = device
        self.rooms.add(device.room)
        device.add_observer(SystemObserver(self))
        return device.device_id
        
    def remove_device(self, device_id: str) -> bool:
        """Remove a device from the system.
        
        Args:
            device_id: The ID of the device to remove
            
        Returns:
            True if the device was found and removed, False otherwise
        """
        if device_id in self.devices:
            # Remove from any groups
            for group in self.device_groups.values():
                if device_id in group:
                    group.remove(device_id)
            # Remove device
            del self.devices[device_id]
            return True
        return False
        
    def get_device(self, device_id: str) -> Optional[BaseDevice]:
        """Get a device by ID.
        
        Args:
            device_id: The ID of the device to retrieve
            
        Returns:
            The requested device, or None if not found
        """
        return self.devices.get(device_id)
        
    def get_devices_by_room(self, room: str) -> List[BaseDevice]:
        """Get all devices in a specific room.
        
        Args:
            room: The room to filter devices by
            
        Returns:
            A list of devices in the specified room
        """
        return [d for d in self.devices.values() if d.room == room]
        
    def get_devices_by_type(self, device_type: DeviceType) -> List[BaseDevice]:
        """Get all devices of a specific type.
        
        Args:
            device_type: The device type to filter by
            
        Returns:
            A list of devices of the specified type
        """
        return [d for d in self.devices.values() if d.get_type() == device_type]
        
    def create_device_group(self, name: str, device_ids: List[str]) -> bool:
        """Create a group of devices.
        
        Args:
            name: The name of the group
            device_ids: List of device IDs to include in the group
            
        Returns:
            True if at least one valid device was added to the group
        """
        valid_ids = [d_id for d_id in device_ids if d_id in self.devices]
        if valid_ids:
            self.device_groups[name] = valid_ids
            return True
        return False
        
    def create_scene(self, name: str, device_states: Dict[str, dict]) -> bool:
        """Create a scene (preset device states).
        
        Args:
            name: The name of the scene
            device_states: Dictionary mapping device IDs to their target states
            
        Returns:
            True if at least one valid device state was added to the scene
        """
        valid_states = {}
        for d_id, state in device_states.items():
            if d_id in self.devices:
                valid_states[d_id] = state
        
        if valid_states:
            self.scenes[name] = valid_states
            return True
        return False
        
    def activate_scene(self, scene_name: str) -> bool:
        """Activate a scene.
        
        Args:
            scene_name: The name of the scene to activate
            
        Returns:
            True if the scene was found and activated, False otherwise
        """
        if scene_name not in self.scenes:
            return False
            
        for d_id, state in self.scenes[scene_name].items():
            device = self.devices.get(d_id)
            if not device:
                continue
                
            # Apply states based on device type
            if device.get_type() == DeviceType.LIGHT:
                if "power" in state:
                    if state["power"] == "on":
                        device.turn_on()
                    elif state["power"] == "off":
                        device.turn_off()
                    
                if hasattr(device, "set_brightness") and "brightness" in state:
                    device.set_brightness(state["brightness"])
                    
                if hasattr(device, "set_color") and "color" in state:
                    device.set_color(*state["color"])
                    
            elif device.get_type() == DeviceType.THERMOSTAT:
                if "power" in state:
                    if state["power"] == "on":
                        device.turn_on()
                    elif state["power"] == "off":
                        device.turn_off()
                    
                if hasattr(device, "set_target_temperature") and "target_temp" in state:
                    device.set_target_temperature(state["target_temp"])
                    
                if hasattr(device, "set_mode") and "mode" in state:
                    device.set_mode(state["mode"])
                    
            elif device.get_type() == DeviceType.SECURITY:
                if "armed" in state and hasattr(device, "arm") and hasattr(device, "disarm"):
                    if state["armed"]:
                        device.arm()
                    else:
                        device.disarm()
        
        self.log_event("scene_activated", {"scene_name": scene_name})
        return True
        
    def log_event(self, event_type: str, data: dict):
        """Log system events.
        
        Args:
            event_type: The type of event
            data: Additional event data
        """
        event = {
            "timestamp": datetime.datetime.now().isoformat(),
            "type": event_type,
            "data": data
        }
        self.event_log.append(event)
        
    def get_system_status(self) -> dict:
        """Get the overall system status.
        
        Returns:
            A dictionary containing system status information
        """
        return {
            "name": self.name,
            "device_count": len(self.devices),
            "rooms": list(self.rooms),
            "groups": list(self.device_groups.keys()),
            "scenes": list(self.scenes.keys()),
            "devices_by_status": {
                status.value: len([d for d in self.devices.values() if d.status == status])
                for status in DeviceStatus
            },
            "devices_by_type": {
                dev_type.value: len([d for d in self.devices.values() if d.get_type() == dev_type])
                for dev_type in DeviceType
            }
        }