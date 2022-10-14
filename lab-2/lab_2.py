import lammps_logfile
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress as linreg

log1 = lammps_logfile.File('log.lammps1')
log2 = lammps_logfile.File('log.lammps2')
log3 = lammps_logfile.File('log.lammps3')
log4 = lammps_logfile.File('log.lammps4')

def plot(log_file, title, labels, ax):

    log = lammps_logfile.File(log_file)
    T = log.get('Temp')
    E = log.get('TotEng')
    H = log.get('Enthalpy')

    ax.set_title(title)
    ax.plot(T, E, color='red', lw=1, label='E$_{tot}$')
    ax.plot(T, H, color='royalblue', lw=1, label='H')
    ax.set_xlabel(labels[1])
    ax.set_ylabel(labels[0])
    ax.legend()

fig, axes = plt.subplots(2, 2, figsize=(8, 6))
plt.suptitle('Energies vs temperature')

filename = 'log.lammps'
phases = ['Ice', 'Melting ice', 'Evaporating water', f'NPT at $T={383}$ K']
labels = ['Energy', 'Temp [K]']

for i in range(2):
    for j in range(2):

        no = j + 1 + 2 * i
        log_file = filename + f'{no}'
        ax = axes[i, j]

        plot(log_file, phases[no - 1], labels, ax)

fig.tight_layout()
# plt.savefig('energy_plot.pdf')
plt.show()
