# We want to extract the thermodynamic data from the file log.lammps
import lammps_logfile
import matplotlib.pyplot as plt


log = lammps_logfile.File("log.lammps_ORIGINAL")
keyWords = log.get_keywords()

# print(keyWords)
'''['E_mol', 'E_pair', 'Press', 'Step', 'Temp', 'TotEng']'''

E_mol = log.get('E_mol')
E_pair = log.get('E_pair')
press = log.get('Press')
step = log.get('Step')
temp = log.get('Temp')
totEng = log.get('TotEng')

avgE_mol = lammps_logfile.running_mean(E_mol, 100)
avgE_pair = lammps_logfile.running_mean(E_pair, 100)
avgPress = lammps_logfile.running_mean(press, 100)
avgTemp = lammps_logfile.running_mean(temp, 100)
avgTotEng = lammps_logfile.running_mean(totEng, 100)
