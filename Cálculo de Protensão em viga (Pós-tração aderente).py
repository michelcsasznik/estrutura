#Importar bibliotecas

#import numpy as np
#import pandas as pd
import math
import os
os.system("clear")

#Pesos específicos

peso_esp_concreto_armado = 25 # KN/m3
peso_esp_concreto_protendido = 25 # KN/m3
peso_esp_pavimentacao = 24 # KN/m3


#Propriedades do concreto

fck = 35 #MPa
fckj = 35 #MPa
Es_c = 29 #GPa
gamma_c = 1.4


#Propriedades da CORDOALHAS PARA PROTENSÃO ENGRAXADAS E PLASTIFICADAS
# Cord. CP 190 RB 12,70 - Belgo

# z = 0 para pos tracao
# z = 1 para pre tracao

z = 0

phi_original = 12.7

phi_calc = phi_original - 1.5 #mm diminuir 15mm de 127 devido a capa plástica
area_phi = math.pi *float(((phi_calc/10)**2)/4)#cm2
print("A area da cordoalha e: " + str(area_phi))
fptk = 1900 #MPa
fpyk = 1710 #MPa
Ep = 200 #GPa
gamma_s = 1.15


#Coeficientes de combinação

gamma_f = 1.4
psi_0 = 0.6
psi_1 = 0.4
psi_2 = 0.3


#Perdas

perdas_iniciais = 0.05
perdas_finais = 0.25


#Cargas
vao = 8 #m
g1 = 3.5 #KN/m - peso proprio 
g2 = 0 #KN/m - laje alveolar
g3 = 0 #KN/m - capa
g4 = 1.3 #KN/m - alvenaria
g5 = 0 #KN/m - revestimento
q = 1.5 #KN/m - acidental 

Mkmax_g1 = (g1 * vao**2)/8 #KNm
Mkmax_g2 = (g2 * vao**2)/8 #KNm
Mkmax_g3 = (g3 * vao**2)/8 #KNm
Mkmax_g4 = (g4 * vao**2)/8 #KNm
Mkmax_g5 = (g5 * vao**2)/8 #KNm
Mkmax_q = (q * vao**2)/8 #KNm

Mk = Mkmax_g1+Mkmax_g2+Mkmax_g3+Mkmax_g4+Mkmax_g5+Mkmax_q #KNm
Md = gamma_f*Mk
print("Mk e igual a: " + str(Mk)+ " KNm")
print("Md e igual a: " + str(Md)+ " KNm")


#Seção em T

bf = 0.40 #valor da mesa em m
bw = 0.40 #valor da base retangular/viga em m
h = 0.30 #valor da altura total/viga + laje em m
hw = 0.0 #valor da altura da viga/abaixo da laje em m
hf = 0.30 #valor da altura da mesa em m
hf_linha = h - hf-hw
yi = bw/2
ys = h - yi
Ac = (bw*hw+hf*bf+(bf+bw)*hf_linha/2)
Ic = (bw*h**3)/12
Wi = Ic/yi
Ws = Ic/ys
Wsimples = bw*(hw**2)/6
print("yi e igual a: " + str(yi)+ " m")
print("ys e igual a: " + str(ys)+ " m")
print("Ac e igual a: " + str(Ac)+ " m2")
print("Ic e igual a: " + str(Ic)+ " m4")
print("Wi e igual a: " + str(Wi)+ " m3")
print("Ws e igual a: " + str(Ws)+ " m3")
print("Wsimples e igual a: " + str(Wsimples)+ " m3")


#Calculo do Ap no ELU - t = ထ

#Ap = Md/(KZ * d * ɣpd)
#KMD=Md/(b * d^2 * fcd)
#d' = c + phi estribo + phi arm/2

d_linha = 0.05 #m
d= h-d_linha #m

print("O valor de d linha e: " + str(d_linha) + " m")
print("O valor de d linha e: " + str(d) + " m")
 

#Supondo que a Linha Neutra esta na mesa

KX = 0.000
KZ = 0.000
Es = 0.000

KMD = Md/(bf*(d**2)*((fck*1000)/gamma_c))
print("O valor do KMD e: " + str(KMD))

if KMD <= 0.01:
    KX = 0.0148
    KZ = 0.9941
    Es = 10.000
    
elif KMD > 0.01 and KMD <=0.02:
    KX = 0.0298
    KZ = 0.9881
    Es = 10.000
    
elif KMD > 0.02 and KMD <=0.03:
    KX = 0.0449
    KZ = 0.9820
    Es = 10.000
    
elif KMD > 0.03 and KMD <=0.04:
    KX = 0.00603
    KZ = 0.9759
    Es = 10.000
    
elif KMD > 0.04 and KMD <=0.05:
    KX = 0.0758
    KZ = 0.9697
    Es = 10.000    
    
elif KMD > 0.05 and KMD <=0.055:
    KX = 0.0836
    KZ = 0.9665
    Es = 10.000 
    
elif KMD > 0.055 and KMD <=0.06:
    KX = 0.0916
    KZ = 0.9634
    Es = 10.000     
    
elif KMD > 0.06 and KMD <=0.065:
    KX = 0.0995
    KZ = 0.9602
    Es = 10.000 
    
elif KMD > 0.065 and KMD <=0.07:
    KX = 0.1076
    KZ = 0.9570
    Es = 10.000  
    
elif KMD > 0.07 and KMD <=0.075:
    KX = 0.1156
    KZ = 0.9537
    Es = 10.000 
    
elif KMD > 0.075 and KMD <=0.08:
    KX = 0.1238
    KZ = 0.9505
    Es = 10.000     
    
elif KMD > 0.08 and KMD <=0.085:
    KX = 0.1320
    KZ = 0.9472
    Es = 10.000 
    
elif KMD > 0.085 and KMD <=0.09:
    KX = 0.1403
    KZ = 0.9439
    Es = 10.000 
    
elif KMD > 0.09 and KMD <=0.095:
    KX = 0.1485
    KZ = 0.9606
    Es = 10.000 
    
elif KMD > 0.095 and KMD <=0.100:
    KX = 0.1569
    KZ = 0.9372
    Es = 10.000     
    
elif KMD > 0.100 and KMD <=0.105:
    KX = 0.1654
    KZ = 0.9339
    Es = 10.000 
    
elif KMD > 0.105 and KMD <=0.110:
    KX = 0.1739
    KZ = 0.9305
    Es = 10.000 
    
elif KMD > 0.110 and KMD <=0.115:
    KX = 0.1824
    KZ = 0.9270
    Es = 10.000 
    
elif KMD > 0.115 and KMD <=0.120:
    KX = 0.1911
    KZ = 0.9236
    Es = 10.000     
    
elif KMD > 0.120 and KMD <=0.125:
    KX = 0.1998
    KZ = 0.9201
    Es = 10.000 
    
elif KMD > 0.125 and KMD <=0.130:
    KX = 0.2086
    KZ = 0.9166
    Es = 10.000   
    
elif KMD > 0.130 and KMD <=0.135:
    KX = 0.2175
    KZ = 0.9130
    Es = 10.000 
    
elif KMD > 0.135 and KMD <=0.140:
    KX = 0.2264
    KZ = 0.9094
    Es = 10.000    
    
elif KMD > 0.140 and KMD <=0.145:
    KX = 0.2354
    KZ = 0.9058
    Es = 10.000 
    
elif KMD > 0.145 and KMD <=0.150:
    KX = 0.2445
    KZ = 0.9022
    Es = 10.000   
        
elif KMD > 0.150 and KMD <=0.155:
    KX = 0.2536
    KZ = 0.8985
    Es = 10.000 
    
elif KMD > 0.155 and KMD <= 0.160:
    KX = 0.2630
    KZ = 0.8948
    Es = 9.8104

elif KMD > 0.160 and KMD <= 0.165:
    KX = 0.2723
    KZ = 0.8911
    Es = 9.3531

elif KMD > 0.165 and KMD <= 0.170:
    KX = 0.2818
    KZ = 0.8873
    Es = 8.9222

elif KMD > 0.170 and KMD <= 0.175:
    KX = 0.2723
    KZ = 0.8911
    Es = 8.5154


else:
    print("Ainda nao colocado aqui")    
      
print("O valor de KX e: " + str(KX))
print("O valor de KZ e: " + str(KZ))
print("O valor de Es e: " + str(Es))


#verificando a LN

x = KX/d
print("O valor de x = KX/d e: " + str(x))
print("O valor de hf e: " + str(hf))
if x < hf:
    print("A LN esta na mesa")
else:
    print("A LN nao esta na mesa")


#Tensao Inicial
#Cordoalhas engraxadas

deltap_i_1= 0.80*fptk
deltap_i_2 = 0.88*fpyk
print("O valor de deltap inicial 1 e: " + str(deltap_i_1))
print("O valor de deltap inicial 2 e: " + str(deltap_i_2))

if deltap_i_1 > deltap_i_2:
    deltap_i = deltap_i_2
else:
    deltap_i = deltap_i_1
    
print("O delta p inicial a ser utilizado e: " + str(deltap_i))    

deltap_t_infinito = deltap_i*(1-perdas_finais)
print("O delta p no tempo infinito e: " + str(deltap_t_infinito))


#Vasconcelos

if deltap_t_infinito <= 1025:
    Ep = 5.25
    
elif deltap_t_infinito > 1025 and deltap_t_infinito <= 1314:
    Ep  =6.794

elif deltap_t_infinito > 1314 and deltap_t_infinito <= 1411:
    Ep  =7.438
    
elif deltap_t_infinito > 1411 and deltap_t_infinito <= 1459:
    Ep  =8.167    
    
elif deltap_t_infinito > 1459 and deltap_t_infinito <= 1482:
    Ep  =9.000
    
elif deltap_t_infinito > 1482 and deltap_t_infinito <= 1486:
    Ep  =9.962  
    
elif deltap_t_infinito > 1486 and deltap_t_infinito <= 1486:
    Ep  =10.000    
    
elif deltap_t_infinito > 1486 and deltap_t_infinito <= 1496:
    Ep  =12.50    
    
elif deltap_t_infinito > 1496 and deltap_t_infinito <= 1507:
    Ep  =15.00    
    
elif deltap_t_infinito > 1507 and deltap_t_infinito <= 1517:
    Ep  =17.50   
    
elif deltap_t_infinito > 1517 and deltap_t_infinito <= 1527:
    Ep  =20.00   
    
elif deltap_t_infinito > 1527 and deltap_t_infinito <= 1538:
    Ep  =22.50       
    
elif deltap_t_infinito > 1538 and deltap_t_infinito <= 1548:
    Ep  =25.00       
    
elif deltap_t_infinito > 1548 and deltap_t_infinito <= 1559:
    Ep  =27.50       
    
elif deltap_t_infinito > 1559 and deltap_t_infinito <= 1569:
    Ep  =30.00       
    
elif deltap_t_infinito > 1569 and deltap_t_infinito <= 1579:
    Ep  =32.50       
    
elif deltap_t_infinito > 1579 and deltap_t_infinito <= 1590:
    Ep  =35.00       

elif deltap_t_infinito > 1590 and deltap_t_infinito <= 1600:
    Ep  =37.50       
    
elif deltap_t_infinito > 1600 and deltap_t_infinito <= 1611:
    Ep  =40.00       

print("O Ep e: " + str(Ep) + " %o")
print("O Es e: " + str(Es) + " %o")

Et_inicial = Ep + Es
print("O Et inicial e: " + str(Et_inicial) + " %o")

if Et_inicial <= 5.25:
    deltap_t_infinito_final = 1025
    
elif Et_inicial > 5.25 and Et_inicial <= 6.794:
    deltap_t_infinito_final  =1314

elif Et_inicial > 6.794 and Et_inicial <= 7.438:
    deltap_t_infinito_final  =1411
    
elif Et_inicial > 7.438 and Et_inicial <= 8.167:
    deltap_t_infinito_final  =1459   
    
elif Et_inicial > 8.167 and Et_inicial <= 9.000:
    deltap_t_infinito_final  =1482
    
elif Et_inicial > 9.000 and Et_inicial <= 9.962:
    deltap_t_infinito_final  =1486
    
elif Et_inicial> 9.962 and Et_inicial <= 10.000:
    deltap_t_infinito_final  =1486    
    
elif Et_inicial > 10.000 and Et_inicial <= 12.50:
    deltap_t_infinito_final  =1496   
    
elif Et_inicial > 12.50 and Et_inicial <= 15.00:
    deltap_t_infinito_final  =1507   
    
elif Et_inicial > 15.00 and Et_inicial <= 17.50:
    deltap_t_infinito_final  =1517   
    
elif Et_inicial > 17.50 and Et_inicial <= 20.00:
    deltap_t_infinito_final  =1527  
    
elif Et_inicial > 20.00 and Et_inicial <= 22.50:
    deltap_t_infinito_final  =1538      
    
elif Et_inicial> 22.50 and Et_inicial <= 25.00:
    deltap_t_infinito_final  =1548       
    
elif Et_inicial > 25.00 and Et_inicial <= 27.50:
    deltap_t_infinito_final  =1559       
    
elif Et_inicial > 27.50 and Et_inicial <= 30.00:
    deltap_t_infinito_final  =1569     
    
elif Et_inicial > 30.00 and Et_inicial <= 32.50:
    deltap_t_infinito_final  =1579       
    
elif Et_inicial > 32.50 and Et_inicial <= 35.00:
    deltap_t_infinito_final  =1590       

elif Et_inicial > 35.00 and Et_inicial <= 37.50:
    deltap_t_infinito_final  =1600      
    
elif Et_inicial > 37.50 and Et_inicial <= 40.00:
    deltap_t_infinito_final  =1611     
    
print("O deltap no tempo infinito final e: " + str(deltap_t_infinito_final) + "MPa")


#Area de aço

Ap_final = (1.4*Mk)/(KZ*d*deltap_t_infinito_final*1000)

print("A area de aco necessaria e: " + str(Ap_final) + " m2 = " + str(Ap_final*10000) + " cm2")


#Numero de cordoalhas

Ncord = Ap_final*10000/area_phi
print("O numero de cordoalhas e: " + str(math.ceil(Ncord)) + " unidades")


#Verificacao no tempo 0

deltap_t_zero = deltap_t_infinito_final*(1-perdas_iniciais)
print("O deltap no tempo 0 e: " + str(deltap_t_zero) + " MPa")


#Normal de protensao no tempo 0
Np_t_zero = z*(math.ceil(Ncord))*area_phi*0.0001*deltap_t_zero*1000

print("A Normal de protensao no tempo 0 e :" + str(Np_t_zero) + " MPa")


#Limites

#deltac<=0.7*fckj

deltac = 0.7*fckj
print("O limite deltac e: " + str(deltac) + " MPa")

#deltat >= -1.2*fctm

deltat = -1.2*0.3*fckj**(2/3)
print("O limite deltat e: " + str(deltat) + " MPa")

print(str(round(deltat,5)) + " MPa <= delta_limite < " + str(deltac) + " MPa")


#Verificacao no meio do vao

delta_1 = Np_t_zero/Ac

delta_2 = Np_t_zero*(hw/2-d_linha)/Wsimples

delta_3 = Mkmax_g1/Wsimples

print("Np/Ac e: " + str(delta_1))
print("Np*e/W e: " + str(delta_2))
print("Mg/W e: " + str(round(delta_3,2)))


#Borda Superior Tracao

deltas = delta_1 - delta_2 + delta_3

#Borda Inferior Compressao

deltai = delta_1 + delta_2 - delta_3

print("O deltas na borda superior e: " + str(deltas) + " KN/m2")
print("O deltai na borda inferior e: " + str(deltai) + " KN/m2")

