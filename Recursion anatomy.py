# Recursion anatomy! 
## To make it return we need to reutrn the function itself! line11!

counter = 0 
def inception():
    global counter
    print(counter)
    if (counter>3):
        return 'done!'    
    counter+=1
    return inception()

x = inception()
print(x)


## To understand recursion deeper: 
### recusive function will just add the function to the stack! 
### thus the BASE CASE is met (counter>3), the function will be removed from the stack, 
### and the REMAINING CODE (line 29) will then be executed! 
### Thus, when the following code is run, it prints out the latest counter number/4!! 
       
counter = 0 
def inception():
    global counter
    print(counter)
    if (counter>3):
        return 'done!'    
    counter+=1    
    inception()    
    print(f'end of {counter}')

inception()
