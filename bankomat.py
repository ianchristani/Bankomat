class Operacoes:
    
    def __init__(self,nome,saldo):
        self.nome=nome
        self.saldo=saldo
        
        print(f'Welcome {self.nome}')
            
        
    def deposito(self,dep):
        self.saldo=self.saldo+dep
        print(f'Your balance is {self.saldo}')

        
    def saque(self,saq):
        if saq>self.saldo:
            print('You have no enough amount')
        else:
            self.saldo=self.saldo-saq
            valores=[100,50,20,10,5,1]
            for c in valores:
                notas=int(saq/c)
                resto=(int(saq%c))
                saq=resto
                if notas<1:
                    print('')
                else:
                    print(f'You will get {notas} bills of with value {c}')
        print(f'Now your balance is {self.saldo}')

costumer=Operacoes('Ian',5000)

opcao=int(input(''' Chose one option:
    1. Deposit
    2. Withdraw\n'''))
            
if opcao==1:
    dep=int(input('Deposit value R$ '))
    costumer.deposito(dep)
elif opcao==2:
    saq=int(input('Withdraw value R$ '))
    costumer.saque(saq)
else:
    print('Thank you for using our terminal.')
 
