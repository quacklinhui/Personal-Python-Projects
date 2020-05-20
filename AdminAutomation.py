ld = 'label define '
lastpart = ', modify'
def lazy():
    print("\n")
    varname = input("insert varname: ")
    firstpart = ld + varname + ' '
    with open (r"C:\Users\theco\OneDrive\Documents\eehweetexfile.txt","r") as a_file:
        for line in a_file:
            #line.replace(firstpart,'')
            #line.replace(lastpart,'')
            edit1=line.strip(firstpart)
            edit2 = edit1[:-10]
            edit3=edit2.replace('"','')
            edit4=edit3.replace(' `',': ')
            print(edit4, end = '\n')
        lazy()
lazy()
