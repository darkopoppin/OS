import math

def printf(dirs):
    #print(len(dirs))
    columns = math.ceil(len(dirs)/3) #gets the average number of content in every column
    #print("columns " + str(columns))
    fcolumn = dirs[0:columns] #the content in the first column
    #print("fcolumn " + str(fcolumn))
    max_f = get_max_len(fcolumn) #the max length of a file or directory from the first column
    #print(max_f)
    scolumn = dirs[columns:columns*2] #the content in the second column
    #print("scolumn " + str(scolumn))
    max_s = get_max_len(scolumn) #the max length of a file or directory from the second column
    tcolumn = dirs[columns*2:] #the content in the third column
    #print("tcolumn" + str(tcolumn))

    while len(fcolumn) != 0:
        if len(fcolumn) == 1 and len(scolumn) == 0 and len(tcolumn) == 0: 
            first = fcolumn.pop(0)
            print(first)

        elif len(fcolumn) >= 1 and len(scolumn) >= 1 and len(tcolumn) == 0:
            first = fcolumn.pop(0)
            second = scolumn.pop(0)
            print("{!s} {!s}".format(first + " " * (max_f - len(first) + 1), second))

        else:
            first = fcolumn.pop(0)
            second = scolumn.pop(0)
            third = tcolumn.pop(0)
            print("{!s} {!s} {!s}".format(first + " " * (max_f - len(first) + 4), second + " " * (max_s - len(second) + 4), third))

def get_max_len(column):
    return len(max(column, key=len))
