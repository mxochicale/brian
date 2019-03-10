import matplotlib.pyplot as plt
from brian2 import *

def main():

	#start_scope()
	## All it does is make sure that any Brian objects 
	## created before the function is called aren’t included 
	## in the next run of the simulation.

	tau = 5*ms
	eqs = '''dv/dt = (1-v)/tau : 1'''
	#G = NeuronGroup(1, eqs, threshold= 'v>0.5', reset='v=0', method='exact')
	G = NeuronGroup(1, eqs, threshold='v>0.8', reset='v = 0', refractory=15*ms, method='exact')

	statemon = StateMonitor(G, 'v', record=0)
	spikemon = SpikeMonitor(G)

	run(50*ms)
	plt.plot(statemon.t/ms, statemon.v[0])
	for t in spikemon.t:
		axvline(t/ms, ls='--', c='C1', lw=3)
	axhline(0.8, ls=':', c='C2', lw=3)
	xlabel('Time (ms)')
	ylabel('v')

	
	plt.show()

		
	

if __name__=='__main__':
	main()


