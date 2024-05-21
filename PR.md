---
Título: Teste de Avaliação (Época Normal)
Data: 21 de maio de 2024
Autor: Afonso Ferreira
UC: RPCW
---

# Teste de Avaliação (Época Normal)

## Exercício 1 - A Ontologia

### A História

O Sr. João é um agricultor que vive na vila de São José. Ele possui uma pequena fazenda onde cultiva vários tipos de frutas, como maçãs, laranjas e bananas. Na sua fazenda, ele também cria alguns animais, incluindo vacas, galinhas e porcos.

A esposa do Sr. João, a Sra. Maria, ajuda na colheita e na alimentação dos animais. Além disso, ela faz geleias de frutas para vender na feira local. Eles têm dois filhos, Pedro e Ana. Pedro gosta de ajudar o pai com os animais, enquanto Ana prefere ajudar a mãe a fazer as geleias.

O Sr. João tem um vizinho chamado Sr. Carlos, que possui uma fazenda maior onde cultiva principalmente vegetais, como tomates, alfaces e cenouras. O Sr. Carlos frequentemente troca vegetais por frutas com o Sr. João. Ambos também vendem seus produtos na feira de São José todos os sábados.

A fazenda do Sr. João tem um cachorro chamado Rex, que protege a propriedade. A família também possui um trator que é usado para arar os campos e plantar as sementes.

Durante a estação de colheita, o Sr. João contrata trabalhadores temporários para ajudar na colheita das frutas. Esses trabalhadores são pagos por hora e recebem refeições durante o trabalho.

### A Ontologia

Foram criadas as seguintes Classes:

- Pessoa
- Animal
- Planta
  - Fruta
  - Vegetal
- Fazenda
- Produto
- Equipamento
- TrabTemp

Data Properties:

- Nome (Pessoa, Fazenda)
- Profissão (Pessoa)
- Espécie (Animal)
- Tipo (Planta, Produto, Equipamento)

Object Properties:

- temFazenda (Pessoa -> Fazenda)
- temEquipamento (Fazenda -> Equipamento)
- temAnimal (Fazenda -> Animal)
- temPlanta (Fazenda -> Planta)
- cultivaPlanta (Pessoa -> Planta)
- criaAnimal (Pessoa -> Animal)
- fazProduto (Pessoa -> Produto)
- ajuda (Pessoa -> Pessoa)
- trabalhaEm (Pessoa -> Fazenda ou TrabTemp -> Fazenda)
- protege (Animal -> Fazenda)
- vende (Pessoa -> Planta ou Pessoa -> Produto)
- contrata (Pessoa -> TrabTemp)

### As Queries

De seguida foram criadas as queries para responder à segunda parte do exercício.
Elas estão no ficheiro [queries.txt](ex1/queries.txt)

## Exercício 2 - Era uma vez... uma ontologia médica...

Para este exercício, comecou-se por
