#what is method or function

#def employee(name: str):
 #   print(f"{name} belongs to Tkr")

#employee("Tarun")
#employee("Imran")
#employee("Vishal")

def outer_method(z):
    def inner_method(x):
        x=10+x
        print(f"This is my x value:{x}")#--110
    inner_method(z)
    print(f"This is my z value:{z}")#--100

outer_method(100)