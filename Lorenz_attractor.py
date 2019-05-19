import numpy 
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint 

def function(x, t, sigma, beta, rho):

    dxdt = sigma * (x[1] - x[0])
    dydt = x[0] * (rho - x[2]) - x[1] 
    dzdt = x[0]* x[1] - beta * x[2]

    return([dxdt, dydt, dzdt])

sigma = 10
beta = 8/3
rho = 28
args = tuple((sigma, beta, rho))
time_ = numpy.linspace(0.0, 100, 10000)

# X = [[10, 20, 50], [40, 11, 12], [10, 27, 65], [1,2,3]]
X = [[10, 20, 50]] #Initial Conditions

fig = pyplot.figure()
ax = fig.add_subplot(111, projection = "3d")

for x in X:
    sol = odeint(function, x, time_, args)
    ax.plot(sol[:, 0], sol[:, 1], sol[:, 2], lw = 0.05)

ax.set_xlabel(r"$X$", fontsize = 20)
ax.set_ylabel(r"$Y$", fontsize = 20)
ax.set_zlabel(r"$Z$", fontsize = 20)
pyplot.savefig("butterfly.pdf")
pyplot.show()
pyplot.close()
