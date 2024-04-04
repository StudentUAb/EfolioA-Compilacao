# parse_monty.py

import sys # Importamos sys para acessar argv
from antlr4 import * # Importamos classes do ANTLR
from MONTyPythonLexer import MONTyPythonLexer # Importamos o lexer
from MONTyPythonParser import MONTyPythonParser # Importamos o parser
from MONTyPythonCustomVisitor import CustomVisitor # Importamos a classe de visita personalizada
from MontyPythonErrorListener import MontyPythonErrorListener  # Improtamos a classe de tratamento de erros

def parse_file(file_path): # Função para parsear o arquivo
    input_stream = FileStream(file_path, encoding='utf-8') # Criamos um input stream para o arquivo de entrada 
    lexer = MONTyPythonLexer(input_stream) # Criamos um lexer para o input stream
    stream = CommonTokenStream(lexer) # Criamos um token stream para o lexer
    parser = MONTyPythonParser(stream) # Criamos um parser para o token stream

    # Adicionamos o ErrorListener personalizado
    parser.removeErrorListeners()  # Reomvemos os listeners padrão
    parser.addErrorListener(MontyPythonErrorListener())  # Adicionamos o seu ErrorListener personalizado

    tree = parser.program() # Fazemos o parse e obtemos a árvore sintática
    visitor = CustomVisitor() # Criamos um visitante personalizado
    visitor.visit(tree) # Visitamos a árvore sintática

if __name__ == '__main__': # Executa o main apenas se for executado diretamente
    if len(sys.argv) != 2: # Verificamos se foi passado o caminho do arquivo como argumento
        print("Uso: python3 parse_monty.py <caminho_para_arquivo_monty_python>") # Exibimos a mensagem de uso correto
        sys.exit(1) # Encerramos o programa com código de erro

    file_path = sys.argv[1] # Obtemos o caminho do arquivo a ser parseado
    parse_file(file_path) # Chamamos a função de parse passando o caminho do arquivo
