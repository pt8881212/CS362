
# function for cube volume 
def cubeVolume(c):

    if (c <= 0):

        raise ValueError("Erro: integers cannot be negative or zero");
    
    return(c * c * c);