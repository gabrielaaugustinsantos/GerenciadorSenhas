📋 **Sistema de Gerenciamento de Senhas de Atendimento**

Este projeto é uma aplicação para um sistema de atendimento com geração e gerenciamento de senhas (normais e prioritárias). Ele simula o funcionamento de uma fila de atendimento em tempo real, distribuindo senhas entre postos ativos e registrando o histórico de atendimentos e desistências. A aplicação foi desenvolvida com foco em simular o comportamento real de um sistema de filas em ambientes como bancos ou clínicas de saúde.

🔧** Funcionalidades**


• Geração de senhas com prioridade aleatória (normal ou prioritária)

• Atendimento distribuído entre 5 postos (3 ativos e 2 inativos)

• Alternância de atendimento com lógica 2N:1P (duas senhas normais para uma prioritária)

• Registro de atendimentos em uma pilha (ordem reversa: último atendido no topo)

• Simulação de desistência de clientes com chance de 30%

• Visualização das duas próximas senhas a serem chamadas

• Encerramento do sistema com relatório de senhas atendidas e desistências

💻 **Tecnologias Utilizadas**

• Python

• Flask (Framework web para criação das rotas e renderização das páginas HTML)

• HTML 

• collections.deque (Para o gerenciamento eficiente das filas)

![image](https://github.com/user-attachments/assets/74d49b68-0518-4716-b951-4a341d2f41b0)

![image](https://github.com/user-attachments/assets/3ed099ee-7203-48ec-9266-325a849a09a2)


