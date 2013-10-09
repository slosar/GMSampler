GMSampler
=========

Gaussian Mixtures Sampler

See testgame.py for use example.

This is work in progress and I am a spaghetti coder.

You supply a starting point and an idea of errors on parameters to regularize covariance matrix.
The likelihood function takes a list of parameter vectors and returns a list of log likelihoods results - to help parallize shit.

User serviceable part:
  
self.N1=1000 ## how many samples for each Gaussian

# some times we have *fast* parameters aka cosmomic (i.e. parameters whose change is cheap in term of calculating likelihood)
# we want to oversample those
self.N1f=4 ## subsample fast how much
self.fastpars=None ### which are fast parameters

# the parameter below should really be more like 1 or 1.1 for N>10
self.blow=2.0 ## factor by which to increase the enveloping Gauss

# this now determines when to stop. Set to a number >>1.
# at 5000 one gets pretty good sampling.
self.mineffsamp=5000 ### minimum number effective samples that we require

### do not try to lear cov yourself
self.fixedcov=False
### instead us this one
self.fixedcovuse=None

#### maximum number of gaussians
self.maxiter=30

### hard parmeter priors
self.priorlow=None
self.priorhigh=None

### spit put /tmp/game.pickle every 100 Gaussians
self.pickleBetween=False
