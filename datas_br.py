from datetime import datetime, timedelta


class Cadastro:
    def __init__(self):
        self.data_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho", "julho",
            "agosto", "setembro", "outubro",
            "novembro", "dezembro"
        ]
        mes_cadastro = self.data_cadastro.month
        return meses_do_ano[mes_cadastro-1]

    def dia_semana(self):
        dias_semana_lista = [
            "segunda", "terça", "quarta", "quinta"
            "sexta", "sábado", "domingo"
        ]
        dia_semana = self.data_cadastro.weekday() - 1
        return dias_semana_lista[dia_semana]

    def format_data(self):
        data_formatada = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        agora = datetime.now() + timedelta(days=15,hours=12 ,minutes=30, seconds=15)
        return agora - self.data_cadastro
