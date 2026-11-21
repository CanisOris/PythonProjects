class BaseRobot:
    """Base class representing a next-generation autonomous robot."""

    def __init__(self, unit_id: str, power_core: str, firmware_version: str) -> None:
        self.unit_id: str = unit_id
        self.power_core: str = power_core
        self.firmware_version: str = firmware_version


class HumanoidBot(BaseRobot):
    """Child class representing a bipedal humanoid robot with specialized parts."""
    # self (like c#'s this) ties the instance to its attributes and methods. 
    def __init__(
        self,
        unit_id: str,
        power_core: str,
        firmware_version: str,
        actuator_type: str,
        tactile_skin_sensors: int,
    ) -> None:
        super().__init__(
            unit_id=unit_id,
            power_core=power_core,
            firmware_version=firmware_version,
        )
        # Child-specific attributes for future humanoid hardware
        self.actuator_type: str = actuator_type
        self.tactile_skin_sensors: int = tactile_skin_sensors


class FieldDroneBot(BaseRobot):
    """Child class representing a rugged terrain/field robot with specialized parts."""

    def __init__(
        self,
        unit_id: str,
        power_core: str,
        firmware_version: str,
        lidar_channels: int,
        chassis_alloy: str,
    ) -> None:
        super().__init__(
            unit_id=unit_id,
            power_core=power_core,
            firmware_version=firmware_version,
        )
        # Child-specific attributes for future field-deployment hardware
        self.lidar_channels: int = lidar_channels
        self.chassis_alloy: str = chassis_alloy


biped = HumanoidBot(
    unit_id="HB-09",
    power_core="Solid-State Lithium-Sulfur",
    firmware_version="v4.2.0",
    actuator_type="Quasi-Direct-Drive Synthetic Tendon",
    tactile_skin_sensors=4096,
)

rover = FieldDroneBot(
    unit_id="FD-24",
    power_core="Compact Radioisotope Cell",
    firmware_version="v3.8.1",
    lidar_channels=128,
    chassis_alloy="Titanium-Aluminide Lattice",
)

print(biped.unit_id, biped.actuator_type, biped.tactile_skin_sensors)
print(rover.unit_id, rover.lidar_channels, rover.chassis_alloy)