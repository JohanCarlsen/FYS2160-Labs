import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress as lin_reg
import scipy.constants as const

R = const.R

def Temp(ohm):

    r = ohm / 1e5

    return 25 - 24 * np.log(r)


def c_id(f, T, M_mol):

    return np.sqrt((f+2) * R * T / (f * M_mol)) - 273.15


def linreg(K):

    N = len(K)
    x = np.arange(1, N + 1)

    res = lin_reg(x, K)

    return res.slope, res.stderr, res.intercept


def c_expr(slope, L):

    return slope * 2 * L


def uncerteinty(L, dL, a, da):

    return np.sqrt((2 * L * da)**2 + (2 * a * dL)**2)


def measure(ohm, f, M_mol, K, L, dL, gasname):

    T = Temp(ohm)
    N = len(K)

    c_ideal = c_id(f, T, M_mol)
    slope, stderr, intercept = linreg(K)
    c_expriment = c_expr(slope, L)
    err = uncerteinty(L, dL, slope, stderr)

    x = np.arange(1, N+1)

    fig, ax = plt.subplots()

    if gasname == 'CO2':

        ax.set_title(f'CO$_2$ at $T=$ {T:.3f} K')

    else:

        ax.set_title(gasname + f' at $T=$ {T:.3f} K')

    ax.plot(x, slope * x + intercept, lw=1, ls='dashed', color='red', label='Linear regression')
    ax.scatter(x, K, color='black', label='Data points')
    plt.text(7, 500, f'$c=${c_expriment:.3f} $\pm$ {err:.3f} m/s')

    ax.set_xlabel('N')
    ax.set_ylabel('Phase resoonance frequency')
    ax.legend()

    fig.tight_layout()

    plt.savefig(f'{gasname}_at_T_{int(T)}.pdf')

K1 = [122, 177, 268, 386, 521, 651, 774, 903, 1032, 1160, 1290, 1419, 1547, 1675]
ohm_1 = 1.16
f_1 = 3
mMol_1 = 39.948 / 1e3
L1 = 1.243
name_1 = 'Argon'

K2 = [142, 285, 417, 561, 698, 836, 975, 1113, 1252, 1392, 1530, 1671, 1809, 1947]
ohm_2 = 1.13
f_2 = 5
mMol_2 = 28.97 / 1e3
L2 = 1.243
name_2 = 'Air'

K3 = [151.88, 303.88, 458.88, 605.88, 754.88, 903.88, 1053.88, 1203.88, 1355.88, 1505.88]
ohm_3 = .197
f_3 = 5
mMol_3 = mMol_2
L3 = 1.244
name_3 = 'Air'

K4 = [316.2, 449.2, 590.2, 733.2, 877.2, 1021.2, 1165.2, 1311.2, 1457.2, 1600.2, 1746.2, 1887.2]
ohm_4 = .463
f_4 = 5
mMol_4 = mMol_2
L4 = 1.244
name_4 = 'Air'

K5 = [102, 151, 227, 326, 431, 545, 651, 758, 864, 972, 1079, 1187, 1296, 1404]
ohm_5 = .116
f_5 = 5
mMol_5 = 44.01 / 1e3
L5 = 1.243
name_5 = 'CO2'

measure(ohm_1, f_1, mMol_1, K1, L1, 1.5e-3, name_1)
measure(ohm_2, f_2, mMol_2, K2, L2, 1.5e-3, name_2)
measure(ohm_3, f_3, mMol_3, K3, L3, 1.5e-3, name_3)
measure(ohm_4, f_4, mMol_4, K4, L4, 1.5e-3, name_4)
measure(ohm_5, f_5, mMol_5, K5, L5, 1.5e-3, name_5)

plt.show()
