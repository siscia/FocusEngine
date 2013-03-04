# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

import string
import json
from collections import Counter

class FocusEnginePipeline(object):
    def __init__(self):
        self.f = open('items.txt', 'wb')

    def open_spider(self, spider):
        pass
        
    def process_item(self, item, spider):       
        t = item['text']
        #reduce(lambda st, ch: st.replace(ch, " "), string.punctuation, t) ## = t
        t = "".join(t)
        for ch in string.punctuation:
            t = t.replace(ch, " ")
        item['worlds'] = dict(Counter(t.split(" ")))
        
        json.dump(dict(item), self.f)

        print
        return item

    def close_spider(self, spider):
        self.f.close()