#!/Users/bht400/miniconda3/bin/python

import math
import time

start_time = time.time()

#tekstfil = open('output1.txt', 'w')

A_b = 69.85
c_w_b = 0.5677
p_vand = 997
f_m = 0
delta_t = 0.01
m = 3393000
f_d = 0
v_maal = 10.8
s_y = 0
v_y = 0
a_i_y = 0
A_b_luft=711.2
c_w_b_luft=1.05

n = 10000
i = 0

p_luft = 1.2
pi = 3.14 #round(math.pi, 3)
r_cylinder = 2.5
L_cylinder = 30

w = 1
v_vind_x = 8
f_lift = 0

# f_lift = p_luft * v_vind * w * L_cylinder * (2 * pi * r_cylinder)**2


a_side_vand = 932.25
c_w_side_vand = 0.6
a_side_luft = 2550
c_w_side_luft = 0.82
v_x = 0
s_x = 0
phi=0
B=6
A=2
alpha=10**(-4)

distance = 52000

while s_y < distance:
	if v_y < v_maal:
		f_m = f_m + 100

	if v_y > v_maal:
		f_m = f_m - 100

    #if f_m < 0:
    #    f_m == 0

	v_vind_x = A * math.sin(alpha*i*(2*pi)+phi)+B
	f_lift_x = p_luft * v_y * w * L_cylinder * 2 * pi * (r_cylinder) ** 2
	f_d = -0.5 * p_vand * A_b * c_w_b * (v_y ** 2)
	f_d_y_vind = -0.5 * p_luft * A_b_luft * c_w_b_luft * (v_y ** 2)
	f_lift_y = p_luft * v_vind_x * w * L_cylinder * 2 * pi * (r_cylinder) ** 2
	a_i_y = (f_m + f_lift_y + f_d + f_d_y_vind) / m
	v_y = v_y + a_i_y * delta_t
	s_y = s_y + v_y * delta_t

	#print(s_y, f_lift_y, v_vind_x)

	f_a_x = 0.5 * a_side_luft * p_luft * c_w_side_luft * (v_vind_x ** 2)
	f_d_x = -0.5 * a_side_vand * p_vand * c_w_side_vand * (v_x ** 2)
	a_i_x = (f_a_x + f_d_x + f_lift_y) / m
	v_x = v_x + a_i_x * delta_t
	s_x = s_x + v_x * delta_t

	"""
	seperator = ','
	
	tekstfil.write(str(round(s_y, 3)))
	tekstfil.write(seperator)
	tekstfil.write(str(round(v_y, 3)))
	tekstfil.write(seperator)
	tekstfil.write(str(round(s_x, 3)))
	tekstfil.write(seperator)
	tekstfil.write(str(round(v_x, 3)))
	tekstfil.write(seperator)
	tekstfil.write(str(f_m))
	tekstfil.write(seperator)
	tekstfil.write(str(round(f_lift_y)))
	tekstfil.write(seperator)
	tekstfil.write(str(i))
	tekstfil.write(seperator)
	tekstfil.write(str(round(delta_t*i,3)))
	tekstfil.write(seperator)
	tekstfil.write(str(round(v_vind_x,3)))
	tekstfil.write('\n')
	"""

	i = i + 1
	x_m = round(delta_t*i,3)
	#print(s_y, x_m, f_lift_y, f_m)


print("--- %s seconds ---" % (time.time() - start_time))
