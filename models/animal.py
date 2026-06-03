from datetime import datetime
from models.vaccine import VaccineApplication
import database.connection
conn = database.connection.get_connection()

class Animal:
    def __init__(self, id, especie, data_nascimento, peso):
        self.codigo = id
        self.especie = especie
        self.data_nascimento = data_nascimento
        self.peso = peso

        self.historico_vacinacao = []
        self.historico_producao = []
        self.historico_alimentacao = []

    def vacinar(self, VaccineApplication):
        self.historico_vacinacao = []
        self.historico_vacinacao.append(VaccineApplication)
        

    def obter_historico(self, tipo,):
            mapa = {
                "Alimentação": self.historico_alimentacao,
                "Vacinação": self.historico_vacinacao,
                "Produção": self.historico_producao
            }

            return mapa.get(tipo, [])
    

    #  Feed method create a object FeedingRecord
    def alimentar(self, FeedingRecord):
        self.historico_alimentacao = []
        self.historico_alimentacao.append(FeedingRecord)
            

    def produzir(self, tipo, data, quantidade):
        try:
            data_convertida = datetime.strptime(data, r"%d/%m/%Y")
            data_formatada = data_convertida.strftime(r"%d/%m/%Y")
        except ValueError:
            print("Formato de data inválido! Tente novamente!")
            return
        
        registro = {
                    "Tipo": tipo,
                    "Quantidade:": quantidade, 
                    "Data:": data_formatada
                    }

        if quantidade>0:
            self.historico_producao.append(registro)


    def verificar_abate(self):
        idade = self.calcular_idade()

        return idade>3 or self.peso>=240
        
        