from datetime import datetime

class Gerenciador:
     def mostrar_registro(self, codigo, tipo):
            mapa = {
                "Alimentação": self.historico_alimentacao,
                "Vacinação": self.historico_vacinacao,
                "Produção": self.historico_producao
            }

            historico = mapa.get(tipo)

            

            for registro in historico:
                print(registro)

def calcular_idade(self, data_nascimento):
        datadenascimento = datetime.strptime(self.data_nascimento, r"%d/%m/%Y")
        hoje = datetime.today()

        return (hoje - datadenascimento).days/365

