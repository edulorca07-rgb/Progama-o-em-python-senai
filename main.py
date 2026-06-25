senha_correta = "professor123"
tentativas_maximas = 3
tentativas_atuais = 0

# 1. Sistema de Acesso: Login com 3 chances
while tentativas_atuais < tentativas_maximas:
    senha_digitada = input(f"Tentativa {tentativas_atuais + 1} de {tentativas_maximas}. Digite sua senha: ")
    
    if senha_digitada == senha_correta:
        print("\nAcesso concedido! Bem-vindo(a) ao sistema de notas.")
        
        # 2. Inserir notas e calcular média
        soma_notas = 0
        quantidade_notas = 3  # Exemplo com 3 notas
        
        # Estrutura 'for' para inserir notas
        for i in range(quantidade_notas):
            nota = float(input(f"Digite a {i+1}ª nota: "))
            soma_notas += nota
            
        # Cálculo da média
        media = soma_notas / quantidade_notas
        
        print(f"\n--- Relatório Final ---")
        print(f"Média do aluno: {media:.2f}")
        
        if media >= 7:
            print("Situação: Aprovado")
        else:
            print("Situação: Reprovado")
            
        break # Encerra o loop após o cálculo concluído com sucesso
        
    else:
        tentativas_atuais += 1
        print("Senha incorreta!")

# Bloqueio após 3 erros
if tentativas_atuais == tentativas_maximas:
    print("\n[ERRO CRÍTICO] Conta bloqueada! Senha incorreta inserida 3 vezes.")