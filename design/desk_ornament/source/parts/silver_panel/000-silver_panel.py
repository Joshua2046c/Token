# cell: silver_panel

silver_panel_width = param("silver_panel_width", 120)
silver_panel_height = param("silver_panel_height", 150.0)
silver_panel_thickness = param("silver_panel_thickness", 8)
silver_panel_corner_radius = param("silver_panel_corner_radius", 2.0)
silver_panel_window_width = param("silver_panel_window_width", 110)
silver_panel_window_height = param("silver_panel_window_height", 34.0)
silver_panel_window_radius = param("silver_panel_window_radius", 5.0)
silver_panel_window_y = param("silver_panel_window_y", -48.0)
silver_panel_band_width = param("silver_panel_band_width", 114)
silver_panel_band_height = param("silver_panel_band_height", 10.0)
silver_panel_band_y = param("silver_panel_band_y", -16.0)
silver_panel_pin_diameter = param("silver_panel_pin_diameter", 4.0)
silver_panel_pin_length = param("silver_panel_pin_length", 3.0)
silver_panel_pin_half_pitch = param("silver_panel_pin_half_pitch", 45)
silver_panel_pin_upper_y = param("silver_panel_pin_upper_y", 55.0)
silver_panel_pin_lower_y = param("silver_panel_pin_lower_y", -69.0)
silver_panel_logo_width = param("silver_panel_logo_width", 32.0)
silver_panel_logo_depth = param("silver_panel_logo_depth", 0.6)
silver_panel_logo_x = param("silver_panel_logo_x", 0.0)
silver_panel_logo_y = param("silver_panel_logo_y", 32.0)
t=silver_panel_thickness
assert 0<silver_panel_logo_depth<t
plate=extrude(RectangleRounded(silver_panel_width,silver_panel_height,silver_panel_corner_radius),amount=t)
window=Pos(0,silver_panel_window_y,0)*extrude(RectangleRounded(silver_panel_window_width,silver_panel_window_height,silver_panel_window_radius),amount=t)
band=Pos(0,silver_panel_band_y,0)*extrude(Rectangle(silver_panel_band_width,silver_panel_band_height),amount=t)
plate=plate-window-band
for x in [-silver_panel_pin_half_pitch,silver_panel_pin_half_pitch]:
    for y in [silver_panel_pin_lower_y,silver_panel_pin_upper_y]:
        pin=Pos(x,y,-silver_panel_pin_length)*Cylinder(silver_panel_pin_diameter/2,silver_panel_pin_length,align=(Align.CENTER,Align.CENTER,Align.MIN))
        plate=plate+pin
# Immutable normalized contours derived from user reference_3; vertices are artwork, not design parameters.
LOGO_LOOPS=[[[-0.1118012,0.4953416],[-0.0186335,0.492236],[0.0496894,0.4642857],[0.0931677,0.4270186],[0.1614907,0.439441],[0.2173913,0.4363354],[0.2546584,0.4270186],[0.2919255,0.4114907],[0.3416149,0.3773292],[0.3757764,0.3400621],[0.4099379,0.2779503],[0.4223602,0.2313665],[0.4223602,0.1506211],[0.4161491,0.1257764],[0.4596273,0.0791925],[0.4782609,0.0450311],[0.4937888,-0.0015528],[0.5,-0.0388199],[0.4937888,-0.1164596],[0.484472,-0.1475155],[0.4503106,-0.2096273],[0.4006211,-0.2593168],[0.3136646,-0.302795],[0.310559,-0.3276398],[0.2857143,-0.3804348],[0.2453416,-0.4301242],[0.2391304,-0.4301242],[0.2142857,-0.4549689],[0.173913,-0.4767081],[0.1397516,-0.4891304],[0.1118012,-0.492236],[0.0403727,-0.4953416],[-0.0031056,-0.4860248],[-0.0621118,-0.4580745],[-0.0962733,-0.4270186],[-0.1397516,-0.4363354],[-0.2329193,-0.4332298],[-0.2795031,-0.4177019],[-0.3322981,-0.386646],[-0.3757764,-0.3431677],[-0.4068323,-0.2903727],[-0.4254658,-0.2251553],[-0.4254658,-0.1568323],[-0.4192547,-0.1257764],[-0.4409938,-0.1071429],[-0.4658385,-0.0729814],[-0.4968944,0.0046584],[-0.4968944,0.113354],[-0.484472,0.1537267],[-0.4503106,0.2127329],[-0.4037267,0.2593168],[-0.363354,0.2841615],[-0.3291925,0.2934783],[-0.3167702,0.302795],[-0.310559,0.3338509],[-0.2888199,0.3804348],[-0.257764,0.4145963],[-0.257764,0.4208075],[-0.2515528,0.4208075],[-0.2329193,0.4425466],[-0.1708075,0.4798137]],[[0.1770186,0.0295031],[0.173913,-0.265528],[0.1552795,-0.2872671],[-0.0341615,-0.3959627],[-0.0310559,-0.4052795],[-0.0031056,-0.4208075],[0.0372671,-0.4332298],[0.0559006,-0.4332298],[0.1149068,-0.4332298],[0.1801242,-0.4083851],[0.2329193,-0.3586957],[0.2608696,-0.2996894],[0.2639752,-0.0232919],[0.2484472,-0.007764]],[[-0.0931677,0.4363354],[-0.1521739,0.423913],[-0.2080745,0.3897516],[-0.2484472,0.3369565],[-0.2670807,0.2748447],[-0.2670807,0.0232919],[-0.1832298,-0.0295031],[-0.1770186,-0.0295031],[-0.1770186,0.0046584],[-0.1770186,0.2624224],[-0.1708075,0.2779503],[0.0310559,0.3959627],[0.0248447,0.4083851],[-0.0248447,0.4301242]],[[0.1118012,-0.1381988],[-0.1397516,-0.2841615],[-0.1614907,-0.2841615],[-0.1863354,-0.2717391],[-0.257764,-0.2251553],[-0.363354,-0.1692547],[-0.3664596,-0.2034161],[-0.3540373,-0.2531056],[-0.3229814,-0.3121118],[-0.2732919,-0.3524845],[-0.2173913,-0.3742236],[-0.1273292,-0.3742236],[-0.0807453,-0.3555901],[0.0621118,-0.2686335],[0.1024845,-0.25],[0.1149068,-0.2375776]],[[-0.3322981,0.2282609],[-0.3757764,0.2034161],[-0.4006211,0.1785714],[-0.4254658,0.1381988],[-0.4409938,0.0854037],[-0.4409938,0.0326087],[-0.431677,-0.0046584],[-0.4068323,-0.0543478],[-0.3695652,-0.0947205],[-0.1677019,-0.2096273],[-0.1614907,-0.2158385],[-0.1428571,-0.2158385],[-0.0652174,-0.1723602],[-0.0652174,-0.1661491],[-0.3198758,-0.0170807],[-0.326087,-0.007764],[-0.326087,0.2282609]],[[0.1459627,0.3773292],[0.1118012,0.371118],[0.0776398,0.3555901],[0.0372671,0.3276398],[-0.0248447,0.2965839],[-0.0372671,0.2841615],[-0.0465839,0.2841615],[-0.0652174,0.2686335],[-0.0993789,0.2531056],[-0.1180124,0.234472],[-0.1180124,0.1413043],[-0.1086957,0.1381988],[-0.1055901,0.1444099],[0.0931677,0.2593168],[0.136646,0.2841615],[0.1614907,0.2841615],[0.3043478,0.197205],[0.3447205,0.1785714],[0.3478261,0.1723602],[0.363354,0.1692547],[0.363354,0.2127329],[0.3540373,0.2531056],[0.3229814,0.3090062],[0.2950311,0.3369565],[0.2546584,0.3618012],[0.2173913,0.3742236]],[[0.1428571,0.2158385],[0.0714286,0.1785714],[0.0621118,0.1661491],[0.121118,0.1350932],[0.1335404,0.1226708],[0.1583851,0.113354],[0.1925466,0.0885093],[0.2173913,0.0791925],[0.2515528,0.0543478],[0.2701863,0.0481366],[0.3198758,0.0139752],[0.326087,-0.0046584],[0.326087,-0.2282609],[0.3478261,-0.2189441],[0.3664596,-0.2096273],[0.4006211,-0.1754658],[0.431677,-0.1164596],[0.4378882,-0.0885093],[0.4378882,-0.0295031],[0.4223602,0.0232919],[0.3975155,0.0636646],[0.363354,0.0978261],[0.2608696,0.1537267],[0.242236,0.1692547],[0.2173913,0.1785714],[0.1770186,0.2065217],[0.1583851,0.2158385]],[[-0.0062112,0.1319876],[-0.1180124,0.0667702],[-0.1180124,-0.0667702],[-0.0590062,-0.1040373],[-0.0124224,-0.1257764],[-0.0093168,-0.1319876],[0.0031056,-0.1319876],[0.1149068,-0.0698758],[0.1149068,0.0698758],[0.0217391,0.1195652],[0.0186335,0.1257764]]]
def logo_polygon(points):
    return Polygon(*[(x*silver_panel_logo_width+silver_panel_logo_x,y*silver_panel_logo_width+silver_panel_logo_y) for x,y in points],align=None)
logo=logo_polygon(LOGO_LOOPS[0])
for loop in LOGO_LOOPS[1:]:
    logo=logo-logo_polygon(loop)
cut=Pos(0,0,t-silver_panel_logo_depth)*extrude(logo,amount=silver_panel_logo_depth,dir=(0,0,1))
assert abs(cut.bounding_box().min.Z-(t-silver_panel_logo_depth))<0.0001
assert abs(cut.bounding_box().max.Z-t)<0.0001
assert len(logo.faces())==1
assert len(logo.wires())==8
plate=plate-cut
assert len(plate.solids())==1
assert plate.is_valid
# Centroid projected using this revision's assembly placement.
from math import sin, cos, radians
c=plate.center(CenterOf.MASS)
assert abs(c.X)<58
world_center_y=29.724115975966416+c.Y*sin(radians(12))-c.Z*cos(radians(12))
assert -22<world_center_y<53
plate.color=Color(0.75,0.77,0.80)
publish("silver_panel",plate,"银色面板",material="pla")
print("Silver panel volume and local center",plate.volume,plate.center(CenterOf.MASS))
