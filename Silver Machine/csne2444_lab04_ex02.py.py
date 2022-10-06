# Basil Agboola
# Lab 04
# 9-19-22
# Intro to Comp Sci 1
#pipe volume
# formula pi * r**2 * h
def calculate_pipe_volume(h,r1,r2):
    import math
    bigvolume =  math.pi * (r1**2) * h
    littlevolume = math.pi * (r2**2) * h
    result = bigvolume - littlevolume
    return float(result)
    
volume = calculate_pipe_volume(80,60,20)
volume2 = calculate_pipe_volume(87,78,21)
volume3 = calculate_pipe_volume(87,68,50)
print(volume)
print(volume2)
print(volume3)
#box volume
def calculate_box_volume(l,w,h):
    output = l * w * h
    return float(output)
box1 = calculate_box_volume(21,23,2)
box2 = calculate_box_volume(23,3903,23)
box3 = calculate_box_volume(21,3.5,7)
print(box1)
print(box2)
print(box3)