top_cover_width=param("top_cover_width",118)
top_cover_depth=param("top_cover_depth",8)
top_cover_thickness=param("top_cover_thickness",2)
top_cover_corner_radius=param("top_cover_corner_radius",2)
# Local Y is the 2 mm height of the top cap; local Z spans the black backing.
h=2*(top_cover_thickness+top_cover_corner_radius)
outline=Pos(0,top_cover_thickness-h/2,0)*extrude(RectangleRounded(top_cover_width,h,top_cover_corner_radius),amount=top_cover_depth)
body=outline & Box(top_cover_width,top_cover_thickness,top_cover_depth,align=(Align.CENTER,Align.MIN,Align.MIN))
assert len(body.solids())==1 and body.is_valid
body.color=Color(0.055,0.06,0.065)
publish("top_cover",body,"顶部防脱盖板",material="pla")
