
"""
e.g.
Average accross classes:
145 classes with 1 students => 145 student
334 classes with 100+ students => 33400 student

Large classes get oversampled

Class size x gets oversampled by x 

"""


import numpy as np
class BiasChecker:
    def lenght_biased_sampling(self, sample, weight):
        """
        Generate a biased sammple using weight of an unbiased sample.
        sample : unbiased sample as a numpy array
        weight : a weight of sample as a numpy array same size with sample. It can be sample itself!
        """
        n = len(sample)
        p = weight / np.sum(weight)
        return np.random.choice(sample, n, p=p)

