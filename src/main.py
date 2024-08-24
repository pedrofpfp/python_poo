from frota import *
def operar_carro(carro: Carro):
    print('1- Ligar motor')
    print('2- Desligar motor')
    print('3- Acelerar')
    op = 0
    while op not in (1, 2, 3):
        op = int(input("Digite as opcoes[1-3]: "))

    if op == 1:
        carro.ligar()
    elif op == 2:
        carro.desligar()
    elif op == 3:
        v = float(input("Informe a velocidade: "))
        t = float(input("Informe o tempo: "))
        carro.acelerar(v, t)
    print('Infos atuais do carro')
    print(carro)
if __name__ == "__main__":
    print('Cadastre carro 1')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    kms = float(input('Digite com quantos Kms: '))
    consumo_medio = float(input('Digite consumo medio: '))
    tanque = float(input('Digite litros no tanque: '))
    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0,  False, tanque, consumo_medio)

    print('Cadastre carro 2')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    kms = float(input('Digite com quantos Kms: '))
    consumo_medio = float(input('Digite consumo medio: '))
    tanque = float(input('Digite litros no tanque: '))
    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0, False, tanque, consumo_medio)

    while carro1.odometro < 600 and carro2.odometro < 600 and (carro1.tanque>0 or carro2.tanque>0):
        try:
            opCar = 0
            while opCar not in (1,2):
                opCar = int(input("Digite qual carro deseja operar:"))
            if opCar == 1:
                operar_carro(carro1)
            else:
                operar_carro(carro2)
        except Exception as e:
            print("Erro!")
            print(e)

    carro1.desligar()
    carro2.desligar()
    if carro1.odometro > carro2.odometro:
        print("Carro 1 Venceu!")
    else:
        print("Carro 2 Venceu!! ")
