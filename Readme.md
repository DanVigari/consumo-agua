# 💧 Calculadora de Consumo de Água

Programa em Python que calcula e avalia o consumo mensal de água de um imóvel, de acordo com o seu tipo: **Comercial**, **Casa** ou **Apartamento**.

Projeto desenvolvido durante o curso técnico de Análise e Desenvolvimento de Sistemas (ADS), como exercício de lógica de programação.

![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)

## 📑 Sumário

- [Sobre o projeto](#-sobre-o-projeto)
- [Como funciona](#-como-funciona)
- [Regras de consumo](#-regras-de-consumo)
- [Tecnologias e conceitos aplicados](#-tecnologias-e-conceitos-aplicados)
- [Como executar](#-como-executar)
- [Exemplo de uso](#-exemplo-de-uso)


## 📌 Sobre o projeto

O programa solicita ao usuário o tipo de imóvel e o consumo mensal de água em m³, valida essas informações e retorna um feedback sobre o padrão de consumo, com base em faixas específicas para cada tipo de imóvel.

## ⚙️ Como funciona

**1. Entrada de dados**

```python
tipo_imovel = input("Digite qual o tipo de imóvel: \n 1-Comercial \n 2-Casa \n 3-Apartamento \n>  ")
consumo = float(input("Digite o consumo mensal de água em m³: "))
```

O tipo de imóvel pode ser informado tanto por número (1, 2, 3) quanto por nome (Comercial, Casa, Apartamento), em maiúsculas ou minúsculas.

**2. Validação**

```python
if consumo <= 0 and tipo_imovel not in ["1","Um","um","comercial","Comercial", ...]:
    print("Tipo de imóvel ou consumo inválido. Por favor, insira valores válidos.")
```

Impede que o programa processe consumo zero/negativo combinado com um tipo de imóvel fora da lista de opções válidas.

**3. Cálculo e feedback**

Com os dados validados, a estrutura `match/case` avalia o tipo de imóvel e aplica a regra de consumo correspondente.

## 📊 Regras de consumo

| Tipo de imóvel | Faixa de consumo | Resultado |
|---|---|---|
| 🏢 Comercial | — | Segue plano corporativo próprio |
| 🏠 Casa | até 25 m³ | Consumo moderado |
| 🏠 Casa | acima de 25 m³ | Consumo excessivo |
| 🏬 Apartamento | menos de 10 m³ | Consumo econômico |
| 🏬 Apartamento | até 25 m³ | Consumo moderado |
| 🏬 Apartamento | acima de 25 m³ | Consumo excessivo |

## 🧠 Tecnologias e conceitos aplicados

- Python
- Entrada de dados com `input()`
- Conversão de tipos com `float()`
- Estruturas condicionais `if` / `else`
- Estrutura `match/case`
- Validação de dados do usuário


## 💻 Exemplo de uso

```
Digite qual o tipo de imóvel: 
 1-Comercial 
 2-Casa 
 3-Apartamento 
>  2
Digite o consumo mensal de água em m³: 18
Consumo moderado - dentro do padrão residencial.
```


