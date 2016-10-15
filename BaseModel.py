class BaseClass:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print("BaseClass is inited")
    def speak(self,name):
        print("BaseClass is speak:%s" % name)
if(__name__=="__main__"):
    b=BaseClass()
