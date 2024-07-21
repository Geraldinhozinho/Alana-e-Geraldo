from hemocentro import Doador


class TesteHemocentro:
    def __init__(self):
        self.doadores = []


    def adicionar_doador(self, nome, idade, tipo_sanguineo, id_doador):
        doador = Doador(nome, idade, tipo_sanguineo, id_doador)
        self.doadores.append(doador)


    def listar_doadores(self):
        for i, doador in enumerate(self.doadores):
            info = doador.get_doador_info()
            print(f"Índice: {i}\n Nome: {info['nome']}\n Idade: {info['idade']}\n Tipo Sanguíneo: {info['tipo_sanguineo']}\n ID Doador: {info['id_doador']}")


if __name__ == "__main__":
    teste = TesteHemocentro()


    while True:
        nome = input("Digite o nome do doador: ")
        idade = int(input("Digite a idade do doador: "))
        tipo_sanguineo = input("Digite o tipo sanguíneo do doador: ")
        id_doador = input("Digite o ID do doador: ")
       
        teste.adicionar_doador(nome, idade, tipo_sanguineo, id_doador)


        continuar = input("Deseja adicionar outro doador? (s/n): ").lower()
        if continuar != 's':
            break
   
    teste.listar_doadores()


    modificar = input("Deseja modificar os dados de algum doador? (s/n): ").lower()
    if modificar == 's':
        doador_index = int(input(f"Escolha o índice do doador (1 a {len(teste.doadores) - 1}): "))
        doador = teste.doadores[doador_index]
       
        modificar_nome = input("Deseja modificar o nome? (s/n): ").lower()
