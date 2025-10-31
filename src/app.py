# =========================================================================
# SPRINT 1: Infraestrutura e Cadastro Básico
# Funcionalidades: Menu (Loop), Cadastrar Paciente, Listar Todos os Pacientes
# =========================================================================

# Estrutura de dados para armazenar os pacientes.
# Usamos uma lista de dicionários para armazenar múltiplos pacientes (Requisito Técnico).
pacientes = []

def cadastrar_paciente():
    """
    [Épico 2 - 003] Funcionalidade: Cadastrar Paciente
    Solicita Nome, Idade, CPF e Telefone do paciente e armazena.
    """
    print("\n=== CADASTRO DE PACIENTE ===")
    
    # Coleta de dados
    nome = input("Nome do paciente: ")
    
    # Coleta a Idade. Implementação básica de tratamento de erro para int (Requisito Técnico).
    while True:
        try:
            idade = int(input("Idade: ")) # A idade deve ser armazenada como um número inteiro.
            if idade <= 0:
                print("Erro: A idade deve ser um número positivo.")
                continue
            break
        except ValueError:
            print("Erro: A idade deve ser um valor numérico.")
    
    # Incluímos o CPF, conforme definido na Sprint 1 para futura necessidade.
    cpf = input("CPF: ")
    telefone = input("Telefone: ")
    
    # Cria o dicionário do paciente
    novo_paciente = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "telefone": telefone
    }
    
    # Adiciona o novo paciente à lista principal
    pacientes.append(novo_paciente)
    print("\nPaciente cadastrado com sucesso!")
    
    # [cite_start]Simulação do exemplo de execução esperado [cite: 89, 90, 91, 92]
    # (Nome: João Silva, Idade: 45, Telefone: (11) 99999-9999) 
    # Obs: Adicionamos o CPF como requisito extra, mas o fluxo segue a lógica.


def listar_pacientes():
    """
    [Épico 2 - 004] Funcionalidade: Listar Todos os Pacientes
    Exibe todos os pacientes cadastrados de forma organizada.
    """
    print("\n=== LISTA DE PACIENTES CADASTRADOS ===")
    if not pacientes:
        print("Nenhum paciente cadastrado.") # Exibe mensagem se lista vazia (Critério de Aceitação)
        return

    # Cabeçalho da tabela
    print("-" * 50)
    print(f"{'NOME':<20} {'IDADE':<6} {'CPF':<15} {'TELEFONE':<20}")
    print("-" * 50)
    
    # Iteração e exibição dos dados
    for paciente in pacientes:
        print(f"{paciente['nome']:<20} {paciente['idade']:<6} {paciente['cpf']:<15} {paciente['telefone']:<20}")
    
    print("-" * 50)
    print(f"Total de pacientes: {len(pacientes)}")


# Implementação do Menu Principal (Loop)
def menu_principal():
    """
    [Épico 2 - 002] Implementar Menu Principal (Loop)
    [cite_start]O programa deve funcionar em loop até o usuário escolher sair (Requisito Técnico)[cite: 80].
    """
    while True:
        print("\n" + "="*25)
        print("=== SISTEMA CLÍNICA VIDA+ ===") # Exemplo de execução esperada [cite: 82]
        print("="*25)
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas (PRÓXIMA SPRINT)")
        print("3. Buscar paciente (PRÓXIMA SPRINT)")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        print("---------------------------")
        
        # Tratamento básico de erro para escolha de opção
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            print("\nFuncionalidade 'Ver estatísticas' será implementada na Sprint 2.")
        elif opcao == '3':
            print("\nFuncionalidade 'Buscar paciente' será implementada na Sprint 2.")
        elif opcao == '4':
            listar_pacientes()
        elif opcao == '5':
            print("Saindo do sistema. Até mais!")
            break  # Encerra o loop (Critério de Aceitação: Sair encerra o programa)
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.") # Trata erro de entrada (Requisito Técnico) [cite: 79]

# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()