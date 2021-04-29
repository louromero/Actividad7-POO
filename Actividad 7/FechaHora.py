from Hora import Hora

class FechaHora:
    __dia=0
    __mes=0
    __anio=0
    __hora=0
    __minuto=0
    __segundo=0

    def __init__ (self,dia=1,mes=1,anio=2020,hora=0,minuto=0,segundo=0):
        self.__dia = dia
        self.__mes = mes
        self.__anio = anio
        self.__hora = hora
        self.__minuto = minuto
        self.__segundo = segundo

        if (self.__segundo>=60):
            self.__minuto+=int(self.__segundo/60)
            self.__segundo= self.__segundo%60
            

        if (self.__minuto>=60):
            self.__hora+=int(self.__minuto/60)
            self.__minuto= self.__minuto%60
            

        if (self.__hora>=24):
            self.__dia+= int(self.__hora/24)
            self.__hora= self.__hora%24

        #MES
        if (self.__mes>12):
            self.__anio+=int(self.__mes/12)
            self.__mes=self.__mes%12
            

        if (self.__mes == 4 or self.__mes==6 or self.__mes==9 or self.__mes==11) and (self.__dia>30):
            self.__mes+=int(self.__dia/30)
            self.__dia=self.__dia%30
            

        if (self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or (self.__mes==12)) and self.__dia>31:
            self.__mes+=int(self.__dia/31)
            self.__dia=self.__dia%31
            

        #si el año es bisiesto
        if (self.__anio%4) == 0:
            #si 
            if (self.__anio%100)==0:
                if (self.__anio%400):
                    if (self.__mes==2) and (self.__dia>29):
                        self.__dia=1
                        self.__mes+=1
                    else:
                         if (self.__mes==2) and (self.__dia<29):
                            self.__dia+=1
            else:
                if (self.__mes==2) and (self.__dia>29):
                    self.__dia=1
                    self.__mes+=1
                else:
                    if (self.__mes==2) and (self.__dia<29):
                        self.__dia+=1
        #Al no ser bisiesto, se valida los días de los meses
        else:
            if (self.__mes == 2) and (self.__dia>28):
                self.__dia=1
                self.__mes+=1

##EXPERIMENTO - cuando la resta es numero negativo, hace el tiempo para atrás
        if(self.__segundo<0):
            self.__segundo= self.__segundo+60
            self.__minuto=self.__minuto-1
            

        if (self.__minuto<0):
            self.__minuto=self.__minuto+60
            self.__hora=self.__hora-1
            

        if (self.__hora<0):
            self.__hora= self.__hora+24
            self.__dia= self.__dia-1


        #MES
        if (self.__mes<0):
            self.__mes=self.__mes+12
            self.__anio=self.__anio-1
            

        if (self.__mes == 4 or self.__mes==6 or self.__mes==9 or self.__mes==11) and (self.__dia<0):
            self.__dia=self.__dia+30
            self.__mes=self.__mes-1
            
            

        if (self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or (self.__mes==12)) and (self.__dia<0):
            self.__dia=self.__dia+31
            self.__mes=self.__mes-1

    def Mostrar(self):
        print("{}/{}/{}\t\t{}:{}:{}".format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minuto,self.__segundo))
        print(" ")

    def getDia(self):
        return self.__dia

    def getMes(self):
        return self.__mes

    def getAnio(self):
        return self.__anio

    def getHora(self):
        return self.__hora

    def getMinuto(self):
        return self.__minuto

    def getSegundo(self):
        return self.__segundo

    #Sobrecargas
    def __add__(self,x):
        hora= self.__hora+x.getH()
        minu=self.__minuto+x.getM()
        segu=self.__segundo+x.getS()
        return FechaHora(self.__dia,self.__mes,self.__anio,hora,minu,segu)

    def __radd__(self,x):
        if type(x)==Hora:
            hora= self.__hora+x.getH()
            minu=self.__minuto+x.getM()
            segu=self.__segundo+x.getS()
            return FechaHora(self.__dia,self.__mes,self.__anio,hora,minu,segu)
        else:
            if type(x)==int:
                return FechaHora(self.__dia+x,self.__mes,self.__anio,self.__hora,self.__minuto,self.__segundo)

    def __sub__(self,x):
        return FechaHora(self.__dia-x,self.__mes,self.__anio,self.__hora,self.__minuto,self.__segundo)

    