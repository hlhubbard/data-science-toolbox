HH Toolbox
==================

# Distributions

This package allows you to draw random numbers from a given distribution (normal, poisson or binomial) through a function (random_numbers_from_dist) or a Class (RandomNumbers).

## Installation

```
$ pip install data_science_toolbox
```

```
$ python
from hh_toolbox import distributions
```

## Function random_numbers_from_dist

### Example inputs
```python
#Normal distribution
random_numbers_from_dist(size=1000, dist_type='Normal', mean=1, stdev=0.1)
```

```python
#Poisson distribution
random_numbers_from_dist(size=1000, dist_type='poisson', p_lambda=1)
```

```python
#Binomial distribution
random_numbers_from_dist(size=1000, dist_type='binomial', n_trials=1, prob=0.5)
```

## Class RandomNumbers

### Example input
```python
#Normal distribution
rn = distributions.RandomNumbers(size=1000, dist_type='normal', args={'mean': 5, 'stdev': 0.1})
```
```python
#Poisson distribution
rn = distributions.RandomNumbers(size=1000, dist_type='poisson')
```
```python
#Binomial distribution
rn = distributions.RandomNumbers(size=1000, dist_type='binomial', args={'n_trials': 10, 'p': 0.5})
```
### Draw the random numbers depending on distribution specified
```python
rn.draw_numbers()
```
### Change or check the arguments
```python
args = {
    'mean': 5,
    'stdev': 0.1
}
rn.set_args(args)
rn.check_args()
```
### Check the current numbers saved by the number generator
```python
rn.check_numbers()
```
### Calculate the minimum, maximum, mean and standard deviation of the numbers generated
```python
rn.summarize()
```
