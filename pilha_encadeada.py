#Pilha encadeada

class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.topo = None #armazena o último item inserido
    
    def push(self, valor):
        novo = Node(valor)
        novo.proximo = self.topo #faz o novo nó apontar (novo.proximo) para o antigo topo
        self.topo = novo #Atualiza o topo da pilha para ser esse novo nó.

    
    def pop(self):
        if self.topo is None:
            return None
        
        valor = self.topo.valor
        self.topo = self.topo.proximo
        return valor
    
    def is_empty(self):
        return self.topo is None