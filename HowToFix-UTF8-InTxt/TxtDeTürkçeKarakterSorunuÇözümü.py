# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 16:12:55 2020

@author: Ozgur Kucet
"""

import codecs
with codecs.open("filename", 'r', encoding='utf8') as f:
    text = f.read()
# process Unicode text
with codecs.open("filename", 'w', encoding='utf8') as f:
    f.write(text)





import io
with io.open("filename", 'r', encoding='utf8') as f:
    text = f.read()
# process Unicode text
with io.open("filename", 'w', encoding='utf8') as f:
    f.write(text)




