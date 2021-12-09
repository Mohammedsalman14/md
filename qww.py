class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def about(self):
        print(self.name)
pp=person("salman",20)
pp.about()