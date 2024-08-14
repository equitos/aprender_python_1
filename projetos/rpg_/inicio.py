from modolos.planilha import *
from modolos.costantes import *
from modolos.basic import *


jogo_step_player = panilha(get_conexao.conexao_step(), get_lista_player())
jogo_step_inimigo = panilha(get_conexao.conexao_step_inimigos(),'nan')