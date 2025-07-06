from collections import deque # mais eficiente do que as listas comuns p inserção e remoção no início/fim da fila
# permite inserir no fim com append() / remover do início com popleft()

import random

class Senha:
    def __init__(self, codigo, tipo):
        self.codigo = codigo
        self.tipo = tipo

    def __str__(self):
        inicial = "P" if self.tipo == "prioritaria" else "N"
        return f"{inicial}{self.codigo:03d}"

class SistemaAtendimento:
    def __init__(self):
        self.fila_comum = deque()
        self.fila_prioritaria = deque()
        self.pilha_atendidos = []
        self.postos = [True] * 3 + [False] * 2
        self.contador_senhas = 1
        self.contador_normais = 0  # conta quantas senhas normais foram chamadas consecutivamente
        self.desistencias = 0 # Inicia com zero, porque no começo do sistema ninguém desistiu ainda

    def gerar_senha(self):
        tipo = random.choice(["comum", "prioritaria"])
        senha = Senha(self.contador_senhas, tipo)
        self.contador_senhas += 1

        if tipo == "prioritaria":
            self.fila_prioritaria.append(senha)
        else:
            self.fila_comum.append(senha)
            
    def chamar_proxima(self):
        
        if self.contador_normais < 2 and self.fila_comum:
            self.contador_normais += 1

            return self.fila_comum.popleft()
        
        elif self.fila_prioritaria:
            self.contador_normais = 0

            return self.fila_prioritaria.popleft()
        
        elif self.fila_comum:
            
            return self.fila_comum.popleft()
        
        return None
    
    def desistir_cliente(self):
        if random.random() < 0.3:    # 30% de chance de alguém desistir
            if self.fila_comum:
                self.fila_comum.popleft()
                self.desistencias += 1
            elif self.fila_prioritaria:
                self.fila_prioritaria.popleft()
                self.desistencias += 1

    def ver_proximas(self):  # visualizar próximas duas senhas a serem chamadas
        simulador_fila_comum = list(self.fila_comum) #simulador pra não afetar a fila real
        simulador_fila_prioritaria = list(self.fila_prioritaria)
        simulador_contador_normais = self.contador_normais
        proximas = []

        for _ in range(2):
            if simulador_contador_normais < 2 and simulador_fila_comum:
                proximas.append(simulador_fila_comum.pop(0))
                simulador_contador_normais += 1
            elif simulador_fila_prioritaria:
                proximas.append(simulador_fila_prioritaria.pop(0))
                simulador_contador_normais = 0
            elif simulador_fila_comum:
                proximas.append(simulador_fila_comum.pop(0))
        return proximas

    def processar_atendimentos(self):
        mensagens = []

        self.desistir_cliente()
        
        for i in range(len(self.postos)):
            if self.postos[i]:
                senha = self.chamar_proxima()
                if senha:
                    self.pilha_atendidos.append(senha) #empilhar as senhas atendidas (último atendimento vai para o topo)

                    mensagens.append(f"Posto {i+1}: Senha {senha}")
                else:
                    mensagens.append(f"Posto {i+1}: Posto livre")
            else:
                mensagens.append(f"Posto {i+1}: Inativo")
        
        return mensagens

       