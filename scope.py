x=20 #global variable
def message():
    global x
    x=10 #local variable
    print("iam from message function and my value is",x)
message()
print("iam from main programme and my value is",x)