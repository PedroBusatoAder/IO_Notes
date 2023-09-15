import picos

P =  picos.Problem()    

x = picos.RealVariable('x', 30, lower = 0)

P.set_objective('min', x[0]*13 +x[1]*10 + x[2]*22 + x[3]*29 + x[4]*18 + x[5]*0 + x[6]*14 + x[7]*13 + x[8]*16 + x[9]*21 + x[10]*1000 + x[11]*0 + x[12]*3 + x[13]*0 + x[14]*1000 + x[15]*11 + x[16]*6 + x[17]*0 + x[18]*18 + x[19]*9 + x[20]*19 + x[21]*23 + x[22]*11 + x[23]*0 + x[24]*30 + x[25]*24 + x[26]*34 + x[27]*36 + x[28]*28 + x[29]*0)
#Restricciones

#Restricciones de oferta
P.add_constraint(x[0] + x[1] + x[2] + x[3] + x[4] + x[5] <= 5)
P.add_constraint(x[6] + x[7] + x[8] + x[9] + x[10] + x[11] <= 6)
P.add_constraint(x[12] + x[13] + x[14] + x[15] + x[16] + x[17] <= 7)
P.add_constraint(x[18] + x[19] + x[20] + x[21] + x[22] + x[23] <= 4)
P.add_constraint(x[24] + x[25] + x[26] + x[27] + x[28] + x[29] <= 3)

#Restricciones de demanda
P.add_constraint(x[0] + x[6] + x[12] + x[18] + x[24] == 3)
P.add_constraint(x[1] + x[7] + x[13] + x[19] + x[25] == 5)
P.add_constraint(x[2] + x[8] + x[14] + x[20] + x[26] == 4)
P.add_constraint(x[3] + x[9] + x[15] + x[21] + x[27] == 5)
P.add_constraint(x[4] + x[10] + x[16] + x[22] + x[28] == 6)
P.add_constraint(x[5] + x[11] + x[17] + x[23] + x[29] == 2)

P.solve()
print(x)
