import enum


class DeviceStatus(enum.Enum):
    """Enum representing the possible statuses of a device."""
    ONLINE = "online"
    OFFLINE = "offline"
    ERROR = "error"
    MAINTENANCE = "maintenance"


class DeviceType(enum.Enum):
    """Enum representing the types of devices available in the system."""
    LIGHT = "light"
    THERMOSTAT = "thermostat"
    SECURITY = "security"
    ENTERTAINMENT = "entertainment"
    SENSOR = "sensor"