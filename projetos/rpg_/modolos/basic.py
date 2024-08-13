class get_conexao:
    def conexao_step():
        return 'step_rpg.db'
    
    def conexao_step_inimigos():
        return 'step_step_inimigos'


def get_lista_paramitos():
    return 'vida INTEGER DEFAULT 0, sanidade INTEGER DEFAULT 0'

def get_lista_player():
    return ['Hiago', 'ryan', 'jhuan']

def linha(linha=60):
    print("-"*linha)

