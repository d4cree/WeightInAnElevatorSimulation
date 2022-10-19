from numpy import *
from matplotlib import pyplot as plt

m = 70.0 # masa coveka
M = 2000.0 # masa lifta
k = 20000.0 # konstanta istezanja opruge
L0 = 0.1 
g = 9.81 # ubrzanje gravitacionog polja
T = (m+M)*g # sila zatezanja konopca
dT = 4000.0 # delta T
T = T + dT
time = 1.0
dt = 0.0001 # vremenski korak
n = round(time/dt)
N = linspace(0, n, n)
xL = zeros_like(N) # x lift
VL = zeros_like(N) # brzina lifta
aL = zeros_like(N) # ubrzanje lifta
xC = zeros_like(N) # x coveka
VC = zeros_like(N) # brzina coveka
aC = zeros_like(N) # ubrzanje coveka
t = zeros_like(N) # vremenski interval
Cp = zeros_like(N) # Sila tezine N

xL[1] = 0.0
VL[1] = 0.0

xC[1] = xL[1]+L0-m*g/k
VC[1] = 0.0
Cp[1] = 0.0

for i in range(1, n-1):
    aL[i] = (T-M*g+k*(xC[i]-xL[i]-L0))/M
    VL[i+1] = VL[i] + aL[i]*dt
    xL[i+1] = xL[i] + VL[i+1]*dt
    aC[i] = (-k*(xC[i]-xL[i]-L0)-m*g)/m
    VC[i+1] = VC[i] + aC[i]*dt
    xC[i+1] = xC[i] + VC[i+1]*dt
    t[i+1] = t[i] + dt
    Cp[i] = -k*(xC[i]-xL[i]-L0)


plt.figure()
plt.plot(t, Cp)
plt.xlabel('t[s]')
plt.ylabel('N[N]')
plt.grid()

plt.figure()
plt.plot(t, xL, 'b')
plt.plot(t, xC, 'r')
plt.xlabel('t[s]')
plt.ylabel('x[m]')
plt.grid()
plt.show()



