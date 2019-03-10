import matplotlib.pyplot as plt
from brian2 import *

def main():

	#start_scope()
	## All it does is make sure that any Brian objects 
	## created before the function is called aren’t included 
	## in the next run of the simulation.

	N=100
	tau = 5*ms
	eqs = '''dv/dt = (1-v)/tau : 1'''
	G = NeuronGroup(N, eqs, threshold= 'v>0.5', reset='v=0', method='exact')
	G.v = 'rand()'

	spikemon = SpikeMonitor(G)

	run(50*ms)
	plt.plot(spikemon.t/ms, spikemon.i, '.k')
	
	plt.show()

		
	

if __name__=='__main__':
	main()


