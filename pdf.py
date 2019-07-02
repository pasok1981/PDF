import PyPDF2
import collections

from nltk.tokenize import word_tokenize
from pickling import write_json
from pickling import write_pickle

def read(path_):
    pdf_file_object = open(path_, 'rb')
    pdf_object = PyPDF2.PdfFileReader(pdf_file_object)

    page_num = pdf_object.numPages

    t = ""
    for page in range(page_num):
        page_obj = pdf_object.getPage(page)
        t += page_obj.extractText()
    return t

def _tokens(text):
    tokens = word_tokenize(text)
    punctuations = ['(',')',';',':','[',']',',', ' ']

    keywords = [word for word in tokens if not word in punctuations]

    #del keywords[204] # can't decode greek chars .|. sux...

    return keywords

def create_dict(alist):
    alist_ = list(filter(None, alist))
    ranks_i = list(map(int, alist[1::2]))
    _dict = dict(zip(alist_[::2], ranks_i))

    return dict(collections.OrderedDict(sorted(_dict.items(), key = lambda x:x[1], reverse=True)))


if __name__ == "__main__":
    l = read('/path/to/pdf')
    li = _tokens(l)
    _dict = create_dict(li)
    
    # to JSON
    write_json('/path/to/file/creation', _dict)
    # Serialize
    write_pickle('./data', _dict)


