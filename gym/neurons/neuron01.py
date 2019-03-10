

import matplotlib.pyplot as plt
from brian2 import *

def main():

	#start_scope()
	# All it does is make sure that any Brian objects 
	# created before the function is called aren’t included 
	# in the next run of the simulation.

	tau = 10*ms
	eqs = '''
	dv/dt = (sin(2*pi*100*Hz*t)-v)/tau : 1
	'''
	# Integrator Euler method
	G = NeuronGroup(1, eqs, method='euler')
	M = StateMonitor(G, 'v', record=0)
	G.v=5#Initial value

	run(60*ms)
	plt.plot(M.t/ms, M.v[0])
	xlabel('Time (ms)')
	ylabel('v');
	plt.show()


if __name__=='__main__':
	main()


