# Function for re.search loop

import re

def main(exp, text):
    cont = False
    output = re.search(exp, text)
    if output:
        
        cont = True
        lb = output.span()[0]
        rb = output.span()[1]
        
        print(output.span())
        
        while cont:

            new_output = re.search(exp, text[rb:])
            if new_output:
                lb += new_output.span()[1]
                rb += new_output.span()[1]  
                print((lb, rb))
            else:
                cont = False
            
    else:
        print("None found")