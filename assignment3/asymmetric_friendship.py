import MapReduce
import sys
import collections
"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
   # print key
    value = record[1]
    #print value
    #words = value.split()
    #for w in key:
    mr.emit_intermediate(key, value)
    mr.emit_intermediate(value,key)
    #print value 
def reducer(key, list_of_values):
    count=collections.Counter(list_of_values)
    print count
    for v in count:
        if(count[v]<2):
          mr.emit((key, v))
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
