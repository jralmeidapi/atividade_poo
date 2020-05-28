from pessoa import Pessoa

p1 = Pessoa("Paulo Jr")
p2 = Pessoa("Telma Maria")

from conta import Conta

c1 = Conta(p1, "Pagar", "10/06/2020", 200)
c2 = Conta(p2, "Receber", "18/10/2020", 550)

print('Dados da Conta 1')
print('Nome: ', p1.nome)
print('Tipo de Conta: ', c1.tipo_conta)
print('Data Vencimento: ', c1.data_vencimento)
print('Valor: ', c1.valor)

print('Dados da Conta 2')
print('Nome: ', p2.nome)
print('Tipo de Conta: ', c2.tipo_conta)
print('Data Vencimento: ', c2.data_vencimento)
print('Valor: ', c2.valor)