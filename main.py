class CloudCost():
    def lambda_execution(self):
        valor_mensagem = 0.00000040
        valor_execucao_funcao = 0.0000002
        valor_tempo_execucao = 0.0002080
        total = (valor_execucao_funcao + (valor_tempo_execucao *3))
        return total

    def app_execution(self, execution_times):
        valor_mensagem = 0.00000040
        valor_execucao_funcao = 0.0000002
        valor_tempo_execucao = 0.0002080
        total = (execution_times ) * ((valor_tempo_execucao*3*2) + valor_execucao_funcao*2 + valor_mensagem)

        print(total)
        return total

    def month(self, execution_times, month_of_year):
        year_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        app_dias = self.app_execution(execution_times)
        total_month = app_dias * year_mes[month_of_year]
        print(total_month)
        return total_month
    
    def year(self, execution_times):
        year_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        total_year = []
        for mes in year_mes:
            total = self.month(execution_times, mes)
            total_year.append(total)

        print(total_year)
        return total_year


cc = CloudCost()
cc.month(1, 1)
cc.month(1, 2)
cc.month(1, 4)
cc.month(50, 4)
cc.month(100, 4)
cc.month(1000, 4)
cc.month(50000, 4)

print("Ano")
cc.year(1)
cc.year(50)
cc.year(100)
cc.year(1000)
