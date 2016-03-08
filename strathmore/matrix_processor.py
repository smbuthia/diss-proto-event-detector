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

        for i in len(features):
            vector[i] = tree.find(tree.root, features[i]).value
        return vector

    def get_features_array(self, file_name, count):
        features = []
        with open(file_name) as f:
            i = 0
            for line in f:
                if i < count:
                    features[i] = line
                    i += 1
                else:
                    break
        return features