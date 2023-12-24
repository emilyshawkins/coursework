import numpy as np
import matplotlib.pyplot as plt

def popHistogram(population_data, dataset):
    '''
    Input:
        population_data (ndarray): An array of all observations from population
        dataset (int): Which population the data is from

    Output:
        Return: None

    Displays a histogram for the population data
    '''

    fig, ax = plt.subplots(1, 1)
    ax.hist(population_data)
    ax.set_title(f'Population {dataset} Daily Income')
    ax.set_xlabel('Daily Income (x)')
    ax.set_ylabel('frequency (y)')
    plt.show()

def sampleMeanSDHistogram(population, n, k, dataset):
    
    '''
    Input:
        population (ndarry): The data set to be sampled from
        n (int): The size of a generated sample
        k (int): The number of samples to generate
        dataset (int): Which dataset the population is from

    Output:
        Return: Generated samples

    Generates k samples of n size, calculates the sample mean and standard deviation of each sample, and displays histograms
    with frequencies of the sample means and standard deviations.
    '''
    sample = np.random.choice(population, (k, n), replace=True)
    sample_means = np.mean(sample, axis=1)
    sample1_sds = np.std(sample, axis=1, ddof=1)

    fig, ax = plt.subplots(1, 2)
    ax[0].hist(sample_means)
    ax[0].set_title(f'Population {dataset}: n = {n}, k = {k}')
    ax[0].set_xlabel('Sample Mean')
    ax[0].set_ylabel('frequency')
    ax[1].hist(sample1_sds)
    ax[1].set_title(f'Population {dataset}: n = {n}, k = {k}')
    ax[1].set_xlabel('Sample Standard Deviation')
    ax[1].set_ylabel('frequency')
    plt.show()

    return sample

def sampleMeanExpectedValue(samples, k):

    '''
    Input: 
        samples (ndarray): Generated sample
        k (int): The number of generated samples

    Output:
        Return: Expected value of the sample mean for the generated samples
    '''
    sample_means = np.mean(samples, axis=1)
    return sum(sample_means) / k

def sampleMeanSD(samples):
    '''
    Input: 
        sample (ndarray): Generated samples

    Output:
        Return: Standard deviation of the sample mean
    '''
    sample_means = np.mean(samples, axis=1)
    return np.std(sample_means)

def sampleSDExpectedValue(samples, k):
    '''
    Input: 
        sample (ndarray): Generated samples

    Output:
        Return: Expected standard deviation of the samples
    '''
    sample_sd = np.std(samples, axis=1, ddof=1)
    return sum(sample_sd) / k

def main():

    data1 = np.loadtxt('data1.txt') # Store data into an array

    # Generate Population 1 Histogram
    popHistogram(data1, 1)

    # Calculate mean and sd of Population 1
    pop1_mean = np.mean(data1)
    print('Population 1: Daily Income Mean =', pop1_mean)
    pop1_sd = np.std(data1)
    print('Population 1: Daily Income Standard Deviation =', pop1_sd)

    # Generate random samples and histogram
    n_k = [(2, 10), (2, 100), (2, 1000),
           (20, 100), (20, 1000),
           (200, 100), (200, 1000)]
    
    for (n, k) in n_k:
        print(f'n = {n}, k = {k}')
        samples = sampleMeanSDHistogram(data1, n, k, 1)

        expectedMeanValue = sampleMeanExpectedValue(samples, k)
        print(f'    E(x bar) = {expectedMeanValue}')

        sampleMean_SD = sampleMeanSD(samples)
        print(f'    S(x bar) = {sampleMean_SD}')

        expectedSD = sampleSDExpectedValue(samples, k)
        print(f'    E(s) = {expectedSD}')

    print()

    data2 = np.loadtxt('data2.txt') # Store data into an array

    # Generate Population 2 Histogram
    popHistogram(data2, 2)

    # Calculate mean and sd of Population 1
    pop2_mean = np.mean(data2)
    print('Population 2: Daily Income Mean =', pop2_mean)
    pop2_sd = np.std(data2)
    print('Population 2: Daily Income Standard Deviation =', pop2_sd)

    # Generate random samples and histogram
    n_k = [(2, 10), (2, 100), (2, 1000),
           (20, 100), (20, 1000),
           (200, 100), (200, 1000)]
    
    for (n, k) in n_k:
        print(f'n = {n}, k = {k}')
        samples = sampleMeanSDHistogram(data2, n, k, 2)

        expectedMeanValue = sampleMeanExpectedValue(samples, k)
        print(f'    E(x bar) = {expectedMeanValue}')

        sampleMean_SD = sampleMeanSD(samples)
        print(f'    S(x bar) = {sampleMean_SD}')

        expectedSD = sampleSDExpectedValue(samples, k)
        print(f'    E(s) = {expectedSD}')

main()
