from astronomical_object_class import AstronomicalObject


class Simulation:
    def __init__(self, astronomical_object_data, hr):
        astronomical_objects = {}
        for ao in astronomical_object_data:
            if ao[12]:
                astronomical_objects[ao[1]] = AstronomicalObject(
                    identifier=ao[0],
                    name=ao[1],
                    pos_x=ao[2],
                    pos_y=ao[3],
                    pos_z=ao[4],
                    radius=ao[5],
                    clr=ao[6],
                    mass=ao[7],
                    velocity_x=ao[8],
                    velocity_y=ao[9],
                    velocity_z=ao[10],
                    trail=ao[11]
                )

        # half an hour
        dt = 60 * 60 * hr
        t = 0

        # 30 years simulation
        while True:
            for astronomical_object in astronomical_objects:
                astronomical_objects[astronomical_object].move(astronomical_objects, dt)
            t += dt

#
# sun = AstronomicalObject(
#     name='sun',
#     pos_x=0,
#     pos_y=0,
#     pos_z=0,
#     radius=695510e3,
#     clr='yellow',
#     mass=1.989e30,
#     velocity_x=0,
#     velocity_y=0,
#     velocity_z=0,
#     trail=False
# )
#
# jupiter = AstronomicalObject(
#     name='jupiter',
#     pos_x=778.5e9,
#     pos_y=0,
#     pos_z=0,
#     radius=69911e3,
#     clr='orange',
#     mass=1.898e27,
#     velocity_x=0,
#     velocity_y=13e3,
#     velocity_z=0,
#     trail=True
# )
#
# trojans = AstronomicalObject(
#     name='trojans',
#     pos_x=0.5*(sun.pos.x+jupiter.pos.x),
#     pos_y=0.5*(sun.pos.x+jupiter.pos.x)*tan(pi/3),
#     pos_z=0,
#     radius=69911e3*0.7,
#     clr='magenta',
#     mass=jupiter.mass / 100,
#     velocity_x=13e3 * sin(-pi/3),
#     velocity_y=13e3 * cos(-pi/3),
#     velocity_z=0,
#     trail=True
# )
#
# greeks = AstronomicalObject(
#     name='greeks',
#     pos_x=0.5*(sun.pos.x+jupiter.pos.x),
#     pos_y=-0.5*(sun.pos.x+jupiter.pos.x)*tan(pi/3),
#     pos_z=0,
#     radius=69911e3*0.7,
#     clr='cyan',
#     mass=jupiter.mass / 100,
#     velocity_x=13e3 * sin(pi/3),
#     velocity_y=13e3 * cos(pi/3),
#     velocity_z=0,
#     trail=True
# )
#
# swirling_trojan = AstronomicalObject(
#     name='swirling_trojan',
#     pos_x=0.5*(sun.pos.x+jupiter.pos.x * 1.05),
#     pos_y=0.5*(sun.pos.x+jupiter.pos.x * 1.05)*tan(pi/3),
#     pos_z=0,
#     radius=69911e3*0.7,
#     clr='red',
#     mass=jupiter.mass / 100,
#     velocity_x=13e3 * sin(-pi/3) * 1.2,
#     velocity_y=13e3 * cos(-pi/3) * 1.2,
#     velocity_z=0,
#     trail=True
# )


# no lagrange
# velocity x direction 13000
# position x,y,z 0, -778500000000.0, 0
# radius 48937700.0
# mass 1.898e+25
