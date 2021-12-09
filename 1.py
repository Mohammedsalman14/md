class phone:
    def __init__(self,ram,rom):
        self.rom=rom
        self.ram=ram

pi=phone("512","8")
print(pi.ram)
print(pi.rom)