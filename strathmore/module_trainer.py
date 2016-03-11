from numpy import loadtxt, where, transpose, dot, zeros, ones, log
import numpy as np
import scipy.optimize as op

__author__ = 'smbuthia'


class ModuleTrainer:
    """Implementation for class that trains the module"""

    def load_training_data(self, filename, number_of_features):
        data = loadtxt(filename, delimiter=',')
        return data[:,0:number_of_features], data[:,number_of_features]

    def sigmoid(self, z):
        deno = 1 + np.exp(-1.0 * z)
        return 1.0/deno

    def compute_cost(self, theta, X, y):
        m = X.shape[0]
        z = X.dot(theta)
        J = (1./m)*(-transpose(y).dot(self.safe_log(self.sigmoid(z))) - transpose(1-y).dot(self.safe_log(1 - self.sigmoid(z))))
        grad = transpose((1./m) * transpose(self.sigmoid(z) - y).dot(X))
        return J, grad

    def safe_log(self, x):
        return np.log(x.clip(min=0.00000001))

    def predict(self, theta, X, threshold):
        z = X.dot(theta)
        h = self.sigmoid(z)
        h[h > threshold] = 1
        h[h <= threshold] = 0
        return h

    def accuracy(self, theta, X_test, y_test, threshold):
        h = self.predict(theta, X_test, threshold)
        return np.mean(np.double(h == y_test)) * 100


trainer = ModuleTrainer()
X, y = trainer.load_training_data('C:/Users/smbuthia/Desktop/MachineLearning/My ML Projos/accident_ready_data_set.txt', 85)
# X, y = trainer.load_training_data('C:/Users/smbuthia/Desktop/MachineLearning/ex2/ex2data1.txt', 2)
m = X.shape[0]
X = np.column_stack([ones(m), X])
n = X.shape[1]
initial_theta = zeros(n)
J, gradient = trainer.compute_cost(initial_theta, X, y)
print('The initial cost is: {cost}'.format(cost=J))
print('The initial gradient is: {g}'.format(g=gradient))


def cost_function(theta):
    cost, gradient = trainer.compute_cost(theta, X, y)
    return cost

result = op.fmin_bfgs(cost_function, initial_theta, maxiter=400)
final_cost, final_grad = trainer.compute_cost(result, X, y)
print('The final cost will be: {cst}'.format(cst=final_cost))
print('The final gradient will be: {fgrad}'.format(fgrad=final_grad))
