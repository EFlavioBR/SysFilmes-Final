
"""
SysFilmes: Sistema de Gerenciamento e Avaliação de Filmes

Descrição:
Este programa implementa um sistema de linha de comando para gerenciar uma
coleção de filmes, conforme especificado no trabalho final da disciplina de
Fundamentos de Programação (CK0211) da Universidade Federal do Ceará.
O sistema permite cadastrar, avaliar, consultar e listar filmes, além de
carregar e salvar dados a partir de arquivos.

Autores:
  Cícero Rogério dos Santos Alves Filho - 578748
  Emanuel Flávio Sousa Costa - 581949
  Matheus Alves Cavalcante - 79229
  Francisco Gustavo Gonzaga Pacheco - 582944

"""
# ---- importações ----
from IPython.display import clear_output
import csv

# --- Definições das funções ---

# Funções Recursivas
def ano_valido():
  """
    Garante que o usuário insira um ano válido (número inteiro).

    Return: int: o ano validado.
  """
  try:
    ano = int(input("Ano: "))
    return ano # CASO BASE: Se der certo, retorna o valor e para a recursão.
  except ValueError:
    print("Erro: O ano deve ser um número inteiro. Tente novamente.")
    # PASSO RECURSIVO: Se der errado, a função chama a si mesma para tentar de novo.
    return ano_valido()


def nota_estrela(nome_do_filme):
    """
    Solicita e valida a nota (1 a 5) para um filme.

    Argumento:
        nome_do_filme (str): O nome do filme sendo avaliado
    Retorno:
        int: a nota de 1 a 5.
    """
    avalia_str = input(f"Quantas estrelas você dá para {nome_do_filme} ?, entre 1 a 5: ")
    if not avalia_str.isdigit():
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return nota_estrela(nome_do_filme)
    nota = int(avalia_str)
    if 1 <= nota <= 5:
        return nota
    else:
        print("Número de estrelas inválido. Digite novamente!, entre 1 a 5: ")
        return nota_estrela(nome_do_filme)

# função do menu
def mostra_menu(total):

  """
    exibe o menu principal do programa

    argumento:
        total (int) : número de filmes cadastrados no sistema

    retorno:
        opcao (str) : opção digita pelo usuario para o menu
  """

  print(f'''*********** SysFilmes ***********
  ******* Existem: {total} filmes *******
  *********************************
  1. Cadastrar Filme
  2. Avaliar Filme
  3. Consultar Filme por Título
  4. Listar Filmes por Gênero
  5. Listar Filmes por Estrelas
  6. Listar Todos os Filmes
  7. Carregar Filmes de Arquivo
  8. Carregar Avaliações de Arquivo
  9. Sair do Sistema
  *********************************''')

  opcao = input("Digite a opção desejada: ")
  return opcao
#parte 3
#função para cadastrar filme ( opção 1 )
def criar_filme():

  """
    Solicita os dados de um novo filme ao usuário e o cria.

    A função pede o título, ano e gênero. As estrelas e o número
    de avaliações são inicializados com 0.

    retorno:
      dicionário :
        titulo (stg): Digitado pelo usuario
        ano (int): Digitado pelo usuario
        genero (stg): Digitado pelo usuario
        estrela (float): Deinido como 0.0
        avaliacao (int): Deinido como 0
  """
  titulo = input("Título: ")
  ano = ano_valido()
  genero = input("Gênero: ")
  filme = {
        'título': titulo,
        'ano': ano,
        'gênero': genero,
        'estrelas': 0.0, # Inicializado com 0.0 (float)
        'avaliação': 0 # Inicializado com 0 (int)
    }

  return filme
#parte 4
# função que lista todos os filmes ( opção 6 )
# Laço que interá sobre a lista filmes
def lista_todos(filmes):
  """
    Exibe todos os filmes cadastrados na lista.

    A função percorre a lista de filmes e chama a função mostra_filme()
    para cada um.

    argumento:
      filmes (list) : Lista que contém os registros de cada filme
  """
  for i in filmes:
    mostra_filme(i)

# função que interá sobre os elementos do filme
def mostra_filme(filme):
    """
    Mostra os dados de um filme na tela.

    Argumento:
        filme: dicionário com as infos do filme a ser exibido.
    """
    # Garanta que esta linha tenha 4 espaços de recuo
    print(f'''Título: {filme['título']}
Ano: {filme['ano']}
Gênero: {filme['gênero']}
Estrelas: {filme['estrelas']:.1f}
Número de avaliação: {filme['avaliação']}
''')



# função buscar filme pelo titulo
def buscar_titulo(titulo, filmes):
    """
    Busca por filme na lista com base no título digitado.
    aceita tanto letra maiuscula quanto minúscula para facilitar

    argumento:
        titulo(str): o título do filme na lista
        filmes(list): a lista dos dicionários de filme onde vai ser feita
    retorno:
        dict = dicionario completo
        none= se não tiver nenhum filme na lista com o nome correspondente
    """
    for filme in filmes:
        if filme['título'].lower() == titulo.lower():
            return filme
    return None

def avalia_filme(filmes):
    """
    solicita ao usuário um título e uma nova avaliação em estrelas.

    args:
        filmes(list): A lista de filmes cadastrados no sistema.
    return:
        None: a função não retorna nenhum valor, apenas modifica a lista de filmes e exibe o resultado da operação.
    """
    titulo_busca = input("Digite o título do filme a ser avaliado: ")
    filme_encontrado = buscar_titulo(titulo_busca, filmes)
    if filme_encontrado:
        nova_avaliacao_estrelas = nota_estrela(filme_encontrado['título'])
        soma_antiga = filme_encontrado['estrelas'] * filme_encontrado['avaliação']
        nova_contagem = filme_encontrado['avaliação'] + 1
        filme_encontrado['avaliação'] = nova_contagem
        filme_encontrado['estrelas'] = (soma_antiga + nova_avaliacao_estrelas) / nova_contagem
        print("\nFlme Avaliado com sucesso!.")

        atualiza_avaliacoes(filme_encontrado['título'], nova_avaliacao_estrelas)
def consultar_titulo(filmes):
    """
    função para realizar a busca do filme correspondente e exbir as informações na tela!.
    args:
        filmes(list): lista de filmes cadastrados onde a busca será feita.

    return:
        None: não retnorna valores, apenas o resultado na tela.
    """
    titulo_busca = input("Digite o título do filme desejado: ")
    filme_encontrado = buscar_titulo(titulo_busca, filmes)
    if filme_encontrado:
        print("Filme encontrado:")
        mostra_filme(filme_encontrado)
    else:
        print("Filme não encontrado!.")

def listar_por_genero(filmes):
    """
    Busca filmes por gênero a partir da escolha do usuário e mostra os resultados.
    Após o usuário digitar o gênero, vai procurar na lista de filmes(ignora se é maiúscula ou minúscula) e usa
    a função mostra_filme() para exibir os que foram encontrados.

    Argumento:
        filmes(list) : A lista completa contendo os dicionários de filmes.
    """
    buscar_genero = input("Digite o gênero de busca: ").strip()
    genero_encontrado = []
    for filme in filmes:
        if filme['gênero'].lower() == buscar_genero.lower():
            genero_encontrado.append(filme)
    if genero_encontrado:
        print(f"Foi encontrado {len(genero_encontrado)} do gênero {buscar_genero}: ")
        for filme in genero_encontrado:
            mostra_filme(filme)
    else:
        print("Nenhum filme do gênero foi encontrado")

def listar_por_estrelas(filmes):
    """
    Lista os filmes que possuem uma quantidade de estrelas maior ou igual
    a um valor fornecido pelo usuário.

    argumento:
        filmes(list): a lista de filmes do sistema
    """
    if not filmes:
        print("Nenhum filme cadastrado no sistema.")
        return

    entrada_estrelas = 0.0
    entrada_valida = False
    while not entrada_valida:
        entrada = input("Digite o número de estrelas (entre 1 a 5): ")
        teste_str = entrada.replace('.', '', 1)
        if teste_str.isdigit():
            estrelas = float(entrada)
            if 1 <= estrelas <= 5:
                entrada_estrelas = estrelas
                entrada_valida = True
            else:
                print("Número inválido. O valor deve estar entre 1 e 5.")
        else:
            print("Entrada inválida. Por favor, digite um número.")

    filmes_encontrados = []
    for filme in filmes:
        if filme['estrelas'] >= entrada_estrelas:
            filmes_encontrados.append(filme)

    # Bloco com a indentação corrigida
    if filmes_encontrados:
        print(f"\nListando filmes com {entrada_estrelas:.1f} ou mais estrelas:")
        for filme in filmes_encontrados:
            mostra_filme(filme)
    else:
        # Opcional: Adicionar um 'else' para o caso de nenhum filme ser encontrado
        print(f"\nNenhum filme encontrado com {entrada_estrelas:.1f} ou mais estrelas.")

def carrega_filmes(filmes):
    """
    Carrega filmes de um arquivo CSV para a lista de filmes.
    Pede o nome de um arquivo ao usuário e o lê. O arquivo deve ter um cabeçalho e as colunas: título,ano,genero.

    Argumento:
        filmes(list): A lista de filmes que será adicionada.
    """
    nome_arquivo = input("Digite o nome do arquivo: ")
    try:
        with open (nome_arquivo, 'r', encoding ='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            next(leitor_csv)
            for linha in leitor_csv:
                titulo, ano, genero = linha
                filme = {
                    'título': titulo,
                    'ano': int(ano),
                    'gênero': genero,
                    'estrelas': 0.0,
                    'avaliação': 0
                }
                filmes.append(filme)
        print("Filmes carregados com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado!")

def carrega_avaliacoes(filmes):
    """
    Carrega avaliações a partir de um arquivo .csv informado pelo usuário lido na mesma pasta onde se encontra o arquivo.

    Pede um nome de arquivo ao usuário, le cada avaliação e atualiza a nota média e avaliações.

    Argumento:
        filmes(list): a lista de dicionários de filmes que será atualizada

    Evita erros:
      - FileNotFoundError: se o arquivo de avaliações não for encontrado.
    """

    nome_arquivo = input("Digite o nomo do arquivo: ")
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            next(leitor_csv)

            for linha in leitor_csv:

                if len(linha) == 2:
                    titulo, estrelas = linha
                    filme = buscar_titulo(titulo, filmes)
                    if filme:
                        nova_avaliacao_estrelas = int(estrelas)
                        soma_antiga = filme['estrelas'] *filme['avaliação']

                        nova_contagem = filme['avaliação'] + 1
                        filme['avaliação'] = nova_contagem
                        filme['estrelas'] = (soma_antiga + nova_avaliacao_estrelas) / nova_contagem
        print("Avaliações carregadas com sucesso!")
    except FileNotFoundError:
        print("Arquivo não encontrado!")

def atualiza_filmes(filmes):
    """
    Regrava todos os filmes no arquivo filmes.csv.

    Argumento:
        filmes(list): a lista completa salva

    """
    with open('filmes.csv', 'w', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(['Título', 'Ano', 'Gênero'])
        for filme in filmes:
            escritor_csv.writerow([filme['título'], filme['ano'], filme['gênero']])
    print("Arquivo 'filmes.csv' atualizado com todos os filmes!")


def atualiza_avaliacoes(titulo_filme, nova_nota):
    """
    Adiciona uma nova linha de avaliação ao arquivo avaliacoes.csv

    Argumento:
        titulo_filme(str): o título
        nova_nota(int): a nova nota (estrela) que vai ser registrada.

    """
    with open('avaliacoes.csv', 'a', newline='', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow([titulo_filme, nova_nota])
    print("Arquivo 'avaliacoes.csv' atualizado com sucesso!")



# --- programa principal ---

def main():
  """
    Função principal que executa o loop do menu do sistema.
  """
   # Esta lista irá armazenar os filmes
  filmes = []

  while True:
    # Limpa a tela antes de mostrar o menu
    clear_output()
    # Total de filmes na lista filmes
    filmes_cadastrados = len(filmes)
    # Chama a função que mostra o menu e obtém a opção do usuário
    opcao = mostra_menu(filmes_cadastrados)

    if opcao == '1':
      filme = criar_filme()
      filmes.append(filme)
      atualiza_filmes(filmes)
      input("[**Tecle enter para voltar ao Menu Principal**]")

    elif opcao =='2':
      avalia_filme(filmes)
      input("[**Tecle enter para voltar ao Menu Principal**]")
    elif opcao =='3':
        consultar_titulo(filmes)
        input("[**Tecle enter para voltar ao Menu Principal**]")
    elif opcao =='4':
        listar_por_genero(filmes)
        input("[**Tecle enter para voltar ao Menu Principal**]")
    elif opcao =='5':
        listar_por_estrelas(filmes)
        input("[**Tecle enter para voltar ao Menu Principal**]")

    elif opcao == '6':
      lista_todos(filmes)
      input("[**Tecle enter para voltar ao Menu Principal**]")

    elif opcao == '7':
        carrega_filmes(filmes)
        input("[**Tecle enter para voltar ao Menu Principal**]")
    elif opcao =='8':
        carrega_avaliacoes(filmes)
        input("[**Tecle enter para voltar ao Menu Principal**]")

    elif opcao == '9':
      # Se o usuario digitar 9, o programa para de rodar
      print("[**Bye, você saiu do SysFilmes!**]")
      break

# A linha abaixo garante que a função main() só será executada
# quando o script for rodado diretamente.
if __name__ == '__main__':
  main()