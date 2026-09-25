import math

def temp_calc(d_out, Rext, BETA, R0):
	
	T0 = 298.15 #Temperature in Kelvin relative to the reference value of 25 °C
	
	#SIGN MANAGEMENT
	if d_out >= 1024:
		d_out_signed = d_out - 2048
	else:
		d_out_signed = d_out

	#R_ntc and ratio calculation
	ratio = 0.174387 + (d_out_signed*0.010404)/8
	R_ntc = R_ext * (1.0 / ratio - 1.0)

	#T_kelvin calculation
	inv_T = (1.0 / T0) + (1.0 / BETA) * math.log(R_ntc / R0)
	T_k = 1.0 / inv_T

	#T_celsius calculation
	T_c = T_k - 273.15
	return round(T_c)
	
if __name__ == "__main__":

	print("Challenge 1 Task 1 verification")
	
	res_1 = temp_calc(447)
	print(f"TEST 1 - Input Dout -> Result: {res_1}°C")

	res_2 = temp_calc(2032) 
	print(f"TEST 2 - Input Dout -> Result: {res_2}°C")
