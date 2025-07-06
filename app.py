from flask import Flask, render_template, redirect, url_for
from sistema import SistemaAtendimento

app = Flask(__name__)
sistema = SistemaAtendimento()

@app.route('/')
def index():
    postos = sistema.processar_atendimentos()
    proximas = [str(s) for s in sistema.ver_proximas()] #P visualizar as duas próximas senhas na fila
    
    return render_template(
        'index.html',
        fila_comum=[str(s) for s in sistema.fila_comum],
        fila_prioritaria=[str(s) for s in sistema.fila_prioritaria],
        atendidos=[str(s) for s in reversed(sistema.pilha_atendidos)],
        postos=postos,
        desistencias=sistema.desistencias,
        proximas=proximas  
    )

@app.route('/gerar') # chama a função p gerar uma nova senha
def gerar():
    for _ in range(5): #gera 5 senhas a cada vez que clicar no botão de gerar
        sistema.gerar_senha()
    return redirect(url_for('index'))


@app.route('/encerrar') # direciona pra página de encerramento do sistema
def encerrar():
    return render_template(
        'encerrar.html',
        atendidos=[str(s) for s in reversed(sistema.pilha_atendidos)], # reversed para mostrar do mais recente para o mais antigo
        desistencias=sistema.desistencias
    )

if __name__ == '__main__':
    app.run(debug=True)


