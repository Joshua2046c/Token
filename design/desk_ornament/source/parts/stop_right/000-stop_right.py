stop_right_width=param("stop_right_width",6)
stop_right_neck_width=param("stop_right_neck_width",3)
stop_right_length=param("stop_right_length",30)
stop_right_head_thickness=param("stop_right_head_thickness",2.5)
stop_right_neck_height=param("stop_right_neck_height",2.5)
# Glue into the guide entry after the handle is inserted; lower end is the upper travel stop.
body=Box(stop_right_width,stop_right_length,stop_right_head_thickness,align=(Align.CENTER,Align.MIN,Align.MIN))
body+=Pos(0,0,stop_right_head_thickness)*Box(stop_right_neck_width,stop_right_length,stop_right_neck_height,align=(Align.CENTER,Align.MIN,Align.MIN))
assert len(body.solids())==1 and body.is_valid
body.color=Color(0.055,0.06,0.065)
publish("stop_right",body,"导轨上限位塞",material="pla")
