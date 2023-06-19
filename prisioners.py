import random
import matplotlib.pyplot as plt

def verificar():
    caixas_copia = caixas.copy() # Para embaralhar e não modificar a lista original
    random.shuffle(caixas_copia) # Embaralha caixas_cópia - Distribuição das senhas
    for preso in range(100): # representa cada prisioneiro no loop
        caixa = preso # Define caixa pra representar a caixa inicial de cada preso
        for _ in range(50):
            caixa = caixas_copia[caixa] # Atualiza o valor da variável caixa para representar a nova caixa que o prisioneiro vai trocar, de acordo com a estratégia.
            if caixa == preso:
                break
        else:
            return 0
    return 1

sim = 100_000
caixas = list(range(100))

ganhar = sum([verificar() for _ in range(sim)])

porcentagem_sucesso = (ganhar/sim) * 100
porcentagem_falha = 100 - porcentagem_sucesso

categorias = ['Sucesso', 'Falha']
porcentagens = [porcentagem_sucesso, porcentagem_falha]
cores = ['#55a868', '#d65f5f']

plt.bar(categorias, porcentagens, color=cores)
plt.xlabel('Resultado')
plt.ylabel('Porcentagem')
plt.title('Estratégia de probabilidade vencedora')
plt.show()

print(f"Probabilidade de sucesso com a estratégia do vídeo = {porcentagem_sucesso}")

