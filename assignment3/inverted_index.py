import MapReduce
import sys

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
    #print key
    value = record[1]
    #print value
  #  print key
    temp_list=[]
    words = value.split()
    for w in words:
        if w not in temp_list:
           temp_list.append(w)
    for w in temp_list:
        mr.emit_intermediate(w, key)
        #print w

def reducer(w, key):
    
    # key: word
    # value: doc id
    #total = 0
    #for v in w:
     # total += v
     
    
    mr.emit((w, key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
