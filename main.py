from bfs.bfs import Missionarios_Canibais


def main():
    #inicia os possíveis caminhos e a BFS
    problema = Missionarios_Canibais()
    problema.gerar_solucao()

    for estado in problema.solucao:
        #apenas formata a resposta
        print (estado)
        print (34 * '-')

if __name__ == '__main__':
    main()