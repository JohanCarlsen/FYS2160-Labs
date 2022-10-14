# We want to extract the thermodynamic data from the file log.lammps
import lammps_logfile
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress as linreg


log = lammps_logfile.File("log.lammps")
keyWords = log.get_keywords()

# print(keyWords)
'''['E_mol', 'E_pair', 'Press', 'Step', 'Temp', 'TotEng']'''

_E_mol = log.get('E_mol')
_E_pair = log.get('E_pair')
_P = log.get('Press')
_step = log.get('Step')
_T = log.get('Temp')
_E_tot = log.get('TotEng')

# From looking at the file "log.lammps_ORIGINAL", the correct values start at
# index 6
E_mol = _E_mol[1:]
E_pair = _E_pair[1:]
P = _P[1:]
t = _step[1:] - 101000
T = _T[1:]
E_tot = _E_tot[1:]

# Taking the average w/ 100 elements, not sure we need it.
avgE_mol = lammps_logfile.running_mean(E_mol, 100)
avgE_pair = lammps_logfile.running_mean(E_pair, 100)
avgPress = lammps_logfile.running_mean(P, 100)
avgTemp = lammps_logfile.running_mean(T, 100)
avgTotEng = lammps_logfile.running_mean(E_tot, 100)

# Make a subplot of each value from the .log file
# fig = plt.figure(figsize=(11, 6.5))
# ax1 = plt.subplot2grid((2, 6), (0, 0), colspan=2)
# ax2 = plt.subplot2grid((2, 6), (0, 2), colspan=2)
# ax3 = plt.subplot2grid((2, 6), (0, 4), colspan=2)
# ax4 = plt.subplot2grid((2, 6), (1, 1), colspan=2)
# ax5 = plt.subplot2grid((2, 6), (1, 3) , colspan=2)
#
# ax1.plot(t, E_mol, color='k', lw=.8)
# ax1.set_title('$E_{mol}$')
# ax1.set_xlabel('$t$')
# ax1.set_ylabel('$E$')
#
# ax2.plot(t, E_pair, color='k', lw=.8)
# ax2.set_title('$E_{pair}$')
# ax2.set_xlabel('$t$')
# ax2.set_ylabel('$E$')
#
# ax3.plot(t, P, color='k', lw=.8)
# ax3.set_title('Pressure')
# ax3.set_xlabel('$t$')
# ax3.set_ylabel('$P$')
#
# ax4.plot(t, T, color='k', lw=.8)
# ax4.set_title('Temperature')
# ax4.set_xlabel('$t$')
# ax4.set_ylabel('$T$')
#
# ax5.plot(t, E_tot, color='k', lw=.8)
# ax5.set_title('Total energy')
# ax5.set_xlabel('$t$')
# ax5.set_ylabel('$E$')
#
# plt.tight_layout()

# Now, let's solve the first task. We want to find the heat capacity C_V at
# constant volume. This is done w/ dU/dT
data = linreg(T, E_tot)

plt.figure()
plt.scatter(T, E_tot, color='k', s=2, label='Data points')
plt.plot(T, data.slope * T + data.intercept, color='r', label='Linear regression')
plt.text(1.3, 1.6, f'$C_V=${data.slope:.3f} $\pm$ {data.stderr:.3e}')

plt.xlabel('$T$')
plt.ylabel('$E$')

plt.legend()
plt.savefig('cv_9.pdf')
plt.tight_layout()

rho = .001
Z = P / (rho * T)
x = np.arange(len(Z))

data_2 = linreg(x, Z)

plt.figure()

plt.scatter(x, Z, color='k', s=1, label='Data points')
plt.plot(x, data_2.slope * x + data_2.intercept, color='red', label='Linear regression')
plt.text(200, .98, f'$Z=${data_2.intercept:.3f} $\pm$ {data_2.intercept_stderr:.3e}')

plt.xlabel('Data points')
plt.ylabel('Virial expansion')

plt.legend()
plt.savefig('z_9.pdf')



plt.show()
