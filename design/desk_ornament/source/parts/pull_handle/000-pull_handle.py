pull_handle_width=param("pull_handle_width",120)
pull_handle_height=param("pull_handle_height",150)
pull_handle_thickness=param("pull_handle_thickness",18)
pull_handle_top_radius=param("pull_handle_top_radius",2)
pull_handle_bottom_radius=param("pull_handle_bottom_radius",5)
pull_handle_opening_width=param("pull_handle_opening_width",110)
pull_handle_window_height=param("pull_handle_window_height",38)
pull_handle_window_y=param("pull_handle_window_y",-50)
pull_handle_notch_bottom_y=param("pull_handle_notch_bottom_y",-21)
pull_handle_notch_radius=param("pull_handle_notch_radius",2)
pull_handle_guide_half_pitch=param("pull_handle_guide_half_pitch",53)
pull_handle_guide_length=param("pull_handle_guide_length",40)
pull_handle_guide_center_y=param("pull_handle_guide_center_y",25)
pull_handle_guide_head_width=param("pull_handle_guide_head_width",6)
pull_handle_guide_neck_width=param("pull_handle_guide_neck_width",3)
pull_handle_guide_head_back_z=param("pull_handle_guide_head_back_z",-5.5)
pull_handle_guide_head_thickness=param("pull_handle_guide_head_thickness",2.5)
pull_handle_guide_neck_front_z=param("pull_handle_guide_neck_front_z",1)
pull_handle_wing_back_z=param("pull_handle_wing_back_z",0.4)
pull_handle_wing_thickness=param("pull_handle_wing_thickness",2)
t=pull_handle_thickness
body=extrude(Rectangle(pull_handle_width,pull_handle_height),amount=t)
body=fillet([e for e in body.edges().filter_by(Axis.Z) if e.center().Y>0],radius=pull_handle_top_radius)
body=fillet([e for e in body.edges().filter_by(Axis.Z) if e.center().Y<0],radius=pull_handle_bottom_radius)
# The upper opening is a U notch, open through the top for the fixed logo panel.
notch_h=pull_handle_height
notch=Pos(0,pull_handle_notch_bottom_y+notch_h/2,0)*extrude(RectangleRounded(pull_handle_opening_width,notch_h,pull_handle_notch_radius),amount=t)
window=Pos(0,pull_handle_window_y,0)*extrude(RectangleRounded(pull_handle_opening_width,pull_handle_window_height,pull_handle_bottom_radius),amount=t)
body=body-notch-window
for sign in [-1,1]:
    gx=sign*pull_handle_guide_half_pitch
    gy=pull_handle_guide_center_y
    shoulder=pull_handle_guide_head_back_z+pull_handle_guide_head_thickness
    cap=Pos(gx,gy,pull_handle_guide_head_back_z)*Box(pull_handle_guide_head_width,pull_handle_guide_length,pull_handle_guide_head_thickness,align=(Align.CENTER,Align.CENTER,Align.MIN))
    neck=Pos(gx,gy,shoulder)*Box(pull_handle_guide_neck_width,pull_handle_guide_length,pull_handle_guide_neck_front_z-shoulder,align=(Align.CENTER,Align.CENTER,Align.MIN))
    inner=pull_handle_guide_half_pitch-pull_handle_guide_neck_width/2
    wing_width=pull_handle_width/2-inner
    wing=Pos(sign*(inner+wing_width/2),gy,pull_handle_wing_back_z)*Box(wing_width,pull_handle_guide_length,pull_handle_wing_thickness,align=(Align.CENTER,Align.CENTER,Align.MIN))
    body=body+wing+neck+cap
assert len(body.solids())==1, ("handle solids",len(body.solids()))
assert body.is_valid, "handle invalid"
assert abs((pull_handle_window_y-pull_handle_window_height/2)-(-pull_handle_height/2)-6)<1e-6
body.color=Color(0.75,0.77,0.80)
publish("pull_handle",body,"银色下拉柄",material="pla")
