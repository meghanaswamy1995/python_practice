class LogicGates():
    def __init__(self,n):
        self.label = n
        self.output = None
    def getLabel(self):
        return self.label
    def getOutput(self):
        self.output = self.performLogicFunction()
        return self.output

class BinaryGate(LogicGates):
    def __init__(self,n):
        super().__init__(n)
        self.pinA = None
        self.pinB = None

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
    
    def getpinA(self):
        if self.pinA == None:
            return str(input("enter pin A input for "+ self.getLabel()+"--> "))
        else:
            return self.pinA.getFrom().getOutput()

    def getpinB(self):
        if self.pinB == None:
            return str(input("enter pin B input for "+self.getLabel()+"--> "))
        else:
            return self.pinB.getFrom().getOutput()

class UnaryGate(LogicGates):
    def __init__(self,n):
        super().__init__(n)
        self.pin = None
    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")
    def getpin(self):
        if self.pin == None:
            return str(input("enter pin for gate "+ self.getLabel()+ "--> "))
        else:
            return self.pin.getFrom().getOutput()

class AndGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)

    def performLogicFunction(self):
        a = self.getpinA()
        b = self.getpinB()
        #print("a=",a,"b=",b)
        if a=="1" and b=="1":
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        super().__init__(n)
    def performLogicFunction(self):
        a = self.getpinA()
        b = self.getpinB()
        if a=="0" and b=="0":
            return 0
        else:
            return 1

class NotGate(UnaryGate):
    def __init__(self,n):
        super().__init__(n)
    def performLogicFunction(self):
        a = self.getpin()
        if a == "1":
            return 0
        else:
            return 1

class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate
        print("tgate",self.togate)
        tgate.setNextPin(self)
    def getFrom(self):
        return self.fromgate
    def getTo(self):
        return self.togate


# g1 = AndGate("G1")
# result=g1.getOutput()
# print("final_reslt of G1: "+ str(result))

# g2 = OrGate("G2")
# resultg2 = g2.getOutput()
# print("final result of G2: "+ str(resultg2))

# g3 = NotGate("G3")
# resultg3 = g3.getOutput()
# print("final result of G3: "+str(resultg3))

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g3)
c2 = Connector(g2,g3)
c3 = Connector(g3,g4)
final=g4.getOutput()
print("final output ", final)