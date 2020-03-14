from vpython import *


class AstronomicalObject(sphere):
    scale_factor = 200

    # radius is multiplied by a scaling factor of 200 so the astronomical objects are visible on the drawing

    def __init__(self, identifier: int, name: str, pos_x: float, pos_y: float, pos_z: float, radius: float, clr: str,
                 mass: float, velocity_x: float, velocity_y: float, velocity_z: float, trail: bool, **args):
        super().__init__(**args)
        self.identifier = identifier
        self.name = name
        self.pos = vec(pos_x, pos_y, pos_z)
        self.radius = radius * self.scale_factor
        self.color = getattr(color, clr)
        self.mass = mass
        self.velocity = vec(velocity_x, velocity_y, velocity_z)
        if trail:
            attach_trail(self, trail_type="curve", interval=10, retain=30)

    def move(self, astronomical_objects, dt):
        g = 6.67e-11
        # calculate the total force of gravity as result of all astronomical objects surrounding the object
        fz = vec(0, 0, 0)
        for ao in astronomical_objects:
            if astronomical_objects[ao].identifier != self.identifier:
                r = astronomical_objects[ao].pos - self.pos
                fz += g * self.mass * astronomical_objects[ao].mass * r / mag(r) ** 3

        # calculate the acceleration, note that this is a vector
        a = fz / self.mass
        # calculate the velocity at 1/2 dt
        self.velocity += a * dt
        self.pos += self.velocity * dt
