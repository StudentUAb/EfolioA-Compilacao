from MONTyPythonParser import MONTyPythonParser
from MONTyPythonVisitor import MONTyPythonVisitor

# Completa a visita para expressões aritméticas, declarações de variáveis e impressão de valores 
class CustomVisitor(MONTyPythonVisitor): # Herdando de MONTyPythonVisitor
    def __init__(self): # Construtor para inicializar o dicionário de variáveis
        self.variables = {}  # Para armazenar o estado atual das variáveis

    def visitAssignment(self, ctx:MONTyPythonParser.AssignmentContext): # Método para visitar expressões de atribuição
        var_name = ctx.ID().getText() # Obtemos o nome da variável
        value = self.visit(ctx.expression()) # Obtemos o valor da expressão
        self.variables[var_name] = value  # Armazenar/atualizar o valor da variável
        print(f"Atribuindo {value} a {var_name}") # Exibimos a atribuição
        return value # Retorna o valor atribuído

    def visitVarDeclaration(self, ctx:MONTyPythonParser.VarDeclarationContext): # Método para visitar declarações de variáveis
        var_type = ctx.INT_TYPE().getText() if ctx.INT_TYPE() else ctx.FLOAT_TYPE().getText() # Obtemos o tipo da variável
        var_name = ctx.ID().getText() # Obtemos o nome da variável
        print(f"Declarando uma variável do tipo {var_type} com o nome {var_name}") # Exibir a declaração
        if ctx.expression() is not None: # Se tiver expressão, é inicialização de variável com valor inicial
            value = self.visit(ctx.expression()) # Obtemos o valor da expressão
            self.variables[var_name] = value # Armazenamos o valor inicial da variável
            print(f"Atribuindo {value} a {var_name} durante a declaração") # Exibimos a atribuição
        else: # Sem valor inicial
            self.variables[var_name] = None # Define a variável sem valor inicial
        return var_name # Retorna o nome da variável declarada

    def visitExpression(self, ctx:MONTyPythonParser.ExpressionContext): # Método para visitar expressões aritméticas 
        if ctx.INT(): # Se for um inteiro 
            return int(ctx.INT().getText()) # Retorna o valor inteiro
        elif ctx.FLOAT(): # Se for um float
            return float(ctx.FLOAT().getText()) # Retorna o valor float
        elif ctx.ID(): # Se for uma variável
            # Verifica se a variável já foi definida
            var_name = ctx.ID().getText() # Obtemos o nome da variável
            if var_name in self.variables: # Verificamos se a variável já foi definida
                return self.variables[var_name] # Retorna o valor da variável
            else: # Variável não definida
                print(f"Erro: Variável '{var_name}' não definida.") # Exibe a mensagem de erro
                return None # Retorna None para indicar erro
        elif ctx.getChildCount() == 3: # Expressão aritmética com operadores binários
            left = self.visit(ctx.getChild(0)) # Visita o nó filho à esquerda 
            op = ctx.getChild(1).getText() # Obtemos o operador
            right = self.visit(ctx.getChild(2)) # Visita o nó filho à direita
            if op == '+': # Se for soma
                return left + right # Retorna a soma
            elif op == '-': # Se for subtração
                return left - right # Retorna a subtração
            elif op == '*': # Se for multiplicação
                return left * right # Retorna a multiplicação
            elif op == '/': # Se for divisão
                return left / right if right != 0 else None  #  Retorna a divisão e prevenimos a divisão por zero
        return 0  # Valor padrão para expressões não cobertas

    def visitPrintStatement(self, ctx:MONTyPythonParser.PrintStatementContext): # Método para visitar impressões de valores 
        value = self.visit(ctx.expression()) # Obtemos o valor da expressão
        print(f"Print: {value}") # Exibimos o valor
        return value # Retornamos o valor impresso

    # Implementações adicionais podem incluir visitantes para estruturas de controle
    # como visitIfStatement, visitWhileLoop, etc., seguindo uma abordagem similar.
