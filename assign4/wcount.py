"""wcount.py: count words from an Internet file.

__author__ = "Bai Guangsheng"
__pkuid__  = "1800011722"
__email__  = "1800011722@pku.edu.cn"
"""

from urllib.request import urlopen
import collections
import sys
print(sys.argv)

URL="http://www.gutenberg.org/cache/epub/19033/pg19033.txt"
doc=urlopen(URL)
docstr=doc.read().decode().lower()
table=str.maketrans(",.!?\"\')(","        ")
doclist=docstr.translate(table).split()
sort=collections.Counter(doclist).most_common(10)
for i in sort:
	print(i[0],"\t",i[1])

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)