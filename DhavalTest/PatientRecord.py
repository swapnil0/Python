class PatientRecord:
    def __init__(self, age, name, pid):
        self.name=name
        self.age=age
        self.pid=str(pid)+str(age)
    def __str__():
        return self.name+","+self.age+","+self.pid
    
    def __gt__(self,obj):
        return self.age > obj.age
