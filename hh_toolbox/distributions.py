import numpy as np

class RandomNumbers:

    def __init__(self, size, dist_type, args = {}):
        self.size = size
        self.dist_type = dist_type
        self.args = args
        self.output = None
        self.summary = {}

    def set_args(self, args):
        self.args = args

    def check_args(self):

        return self.args

    def draw_numbers(self):
        if self.dist_type.lower() == 'normal':
            if self.args.get('mean') == None or self.args.get('stdev') == None:
                raise ValueError('Please set the mean and standard dev (stdev) in args')
            self.output = np.random.normal(self.args['mean'], self.args['stdev'], self.size)

        elif self.dist_type.lower() == 'poisson':
            if self.args.get('p_lambda') == None:
                self.args['p_lambda'] = 1
            self.output = np.random.poisson(self.args['p_lambda'], self.size)

        elif self.dist_type.lower() == 'binomial':
            if self.args.get('n_trials') == None or self.args.get('prob') == None:
                raise ValueError('Please set the number of trials (n_trials) and probability (prob) in args')
            self.output = np.random.binomial(self.args['n_trials'], self.args['prob'], self.size)

        return self.output

    def check_numbers(self):

        return self.output

    def summarize(self):
        if self.output is None:
            return self.summary
        self.summary['min'] = self.output.min()
        self.summary['max'] = self.output.max()
        self.summary['mean'] = self.output.mean()
        self.summary['stdev'] = self.output.std()

        return self.summary
