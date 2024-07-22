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
        doador_index = int(input(f"Escolha o índice do doador (0 a {len(teste.doadores) - 1}): "))
        doador = teste.doadores[doador_index]
       
        modificar_nome = input("Deseja modificar o nome? (s/n): ").lower()

        if modificar_nome == 's':
            print(f"Nome antes da modificação: {doador.nome}")
            novo_nome = input("Digite o novo nome: ")
            doador.set_nome(novo_nome)
            print(f"Nome após modificação: {doador.nome}")



        modificar_idade = input("Deseja modificar a idade? (s/n): ").lower()
        if modificar_idade == 's':
            print(f"Idade antes da modificação: {doador.get_idade()}")
            nova_idade = int(input("Digite a nova idade: "))
            doador.set_idade(nova_idade)
            print(f"Idade após modificação: {doador.get_idade()}")


        modificar_tipo_sanguineo = input("Deseja modificar o tipo sanguíneo? (s/n): ").lower()
        if modificar_tipo_sanguineo == 's':
            print(f"Tipo Sanguíneo antes da modificação: {doador.get_tipo_sanguineo()}")
            novo_tipo_sanguineo = input("Digite o novo tipo sanguíneo: ")
            doador.set_tipo_sanguineo(novo_tipo_sanguineo)
            print(f"Tipo Sanguíneo após modificação: {doador.get_tipo_sanguineo()}")

    print("\n-------------------Dados-------------------:\n ")
    teste.listar_doadores()    
