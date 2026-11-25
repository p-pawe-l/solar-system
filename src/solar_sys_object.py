import numpy as np

from consts import G
class SolarSystemObject:
    def __init__(self,
                 name: str, 
                 mass: float,
                 radius: float, 
                 init_pos: np.ndarray, 
                 init_vel: np.ndarray) -> None:
        self.name: str = name 
        self.mass: float = mass
        self.radius: float = radius
        self.position: np.ndarray = init_pos
        self.velocity: np.ndarray = init_vel
        self.forces: np.ndarray | None = None

    def get_mass(self) -> float:
        return self.mass

    def get_radius(self) -> float:
        return self.radius

    def get_pos(self) -> np.ndarray:
        return self.position

    def get_vel(self) -> np.ndarray:
        return self.velocity

    def get_force(self) -> np.ndarray:
        return self.forces

    def calc_distance(self, other: "SolarSystemObject") -> float:
        qsums = np.sum((self.position - other.get_pos() ** 2))
        return np.sqrt(qsums)

    def total_gravity_force(self, other: "SolarSystemObject") -> float:
        return G * (self.mass * other.get_mass()) / (self.calc_distance(other) ** 2)

    def update_forces(self, other: "SolarSystemObject") -> None:
        total_gforce: float = self.total_gravity_force(other)
        distance_delta = other.get_pos() - self.position
        normalized_distance_delta = distance_delta / self.calc_distance(other)
        self.forces = total_gforce * normalized_distance_delta

    def update_position(self, dt: float) -> None:
        """
        lim dt -> 0
        v(t + dt) = v(t) + (F / m) * dt
        """
        self.position = self.position + self.velocity * dt

    def update_velocity(self, dt: float) -> None:
        """
        lim dt -> 0
        x(t + dt) = x(t) + v(t) * dt
        """
        acceleration= self.forces / self.mass 
        self.velocity = self.velocity + acceleration * dt