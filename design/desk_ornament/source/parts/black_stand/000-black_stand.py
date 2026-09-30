
black_stand_top_corner_radius = param("black_stand_top_corner_radius", 2.0)
black_stand_width = param("black_stand_width", 118)
black_stand_height = param("black_stand_height", 240.0)
black_stand_thickness = param("black_stand_thickness", 8.0)
black_stand_base_width = param("black_stand_base_width", 124)
black_stand_base_depth = param("black_stand_base_depth", 95)
black_stand_base_thickness = param("black_stand_base_thickness", 8.0)
black_stand_base_front = param("black_stand_base_front", 32.0)
black_stand_base_radius = param("black_stand_base_radius", 4.0)
black_stand_front_y = param("black_stand_front_y", -3.8)
black_stand_flare_height = param("black_stand_flare_height", 14.0)
black_stand_rear_brace_height = param("black_stand_rear_brace_height", 50.0)
black_stand_rear_brace_reach = param("black_stand_rear_brace_reach", 38)
black_stand_socket_diameter = param("black_stand_socket_diameter", 4.6)
black_stand_socket_depth = param("black_stand_socket_depth", 3.4)
black_stand_socket_half_pitch = param("black_stand_socket_half_pitch", 45)
black_stand_socket_upper_z = param("black_stand_socket_upper_z", 220.4370479853239)
black_stand_socket_lower_z = param("black_stand_socket_lower_z", 99.14674549433198)
black_stand_tilt_deg = param("black_stand_tilt_deg", 12.0)
from math import sin, cos, tan, radians
a=radians(black_stand_tilt_deg)
w=black_stand_width
h=black_stand_height
fy=black_stand_front_y
ft=black_stand_base_thickness
front=-black_stand_base_front
assert black_stand_base_width>=w
assert black_stand_socket_depth<black_stand_thickness
base = Pos(0,black_stand_base_depth/2-black_stand_base_front,0)*extrude(RectangleRounded(black_stand_base_width,black_stand_base_depth,black_stand_base_radius), amount=ft)
# All elevations are in world Z. The plate is a true constant-normal-thickness tilted slab.
def front_y(z):
    return fy+(z-ft)*tan(a)
top_y=front_y(h)
top_back=(top_y+black_stand_thickness*cos(a),h-black_stand_thickness*sin(a))
rear_y=front_y(black_stand_rear_brace_height)+black_stand_thickness/cos(a)
# Front: a small circular blend tangent to the sole and inclined face.
front_radius=(black_stand_flare_height-ft)/(1-sin(a))
front_center=(fy-(black_stand_flare_height-ft)/cos(a),ft+front_radius)
front_foot=(front_center[0],ft)
front_tangent=(front_y(black_stand_flare_height),black_stand_flare_height)
mid_angle=(-90-black_stand_tilt_deg)/2
front_mid=(front_center[0]+front_radius*cos(radians(mid_angle)),front_center[1]+front_radius*sin(radians(mid_angle)))
# Rear: a smooth cubic blend; both end tangents match the straight adjoining faces.
rear_top=(rear_y,black_stand_rear_brace_height)
rear_foot=(black_stand_rear_brace_reach,ft)
rear_drop=black_stand_rear_brace_height-ft
rear_run=black_stand_rear_brace_reach-rear_y
assert rear_drop>0 and rear_run>0
assert front_foot[0]>front
assert black_stand_rear_brace_reach<black_stand_base_depth-black_stand_base_front
rear_control1=(rear_top[0]-0.55*rear_drop*tan(a),rear_top[1]-0.55*rear_drop)
rear_control2=(rear_foot[0]-0.55*rear_run,ft)
with BuildLine(Plane.YZ) as side_outline:
    Polyline((front,ft*0.75),(front,ft),front_foot)
    ThreePointArc(front_foot,front_mid,front_tangent)
    Polyline(front_tangent,(top_y,h),top_back,rear_top)
    Bezier(rear_top,rear_control1,rear_control2,rear_foot)
    Polyline(rear_foot,(black_stand_rear_brace_reach,ft*0.75),(front,ft*0.75))
side=Face(Wire(side_outline.edges()))
body=base+Pos(-w/2,0,0)*extrude(side,amount=w,dir=(1,0,0))
for x in [-black_stand_socket_half_pitch,black_stand_socket_half_pitch]:
    for z in [black_stand_socket_lower_z,black_stand_socket_upper_z]:
        bore=Pos(x,front_y(z),z)*Rot(-90-black_stand_tilt_deg,0,0)*Cylinder(black_stand_socket_diameter/2,black_stand_socket_depth,align=(Align.CENTER,Align.CENTER,Align.MIN))
        body=body-bore
# Round the two exposed upper backing corners in the same plane as the silver outline.
top_edges=[e for e in body.edges() if abs(abs(e.center().X)-w/2)<1e-5 and abs(e.length-black_stand_thickness)<1e-5 and e.center().Z>h-black_stand_thickness]
assert len(top_edges)==2
body=fillet(top_edges,radius=black_stand_top_corner_radius)
# Guide dimensions are in the silver panel's assembly frame.
black_stand_guide_half_pitch=param("black_stand_guide_half_pitch",53)
black_stand_guide_head_width=param("black_stand_guide_head_width",6.6)
black_stand_guide_neck_width=param("black_stand_guide_neck_width",3.6)
black_stand_guide_back_z=param("black_stand_guide_back_z",-5.8)
black_stand_guide_shoulder_z=param("black_stand_guide_shoulder_z",-2.7)
black_stand_guide_parked_lower_y=param("black_stand_guide_parked_lower_y",5)
black_stand_guide_entry_y=param("black_stand_guide_entry_y",90)
black_stand_guide_origin_y=param("black_stand_guide_origin_y",29.724115975966416)
black_stand_guide_origin_z=param("black_stand_guide_origin_z",166.68051228312814)
black_stand_guide_stroke=param("black_stand_guide_stroke",15)
guide_pose=Pos(0,black_stand_guide_origin_y,black_stand_guide_origin_z)*Rot(90-black_stand_tilt_deg,0,0)
black_stand_guide_lower_y=black_stand_guide_parked_lower_y-black_stand_guide_stroke
gl=black_stand_guide_entry_y-black_stand_guide_lower_y
gy=(black_stand_guide_entry_y+black_stand_guide_lower_y)/2
for sign in [-1,1]:
    gx=sign*black_stand_guide_half_pitch
    head=Pos(gx,gy,black_stand_guide_back_z)*Box(black_stand_guide_head_width,gl,black_stand_guide_shoulder_z-black_stand_guide_back_z,align=(Align.CENTER,Align.CENTER,Align.MIN))
    neck=Pos(gx,gy,black_stand_guide_shoulder_z)*Box(black_stand_guide_neck_width,gl,-black_stand_guide_shoulder_z+0.2,align=(Align.CENTER,Align.CENTER,Align.MIN))
    body-=guide_pose*(head+neck)
# Seat for one thin top cover, leaving 0.2 mm adhesive gap below it.
black_stand_cover_seat_y=param("black_stand_cover_seat_y",72.8)
seat=Pos(0,black_stand_cover_seat_y,black_stand_guide_back_z-black_stand_thickness)*Box(black_stand_width+2,black_stand_guide_entry_y-black_stand_cover_seat_y,black_stand_thickness*3,align=(Align.CENTER,Align.MIN,Align.MIN))
body-=guide_pose*seat
assert len(body.solids())==1
assert body.is_valid
# Uniform-density centroid of this printed body stays within the support footprint.
c=body.center(CenterOf.MASS)
assert abs(c.X)<black_stand_base_width/2-black_stand_base_radius
assert -black_stand_base_front+10<c.Y<black_stand_base_depth-black_stand_base_front-10
body.color=Color(0.055,0.06,0.065)
publish("black_stand",body,"黑色支架底座",material="pla")
print("Black stand volume and center",body.volume,body.center(CenterOf.MASS))
