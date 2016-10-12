import scipy.stats
import numpy as np

def proportions_diff_z_stat_ind(sample1, sample2):
    '''
    Computes z-statistic for two samples of binary variables.
    :param sample1 (list or array) - first binary array
    :param sample2 (list or array) - second binary array
    
    :return Z statistic (float)
    '''
    n1 = len(sample1)
    n2 = len(sample2)
    
    p1 = float(sum(sample1)) / n1
    p2 = float(sum(sample2)) / n2 
    P = float(p1*n1 + p2*n2) / (n1 + n2)
    
    return (p1 - p2) / np.sqrt(P * (1 - P) * (1. / n1 + 1. / n2))


def proportions_diff_z_test(z_stat, alternative = 'two-sided'):
    '''
    :param z_stat (float) - Z-statistic computed for 2 binary vectors
    :alternative (str) - 'two-sided', 'less' or 'greater'
    
    :return p-value (float)
    '''
    if alternative not in ('two-sided', 'less', 'greater'):
        raise ValueError("alternative not recognized\n"
                         "should be 'two-sided', 'less' or 'greater'")
    
    if alternative == 'two-sided':
        return 2 * (1 - scipy.stats.norm.cdf(np.abs(z_stat)))
    
    if alternative == 'less':
        return scipy.stats.norm.cdf(z_stat)

    if alternative == 'greater':
        return 1 - scipy.stats.norm.cdf(z_stat)