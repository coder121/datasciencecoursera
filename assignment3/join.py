import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    if record[0] == "order":   
       mr.emit_intermediate(record[1],(record,[]))
    if record[0] == "line_item":
       mr.emit_intermediate(record[1],([],record))

def reducer(key, list_of_values):
    new_list=[]
    for v in list_of_values:
        if(len(v[0]))>0:
          new_list=v[0]
    
    for v in list_of_values:
        #new_list.append(v)
        mr.emit((new_list+v[1]))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
