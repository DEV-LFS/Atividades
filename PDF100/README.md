# 100 Exercícios de Lógica de Programação — Soluções em Python

> Baseado no PDF enviado pelo usuário. As soluções foram escritas em Python 3 e organizadas em arquivos individuais.

## Observação importante sobre o PDF

O arquivo fornecido contém os exercícios **01 a 10** e depois salta diretamente para o **14**. Os enunciados dos exercícios **11, 12 e 13 não aparecem no PDF**. Para não inventar requisitos, mantive esses três números no projeto com arquivos de aviso. Todos os demais exercícios presentes no material foram implementados.

## Como executar

Entre na pasta `solucoes` e execute o arquivo desejado:

```bash
python ex001_soma_de_dois_numeros.py
```

Não há dependências externas; basta Python 3.

## Estrutura

- `README.md`: explicação de cada exercício.
- `solucoes/`: um arquivo `.py` por número de exercício.

## Índice rápido

- [Módulo 01 — Primeiros algoritmos](#modulo-01-primeiros-algoritmos) — exercícios 01 a 15
- [Módulo 02 — Estruturas condicionais](#modulo-02-estruturas-condicionais) — exercícios 16 a 35
- [Módulo 03 — Estruturas de repetição](#modulo-03-estruturas-de-repeticao) — exercícios 36 a 60
- [Módulo 04 — Vetores e matrizes](#modulo-04-vetores-e-matrizes) — exercícios 61 a 80
- [Módulo 05 — Funções e desafios combinados](#modulo-05-funcoes-e-desafios-combinados) — exercícios 81 a 100


## Módulo 01 — Primeiros algoritmos

### Exercício 01 — Soma de dois números

**Objetivo:** Ler dois números inteiros e mostrar a soma entre eles.

**Lógica usada:** Armazene os dois valores em variáveis e use o operador `+` para calcular o resultado.

**Ponto-chave:** A soma funciona também com zero e números negativos.

**Arquivo:** [`solucoes/ex001_soma_de_dois_numeros.py`](solucoes/ex001_soma_de_dois_numeros.py)

### Exercício 02 — Média de duas notas

**Objetivo:** Ler duas notas reais, calcular a média aritmética e exibi-la com uma casa decimal.

**Lógica usada:** Some as duas notas, divida por 2 e formate apenas a saída com `:.1f`.

**Ponto-chave:** A formatação não altera o valor armazenado, apenas a forma como ele é exibido.

**Arquivo:** [`solucoes/ex002_media_de_duas_notas.py`](solucoes/ex002_media_de_duas_notas.py)

### Exercício 03 — Antecessor e sucessor

**Objetivo:** Ler um número inteiro e mostrar seu antecessor e sucessor.

**Lógica usada:** O antecessor é `n - 1` e o sucessor é `n + 1`.

**Ponto-chave:** A diferença entre sucessor e antecessor é sempre 2.

**Arquivo:** [`solucoes/ex003_antecessor_e_sucessor.py`](solucoes/ex003_antecessor_e_sucessor.py)

### Exercício 04 — Dobro, triplo e metade

**Objetivo:** Ler um número real e mostrar seu dobro, triplo e metade.

**Lógica usada:** Use a entrada original para calcular `valor * 2`, `valor * 3` e `valor / 2`.

**Ponto-chave:** Todos os cálculos partem da mesma entrada original.

**Arquivo:** [`solucoes/ex004_dobro_triplo_e_metade.py`](solucoes/ex004_dobro_triplo_e_metade.py)

### Exercício 05 — Conversão de medidas

**Objetivo:** Converter uma medida em metros para centímetros e milímetros.

**Lógica usada:** Multiplique metros por 100 para obter centímetros e por 1000 para obter milímetros.

**Ponto-chave:** 1 metro = 100 centímetros = 1000 milímetros.

**Arquivo:** [`solucoes/ex005_conversao_de_medidas.py`](solucoes/ex005_conversao_de_medidas.py)

### Exercício 06 — Área e perímetro do retângulo

**Objetivo:** Ler largura e altura e calcular área e perímetro de um retângulo.

**Lógica usada:** Área = largura × altura. Perímetro = 2 × (largura + altura).

**Ponto-chave:** Área e perímetro são grandezas diferentes, mesmo em um quadrado.

**Arquivo:** [`solucoes/ex006_area_e_perimetro_do_retangulo.py`](solucoes/ex006_area_e_perimetro_do_retangulo.py)

### Exercício 07 — Celsius para Fahrenheit

**Objetivo:** Converter uma temperatura em Celsius para Fahrenheit.

**Lógica usada:** Aplique a fórmula `F = C * 9 / 5 + 32`.

**Ponto-chave:** Em -40°, Celsius e Fahrenheit têm o mesmo valor.

**Arquivo:** [`solucoes/ex007_celsius_para_fahrenheit.py`](solucoes/ex007_celsius_para_fahrenheit.py)

### Exercício 08 — Desconto no produto

**Objetivo:** Calcular desconto de 10% e preço final de um produto.

**Lógica usada:** Desconto = preço × 0,10. Preço final = preço - desconto.

**Ponto-chave:** Preço final + desconto deve reconstruir o preço original.

**Arquivo:** [`solucoes/ex008_desconto_no_produto.py`](solucoes/ex008_desconto_no_produto.py)

### Exercício 09 — Reajuste salarial

**Objetivo:** Calcular aumento de 15% e novo salário.

**Lógica usada:** Aumento = salário × 0,15. Novo salário = salário + aumento.

**Ponto-chave:** O novo salário menos o antigo deve ser exatamente o aumento calculado.

**Arquivo:** [`solucoes/ex009_reajuste_salarial.py`](solucoes/ex009_reajuste_salarial.py)

### Exercício 10 — Salário com comissão

**Objetivo:** Calcular comissão de 4% sobre as vendas e somá-la ao salário fixo.

**Lógica usada:** A comissão incide apenas sobre o total vendido, nunca sobre o salário fixo.

**Ponto-chave:** Se não houver vendas, a comissão é zero e o salário total é igual ao salário fixo.

**Arquivo:** [`solucoes/ex010_salario_com_comissao.py`](solucoes/ex010_salario_com_comissao.py)

### Exercício 11 — Exercício 11 — ausente no PDF

**Objetivo:** O enunciado deste exercício não está presente no arquivo enviado.

**Lógica usada:** Para não inventar requisitos, este arquivo apenas registra a ausência do enunciado. Quando a página correspondente for enviada, a solução pode ser substituída sem alterar a numeração do projeto.

**Ponto-chave:** O PDF salta do exercício 10 diretamente para o exercício 14.

**Arquivo:** [`solucoes/ex011_exercicio_11_-_ausente_no_pdf.py`](solucoes/ex011_exercicio_11_-_ausente_no_pdf.py)

> ⚠️ O enunciado não existe no PDF fornecido; por isso, não há solução inventada.

### Exercício 12 — Exercício 12 — ausente no PDF

**Objetivo:** O enunciado deste exercício não está presente no arquivo enviado.

**Lógica usada:** Para não inventar requisitos, este arquivo apenas registra a ausência do enunciado. Quando a página correspondente for enviada, a solução pode ser substituída sem alterar a numeração do projeto.

**Ponto-chave:** O PDF salta do exercício 10 diretamente para o exercício 14.

**Arquivo:** [`solucoes/ex012_exercicio_12_-_ausente_no_pdf.py`](solucoes/ex012_exercicio_12_-_ausente_no_pdf.py)

> ⚠️ O enunciado não existe no PDF fornecido; por isso, não há solução inventada.

### Exercício 13 — Exercício 13 — ausente no PDF

**Objetivo:** O enunciado deste exercício não está presente no arquivo enviado.

**Lógica usada:** Para não inventar requisitos, este arquivo apenas registra a ausência do enunciado. Quando a página correspondente for enviada, a solução pode ser substituída sem alterar a numeração do projeto.

**Ponto-chave:** O PDF salta do exercício 10 diretamente para o exercício 14.

**Arquivo:** [`solucoes/ex013_exercicio_13_-_ausente_no_pdf.py`](solucoes/ex013_exercicio_13_-_ausente_no_pdf.py)

> ⚠️ O enunciado não existe no PDF fornecido; por isso, não há solução inventada.

### Exercício 14 — Troca de valores

**Objetivo:** Ler dois inteiros e trocar seus conteúdos usando uma variável auxiliar.

**Lógica usada:** Guarde temporariamente o valor de A antes de sobrescrevê-lo.

**Ponto-chave:** Fazer a troca duas vezes devolve os valores originais.

**Arquivo:** [`solucoes/ex014_troca_de_valores.py`](solucoes/ex014_troca_de_valores.py)

### Exercício 15 — Custo final da compra

**Objetivo:** Calcular subtotal e total de uma compra considerando preço unitário, quantidade e frete.

**Lógica usada:** Subtotal = preço unitário × quantidade. Total = subtotal + frete.

**Ponto-chave:** Total - subtotal deve ser exatamente o valor do frete.

**Arquivo:** [`solucoes/ex015_custo_final_da_compra.py`](solucoes/ex015_custo_final_da_compra.py)


## Módulo 02 — Estruturas condicionais

### Exercício 16 — Positivo, negativo ou zero

**Objetivo:** Classificar um número real como positivo, negativo ou zero.

**Lógica usada:** Use uma cadeia `if/elif/else` para garantir uma única classificação.

**Ponto-chave:** Zero precisa ser tratado separadamente; ele não é positivo nem negativo.

**Arquivo:** [`solucoes/ex016_positivo_negativo_ou_zero.py`](solucoes/ex016_positivo_negativo_ou_zero.py)

### Exercício 17 — Par ou ímpar

**Objetivo:** Informar se um número inteiro é par ou ímpar.

**Lógica usada:** Um inteiro é par quando `numero % 2 == 0`.

**Ponto-chave:** A regra vale também para zero e inteiros negativos.

**Arquivo:** [`solucoes/ex017_par_ou_impar.py`](solucoes/ex017_par_ou_impar.py)

### Exercício 18 — Maior de dois números

**Objetivo:** Comparar dois números reais e mostrar o maior; se forem iguais, informar a igualdade.

**Lógica usada:** Compare primeiro a igualdade ou use três ramos exclusivos.

**Ponto-chave:** Não escolha arbitrariamente um dos valores quando eles forem iguais.

**Arquivo:** [`solucoes/ex018_maior_de_dois_numeros.py`](solucoes/ex018_maior_de_dois_numeros.py)

### Exercício 19 — Maior e menor de três números

**Objetivo:** Ler três números reais e mostrar o maior e o menor, inclusive com valores repetidos.

**Lógica usada:** Inicialize maior e menor com o primeiro valor e compare os demais.

**Ponto-chave:** Inicializar com uma entrada real evita erros quando todos os valores são negativos.

**Arquivo:** [`solucoes/ex019_maior_e_menor_de_tres_numeros.py`](solucoes/ex019_maior_e_menor_de_tres_numeros.py)

### Exercício 20 — Três valores em ordem crescente

**Objetivo:** Ler três inteiros e exibi-los em ordem crescente, aceitando repetidos.

**Lógica usada:** Use trocas condicionais entre pares para ordenar sem depender de uma função pronta.

**Ponto-chave:** As três comparações garantem que `a <= b <= c`.

**Arquivo:** [`solucoes/ex020_tres_valores_em_ordem_crescente.py`](solucoes/ex020_tres_valores_em_ordem_crescente.py)

### Exercício 21 — Aprovado ou reprovado

**Objetivo:** Calcular a média de duas notas e classificar o aluno.

**Lógica usada:** Média maior ou igual a 7,0 significa APROVADO; abaixo disso, REPROVADO.

**Ponto-chave:** O valor 7,0 pertence à faixa de aprovação.

**Arquivo:** [`solucoes/ex021_aprovado_ou_reprovado.py`](solucoes/ex021_aprovado_ou_reprovado.py)

### Exercício 22 — Situação do aluno por faixa

**Objetivo:** Classificar o aluno em reprovado, recuperação ou aprovado a partir da média.

**Lógica usada:** Use limites sem sobreposição: `<5`, `>=5 e <7`, `>=7`.

**Ponto-chave:** A ordem das condições permite tratar corretamente os valores de fronteira 5,0 e 7,0.

**Arquivo:** [`solucoes/ex022_situacao_do_aluno_por_faixa.py`](solucoes/ex022_situacao_do_aluno_por_faixa.py)

### Exercício 23 — Categoria de votação

**Objetivo:** Classificar a categoria de votação pela idade conforme a tabela do exercício.

**Lógica usada:** Menor de 16: não pode votar; 16-17: opcional; 18-69: obrigatório; 70+: opcional.

**Ponto-chave:** Os limites 16, 18 e 70 precisam cair exatamente nas categorias definidas.

**Arquivo:** [`solucoes/ex023_categoria_de_votacao.py`](solucoes/ex023_categoria_de_votacao.py)

### Exercício 24 — Ano bissexto

**Objetivo:** Determinar se um ano é bissexto.

**Lógica usada:** É bissexto se for divisível por 400, ou se for divisível por 4 e não por 100.

**Ponto-chave:** 1900 não é bissexto; 2000 é bissexto.

**Arquivo:** [`solucoes/ex024_ano_bissexto.py`](solucoes/ex024_ano_bissexto.py)

### Exercício 25 — Preço conforme a forma de pagamento

**Objetivo:** Calcular o preço final conforme a opção de pagamento.

**Lógica usada:** Opção 1: 10% de desconto; 2: 5% de desconto; 3: sem alteração; 4: 8% de acréscimo.

**Ponto-chave:** Cada opção aplica uma única regra.

**Arquivo:** [`solucoes/ex025_preco_conforme_a_forma_de_pagamento.py`](solucoes/ex025_preco_conforme_a_forma_de_pagamento.py)

### Exercício 26 — Reajuste por faixa salarial

**Objetivo:** Aplicar reajuste de acordo com o salário atual e mostrar percentual, aumento e novo salário.

**Lógica usada:** Até R$ 1.500: 15%; de R$ 1.500,01 a R$ 3.000: 10%; acima de R$ 3.000: 5%.

**Ponto-chave:** Os limites 1500 e 3000 pertencem, respectivamente, às faixas de 15% e 10%.

**Arquivo:** [`solucoes/ex026_reajuste_por_faixa_salarial.py`](solucoes/ex026_reajuste_por_faixa_salarial.py)

### Exercício 27 — Classificação de IMC

**Objetivo:** Calcular o IMC e classificá-lo segundo as faixas didáticas do exercício.

**Lógica usada:** IMC = peso / altura². Classifique somente depois de calcular o valor numérico.

**Ponto-chave:** Valores exatamente 18,5; 25,0 e 30,0 iniciam as faixas seguintes.

**Arquivo:** [`solucoes/ex027_classificacao_de_imc.py`](solucoes/ex027_classificacao_de_imc.py)

### Exercício 28 — É possível formar um triângulo?

**Objetivo:** Verificar se três medidas positivas formam um triângulo.

**Lógica usada:** Cada lado deve ser menor que a soma dos outros dois.

**Ponto-chave:** As três desigualdades precisam ser verdadeiras ao mesmo tempo.

**Arquivo:** [`solucoes/ex028_e_possivel_formar_um_triangulo.py`](solucoes/ex028_e_possivel_formar_um_triangulo.py)

### Exercício 29 — Tipo de triângulo

**Objetivo:** Validar três lados e, se formarem triângulo, classificá-lo em equilátero, isósceles ou escaleno.

**Lógica usada:** Primeiro valide a existência do triângulo; só depois compare os lados.

**Ponto-chave:** Uma classificação de tipo só faz sentido depois que a desigualdade triangular foi satisfeita.

**Arquivo:** [`solucoes/ex029_tipo_de_triangulo.py`](solucoes/ex029_tipo_de_triangulo.py)

### Exercício 30 — Aprovação de empréstimo

**Objetivo:** Calcular a prestação mensal de um imóvel e verificar se ela não ultrapassa 30% do salário.

**Lógica usada:** Prestação = valor do imóvel / (anos × 12). Aprovar se prestação <= 30% do salário.

**Ponto-chave:** Converta anos em meses antes de calcular a prestação.

**Arquivo:** [`solucoes/ex030_aprovacao_de_emprestimo.py`](solucoes/ex030_aprovacao_de_emprestimo.py)

### Exercício 31 — Divisível por 3 e por 5

**Objetivo:** Classificar um inteiro conforme a divisibilidade por 3 e 5.

**Lógica usada:** Teste primeiro o caso divisível por ambos, depois apenas 3, apenas 5 e nenhum.

**Ponto-chave:** Se testar apenas `por3` primeiro, números divisíveis pelos dois poderiam ser classificados incorretamente.

**Arquivo:** [`solucoes/ex031_divisivel_por_3_e_por_5.py`](solucoes/ex031_divisivel_por_3_e_por_5.py)

### Exercício 32 — Número dentro do intervalo

**Objetivo:** Informar se um número real está no intervalo fechado de 10 a 20.

**Lógica usada:** Use `10 <= numero <= 20`.

**Ponto-chave:** Os extremos 10 e 20 pertencem ao intervalo.

**Arquivo:** [`solucoes/ex032_numero_dentro_do_intervalo.py`](solucoes/ex032_numero_dentro_do_intervalo.py)

### Exercício 33 — Dia da semana

**Objetivo:** Converter um número de 1 a 7 para o dia da semana correspondente.

**Lógica usada:** Mapeie cada número para o texto correspondente; qualquer outro valor é inválido.

**Ponto-chave:** Valores fora de 1 a 7 devem produzir a mensagem de opção inválida.

**Arquivo:** [`solucoes/ex033_dia_da_semana.py`](solucoes/ex033_dia_da_semana.py)

### Exercício 34 — Quantidade de dias do mês

**Objetivo:** Ler mês e ano e informar a quantidade de dias, tratando fevereiro e ano bissexto.

**Lógica usada:** Meses 1,3,5,7,8,10,12 têm 31; 4,6,9,11 têm 30; fevereiro tem 28 ou 29.

**Ponto-chave:** Valide o mês antes de decidir a quantidade de dias.

**Arquivo:** [`solucoes/ex034_quantidade_de_dias_do_mes.py`](solucoes/ex034_quantidade_de_dias_do_mes.py)

### Exercício 35 — Valor do ingresso

**Objetivo:** Calcular o preço do ingresso aplicando meia-entrada quando uma das condições for satisfeita.

**Lógica usada:** Preço normal R$ 30. Paga metade quem tem menos de 12 anos, é estudante ou tem 60 anos ou mais. O desconto não acumula.

**Ponto-chave:** Mesmo que a pessoa satisfaça mais de uma condição, o preço continua sendo apenas meia-entrada.

**Arquivo:** [`solucoes/ex035_valor_do_ingresso.py`](solucoes/ex035_valor_do_ingresso.py)


## Módulo 03 — Estruturas de repetição

### Exercício 36 — Contagem de 1 até 10

**Objetivo:** Mostrar os inteiros de 1 a 10, um por linha, usando repetição.

**Lógica usada:** Percorra `range(1, 11)`.

**Ponto-chave:** A saída deve conter exatamente 10 números.

**Arquivo:** [`solucoes/ex036_contagem_de_1_ate_10.py`](solucoes/ex036_contagem_de_1_ate_10.py)

### Exercício 37 — Contagem regressiva

**Objetivo:** Mostrar os números de 10 até 0 e, depois, a mensagem FIM.

**Lógica usada:** Use um intervalo decrescente que inclua o zero.

**Ponto-chave:** São 11 números, de 10 até 0, seguidos por uma única mensagem FIM.

**Arquivo:** [`solucoes/ex037_contagem_regressiva.py`](solucoes/ex037_contagem_regressiva.py)

### Exercício 38 — Contagem até um limite

**Objetivo:** Ler um inteiro positivo N e mostrar de 1 até N.

**Lógica usada:** Use um laço de 1 a N inclusive.

**Ponto-chave:** Para N = 1, a saída contém apenas o número 1.

**Arquivo:** [`solucoes/ex038_contagem_ate_um_limite.py`](solucoes/ex038_contagem_ate_um_limite.py)

### Exercício 39 — Números pares de 1 até 100

**Objetivo:** Mostrar todos os números pares de 1 até 100 usando repetição.

**Lógica usada:** Comece em 2 e avance de 2 em 2.

**Ponto-chave:** A sequência contém exatamente 50 números, começando em 2 e terminando em 100.

**Arquivo:** [`solucoes/ex039_numeros_pares_de_1_ate_100.py`](solucoes/ex039_numeros_pares_de_1_ate_100.py)

### Exercício 40 — Números ímpares de 1 até 100

**Objetivo:** Mostrar todos os números ímpares de 1 até 100.

**Lógica usada:** Comece em 1 e avance de 2 em 2 até 99.

**Ponto-chave:** A sequência contém exatamente 50 números e nenhum valor par.

**Arquivo:** [`solucoes/ex040_numeros_impares_de_1_ate_100.py`](solucoes/ex040_numeros_impares_de_1_ate_100.py)

### Exercício 41 — Tabuada de um número

**Objetivo:** Ler um inteiro e mostrar sua tabuada de 1 a 10.

**Lógica usada:** Repita os multiplicadores de 1 a 10 e calcule `numero * multiplicador`.

**Ponto-chave:** A primeira linha usa multiplicador 1 e a última usa multiplicador 10.

**Arquivo:** [`solucoes/ex041_tabuada_de_um_numero.py`](solucoes/ex041_tabuada_de_um_numero.py)

### Exercício 42 — Tabuada com início e fim

**Objetivo:** Mostrar a tabuada de um número entre multiplicadores inicial e final, funcionando em ordem crescente ou decrescente.

**Lógica usada:** Determine o passo: `+1` se início <= fim, caso contrário `-1`.

**Ponto-chave:** Os dois limites são inclusivos, mesmo quando a contagem é decrescente.

**Arquivo:** [`solucoes/ex042_tabuada_com_inicio_e_fim.py`](solucoes/ex042_tabuada_com_inicio_e_fim.py)

### Exercício 43 — Somatório de 1 até N

**Objetivo:** Calcular a soma de todos os inteiros de 1 até N.

**Lógica usada:** Use um acumulador iniciado em zero e some cada valor do intervalo.

**Ponto-chave:** O resultado pode ser conferido pela fórmula `N * (N + 1) / 2`.

**Arquivo:** [`solucoes/ex043_somatorio_de_1_ate_n.py`](solucoes/ex043_somatorio_de_1_ate_n.py)

### Exercício 44 — Fatorial

**Objetivo:** Calcular o fatorial de um inteiro entre 0 e 12.

**Lógica usada:** Inicie o produto em 1 e multiplique de 2 até N. Para N=0, nenhuma multiplicação é necessária e o resultado permanece 1.

**Ponto-chave:** 0! = 1 e 1! = 1.

**Arquivo:** [`solucoes/ex044_fatorial.py`](solucoes/ex044_fatorial.py)

### Exercício 45 — Sequência de Fibonacci

**Objetivo:** Ler a quantidade de termos e mostrar os primeiros valores da sequência de Fibonacci.

**Lógica usada:** Comece com 0 e 1; cada termo seguinte é a soma dos dois anteriores.

**Ponto-chave:** A sequência deve exibir exatamente a quantidade solicitada.

**Arquivo:** [`solucoes/ex045_sequencia_de_fibonacci.py`](solucoes/ex045_sequencia_de_fibonacci.py)

### Exercício 46 — Soma de cinco valores

**Objetivo:** Ler cinco números reais e exibir a soma total.

**Lógica usada:** Use um acumulador e repita a leitura cinco vezes.

**Ponto-chave:** Exatamente cinco valores devem participar da soma.

**Arquivo:** [`solucoes/ex046_soma_de_cinco_valores.py`](solucoes/ex046_soma_de_cinco_valores.py)

### Exercício 47 — Média de dez notas

**Objetivo:** Ler dez notas reais entre 0 e 10 e calcular a média aritmética.

**Lógica usada:** Some as dez notas e divida por 10.

**Ponto-chave:** A divisão é sempre por 10, mesmo quando há notas repetidas.

**Arquivo:** [`solucoes/ex047_media_de_dez_notas.py`](solucoes/ex047_media_de_dez_notas.py)

### Exercício 48 — Positivos, negativos e zeros

**Objetivo:** Ler oito inteiros e contar quantos são positivos, negativos e iguais a zero.

**Lógica usada:** Mantenha três contadores e atualize exatamente um deles para cada entrada.

**Ponto-chave:** A soma dos três contadores deve ser 8.

**Arquivo:** [`solucoes/ex048_positivos_negativos_e_zeros.py`](solucoes/ex048_positivos_negativos_e_zeros.py)

### Exercício 49 — Pares e ímpares

**Objetivo:** Ler seis inteiros e contar quantos são pares e quantos são ímpares.

**Lógica usada:** Teste `valor % 2 == 0`; zero também é par.

**Ponto-chave:** Pares + ímpares deve ser igual a 6.

**Arquivo:** [`solucoes/ex049_pares_e_impares.py`](solucoes/ex049_pares_e_impares.py)

### Exercício 50 — Maior valor informado

**Objetivo:** Ler dez números reais e mostrar o maior.

**Lógica usada:** Inicialize o maior com a primeira entrada, nunca com zero ou outro valor fixo.

**Ponto-chave:** Inicializar pela primeira entrada garante correção quando todos os números são negativos.

**Arquivo:** [`solucoes/ex050_maior_valor_informado.py`](solucoes/ex050_maior_valor_informado.py)

### Exercício 51 — Maior e menor valor

**Objetivo:** Ler dez números reais e mostrar o maior e o menor.

**Lógica usada:** Inicialize maior e menor com a primeira entrada e atualize ambos durante o laço.

**Ponto-chave:** A estratégia funciona com valores positivos, negativos e repetidos.

**Arquivo:** [`solucoes/ex051_maior_e_menor_valor.py`](solucoes/ex051_maior_e_menor_valor.py)

### Exercício 52 — Pesquisa de idades

**Objetivo:** Ler a idade de dez pessoas e mostrar média, quantidade de menores de 18 e quantidade com 60 anos ou mais.

**Lógica usada:** Acumule a soma das idades e use dois contadores independentes.

**Ponto-chave:** 18 não conta como menor; 60 já entra no grupo de 60 anos ou mais.

**Arquivo:** [`solucoes/ex052_pesquisa_de_idades.py`](solucoes/ex052_pesquisa_de_idades.py)

### Exercício 53 — Pesquisa de alturas

**Objetivo:** Ler a altura de oito pessoas e mostrar média, maior e menor altura.

**Lógica usada:** Use a primeira altura para inicializar maior e menor e acumule a soma.

**Ponto-chave:** Com oito alturas iguais, média, maior e menor devem coincidir.

**Arquivo:** [`solucoes/ex053_pesquisa_de_alturas.py`](solucoes/ex053_pesquisa_de_alturas.py)

### Exercício 54 — Soma dos múltiplos de 3

**Objetivo:** Ler dois inteiros A e B e somar todos os múltiplos de 3 entre eles, incluindo os limites quando aplicável.

**Lógica usada:** Normalize os limites com `min` e `max` e teste cada inteiro do intervalo.

**Ponto-chave:** Inverter A e B não pode alterar o resultado.

**Arquivo:** [`solucoes/ex054_soma_dos_multiplos_de_3.py`](solucoes/ex054_soma_dos_multiplos_de_3.py)

### Exercício 55 — Progressão aritmética

**Objetivo:** Ler primeiro termo, razão e quantidade de termos de uma PA, mostrar a sequência e sua soma.

**Lógica usada:** Gere cada termo por `primeiro + i * razão`, acumule a soma e preserve a quantidade solicitada.

**Ponto-chave:** O último termo é `primeiro + (quantidade - 1) * razão`.

**Arquivo:** [`solucoes/ex055_progressao_aritmetica.py`](solucoes/ex055_progressao_aritmetica.py)

### Exercício 56 — Validação de nota

**Objetivo:** Solicitar notas até que o usuário informe um valor válido entre 0 e 10 e contar quantas tentativas inválidas ocorreram.

**Lógica usada:** Repita a leitura enquanto a nota estiver fora do intervalo fechado [0,10].

**Ponto-chave:** A primeira nota válida encerra o laço e não entra no contador de inválidas.

**Arquivo:** [`solucoes/ex056_validacao_de_nota.py`](solucoes/ex056_validacao_de_nota.py)

### Exercício 57 — Leitura até zero

**Objetivo:** Ler números reais até o usuário informar zero e, ao final, mostrar quantidade, soma e média.

**Lógica usada:** Zero funciona apenas como sentinela: encerra a leitura e não participa dos cálculos.

**Ponto-chave:** Se zero for a primeira entrada, não existe média a calcular.

**Arquivo:** [`solucoes/ex057_leitura_ate_zero.py`](solucoes/ex057_leitura_ate_zero.py)

### Exercício 58 — Idades até valor negativo

**Objetivo:** Ler idades até um valor negativo e mostrar quantidade, média e quantas pessoas têm 18 anos ou mais.

**Lógica usada:** A idade negativa é sentinela e não entra em nenhum cálculo.

**Ponto-chave:** 18 anos já conta como maior de idade no critério do exercício.

**Arquivo:** [`solucoes/ex058_idades_ate_valor_negativo.py`](solucoes/ex058_idades_ate_valor_negativo.py)

### Exercício 59 — Senha até acertar

**Objetivo:** Solicitar uma senha até que o usuário acerte 1234 e mostrar o total de tentativas.

**Lógica usada:** Conte cada entrada, inclusive a tentativa correta.

**Ponto-chave:** Se a primeira senha for correta, o total de tentativas deve ser 1.

**Arquivo:** [`solucoes/ex059_senha_ate_acertar.py`](solucoes/ex059_senha_ate_acertar.py)

### Exercício 60 — Caixa de compras

**Objetivo:** Ler preços até zero e mostrar quantidade de produtos, total da compra e maior preço informado.

**Lógica usada:** Zero encerra a leitura e não representa produto.

**Ponto-chave:** A sentinela zero fica fora da quantidade, soma e busca do maior preço.

**Arquivo:** [`solucoes/ex060_caixa_de_compras.py`](solucoes/ex060_caixa_de_compras.py)


## Módulo 04 — Vetores e matrizes

### Exercício 61 — Vetor com múltiplos de 5

**Objetivo:** Criar automaticamente um vetor de 10 posições contendo 5, 10, 15, ..., 50 e exibi-lo.

**Lógica usada:** Gere os valores com uma estrutura de repetição; no índice i, o valor é `5 * (i + 1)`.

**Ponto-chave:** O vetor deve ter 10 posições, começar em 5 e terminar em 50.

**Arquivo:** [`solucoes/ex061_vetor_com_multiplos_de_5.py`](solucoes/ex061_vetor_com_multiplos_de_5.py)

### Exercício 62 — Leitura e exibição de vetor

**Objetivo:** Ler oito inteiros, armazená-los em um vetor e exibi-los na mesma ordem.

**Lógica usada:** Faça todas as leituras primeiro e depois percorra o vetor para exibição.

**Ponto-chave:** A sequência exibida deve ser idêntica à sequência informada.

**Arquivo:** [`solucoes/ex062_leitura_e_exibicao_de_vetor.py`](solucoes/ex062_leitura_e_exibicao_de_vetor.py)

### Exercício 63 — Vetor em ordem inversa

**Objetivo:** Ler oito inteiros e exibi-los em ordem inversa.

**Lógica usada:** Percorra os índices do último elemento até o primeiro.

**Ponto-chave:** Inverter a sequência duas vezes recupera a ordem original.

**Arquivo:** [`solucoes/ex063_vetor_em_ordem_inversa.py`](solucoes/ex063_vetor_em_ordem_inversa.py)

### Exercício 64 — Soma dos elementos do vetor

**Objetivo:** Ler dez números reais, armazená-los em um vetor e mostrar a soma de todos.

**Lógica usada:** Percorra o vetor usando um acumulador.

**Ponto-chave:** Misturas de positivos e negativos devem ser somadas sem ignorar nenhum elemento.

**Arquivo:** [`solucoes/ex064_soma_dos_elementos_do_vetor.py`](solucoes/ex064_soma_dos_elementos_do_vetor.py)

### Exercício 65 — Valores acima da média

**Objetivo:** Ler oito notas, calcular a média e mostrar as notas estritamente acima dela e sua quantidade.

**Lógica usada:** Calcule a média primeiro; depois faça um segundo percurso para filtrar `nota > media`.

**Ponto-chave:** Notas exatamente iguais à média não entram na lista.

**Arquivo:** [`solucoes/ex065_valores_acima_da_media.py`](solucoes/ex065_valores_acima_da_media.py)

### Exercício 66 — Pares e suas posições

**Objetivo:** Ler dez inteiros e mostrar cada valor par acompanhado de seu índice no vetor.

**Lógica usada:** Percorra o vetor com índice e teste a paridade. Se nenhum par existir, informe isso.

**Ponto-chave:** Zero é par e deve ser exibido com a posição correta.

**Arquivo:** [`solucoes/ex066_pares_e_suas_posicoes.py`](solucoes/ex066_pares_e_suas_posicoes.py)

### Exercício 67 — Maior valor e posição

**Objetivo:** Ler oito inteiros e mostrar o maior valor e a primeira posição em que ele aparece.

**Lógica usada:** Inicialize maior e posição com o primeiro elemento e atualize apenas quando surgir um valor estritamente maior.

**Ponto-chave:** Usar `>` em vez de `>=` preserva a posição da primeira ocorrência em caso de empate.

**Arquivo:** [`solucoes/ex067_maior_valor_e_posicao.py`](solucoes/ex067_maior_valor_e_posicao.py)

### Exercício 68 — Menor valor e posição

**Objetivo:** Ler oito inteiros e mostrar o menor valor e a primeira posição em que ele aparece.

**Lógica usada:** Inicialize com o primeiro elemento e atualize apenas quando surgir valor estritamente menor.

**Ponto-chave:** Empates não substituem a primeira posição já encontrada.

**Arquivo:** [`solucoes/ex068_menor_valor_e_posicao.py`](solucoes/ex068_menor_valor_e_posicao.py)

### Exercício 69 — Busca de valor no vetor

**Objetivo:** Ler dez inteiros, depois um valor de busca, e mostrar todas as posições em que ele aparece.

**Lógica usada:** Percorra o vetor inteiro e armazene todos os índices cujo valor seja igual ao procurado.

**Ponto-chave:** Quando o valor se repete, todas as posições devem ser informadas.

**Arquivo:** [`solucoes/ex069_busca_de_valor_no_vetor.py`](solucoes/ex069_busca_de_valor_no_vetor.py)

### Exercício 70 — Quantidade de ocorrências

**Objetivo:** Ler dez inteiros e um valor de busca e informar quantas vezes ele aparece.

**Lógica usada:** Percorra o vetor e incremente um contador a cada igualdade.

**Ponto-chave:** Uma busca sem resultado deve retornar 0.

**Arquivo:** [`solucoes/ex070_quantidade_de_ocorrencias.py`](solucoes/ex070_quantidade_de_ocorrencias.py)

### Exercício 71 — Copiar apenas valores positivos

**Objetivo:** Ler dez números reais em A e criar B contendo somente os valores positivos, preservando a ordem.

**Lógica usada:** Filtre apenas valores `> 0`; zero e negativos ficam fora.

**Ponto-chave:** O vetor B mantém a ordem relativa dos positivos encontrados em A.

**Arquivo:** [`solucoes/ex071_copiar_apenas_valores_positivos.py`](solucoes/ex071_copiar_apenas_valores_positivos.py)

### Exercício 72 — Intercalar dois vetores

**Objetivo:** Ler dois vetores A e B com cinco elementos e criar C alternando um valor de A e um de B.

**Lógica usada:** Para cada índice i, acrescente primeiro `A[i]` e depois `B[i]`.

**Ponto-chave:** O vetor C terá exatamente 10 elementos, no padrão A, B, A, B até o final.

**Arquivo:** [`solucoes/ex072_intercalar_dois_vetores.py`](solucoes/ex072_intercalar_dois_vetores.py)

### Exercício 73 — Comparar dois vetores

**Objetivo:** Ler dois vetores de cinco inteiros e mostrar os índices em que os valores correspondentes são iguais.

**Lógica usada:** Compare apenas posições de mesmo índice.

**Ponto-chave:** Valores iguais em posições diferentes não contam como correspondência.

**Arquivo:** [`solucoes/ex073_comparar_dois_vetores.py`](solucoes/ex073_comparar_dois_vetores.py)

### Exercício 74 — Nomes acima da média

**Objetivo:** Ler nome e nota de cinco alunos em vetores paralelos, calcular a média e mostrar os nomes com nota acima dela.

**Lógica usada:** Mantenha nome e nota no mesmo índice e filtre somente notas estritamente maiores que a média.

**Ponto-chave:** Alunos com nota exatamente igual à média não aparecem.

**Arquivo:** [`solucoes/ex074_nomes_acima_da_media.py`](solucoes/ex074_nomes_acima_da_media.py)

### Exercício 75 — Ordenação crescente

**Objetivo:** Ler dez inteiros e ordená-los em ordem crescente sem usar função pronta de ordenação.

**Lógica usada:** Use Bubble Sort: compare pares adjacentes e troque quando estiverem fora de ordem.

**Ponto-chave:** O algoritmo preserva negativos, zeros e valores repetidos e não chama `sorted()` nem `.sort()`.

**Arquivo:** [`solucoes/ex075_ordenacao_crescente.py`](solucoes/ex075_ordenacao_crescente.py)

### Exercício 76 — Leitura de matriz 3 x 3

**Objetivo:** Ler nove inteiros, armazená-los em uma matriz 3×3 e exibi-la em três linhas.

**Lógica usada:** Crie três linhas com três elementos cada e preserve a ordem de leitura.

**Ponto-chave:** Cada valor é armazenado uma única vez e recuperado pela linha e coluna corretas.

**Arquivo:** [`solucoes/ex076_leitura_de_matriz_3_x_3.py`](solucoes/ex076_leitura_de_matriz_3_x_3.py)

### Exercício 77 — Soma dos elementos da matriz

**Objetivo:** Ler uma matriz 3×3 e calcular a soma de todos os seus elementos.

**Lógica usada:** Use dois laços: um para as linhas e outro para os elementos de cada linha.

**Ponto-chave:** A soma das três linhas deve coincidir com a soma total da matriz.

**Arquivo:** [`solucoes/ex077_soma_dos_elementos_da_matriz.py`](solucoes/ex077_soma_dos_elementos_da_matriz.py)

### Exercício 78 — Diagonal principal

**Objetivo:** Ler uma matriz 3×3, mostrar os elementos da diagonal principal e somá-los.

**Lógica usada:** Na diagonal principal, linha e coluna têm o mesmo índice: [0][0], [1][1], [2][2].

**Ponto-chave:** Uma matriz 3×3 possui exatamente três elementos na diagonal principal.

**Arquivo:** [`solucoes/ex078_diagonal_principal.py`](solucoes/ex078_diagonal_principal.py)

### Exercício 79 — Soma de cada linha e coluna

**Objetivo:** Ler uma matriz 3×3 e mostrar a soma de cada linha e de cada coluna.

**Lógica usada:** Some as linhas diretamente; para colunas, fixe a coluna e percorra as três linhas.

**Ponto-chave:** A soma de todas as linhas deve ser igual à soma de todas as colunas e à soma total da matriz.

**Arquivo:** [`solucoes/ex079_soma_de_cada_linha_e_coluna.py`](solucoes/ex079_soma_de_cada_linha_e_coluna.py)

### Exercício 80 — Maior elemento da matriz

**Objetivo:** Ler uma matriz 4×4 e mostrar o maior elemento e a linha e coluna de sua primeira ocorrência.

**Lógica usada:** Inicialize o maior com [0][0] e percorra a matriz em ordem de linhas; atualize somente com `>`.

**Ponto-chave:** Usar `>` mantém as coordenadas da primeira ocorrência do maior valor.

**Arquivo:** [`solucoes/ex080_maior_elemento_da_matriz.py`](solucoes/ex080_maior_elemento_da_matriz.py)


## Módulo 05 — Funções e desafios combinados

### Exercício 81 — Função para somar

**Objetivo:** Criar uma função `soma` que recebe dois números reais e retorna a soma.

**Lógica usada:** A função calcula e devolve o valor; a exibição fica fora dela.

**Ponto-chave:** O retorno pode ser usado dentro de outras expressões.

**Arquivo:** [`solucoes/ex081_funcao_para_somar.py`](solucoes/ex081_funcao_para_somar.py)

### Exercício 82 — Função maior

**Objetivo:** Criar uma função `maior` que recebe dois números reais e retorna o maior deles.

**Lógica usada:** Compare os dois valores e retorne um deles; em caso de igualdade, o valor comum é válido.

**Ponto-chave:** Dois parâmetros iguais devem retornar corretamente esse mesmo valor.

**Arquivo:** [`solucoes/ex082_funcao_maior.py`](solucoes/ex082_funcao_maior.py)

### Exercício 83 — Menor de três valores

**Objetivo:** Criar uma função `menor3` que recebe três números reais e retorna o menor.

**Lógica usada:** Inicialize o menor com o primeiro argumento e compare os outros dois.

**Ponto-chave:** A ordem dos parâmetros não deve alterar o valor mínimo encontrado.

**Arquivo:** [`solucoes/ex083_menor_de_tres_valores.py`](solucoes/ex083_menor_de_tres_valores.py)

### Exercício 84 — Função par ou ímpar

**Objetivo:** Criar uma função `ehPar` que recebe um inteiro e retorna `True` quando ele é par.

**Lógica usada:** Retorne diretamente o resultado de `numero % 2 == 0`.

**Ponto-chave:** Zero e números negativos seguem a mesma definição matemática de paridade.

**Arquivo:** [`solucoes/ex084_funcao_par_ou_impar.py`](solucoes/ex084_funcao_par_ou_impar.py)

### Exercício 85 — Função de média

**Objetivo:** Criar uma função `media3` que recebe três notas reais e retorna a média aritmética.

**Lógica usada:** Some as três notas e divida por 3. Formate a exibição final com duas casas decimais.

**Ponto-chave:** Três notas iguais produzem exatamente o próprio valor como média.

**Arquivo:** [`solucoes/ex085_funcao_de_media.py`](solucoes/ex085_funcao_de_media.py)

### Exercício 86 — Função de conversão de temperatura

**Objetivo:** Criar `celsiusParaFahrenheit` para converter Celsius em Fahrenheit.

**Lógica usada:** Retorne `celsius * 9 / 5 + 32`.

**Ponto-chave:** Com -40 como argumento, o retorno também deve ser -40.

**Arquivo:** [`solucoes/ex086_funcao_de_conversao_de_temperatura.py`](solucoes/ex086_funcao_de_conversao_de_temperatura.py)

### Exercício 87 — Função fatorial

**Objetivo:** Criar uma função `fatorial` que recebe um inteiro de 0 a 12 e retorna seu fatorial.

**Lógica usada:** Multiplique de 2 até N; para 0 e 1, o acumulador inicial 1 já é a resposta.

**Ponto-chave:** 0! e 1! são ambos iguais a 1.

**Arquivo:** [`solucoes/ex087_funcao_fatorial.py`](solucoes/ex087_funcao_fatorial.py)

### Exercício 88 — N-ésimo termo de Fibonacci

**Objetivo:** Criar uma função `fibonacci` que recebe o índice N e retorna o termo correspondente, com F0=0 e F1=1.

**Lógica usada:** Avance iterativamente mantendo dois termos consecutivos.

**Ponto-chave:** A convenção de índices do exercício é F0=0 e F1=1.

**Arquivo:** [`solucoes/ex088_n-esimo_termo_de_fibonacci.py`](solucoes/ex088_n-esimo_termo_de_fibonacci.py)

### Exercício 89 — Validação de nota

**Objetivo:** Criar uma função `notaValida` que retorna `True` apenas para valores entre 0 e 10, inclusive.

**Lógica usada:** Retorne a comparação encadeada `0 <= nota <= 10`.

**Ponto-chave:** 0 e 10 são válidos; valores imediatamente abaixo ou acima são inválidos.

**Arquivo:** [`solucoes/ex089_validacao_de_nota.py`](solucoes/ex089_validacao_de_nota.py)

### Exercício 90 — Procedimento para mostrar a tabuada

**Objetivo:** Criar um procedimento `mostrarTabuada` que recebe um inteiro e exibe a tabuada de 1 a 10.

**Lógica usada:** A função é usada por seu efeito de exibição e não precisa retornar um valor.

**Ponto-chave:** O procedimento produz dez linhas e seu retorno implícito é `None`.

**Arquivo:** [`solucoes/ex090_procedimento_para_mostrar_a_tabuada.py`](solucoes/ex090_procedimento_para_mostrar_a_tabuada.py)

### Exercício 91 — Contar positivos no vetor

**Objetivo:** Criar `contarPositivos` para retornar quantos elementos de um vetor são maiores que zero.

**Lógica usada:** Percorra o vetor e incremente o contador apenas quando `valor > 0`.

**Ponto-chave:** Zero não é positivo.

**Arquivo:** [`solucoes/ex091_contar_positivos_no_vetor.py`](solucoes/ex091_contar_positivos_no_vetor.py)

### Exercício 92 — Média dos elementos do vetor

**Objetivo:** Criar `mediaVetor` para retornar a média dos valores de um vetor não vazio.

**Lógica usada:** Some os elementos e divida pelo comprimento do vetor.

**Ponto-chave:** Um vetor com um único elemento tem esse próprio valor como média.

**Arquivo:** [`solucoes/ex092_media_dos_elementos_do_vetor.py`](solucoes/ex092_media_dos_elementos_do_vetor.py)

### Exercício 93 — Maior valor do vetor

**Objetivo:** Criar `maiorVetor` para retornar o maior elemento de um vetor não vazio.

**Lógica usada:** Inicialize o maior com o primeiro elemento e percorra os demais.

**Ponto-chave:** A inicialização pela primeira posição evita erro com vetores totalmente negativos.

**Arquivo:** [`solucoes/ex093_maior_valor_do_vetor.py`](solucoes/ex093_maior_valor_do_vetor.py)

### Exercício 94 — Posições de um valor

**Objetivo:** Criar `buscarPosicoes` para retornar todos os índices em que um valor aparece no vetor.

**Lógica usada:** Percorra com `enumerate` e armazene cada índice correspondente.

**Ponto-chave:** Quando não houver ocorrência, retorne uma lista vazia.

**Arquivo:** [`solucoes/ex094_posicoes_de_um_valor.py`](solucoes/ex094_posicoes_de_um_valor.py)

### Exercício 95 — Contar ocorrências em função

**Objetivo:** Criar `contarOcorrencias` para retornar quantas vezes um valor aparece no vetor.

**Lógica usada:** Percorra o vetor e incremente um contador nas igualdades.

**Ponto-chave:** Diferentemente do exercício 94, aqui o retorno é um número, não uma coleção de índices.

**Arquivo:** [`solucoes/ex095_contar_ocorrencias_em_funcao.py`](solucoes/ex095_contar_ocorrencias_em_funcao.py)

### Exercício 96 — Estatísticas de vendas

**Objetivo:** Ler dez valores de vendas e usar funções para calcular total, média, maior venda e quantidade acima da média.

**Lógica usada:** Separe cada responsabilidade em uma função reutilizável e use a média calculada no filtro final.

**Ponto-chave:** Somente valores estritamente acima da média entram na contagem.

**Arquivo:** [`solucoes/ex096_estatisticas_de_vendas.py`](solucoes/ex096_estatisticas_de_vendas.py)

### Exercício 97 — Estatísticas da turma

**Objetivo:** Ler nome e nota de oito alunos em vetores paralelos e usar funções para calcular média, maior nota, menor nota e nomes acima da média.

**Lógica usada:** Mantenha nomes e notas sincronizados pelo mesmo índice e separe os cálculos em funções.

**Ponto-chave:** Alunos exatamente na média ficam fora da lista e a associação entre nome e nota deve ser preservada.

**Arquivo:** [`solucoes/ex097_estatisticas_da_turma.py`](solucoes/ex097_estatisticas_da_turma.py)

### Exercício 98 — Temperaturas da semana

**Objetivo:** Ler sete temperaturas e usar funções para calcular média, maior, menor e quantos dias ficaram acima da média.

**Lógica usada:** Faça os quatro cálculos sobre o mesmo vetor de sete temperaturas.

**Ponto-chave:** Valores exatamente iguais à média não contam como dias acima dela.

**Arquivo:** [`solucoes/ex098_temperaturas_da_semana.py`](solucoes/ex098_temperaturas_da_semana.py)

### Exercício 99 — Controle de estoque

**Objetivo:** Ler nome, quantidade e preço unitário de oito produtos e calcular valor total do estoque, quantos têm quantidade menor que 5 e qual possui maior valor em estoque.

**Lógica usada:** Valor em estoque de cada produto = quantidade × preço unitário. Use vetores paralelos e funções.

**Ponto-chave:** O item com maior valor em estoque não precisa ser o de maior quantidade nem o de maior preço unitário.

**Arquivo:** [`solucoes/ex099_controle_de_estoque.py`](solucoes/ex099_controle_de_estoque.py)

### Exercício 100 — Desafio final — análise de uma turma

**Objetivo:** Ler nome, idade e nota de dez alunos e, usando funções e vetores paralelos, produzir seis estatísticas solicitadas.

**Lógica usada:** Calcule média; maior e menor nota com nomes; quantidade de aprovados (nota >= 7); aluno mais velho com idade; e nomes com nota acima da média.

**Ponto-chave:** A aprovação inclui nota 7,0 e a lista 'acima da média' usa comparação estrita `>`.

**Arquivo:** [`solucoes/ex100_desafio_final_-_analise_de_uma_turma.py`](solucoes/ex100_desafio_final_-_analise_de_uma_turma.py)
