import lammps_logfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress as linreg

log1 = lammps_logfile.File('log_251.lammps')
log2 = lammps_logfile.File('log_300.lammps')
log3 = lammps_logfile.File('log_301.lammps')
log4 = lammps_logfile.File('log_400.lammps')

T1 = log1.get('Temp')
E1 = log1.get('TotEng')
H1 = log1.get('Enthalpy')

T2 = log2.get('Temp')
E2 = log2.get('TotEng')
H2 = log2.get('Enthalpy')

T3 = log3.get('Temp')
E3 = log3.get('TotEng')
H3 = log3.get('Enthalpy')

T4 = log4.get('Temp')
E4 = log4.get('TotEng')
H4 = log4.get('Enthalpy')

plt.plot(T2, E2, lw=1, color='red', label='E$_{tot}$')
plt.plot(T2, H2, lw=1, color='royalblue', label='H')
plt.xlabel('Temp. [K]')
plt.ylabel('Energy [Kcal/mole]')
plt.legend()
plt.tight_layout()

plt.savefig('melting.pdf')
plt.show()
