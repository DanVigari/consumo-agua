#programa de cálculo de consumo de água residencial, comercial e apartamento
#Para calcular o consumo de água, o programa solicita ao usuário que informe o tipo de imóvel e o consumo mensal em metros cúbicos. 
# Com base nessas informações, ele aplica regras específicas para cada tipo de imóvel e fornece feedback sobre o consumo de água.


#entrada do tipo de imóvel

tipo_imovel= input("Digite qual o tipo de imóvel: \n 1-Comercial \n 2-Casa \n 3-Apartamento \n>  ")
consumo= float(input("Digite o consumo mensal de água em m³: "))

# verifica se o consumo é menor ou igual a 0 e se o tipo de imóvel é inválido, caso seja,
# ele é considerado inválido e solicita ao usuário que insira um valor maior que 0.
if consumo <= 0 and tipo_imovel not in ["1","Um","um","comercial","Comercial","2","Dois","dois","casa","Casa","3","Três","três","apartamento","Apartamento"]:
        print("Tipo de imóvel ou consumo inválido. Por favor, insira valores válidos.")
else:
    # Avaliação do Tipo de Imóvel (só executa se o consumo for maior que 0)
    match tipo_imovel:
        case "1" | "Um" | "um" | "Comercial" | "comercial":
            print("Comercial aplicada - consulte o plano corporativo")
        case "2" | "Dois" | "dois" | "Casa" | "casa":
            if consumo <= 25:  # se o consumo for menor ou igual a 25, ele é considerado moderado e dentro dos padrões residenciais.
                print("Consumo moderado - dentro do padrão residencial.")
            else:
                print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
        case "3" | "Três" | "três" | "Apartamento" | "apartamento":
            if consumo < 10:  # se o consumo for menor que 10, ele é considerado econômico e indica um excelente controle de água.
                print("Consumo econômico - excelente controle de água!")
            elif consumo <= 25:  # se o consumo for menor ou igual a 25, ele é considerado moderado e dentro do padrão residencial.
                print("Consumo moderado - dentro do padrão residencial.")
            else:
                print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
        case _:  # caso não seja nenhuma das opções acima, ele é considerado inválido e solicita ao usuário que insira uma opção válida.
            print("Tipo de imóvel inválido. Por favor, insira uma opção válida")


