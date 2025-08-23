import json
from typing import List, Dict, Any, Optional

from smart_home.core.system import HomeAutomationSystem
from smart_home.core.enums import DeviceType
from smart_home.devices.light import LightDevice
from smart_home.devices.thermostat import ThermostatDevice
from smart_home.devices.security import SecurityDevice
from smart_home.devices.sensor import SensorDevice


def save_system_state(system: HomeAutomationSystem, filepath: str) -> bool:
    """Save the current state of the home automation system to a file.
    
    Args:
        system: The home automation system to save
        filepath: The path to save the system state to
        
    Returns:
        True if the save was successful, False otherwise
    """
    try:
        # Build a serializable dictionary of the system state
        system_state = {
            "name": system.name,
            "rooms": list(system.rooms),
            "device_groups": system.device_groups,
            "scenes": system.scenes,
            "devices": []
        }
        
        # Save each device with its specific details
        for device_id, device in system.devices.items():
            details = device.get_details()
            system_state["devices"].append({
                "type": device.get_type().value,
                **details
            })
            
        # Write to file
        with open(filepath, 'w') as f:
            json.dump(system_state, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving system state: {e}")
        return False


def load_system_state(filepath: str) -> Optional[HomeAutomationSystem]:
    """Load a home automation system from a saved state file.
    
    Args:
        filepath: The path to load the system state from
        
    Returns:
        A new HomeAutomationSystem instance populated with the saved state,
        or None if the load failed
    """
    try:
        # Read the file
        with open(filepath, 'r') as f:
            system_state = json.load(f)
            
        # Create a new system
        system = HomeAutomationSystem(system_state["name"])
        
        # Create all the devices
        for device_data in system_state["devices"]:
            device_type = device_data["type"]
            device_id = device_data["id"]
            name = device_data["name"]
            room = device_data["room"]
            
            if device_type == DeviceType.LIGHT.value:
                device = LightDevice(name, room, device_id)
                device.brightness = device_data["brightness"]
                device.color = tuple(device_data["color"])
                
            elif device_type == DeviceType.THERMOSTAT.value:
                device = ThermostatDevice(name, room, device_id)
                device.current_temp = device_data["current_temp"]
                device.target_temp = device_data["target_temp"]
                device.humidity = device_data["humidity"]
                device.mode = device_data["mode"]
                
            elif device_type == DeviceType.SECURITY.value:
                device = SecurityDevice(name, room, device_id)
                device.armed = device_data["armed"]
                device.alarm_triggered = device_data["alarm_triggered"]
                device.sensor_data = device_data["sensor_data"]
                
            elif device_type == DeviceType.SENSOR.value:
                device = SensorDevice(name, room, device_data["sensor_type"], device_id)
                device.value = device_data["value"]
                device.unit = device_data["unit"]
                
            else:
                # Skip unknown device types
                continue
                
            # Add the device to the system
            system.add_device(device)
            
        # Restore device groups
        for group_name, device_ids in system_state["device_groups"].items():
            system.create_device_group(group_name, device_ids)
            
        # Restore scenes
        for scene_name, scene_data in system_state["scenes"].items():
            system.create_scene(scene_name, scene_data)
            
        return system
    except Exception as e:
        print(f"Error loading system state: {e}")
        return None