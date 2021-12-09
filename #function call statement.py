from _typeshed import Self


class phone:
    def parts (self,processor,ram,rom,model):
        #self.processor=processor
        self.processor="mediatek"
        print(self.processor)
        #self.ram=ram
        self.ram="8gb"
        print(self.ram)
        
        #self.rom=rom
        self.rom="512gb"
        print(self.rom)
        #self.model=model
        self.model="note 4"
        print(self.model)
    def display(self):
        print("ram is")
phi=phone()
phi.parts()
