x=20 #global variable
def message():
    global x
    x=10 #local variable
    print("i am from message function and my value is",x)
message()
print("i am from main program and my value is",x)
