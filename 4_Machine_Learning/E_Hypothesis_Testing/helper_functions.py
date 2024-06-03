import pandas as pa
import numpy as np
import scipy.stats
from scipy.stats import ttest_1samp 

# returns confidence intervall based on observations and provided confidence_level
def get_confidence_interval(observations, confidence_level):
    return scipy.stats.t.interval(confidence_level, len(observations) - 1, np.mean(observations), scipy.stats.sem(observations))