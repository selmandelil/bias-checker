
import numpy as np

def lenght_biased_sampling(sample, weight):
    """
    Generate a biased sammple using weight of an unbiased sample.
    sample : numpy array
    weight : numpy array same size with sample.
    """
    n = len(sample)
    p = weight / np.sum(weight)
    return np.random.choice(sample, n, p=p)

