import numpy as np
import scipy.optimize as op

__author__ = 'smbuthia'


class ModuleTrainer:
    """Implementation for class that trains the module"""

    def load_training_data(self, filename, n):
        data = np.loadtxt(filename, delimiter=',')
        return data[:, 0:n], data[:, data.shape[1]-1]

    def sigmoid(self, z):
        deno = 1 + np.exp(-1.0 * z)
        return 1.0/deno

    def compute_cost(self, theta, X, y):
        m = X.shape[0]
        z = X.dot(theta)
        J = (1./m)*(-np.transpose(y).dot(self.safe_log(self.sigmoid(z))) - np.transpose(1-y).dot(self.safe_log(1 - self.sigmoid(z))))
        grad = np.transpose((1./m) * np.transpose(self.sigmoid(z) - y).dot(X))
        return J, grad

    def compute_cost_reg(self, theta, X, y, lambda_):
        J, grad = self.compute_cost(theta, X, y)
        theta_reg = theta
        theta_reg[0] = 0
        m = X.shape[0]
        J = J + ((lambda_/(2 * m)) * np.sum(np.square(theta_reg)))
        grad = grad + ((lambda_/m) * theta_reg)
        return J, grad

    def safe_log(self, x):
        return np.log(x.clip(min=0.00000001))

    def predict(self, theta, X, threshold):
        # z = np.dot(X, theta)
        z = X.dot(theta)
        h = self.sigmoid(z)
        h[h > threshold] = 1
        h[h <= threshold] = 0
        return h

    def accuracy(self, theta, X_test, y_test, threshold):
        h = self.predict(theta, X_test, threshold)
        return np.mean(np.float32(h == y_test)) * 100

"""
trainer = ModuleTrainer()
num_of_feat = 100
m = 125
m_cv = np.int((m/0.6)*0.2)
raw_data_file = 'C:/Users/smbuthia/Desktop/My ML Projos/dissertation/accident_ready_data_set_100.txt'
X_init, y_init = trainer.load_training_data(raw_data_file, num_of_feat)
X = X_init[0:m, :]
y = y_init[0:m]
if m > X.shape[0]:
    m = X.shape[0]
X = np.column_stack([np.ones(m), X])
n = X.shape[1]
lambda_1 = 10000
initial_theta = np.zeros(n)
J, grad = trainer.compute_cost_reg(initial_theta, X, y, lambda_1)
print('The regularized initial cost is: {cost}'.format(cost=J))
print('The regularized initial gradient is: {g}'.format(g=grad))


def cost_function(theta):
    cost, gradient = trainer.compute_cost(theta, X, y)
    return cost


def cost_function_reg(theta):
    cost, gradient = trainer.compute_cost_reg(theta, X, y, lambda_1)
    return cost

result = op.fmin_bfgs(cost_function_reg, initial_theta, maxiter=400)
final_cost, final_grad = trainer.compute_cost_reg(result, X, y, lambda_1)
print('The regularized final cost will be: {cst}'.format(cst=final_cost))
print('The regularized final gradient will be: {fgrad}'.format(fgrad=final_grad))
"""
# write this vector to a file to be used for other predictions
"""
gradients_file = 'C:/Users/smbuthia/Desktop/My ML Projos/dissertation/'\
                 'gradients - {feat_num}'.format(feat_num = num_of_feat)
with open(gradients_file, 'a+') as f1:
    f1.write(','.join([str(x) for x in final_grad]))
"""
"""
if m+m_cv < X_init.shape[0]:
    last_m = m+m_cv
    X_cv = X_init[m:last_m, :]
    y_cv = y_init[m:last_m]
    # print('Dimensions for X_cv: {xcv_d}'.format(xcv_d=X_cv.shape))
    # print('Dimensions for y_cv: {ycv_d}'.format(ycv_d=y_cv.shape))
    # print('Value of m_cv : {mcv_d}'.format(mcv_d=m_cv))
    X_cv = np.column_stack([np.ones(m_cv), X_cv])
    n_cv = X_cv.shape[1]
    acc = trainer.accuracy(result, X_cv, y_cv, 0.5)
    print('The accuracy is {accu}'.format(accu=acc))
else:
    print('Cannot test the accuracy because the data set is too small.')
"""