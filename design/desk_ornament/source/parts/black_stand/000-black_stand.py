# cell: black_stand

black_stand_width = param("black_stand_width", 94.0)
black_stand_height = param("black_stand_height", 240.0)
black_stand_thickness = param("black_stand_thickness", 8.0)
black_stand_base_width = param("black_stand_base_width", 100.0)
black_stand_base_depth = param("black_stand_base_depth", 85.0)
black_stand_base_thickness = param("black_stand_base_thickness", 8.0)
black_stand_base_front = param("black_stand_base_front", 32.0)
black_stand_base_radius = param("black_stand_base_radius", 4.0)
black_stand_front_y = param("black_stand_front_y", -3.8)
black_stand_flare_height = param("black_stand_flare_height", 38.0)
black_stand_rear_brace_height = param("black_stand_rear_brace_height", 50.0)
black_stand_rear_brace_reach = param("black_stand_rear_brace_reach", 28.0)
black_stand_socket_diameter = param("black_stand_socket_diameter", 4.6)
black_stand_socket_depth = param("black_stand_socket_depth", 3.4)
black_stand_socket_half_pitch = param("black_stand_socket_half_pitch", 35.0)
black_stand_socket_upper_z = param("black_stand_socket_upper_z", 220.0)
black_stand_socket_lower_z = param("black_stand_socket_lower_z", 96.0)
w=black_stand_width
h=black_stand_height
fy=black_stand_front_y
by=fy+black_stand_thickness
ft=black_stand_base_thickness
front=-black_stand_base_front
assert black_stand_base_width>=w
assert black_stand_socket_depth<black_stand_thickness
base = Pos(0,black_stand_base_depth/2-black_stand_base_front,0)*extrude(RectangleRounded(black_stand_base_width,black_stand_base_depth,black_stand_base_radius), amount=ft)
# The broad front flare and the rear gusset are fused into one printed part.
side=Plane.YZ*Polygon((front,ft*0.75),(front,ft),(front*0.69,ft*1.4),(front*0.38,black_stand_flare_height*0.53),(fy,black_stand_flare_height),(fy,h),(by,h),(by,black_stand_rear_brace_height),(black_stand_rear_brace_reach,ft),(black_stand_rear_brace_reach,ft*0.75),align=None)
body=base+Pos(-w/2,0,0)*extrude(side,amount=w,dir=(1,0,0))
for x in [-black_stand_socket_half_pitch,black_stand_socket_half_pitch]:
    for z in [black_stand_socket_lower_z,black_stand_socket_upper_z]:
        bore=Pos(x,fy,z)*Rot(-90,0,0)*Cylinder(black_stand_socket_diameter/2,black_stand_socket_depth,align=(Align.CENTER,Align.CENTER,Align.MIN))
        body=body-bore
assert len(body.solids())==1
assert body.is_valid
# Uniform-density centroid of this printed body stays within the support footprint.
c=body.center(CenterOf.MASS)
assert abs(c.X)<black_stand_base_width/2-black_stand_base_radius
assert -black_stand_base_front+10<c.Y<black_stand_base_depth-black_stand_base_front-10
body.color=Color(0.055,0.06,0.065)
publish("black_stand",body,"黑色支架底座",material="pla")
print("Black stand volume and center",body.volume,body.center(CenterOf.MASS))
