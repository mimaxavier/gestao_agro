from datetime import datetime

class Animal:
    def __init__(self, codigo, especie, data_nascimento):
        self.codigo = codigo
        self.especie = especie
        self.data_nascimento = data_nascimento

    def vacinar(self, vacina, data):
        self.historico_vacinacao = []
        self.vacina = vacina
        data = datetime.strptime(data, "%d/%m/%Y")

        registro = {"Vacina": vacina, "Data": data.strftime("%d/%m/%Y")}

        if self.vacina:
            self.historico_vacinacao.append(registro)
            print("Registro adicionado:", registro)
        

    def mostrar_registro(self, codigo):
        for registro in self.historico_vacinacao:
            print(registro)

    def alimentar(self):
        #tipo_De_racao
        #peso
        print("Alimentando...")

    def produzir_leite(self):
        if self.especie == 'vaca':
            print("produzindo leite...")

    def verificar_abate(self):
        if self.idade>5 or self.peso>60:
            print("está pronto para o abate...")
        