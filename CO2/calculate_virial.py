import os
import numpy as np
import scipy.integrate
import pandas as pd

#print("currently in:")
#print(os.getcwd())

#get monomer energy sum
f_en1b = "./en_1body/en_mono.dat"
df_en1b = pd.read_csv(f_en1b, sep='\n',header=None)
en_1b = df_en1b.sum().values[0]
en_1b

kb = 0.0019872041
dR = 0.05
gridsize = 501 + int(2.2/0.05) #501
print("gridsize")
print(gridsize)

#temp = [128.53, 135.58, 168.77, 180.86, 188.14, 188.75, 194.98, 200, 205.25, 206.19, 217.21, 225, 240, 244.62, 250, 260.82, 272.11, 275, 296.25, 298.15, 300, 303.15, 313.15, 323.15, 325, 350, 375, 398.15, 523.15, 573.15, 623.15, 653.15, 769.02, 885.19 ]
temp = [100 + i*10 for i in range(101)]

#temp = [423, 448, 473, 573, 673]
vir = [0.0 for i in range(len(temp))]
for j in range(len(temp)):
    t = temp[j]
    beta = kb * float(t)
    beta = 1.0/beta
    #make sure we are in /tip3/ dir
    grid = [0.0 for i in range(gridsize)]
    mayer = [0.00 for i in range(gridsize)]
    b2 = 0.0
    for i in range(gridsize):
        gp = 0.0 + dR * i
        grid[i] = gp
        gp_fmt = '{:.2f}'.format(gp)
        mf = 0.0
        if ( gp < 2.20 ):
            mf = -1.0
        else:
            en_path = "./r_"+str(gp_fmt)+"/en_"+str(gp_fmt)+".dat"
            #print("in file ",en_path)
            df = pd.read_csv(en_path, sep='\n', header=None)
            df_mf = (np.exp(-1.0 * (df - float(en_1b)) * beta) - 1.0)
            mf = df_mf.mean().values[0]
        mayer[i] = mf
        b2 = b2 + gp * gp * mf
    vir[j] = b2 * (-1.0) * 2.0 * np.pi * dR * 0.6022
    #plt.plot(grid, mayer)
    #plt.show()
    #for i in range(gridsize):
        #mayer[i] = mayer[i] * grid[i] * grid[i]
    #print(scipy.integrate.simps(mayer,grid) * (-1.0) * 2.0 * np.pi * 0.6022 )
    print(str(temp[j])+"\t"+str(vir[j]))
print(vir)

