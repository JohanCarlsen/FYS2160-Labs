# We want to extract the thermodynamic data from the file log.lammps
import lammps_logfile
import matplotlib.pyplot as plt

log = lammps_logfile.File("log.lammps")

step = log.get("Step")
pressure = log.get("Press")
temperature = log.get("Temp")
totEnergy = log.get("TotEng")

plt.plot(step, temperature)
plt.show()
