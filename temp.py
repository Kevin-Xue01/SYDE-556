import nengo

model = nengo.Network()
with model:
    stim = nengo.Node([0])
    a = nengo.Ensemble(n_neurons=20, dimensions=1)

    nengo.Connection(stim, a)
    
    def square(x):
        return x[0]*x[0]
    b = nengo.Ensemble(22, 1)
    nengo.Connection(a, b, function=square, synapse=0.1)
    
    
