import numpy as np


class SolarSystemObject:
    def __init__(self, mass: float, init_pos: np.ndarray, init_vel: np.ndarray) -> None:
        self.mass: float = mass
        self.position: np.ndarray = init_pos
        self.velocity: np.ndarray = init_vel
        self.forces: np.ndarray | None = None

    def get_mass(self) -> float:
        return self.mass

    def get_pos(self) -> np.ndarray:
        return self.position

    def get_vel(self) -> np.ndarray:
        return self.velocity

    def get_force(self) -> np.ndarray:
        return self.forces

    def calc_distance(self, other: "SolarSystemObject") -> float:
        return np.sqrt((self.position - other.get_pos()) ** 2)

    def total_gravity_force(self, other: "SolarSystemObject") -> float:
        return G * (self.mass * other.get_mass()) / (self.calc_distance(other) ** 2)

    def update_forces(self, other: "SolarSystemObject") -> None:
        self.forces = self.total_gravity_force(other) * (
            (other.get_pos() - self.position) / self.calc_distance(other)
        )

    def update_position(self, dt: float) -> None:
        """
        dt -> 0
        v(t + dt) = v(t) + (F / m) * dt
        """
        self.position = self.position + self.velocity * dt

    def update_velocity(self, dt: float) -> None:
        """
        dt -> 0
        x(t + dt) = x(t) + v(t) * dt
        """
        self.velocity = self.velocity + (self.forces / self.mass) * dt