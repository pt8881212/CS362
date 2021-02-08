#function for finding the average element
def avg_element(e):
    if (len(e) == 0):
        raise ValueError("Error: Cannot get average of an empty array");
    elif(sum(e) / len(e) == 0):
        assert(0);   
    return sum(e)/ len(e);