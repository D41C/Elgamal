class Elgamal:
    def __init__(self,P,G):
        self.P=P
        self.G=G
    def firstown(self):
        self.Mas_p = []
        for i in range(self.P-1):
            self.Mas_p.append((self.G**i) % self.P)
            i=+1
        for i in range(2,len(self.Mas_p)):
            if self.Mas_p.count(self.Mas_p[i]) >= 2:
                print("Знаечение P не является первообразным корнем модуля", self.P)
                exit()
            else:
                i=+1
    def secret_massage(self):
        self.X = int(input("Секретный ключ X = "))
        self.Y = (self.G**self.X) % self.P
        print("Открытый ключ Y = ",self.Y)
        self.M=str(input("Введите сообщение(большими буквами,только русский алфавит): "))
        self.K=int(input("Значение K = "))
    def condition(self):
        self.a = self.K
        self.b = self.P
        while self.a>0 and self.b > 0:
            if self.a > self.b:
                self.a=self.a-self.b
            else:
                self.b=self.b-self.a
        if  (self.K<1) or (self.K > (self.P-1)) or (self.a != 1):
            print("Значение K не соответствует условиям (1 < К < Р-1 ,НОД(K, P-1)=1 ")
            exit()
    def shipher(self):
        print("####### Шифрование #######")
        self.a = (self.G**self.K) % self.P
        print("Значение a =",self.a)
        self.shipher_massage=[]
        for i in range(len(self.M)):
            self.b = ((ord(self.M[i])-1039)*(self.Y**self.K)) % self.P
            self.shipher_massage.append(self.b)
            i=i+1
        print("Зашифрованное сообщение =",self.shipher_massage)
    def deshipher(self):
        print("####### Расшифровка #######")
        self.ax = (self.a**(self.P-1-self.X)) % self.P
        print("Обратный элемент для a^x =",self.ax)
        self.mas=''
        for i in range(len(self.shipher_massage)):
            self.M0 = ((self.shipher_massage[i])*self.ax) % self.P
            self.res=chr(self.M0+1039)
            self.mas=self.mas+self.res
            i=i+1
        print("Восстановленное сообщение:",self.mas)

def enter():
    P = int(input("Значение P = "))
    G = int(input("Значение G = "))
    el = Elgamal(P, G)
    el.firstown()
    el.secret_massage()
    el.condition()
    el.shipher()
    el.deshipher()

if __name__ == "__main__":
    enter()