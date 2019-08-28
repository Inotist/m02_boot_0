def retrocontador(e, first=True):
    if not first: print(",{}".format(e), end="")
    else: print("{}".format(e), end="")
    
    if e > 0: retrocontador(e-1, False)
    
retrocontador(10)