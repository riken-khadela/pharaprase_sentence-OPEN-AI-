def my_function():
    arg1 = globals().get('DRIVER',None)
    arg2 = globals().get('arg2',None)
    
    print("arg1:", arg1)
    print("arg2:", arg2)
my_function()