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