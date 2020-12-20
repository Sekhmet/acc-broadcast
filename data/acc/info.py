import ctypes
import mmap

from .graphic import SPageFileGraphic
from .physics import SPageFilePhysics
from .static import SPageFileStatic


class GameInfo:
    def __init__(self):
        self.graphic_map = mmap.mmap(0, ctypes.sizeof(
            SPageFileGraphic), "acpmf_graphics")
        self.physics_map = mmap.mmap(0, ctypes.sizeof(
            SPageFilePhysics), "acpmf_physics")
        self.static_map = mmap.mmap(0, ctypes.sizeof(
            SPageFileStatic), "acpmf_static")

        self.graphic = SPageFileGraphic.from_buffer(self.graphic_map)
        self.physics = SPageFilePhysics.from_buffer(self.physics_map)
        self.static = SPageFileStatic.from_buffer(self.static_map)

    def read(self):
        return {
            'speed': int(self.physics.speedKmh),
            'rpms': self.physics.rpms,
            'gear': self.physics.gear,
            'fuel': self.physics.fuel,
            'wheelsPressure': self.physics.wheelsPressure[:],
            'maxFuel': self.static.maxFuel,
            'fuelXLap': self.graphic.fuelXLap,
            'tyreCompund': self.graphic.tyreCompound,
        }

    def close(self):
        self.graphic_map.close()
        self.physics_map.close()
        self.static_map.close()

    def __del__(self):
        self.close()
