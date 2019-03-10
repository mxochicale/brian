import matplotlib.pyplot as plt
from brian2 import *

def main():

	#start_scope()
	## All it does is make sure that any Brian objects 
	## created before the function is called aren’t included 
	## in the next run of the simulation.

	N=100
	tau = 10*ms
	v0_max=3
	duration = 1000*ms

	eqs = '''
	dv/dt = (v0-v)/tau : 1 (unless refractory)
	v0:1
	'''

	G = NeuronGroup(N, eqs, threshold= 'v>1', reset='v=0', refractory=5*ms, method='exact')
	M = SpikeMonitor(G)

	G.v0 = 'i*v0_max/(N-1)'
	
	run(duration)
	

	figure(figsize=(12,4))
	subplot(121)
	plt.plot(M.t/ms, M.i, '.k')#raster plot
	xlabel('Time (ms)')
	ylabel('Neuron index')
	subplot(122)
	plt.plot(G.v0, M.count/duration)
	xlabel('v0')
	ylabel('Firing rate (sp/s)')
	plt.show()

		
	

if __name__=='__main__':
	main()


