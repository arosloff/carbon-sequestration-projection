import numpy

import util
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.model_selection import train_test_split
import pandas as pd

mpl.rcParams['agg.path.chunksize'] = 40000

np.seterr(all='raise')



factor = 2.0

class LinearModel(object):
    """Base class for linear models."""

    def __init__(self, theta=None):
        """
        Args:
            theta: Weights vector for the model.
        """
        self.theta = theta

    def fit(self, X, y):
        """Run solver to fit linear model. You have to update the value of
        self.theta using the normal equations.

        Args:
            X: Training example inputs. Shape (n_examples, dim).
            y: Training example labels. Shape (n_examples,).
        """
        # *** START CODE HERE ***
        X_transpose = np.transpose(X)
        theta = np.linalg.solve(np.dot(X_transpose, X), (np.dot(X_transpose, y)))
        self.theta = theta
        # *** END CODE HERE ***

    def create_poly(self, k, X):
        """
        Generates a polynomial feature map using the data x.
        The polynomial map should have powers from 0 to k
        Output should be a numpy array whose shape is (n_examples, k+1)

        Args:
            X: Training example inputs. Shape (n_examples, 2).
        """
        # *** START CODE HERE ***
        if (k == 0):
            return numpy.ones([X.shape[0],1])
        if (k == 1):
            return X
        else:
            new_x = np.zeros((X.shape[0], k+1), dtype=X.dtype)
            kRange = range(k+1)
            for row in range(new_x.shape[0]):
                kMap = map(lambda x: X[row][1]**x, kRange)
                new_x[row] =list(kMap)
        return new_x
        # *** END CODE HERE ***

    def create_sin(self, k, X):
        """
        Generates a sin with polynomial featuremap to the data x.
        Output should be a numpy array whose shape is (n_examples, k+2)

        Args:
            X: Training example inputs. Shape (n_examples, 2).
        """
        # *** START CODE HERE ***
        if (k == 0):
            new_x = numpy.ones([X.shape[0],2])
            for row in range(new_x.shape[0]):
                new_x[row][1] = np.sin(X[row][1])
            return new_x
        else:
            new_x = np.zeros((X.shape[0], k+2), dtype=X.dtype)
            kRange = range(k+1)
            for row in range(new_x.shape[0]):
                kMap = map(lambda x: X[row][1]**x, kRange)
                sine = np.sin(X[row][1])
                new_x[row] = np.append(list(kMap), sine)
            return new_x
        # *** END CODE HERE ***

    def predict(self, X):
        """
        Make a prediction given new inputs x.
        Returns the numpy array of the predictions.

        Args:
            X: Inputs of shape (n_examples, dim).

        Returns:
            Outputs of shape (n_examples,).
        """
        # *** START CODE HERE ***
        a = np.dot(X, self.theta)
        return a
        # *** END CODE HERE ***


def run_exp(train_path, ks=[1, 2, 5, 10, 20], filename='plot.png'):
    my_data = pd.read_csv(train_path)
    train, test = train_test_split(my_data, test_size=0.2, shuffle=False)
    trainCSV = train.to_csv("train.csv", index=False)
    testCSV = test.to_csv("test.csv", index=False)
    train_x, train_y=util.load_dataset("train.csv",add_intercept=True)
    test_x, test_y=util.load_dataset("test.csv",add_intercept=True)
    # print(train_x.shape)
    # print(train_y.shape)
    #plt.figure()
    #plt.scatter(train_x[:, 1], train_y, c='pink')

    for k in ks:
        '''
        Our objective is to train models and perform predictions on plot_x data
        '''
        # *** START CODE HERE ***
        lin = LinearModel()

        X = lin.create_poly(k, train_x)
        new_plot_x = lin.create_poly(k, test_x)

        lin.fit(X, train_y)
        plot_y = np.transpose(lin.predict(new_plot_x))

        # *** END CODE HERE ***
        '''
        Here plot_y are the predictions of the linear model on the plot_x data
        '''
        # plt.ylim(0, 30000)
        print(f"Theta: {lin.theta}")
        lossVect = np.square(test_y - plot_y)
        loss = (np.sum(lossVect) / test_y.shape[0])
        print(f"Total Mean Squared Loss: {loss}")

    return plot_y[0]

        #plt.plot(np.sort(new_plot_x[:, 1]), plot_y, label='k=%d' % k)
        #plt.yscale("log")
    # plt.title(filename)
    # plt.legend()
    # plt.savefig(filename)
    # plt.clf()


def main():
    '''
    Run all expetriments
    '''
    # *** START CODE HERE ***
    my_data = pd.read_csv(r'D:\Carbon Data\NACP_Forest_Conservation_1662\data\1979-2014 CSVs\clean.csv')
    print(my_data.shape)
    dir = r'D:\Carbon Data\NACP_Forest_Conservation_1662\data\1979-2014 CSVs\FeatureClean\Locations'
    df = pd.DataFrame()
    for loc in my_data:
        print(loc)
        trainFile = f"\data_{loc}.csv"
        agc = run_exp(dir+trainFile, ks=[1], filename = "GPP v. AGC.png")
        d = {'loc': loc, 'agc': agc}
        df.append(d, ignore_index=True)
    df.to_csv('map.csv', index=False)

    np.set_printoptions(suppress=True)

    # *** END CODE HERE ***

if __name__ == '__main__':
    main()