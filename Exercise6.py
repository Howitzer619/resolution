#class MyClass:
    #nama = "babastudio"

#name = MyClass()
#print(name.nama)

class person:
    def __init__(obj, name, age):
        obj.name = name
        obj.age = age

    def myfunc(abc):
        print("Halo nama saya adalah " + abc.name)
        print("Umur saya adalah " + str(abc.age))    

run = person("Risman",25)
run.myfunc()
    