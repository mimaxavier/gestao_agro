from datetime import datetime

class Animal:
    def __init__(self, codigo, especie, data_nascimento, peso):
        self.codigo = codigo
        self.especie = especie
        self.data_nascimento = data_nascimento
        self.peso = peso
        self.historico_vacinacao = []
        self.historico_producao = []

    def vacinar(self, vacina, data):
        self.vacina = vacina
        data = datetime.strptime(data, "%d/%m/%Y")

        registro = {"Vacina": vacina, "Data": data.strftime("%d/%m/%Y")}

        if self.vacina:
            self.historico_vacinacao.append(registro)
            print("Registro adicionado:", registro)
        

    def mostrar_registro(self, codigo):
        for registro in self.historico_vacinacao:
            print(registro)

    def alimentar(self, tipo_racao, peso_atual, data):
        self.historico_alimentacao = []

        self.tipo_racao = tipo_racao
        self.peso_atual = peso_atual
        data = datetime.now()
        registro = {"Tipo de Ração:": tipo_racao, "Peso atual": peso_atual, "Data": data}

        if self.tipo_racao:
            self.historico_alimentacao.append(registro)
            print("Registro adicionado:", registro)
            
        
        
        print("Alimentando...")

    def produzir_leite(self, data, quantidade):
        try:
            data_convertida = datetime.strptime(data, "%d/%m/%Y")
            data_formatada = data_convertida.strftime("%d/%m/%Y")
        except ValueError:
            print("Formato de data inválido! Tente novamente!")
            return
        
        registro = {"Quantidade:": quantidade, "Data:": data_formatada}

        if quantidade>0:
            self.historico_producao.append(registro)

        if self.especie == 'vaca':
            print("Produzindo leite...")

    def verificar_abate(self):
        if self.idade>5 or self.peso>60:
            print("está pronto para o abate...")
        