"""
Physical data of the Sun and the planets of the Solar System.

Source: NASA Planetary Fact Sheets (https://nssdc.gsfc.nasa.gov/planetary/factsheet/)
All values in SI units: kg, m, m/s, s. Angles in degrees.

Per planet:
    MASS                 [kg]
    RADIUS               mean radius [m]
    SEMI_MAJOR_AXIS      [m]
    PERIHELION           closest distance to the Sun [m]
    APHELION             farthest distance from the Sun [m]
    ECCENTRICITY         [-]
    INCLINATION          orbital inclination to the ecliptic [deg]
    ORBITAL_PERIOD       sidereal orbital period [s]
    MEAN_ORBITAL_VEL     [m/s]
    MAX_ORBITAL_VEL      velocity at perihelion [m/s]
    MIN_ORBITAL_VEL      velocity at aphelion [m/s]
"""

G: float = 6.67430e-11  
AU: float = 1.495978707e11 
DAY: float = 24 * 60 * 60 # Day in seconds
YEAR: float = 365.25 * DAY # Year in seconds


# --- Sun ---
SUN_MASS: float = 1.98847e30
SUN_RADIUS: float = 6.957e8


# --- Mercury ---
MERCURY_MASS: float = 3.3011e23
MERCURY_RADIUS: float = 2.4397e6
MERCURY_SEMI_MAJOR_AXIS: float = 57.909e9
MERCURY_PERIHELION: float = 46.000e9
MERCURY_APHELION: float = 69.818e9
MERCURY_ECCENTRICITY: float = 0.2056
MERCURY_INCLINATION: float = 7.005
MERCURY_ORBITAL_PERIOD: float = 87.969 * DAY
MERCURY_MEAN_ORBITAL_VEL: float = 47.36e3
MERCURY_MAX_ORBITAL_VEL: float = 58.98e3
MERCURY_MIN_ORBITAL_VEL: float = 38.86e3


# --- Venus ---
VENUS_MASS: float = 4.8675e24
VENUS_RADIUS: float = 6.0518e6
VENUS_SEMI_MAJOR_AXIS: float = 108.210e9
VENUS_PERIHELION: float = 107.480e9
VENUS_APHELION: float = 108.941e9
VENUS_ECCENTRICITY: float = 0.0068
VENUS_INCLINATION: float = 3.395
VENUS_ORBITAL_PERIOD: float = 224.701 * DAY
VENUS_MEAN_ORBITAL_VEL: float = 35.02e3
VENUS_MAX_ORBITAL_VEL: float = 35.26e3
VENUS_MIN_ORBITAL_VEL: float = 34.78e3


# --- Earth ---
EARTH_MASS: float = 5.9722e24
EARTH_RADIUS: float = 6.3710e6
EARTH_SEMI_MAJOR_AXIS: float = 149.598e9
EARTH_PERIHELION: float = 147.095e9
EARTH_APHELION: float = 152.100e9
EARTH_ECCENTRICITY: float = 0.0167
EARTH_INCLINATION: float = 0.0  # the ecliptic is defined by Earth's orbit
EARTH_ORBITAL_PERIOD: float = 365.256 * DAY
EARTH_MEAN_ORBITAL_VEL: float = 29.78e3
EARTH_MAX_ORBITAL_VEL: float = 30.29e3
EARTH_MIN_ORBITAL_VEL: float = 29.29e3


# --- Mars ---
MARS_MASS: float = 6.4171e23
MARS_RADIUS: float = 3.3895e6
MARS_SEMI_MAJOR_AXIS: float = 227.956e9
MARS_PERIHELION: float = 206.650e9
MARS_APHELION: float = 249.261e9
MARS_ECCENTRICITY: float = 0.0935
MARS_INCLINATION: float = 1.848
MARS_ORBITAL_PERIOD: float = 686.980 * DAY
MARS_MEAN_ORBITAL_VEL: float = 24.07e3
MARS_MAX_ORBITAL_VEL: float = 26.50e3
MARS_MIN_ORBITAL_VEL: float = 21.97e3


# --- Jupiter ---
JUPITER_MASS: float = 1.89819e27
JUPITER_RADIUS: float = 6.9911e7
JUPITER_SEMI_MAJOR_AXIS: float = 778.479e9
JUPITER_PERIHELION: float = 740.595e9
JUPITER_APHELION: float = 816.363e9
JUPITER_ECCENTRICITY: float = 0.0487
JUPITER_INCLINATION: float = 1.304
JUPITER_ORBITAL_PERIOD: float = 4332.589 * DAY
JUPITER_MEAN_ORBITAL_VEL: float = 13.06e3
JUPITER_MAX_ORBITAL_VEL: float = 13.72e3
JUPITER_MIN_ORBITAL_VEL: float = 12.44e3


# --- Saturn ---
SATURN_MASS: float = 5.6834e26
SATURN_RADIUS: float = 5.8232e7
SATURN_SEMI_MAJOR_AXIS: float = 1432.041e9
SATURN_PERIHELION: float = 1357.554e9
SATURN_APHELION: float = 1506.527e9
SATURN_ECCENTRICITY: float = 0.0520
SATURN_INCLINATION: float = 2.485
SATURN_ORBITAL_PERIOD: float = 10759.22 * DAY
SATURN_MEAN_ORBITAL_VEL: float = 9.68e3
SATURN_MAX_ORBITAL_VEL: float = 10.18e3
SATURN_MIN_ORBITAL_VEL: float = 9.09e3


# --- Uranus ---
URANUS_MASS: float = 8.6813e25
URANUS_RADIUS: float = 2.5362e7
URANUS_SEMI_MAJOR_AXIS: float = 2867.043e9
URANUS_PERIHELION: float = 2732.696e9
URANUS_APHELION: float = 3001.390e9
URANUS_ECCENTRICITY: float = 0.0469
URANUS_INCLINATION: float = 0.770
URANUS_ORBITAL_PERIOD: float = 30685.4 * DAY
URANUS_MEAN_ORBITAL_VEL: float = 6.80e3
URANUS_MAX_ORBITAL_VEL: float = 7.11e3
URANUS_MIN_ORBITAL_VEL: float = 6.49e3


# --- Neptune ---
NEPTUNE_MASS: float = 1.02413e26
NEPTUNE_RADIUS: float = 2.4622e7
NEPTUNE_SEMI_MAJOR_AXIS: float = 4514.953e9
NEPTUNE_PERIHELION: float = 4471.050e9
NEPTUNE_APHELION: float = 4558.857e9
NEPTUNE_ECCENTRICITY: float = 0.0097
NEPTUNE_INCLINATION: float = 1.770
NEPTUNE_ORBITAL_PERIOD: float = 60189.0 * DAY
NEPTUNE_MEAN_ORBITAL_VEL: float = 5.43e3
NEPTUNE_MAX_ORBITAL_VEL: float = 5.50e3
NEPTUNE_MIN_ORBITAL_VEL: float = 5.37e3
