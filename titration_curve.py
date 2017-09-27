from pHcalc.pHcalc import Acid, Neutral, System
import numpy as np
import matplotlib.pyplot as plt

hcl_volumes = np.linspace(0, 20, 500)   # array of HCL volumes
concHcl = 0.1   # mol/liter
sol_volume = 10   # 10ml
naoh = Neutral(charge=1, conc=0.1)

pHsys = []
for vol in hcl_volumes:
    hcl = Neutral(charge=-1, conc=concHcl*vol/(sol_volume))
    system = System(naoh, hcl)
    system.pHsolve(guess_est=True)
    pHsys.append(system.pH)

plt.grid()
plt.grid(b=True, which='both', color='0.65', linestyle='-')
plt.plot(hcl_volumes, pHsys)
plt.title(u"Кривая титрования")
plt.xlabel(u"V(HCL), мл")
plt.ylabel(u"pH р-ра")
plt.ylim(0, 14)
plt.figtext(.23, .83, 'NaOH')
plt.figtext(.73, .19, "NaCL+HCL")

plt.show()
