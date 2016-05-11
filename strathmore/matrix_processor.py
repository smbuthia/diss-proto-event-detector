from edu.strathmore.binary_search_tree import BinarySearchTree
from edu.strathmore.word_processor import WordProcessor
import time

__author__ = 'smbuthia'


class MatrixProcessor:
    """Implementation for class that creates training set matrices"""

    def get_training_vector(self, url, features):
        vector = []
        tree = BinarySearchTree()
        word_processor = WordProcessor()
        for word in word_processor.get_words(url):
            tree.insert(word)
        for i in range(len(features)):
            feat = tree.find(tree.root, features[i])
            if feat is not None:
                vector.insert(i, feat.value)
            else:
                vector.insert(i, 0)

        return vector

    def get_features_array(self, file_name, count):
        features = []
        with open(file_name) as f:
            i = 0
            for line in f:
                if i < count:
                    features.insert(i, line.rstrip())
                    i += 1
                else:
                    break
        return features

# get the start time
"""
start_time = time.time()
mp = MatrixProcessor()
feature_count = 100
top_words_file = 'C:/Users/smbuthia/Desktop/My ML Projos/dissertation/accident_top_words.txt'
feature_arr = mp.get_features_array(top_words_file, feature_count)

data_file = 'C:/Users/smbuthia/Desktop/My ML Projos/dissertation/accidents_data.txt'
ready_data_file = 'C:/Users/smbuthia/Desktop/My ML Projos/dissertation/accident_ready_data_set_{ct}.txt'\
                  .format(ct=feature_count)
with open(data_file) as f1, open(ready_data_file, 'a+') as f2:
    for line in f1:
        vec = []
        l = line.split(' ', 1)
        url = l[0]
        label = l[1]
        vec = mp.get_training_vector(url, feature_arr)
        vec.append(label)
        f2.write(','.join([str(x) for x in vec]))
"""
# print the total time taken to run
"""
print('Total run time = {run_time}'.format(run_time=time.time() - start_time))
"""