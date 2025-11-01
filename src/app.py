# =========================================================================
# SPRINT 2: Manipulação e Análise de Dados
# Funcionalidades: Estatísticas, Busca por Nome e Tratamento de Erros Aprimorado
# =========================================================================

# Estrutura de dados inicial (herdada da Sprint 1)
pacientes = []

def cadastrar_paciente():
    """
    [Épico 2 - 003] Funcionalidade: Cadastrar Paciente (Aprimorado com Tratamento de Erros)
    """
    print("\n=== CADASTRO DE PACIENTE ===")
    
    # Validação de Nome (não pode ser vazio)
    while True:
        nome = input("Nome do paciente: ").strip()
        if nome:
            break
        print("Erro: O nome não pode ser vazio.")
    
    # [Épico 3 - 007] Tratamento de Erros: Validação de Idade (numérico e positivo)
    while True:
        try:
            idade_input = input("Idade: ")
            idade = int(idade_input)
            if idade <= 0:
                print("Erro: A idade deve ser um número inteiro positivo.")
                continue
            break
        except ValueError:
            print("Erro: A idade deve ser um valor numérico.")
    
    # Coleta de CPF e Telefone
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    
    novo_paciente = {
        "nome": nome,
        "idade": idade,
        "cpf": cpf,
        "telefone": telefone
    }
    
    pacientes.append(novo_paciente)
    print("\nPaciente cadastrado com sucesso!")


def ver_estatisticas():
    """
    [Épico 3 - 005] Funcionalidade: Calcular e Exibir Estatísticas
    Calcula o número total, idade média, paciente mais novo e mais velho.
    """
    print("\n=== ESTATÍSTICAS DA CLÍNICA VIDA+ ===")
    
    num_pacientes = len(pacientes)
    
    # 1. Número total de pacientes
    print(f"Número total de pacientes cadastrados: {num_pacientes}") #

    if num_pacientes == 0:
        print("Não há dados suficientes para calcular estatísticas.")
        return

    # Extrai todas as idades
    idades = [p['idade'] for p in pacientes]
    
    # 2. Idade Média
    idade_media = sum(idades) / num_pacientes
    print(f"Idade média dos pacientes: {idade_media:.2f} anos") #

    # 3. Paciente mais novo e mais velho
    paciente_mais_novo = min(pacientes, key=lambda p: p['idade'])
    paciente_mais_velho = max(pacientes, key=lambda p: p['idade'])
    
    print(f"Paciente mais novo: {paciente_mais_novo['nome']} ({paciente_mais_novo['idade']} anos)") #
    print(f"Paciente mais velho: {paciente_mais_velho['nome']} ({paciente_mais_velho['idade']} anos)") #


def buscar_paciente():
    """
    [Épico 3 - 006] Funcionalidade: Buscar Paciente por Nome
    Permite buscar um paciente pelo nome.
    """
    print("\n=== BUSCA DE PACIENTE ===")
    
    termo_busca = input("Digite o nome ou parte do nome do paciente: ").strip().lower()
    
    if not termo_busca:
        print("O termo de busca não pode ser vazio.")
        return

    encontrados = []
    
    # Busca pacientes cujo nome contém o termo de busca (busca parcial)
    for paciente in pacientes:
        if termo_busca in paciente['nome'].lower():
            encontrados.append(paciente)

    if encontrados:
        print(f"\nForam encontrados {len(encontrados)} paciente(s):")
        print("-" * 50)
        print(f"{'NOME':<20} {'IDADE':<6} {'CPF':<15} {'TELEFONE':<20}")
        print("-" * 50)
        for paciente in encontrados:
             print(f"{paciente['nome']:<20} {paciente['idade']:<6} {paciente['cpf']:<15} {paciente['telefone']:<20}")
        print("-" * 50)
    else:
        print(f"Nenhum paciente encontrado com o nome '{termo_busca}'.")


def listar_pacientes():
    """
    [Épico 2 - 004] Funcionalidade: Listar Todos os Pacientes (Herdado da Sprint 1)
    """
    print("\n=== LISTA DE PACIENTES CADASTRADOS ===")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    # (Código de listagem mantido)
    print("-" * 50)
    print(f"{'NOME':<20} {'IDADE':<6} {'CPF':<15} {'TELEFONE':<20}")
    print("-" * 50)
    
    for paciente in pacientes:
        print(f"{paciente['nome']:<20} {paciente['idade']:<6} {paciente['cpf']:<15} {paciente['telefone']:<20}")
    
    print("-" * 50)
    print(f"Total de pacientes: {len(pacientes)}")


def menu_principal():
    """
    [Épico 2 - 002] Implementar Menu Principal (Loop) (Herdado da Sprint 1)
    """
    while True:
        print("\n" + "="*25)
        print("=== SISTEMA CLÍNICA VIDA+ ===") # Exemplo de execução esperado
        print("="*25)
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")
        print("---------------------------")
        
        # [Épico 3 - 007] Tratamento de Erros: Validação de opção de menu
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            cadastrar_paciente()
        elif opcao == '2':
            ver_estatisticas()
        elif opcao == '3':
            buscar_paciente()
        elif opcao == '4':
            listar_pacientes()
        elif opcao == '5':
            print("Saindo do sistema. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, escolha um número de 1 a 5.")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal()