


import matplotlib.pyplot as plt
from brian2 import *

def main():

	start_scope()
	# All it does is make sure that any Brian objects 
	# created before the function is called aren’t included 
	# in the next run of the simulation.

	tau = 10*ms
	eqs = '''dv/dt = (1-v)/tau : 1'''
	G = NeuronGroup(1, eqs, method='exact')
	M = StateMonitor(G, 'v', record=True)
	run(30*ms)
	plt.plot(M.t/ms, M.v[0])
	plt.show()



if __name__=='__main__':
	main()


