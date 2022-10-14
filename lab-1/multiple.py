import lammps_logfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress as linreg

log = lammps_logfile.File("log.lammps")

_E_mol = log.get('E_mol')
_E_pair = log.get('E_pair')
_P = log.get('Press')
_T = log.get('Temp')
_E_tot = log.get('TotEng')

E_mol = _E_mol[1:]
E_pair = _E_pair[1:]
P = _P[1:]
T = _T[1:]
E_tot = _E_tot[1:]

rho = 0.001
Z = P / (rho * T)
x = np.arange(len(Z))

data_1 = linreg(T, E_tot)
data_2 = linreg(x, Z)


print(f'T=10, c_v={data_1.slope:.3f} +/- {data_1.stderr:.3e}')
print(f'Z={data_2.intercept:.3f} +/- {data_2.intercept_stderr:.3e}')

rho = np.array([.32, .426, .532, .683, .744, .850])
cv = np.array([1.772, 1.705, 1.663, 1.608, 1.616, 1.802])
z = np.array([211.223, 325.7, 515.068, 972.107, 1847.774, 3545.913])

plt.plot(rho, cv, color='red', marker='o', label='$c_V$')
plt.plot(rho, z, color='royalblue', marker='o', label='Z')

plt.xlabel('$\\rho$')
plt.legend()
# plt.savefig('rho_varies.pdf')
plt.show()
