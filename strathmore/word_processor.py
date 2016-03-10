import urllib.request
from bs4 import BeautifulSoup
from nltk.tokenize import WordPunctTokenizer, RegexpTokenizer
from nltk.corpus import stopwords
from edu.strathmore.replacers import RegexpReplacer, RepeatReplacer
from edu.strathmore.binary_search_tree import BinarySearchTree
import operator

__author__ = 'smbuthia'


class WordProcessor:
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }

    def fill_bst(self, file_name):
        bst = BinarySearchTree()
        with open(file_name) as f:
            for line in f:
                for word in self.get_words(line):
                    bst.insert(word)
        return bst

    def get_words(self, url):
        request = urllib.request.Request(url,None,self.headers)
        print(url)
        response = urllib.request.urlopen(request)
        data = response.read()
        data_string = data.decode('UTF-8')
        soup = BeautifulSoup(data_string, 'html.parser')
        result = soup.find('section',{'class':'body-copy'})

        #tokenizer = WordPunctTokenizer()
        tokenizer = RegexpTokenizer(r'\w+')
        replacer1 = RegexpReplacer()
        replacer2 = RepeatReplacer()
        words = []

        if len(result.attrs) == 1:
            paras = result.find_all('p')
            for para in paras:
                if para.string:
                    para_string = replacer2.replace(replacer1.replace(para.string))
                    para_string = para_string.lower()
                    try:
                        words += tokenizer.tokenize(para_string)
                    except TypeError:
                        print("Invalid line!")
                else:
                    para_contents = para.contents
                    for para_cont in para_contents:
                        if para_cont.string:
                            para_cont_string = replacer2.replace(replacer1.replace(para_cont.string))
                            para_cont_string = para_cont_string.lower()
                            try:
                                words += tokenizer.tokenize(para_cont_string)
                            except TypeError:
                                print("Invalid line!")
            words = [word for word in words if word not in set(stopwords.words('english'))]

        return words

"""
processor = WordProcessor()
tree = BinarySearchTree()
tree = processor.fill_bst('C:/Users/smbuthia/Desktop/MachineLearning/My ML Projos/accidents_data_urls.txt')
tree.tree_to_list(tree.root)
x = tree.dict_list
sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse=True)

for k, v in sorted_x:
    with open('C:/Users/smbuthia/Desktop/MachineLearning/My ML Projos/accident_top_words','a+') as f:
        f.write(k + '\n')
"""