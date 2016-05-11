from edu.strathmore.matrix_processor import MatrixProcessor
from edu.strathmore.module_trainer import ModuleTrainer
import getopt, sys, numpy as np

__author__ = 'smbuthia'


class EventDetector:
    """ This class detects events."""

    def detect_event(self, url, theta):
        mp = MatrixProcessor()
        feature_count = 100
        top_words_file = 'C:/Users/smbuthia/Desktop/My ML Projos/dissertation/accident_top_words.txt'
        feature_arr = mp.get_features_array(top_words_file, feature_count)
        X = mp.get_training_vector(url, feature_arr)
        mt = ModuleTrainer()
        X.insert(0, 1)

        X = np.array(X)
        theta = np.array(theta)
        z = X.dot(theta)
        h = mt.sigmoid(z)
        print(h)
        if h < 0.4:
            return 1
        else:
            return 0


    def label_event(self, event_name, label):
        if label is 1:
            return 'is {e_name}'.format(e_name=event_name)
        elif label is 0:
            return 'is not {e_name}'.format(e_name=event_name)

# load the weight components - theta
num_of_feat = 100
grads = []
gradients_file = 'C:/Users/smbuthia/Desktop/My ML Projos/dissertation/'\
    'gradients - {feat_num}'.format(feat_num=num_of_feat)
with open(gradients_file) as f1:
    i = 0
    for line in f1:
        grads = line.split(',')
weights = []
i = 0
for g in grads:
    weights.insert(i, float(g.rstrip()))
    i += 1

ed = EventDetector()
try:
    opts, args = getopt.getopt(sys.argv[1:], "")
    for arg in args:
        print('{link} {e_label}'.format(link=arg, e_label=ed.label_event('accident', ed.detect_event(arg, weights))))
except getopt.GetoptError as err:
    print(err)
