from edu.strathmore.binary_search_tree import BinarySearchTree
from edu.strathmore.word_processor import WordProcessor

__author__ = 'smbuthia'

class MatrixProcessor:
    """Implementation for class that creates training set matrices"""

    def create_training_vector(self, url, features):
        vector = []
        tree = BinarySearchTree()
        word_processor = WordProcessor()
        for word in word_processor.get_words(url):
            tree.insert(word)
        print(len(features))
        for i in range(len(features)):
            print(features[i])
            feat = tree.find(tree.root, features[i])
            if feat is not None:
                vector.insert(i,feat.value)
            else:
                vector.insert(i,0)

        return vector

    def get_features_array(self, file_name, count):
        features = []
        with open(file_name) as f:
            i = 0
            for line in f:
                if i < count:
                    features.insert(i,line.rstrip())
                    i += 1
                else:
                    break
        return features

mp = MatrixProcessor()
vec = mp.create_training_vector('http://www.nation.co.ke/counties/nairobi/One-killed-six-injured-Kamiti-crash/-/1954174/2609334/-/ytl871/-/index.html', mp.get_features_array('C:/Users/smbuthia/Desktop/MachineLearning/My ML Projos/accident_top_words',500))
for v in vec:
    print('{vl} \n'.format(vl=v))