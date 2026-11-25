import numpy as np 

from consts import *
from solar_sys_object import SolarSystemObject

def calc_init_pos(perihelion: float, inclination: float) -> np.ndarray:
    radians: float = np.pi * inclination / 180.0
    return np.array([
        np.cos(radians) * perihelion, 0, np.sin(radians) * perihelion
    ])
    
sun = SolarSystemObject(
    name="Sun",
    mass=SUN_MASS,
    radius=SUN_RADIUS, 
    init_pos=np.array([0.0, 0.0, 0.0]),
    init_vel=np.array([0.0, 0.0, 0.0])
)

mercury = SolarSystemObject(
    name="Mercury",
    mass=MERCURY_MASS,
    radius=MERCURY_RADIUS,
    init_pos=calc_init_pos(MERCURY_PERIHELION, MERCURY_INCLINATION),
    init_vel=np.array([0, MERCURY_MAX_ORBITAL_VEL, 0]),
)

venus = SolarSystemObject(
    name="Venus",
    mass=VENUS_MASS,
    radius=VENUS_RADIUS,
    init_pos=calc_init_pos(VENUS_PERIHELION, VENUS_INCLINATION),
    init_vel=np.array([0, VENUS_MAX_ORBITAL_VEL, 0])
)

earth = SolarSystemObject(
    name="Earth",
    mass=EARTH_MASS,
    radius=EARTH_RADIUS,
    init_pos=calc_init_pos(EARTH_PERIHELION, EARTH_INCLINATION),
    init_vel=np.array([0, EARTH_MAX_ORBITAL_VEL, 0])
)

mars = SolarSystemObject(
    name="Mars",
    mass=MARS_MASS,
    radius=MARS_RADIUS,
    init_pos=calc_init_pos(MARS_PERIHELION, MARS_INCLINATION),
    init_vel=np.array([0, MARS_MAX_ORBITAL_VEL, 0])
)

jupiter = SolarSystemObject(
    name="Jupiter",
    mass=JUPITER_MASS,
    radius=JUPITER_RADIUS,
    init_pos=calc_init_pos(JUPITER_PERIHELION, JUPITER_INCLINATION),
    init_vel=np.array([0, JUPITER_MAX_ORBITAL_VEL, 0])
)

saturn = SolarSystemObject(
    name="Saturn",
    mass=SATURN_MASS,
    radius=SATURN_RADIUS,
    init_pos=calc_init_pos(SATURN_PERIHELION, SATURN_INCLINATION),
    init_vel=np.array([0, SATURN_MAX_ORBITAL_VEL, 0])
)

uranus = SolarSystemObject(
    name="Uranus",
    mass=URANUS_MASS,
    radius=URANUS_RADIUS,
    init_pos=calc_init_pos(URANUS_PERIHELION, URANUS_INCLINATION),
    init_vel=np.array([0, URANUS_MAX_ORBITAL_VEL, 0])
)

neptune = SolarSystemObject(
    name="Neptune",
    mass=NEPTUNE_MASS,
    radius=NEPTUNE_RADIUS,
    init_pos=calc_init_pos(NEPTUNE_PERIHELION, NEPTUNE_INCLINATION),
    init_vel=np.array([0, NEPTUNE_MAX_ORBITAL_VEL, 0])
)
