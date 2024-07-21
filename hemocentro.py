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