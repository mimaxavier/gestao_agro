from datetime import datetime

class Animal:
    def __init__(self, codigo, especie, data_nascimento, peso):
        self.codigo = codigo
        self.especie = especie
        self.data_nascimento = data_nascimento
        self.peso = peso

        self.historico_vacinacao = []
        self.historico_producao = []
        self.historico_alimentacao = []

    def vacinar(self, vacina, data):
        self.vacina = vacina
        data = datetime.strptime(data, r"%d/%m/%Y")

        registro = {"Vacina": vacina, "Data": data.strftime(r"%d/%m/%Y")}

        if self.vacina:
            self.historico_vacinacao.append(registro)
            print("Registro adicionado:", registro)
        

    def obter_historico(self, tipo):
            mapa = {
                "Alimentação": self.historico_alimentacao,
                "Vacinação": self.historico_vacinacao,
                "Produção": self.historico_producao
            }

            return mapa.get(tipo, [])
    
    def calcular_idade(self, data_nascimento):
        datadenascimento = datetime.strptime(self.data_nascimento, r"%d/%m/%Y")
        hoje = datetime.today()

        return (hoje - datadenascimento).days/365

    #  O método alimentar recebe o tipo de ração, a quantidade ofertada e a data.
    def alimentar(self, tipo_racao, qtd_racao, data):
        self.tipo_racao = tipo_racao
        self.qtd_racao = qtd_racao

        data_formatada = datetime.strptime(data, "%d/%m/%Y")

        registro = {"Tipo de Ração:": self.tipo_racao, "Quantidade de ração:": self.qtd_racao, "Data": data_formatada.strftime("%d/%m/%Y")}

        if self.tipo_racao:
            self.historico_alimentacao.append(registro)
            print("Registro adicionado:", registro)
            

    def registrar_producao(self, tipo, data, quantidade):
        try:
            data_convertida = datetime.strptime(data, "%d/%m/%Y")
            data_formatada = data_convertida.strftime("%d/%m/%Y")
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

        if self.especie == 'vaca':
            print("Produzindo leite...")

    def verificar_abate(self):
        idade = self.calcular_idade()

        return self.idade>5 or self.peso>=60
        
        