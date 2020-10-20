class Part:
    
    def __init__(self, number, description):
        self.itsNumber = number
        self.itsDescription = description

    # def accept(self, v):
    #     v.visit(self)

class PiecePart(Part):

    def __init__(self, number, description, cost):
        super().__init__(number, description)
        self.itsCost = cost
    
    def accept(self, v):
        v.visitPiecePart(self)
        

class Assembly(Part):
    
    def __init__(self, number, description):
        super().__init__(number, description)
        self.itsParts = []

    def accept(self, v):
        v.visitAssembly(self)

    def add(self, newpart):
        self.itsParts.append(newpart)

class PartVisitor:
    def visitAssembly(self, a):
        for p in a.itsParts:
            p.accept(self)

class ExplodedCostVisitor(PartVisitor):

    def __init__(self):
        self.cost = 0

    def visitPiecePart(self, pp):
        self.cost += pp.itsCost


cellphone     = Assembly("CP-7734", "Cell Phone")
display       = PiecePart("DS-1428", "LCD Display", 14.37)
speaker       = PiecePart("SP-92", "Speaker", 3.50)
microphone    = PiecePart("MC-28", "Microphone", 5.30)
cellRadio     = PiecePart("CR-56", "Cell Radio", 30)
frontCover    = PiecePart("FC-77", "Front Cover", 1.4)
backCover     = PiecePart("RC-77", "RearCover", 1.2)
keypad        = Assembly("KP-62", "Keypad")
button        = Assembly("B52", "Button")
buttonCover   = PiecePart("CV-15", "Cover", .5)
buttonContact = PiecePart("CN-2", "Contact", 1.2)
button.add(buttonCover)
button.add(buttonContact)
for _ in range(15): keypad.add(button)
cellphone.add(display)
cellphone.add(speaker)
cellphone.add(microphone)   
cellphone.add(cellRadio)
cellphone.add(frontCover)
cellphone.add(backCover)
cellphone.add(keypad)

v = ExplodedCostVisitor()
cellphone.accept(v)
print(v.cost)

    
   
    
