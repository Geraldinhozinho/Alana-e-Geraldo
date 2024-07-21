class Pessoa:
    def __init__(self, nome, idade, tipo_sanguineo):
        self.nome = nome  # Atributo público
        self._idade = idade  # Atributo protegido
        self.__tipo_sanguineo = tipo_sanguineo  # Atributo privado


    def get_tipo_sanguineo(self):    
        return self.__tipo_sanguineo


    def set_tipo_sanguineo(self, novo_tipo):
        self.__tipo_sanguineo = novo_tipo


    def get_idade(self):          
        return self._idade


    def set_idade(self, nova_idade):
        self._idade = nova_idade

class Doador(Pessoa):
    def __init__(self, nome, idade, tipo_sanguineo, id_doador):
        super().__init__(nome, idade, tipo_sanguineo)
        self.id_doador = id_doador  


    def get_doador_info(self):
        return {
            "nome": self.nome,
            "idade": self._idade,
            "tipo_sanguineo": self.get_tipo_sanguineo(),
            "id_doador": self.id_doador
        }


    def set_nome(self, novo_nome):  
        self.nome = novo_nome


    def set_id_doador(self, novo_id):  
        self.id_doador = novo_id