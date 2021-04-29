class Hora:
    __hora=''
    __minuto=''
    __segundo=''

    def __init__(self,h,m,s):
        self.__hora=h
        self.__minuto=m
        self.__segundo=s

    def Mostrar(self):
        print("{}:{}:{}".format(self.__hora , self.__minuto , self.__segundo))

    def getH(self):
        return self.__hora

    def getM(self):
        return self.__minuto

    def getS(self):
        return self.__segundo