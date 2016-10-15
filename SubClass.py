import BaseModel
class SubClass(BaseModel.BaseClass):
    def __init__(self,name,age,salary):
        BaseModel.BaseClass.__init__(self,name,age)
        self.salary=salary
        print("SubClass is inited and the salary is:%s" % self.salary)
    def talk(self,sth):
        print("%s talking %s" % (self.name,sth))
        BaseModel.BaseClass.speak(self,sth)
if(__name__=="__main__"):
    s=SubClass("Joan",10,8000)
    s.talk("a story")
