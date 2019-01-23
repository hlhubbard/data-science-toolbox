# HH Toolbox

# Distributions.py

## Function random_numbers_from_dist

Function used to draw random numbers from a given distribution

## Required parameters
* size = number of samples
* dist_type = Normal, Poisson or Binomial

## Specific parameters for distributions
Normal:
* mean = mean
* stdev = standard deviation

Poisson:
* p_lambda = lambda, expectation of interval. Default is 1

Binomial:
* n_trials = number of trials
* prob = probability

Output = array of random numbers of a given distribution

### Example input
```
random_numbers_from_dist(1000, 'binomial', n_trials=1, prob=0.5)
random_numbers_from_dist(1000, 'Normal', mean=1, stdev=0.1)
random_numbers_from_dist(1000, 'POISSON')
```

## Class RandomNumbers

### How to use


.(self, size, dist_type, args = {})

.set_args()

.check_args()

.draw_numbers()

.check_numbers()

.summarize()
