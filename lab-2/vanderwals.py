import numpy as np
import matplotlib.pyplot as plt

T = .9
V = np.linspace(.35, 100, 1000)
P = 8 * T / (3 * V - 1) - 3 / V**2
G = - 8 / 3 * T * np.log(3 * V - 1) - 6 / V + 8 * T * V / (3 * V - 1)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(8, 6))
ax1.plot(V, G, color='red', lw=1)
ax1.set_xlabel('$\hat{V}$')
ax1.set_ylabel('$\hat{G}$')
# ax1.set_xticks(np.arange(0, 7, 2))
# ax1.set_yticks(np.arange(-4.4, -3.8, .2))
# ax1.set_ylim([-4.4, -3.8])

ax2.plot(P, G, color='red', lw=1)
ax2.set_xlabel('$\hat{P}$')
ax2.set_ylabel('$\hat{G}$')
# ax2.set_xticks(np.arange(.4, .9, .2))
# ax2.set_xlim([.4, .9])
# ax2.set_xlim([-6, -5])
# ax2.set_yticks(np.arange(-4.4, -3.8, .2))
# ax2.set_ylim([-4.4, -3.8])
# ax2.set_ylim([-8.2, -8])

ax4.plot(P, V, color='red', lw=1)
ax4.set_xlabel('$\hat{P}$')
ax4.set_ylabel('$\hat{V}$')
# ax4.set_xticks(np.arange(.4, .9, .2))
# ax4.set_xlim([.4, .9])
# ax4.set_yticks(np.arange(0, 7, 2))


fig.tight_layout()
fig.delaxes(ax3)

plt.figure()
T_list = np.arange(.4, 1, .1)
P_list = np.array([.029, .083, .173, .307, .383, .646])
# plt.plot(P, V)
# plt.plot([P_list[5], P_list[5]], [P_list[5], 100])
plt.plot(T_list, P_list, lw=1)
plt.xlabel('$\hat{T}$')
plt.ylabel('$\hat{P}$')
plt.savefig('coexline.pdf')

dV_list = np.array([33.66, 13.43, 6.898, 3.852, 3.647, 1.736])

H = np.diff(P_list) / np.diff(T_list) * T_list[1:] * dV_list[1:]
print(H)
plt.figure()
plt.plot(T_list[1:], H, lw=1)
plt.xlabel('$\hat{T}$')
plt.ylabel('$H_v$')
plt.savefig('hv.pdf')
plt.show()
