stop_left_width=param("stop_left_width",6)
stop_left_neck_width=param("stop_left_neck_width",3)
stop_left_length=param("stop_left_length",30)
stop_left_head_thickness=param("stop_left_head_thickness",2.5)
stop_left_neck_height=param("stop_left_neck_height",2.5)
# Glue into the guide entry after the handle is inserted; lower end is the upper travel stop.
body=Box(stop_left_width,stop_left_length,stop_left_head_thickness,align=(Align.CENTER,Align.MIN,Align.MIN))
body+=Pos(0,0,stop_left_head_thickness)*Box(stop_left_neck_width,stop_left_length,stop_left_neck_height,align=(Align.CENTER,Align.MIN,Align.MIN))
assert len(body.solids())==1 and body.is_valid
body.color=Color(0.055,0.06,0.065)
publish("stop_left",body,"导轨上限位塞",material="pla")
