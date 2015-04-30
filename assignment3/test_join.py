import MapReduce

import sys



"""

SQL Join Example in the Simple Python MapReduce Framework

"""



mr = MapReduce.MapReduce()



# =============================

# Do not modify above this line



def mapper(record):

    if record[0] == "order":

        mr.emit_intermediate(record[1], (record, []))

    if record[0] == "line_item":

        mr.emit_intermediate(record[1], ([],record))

    



def reducer(key, list_of_values):

    order = []

    for a in list_of_values:

        if len(a[0]) > 0:

            order = a[0]

            

    for a in list_of_values:

        if(len(a[1]) > 0):

            mr.emit(order+a[1])



# Do not modify below this line

# =============================

if __name__ == '__main__':

  inputdata = open(sys.argv[1])

  mr.execute(inputdata, mapper, reducer)
