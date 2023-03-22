from Estados.Estado import Estado


class Missionarios_Canibais():


    def __init__(self):
        #inicia os estados iniciais
        self.fila_execucao = [Estado(3, 0, 3, 0, 'esq')]
        self.solucao = None

    def gerar_solucao(self):
        #inicia a BFS

        for elemento in self.fila_execucao:
            if elemento.estado_final():

                self.solucao = [elemento]
                while elemento.pai:
                    self.solucao.insert(0, elemento.pai)
                    elemento = elemento.pai
                break

            elemento.gerar_filhos()
            self.fila_execucao.extend(elemento.filhos)