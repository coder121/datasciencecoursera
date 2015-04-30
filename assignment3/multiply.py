import MapReduce
import sys

"""
Matrix Multiplication
"""


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    columns = 5
    rows = 5
    
    i = record[1]
    j = record[2]
    value = record[3]
    
    if record[0] == "a":
        for column in range(columns):
            mr.emit_intermediate((i, column), record)
    if record[0] == "b":
        for row in range(rows):
            mr.emit_intermediate((row, j), record)
    

def reducer(key, list_of_values):
    columns = 5
    rows = 5
    matrix_a = {}
    matrix_b = {}
    for i in range(columns):
        matrix_a[i] = 0
        matrix_b[i] = 0
        
    for i in list_of_values:
        if i[0] == "a":
            matrix_a[i[2]] = i[3]
        if i[0] == "b":
            matrix_b[i[1]] = i[3]
    total = 0
    for i in range(columns):
        total += matrix_a[i] * matrix_b[i]
        
    mr.emit((key[0], key[1], total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
