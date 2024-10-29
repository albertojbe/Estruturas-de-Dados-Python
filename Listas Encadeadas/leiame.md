# Miniprojeto: Sistema de Gerenciamento de Liderança Rotativa
Miniprojeto envolvendo o desenvolvimento de uma lista encadeada circular.

Membros
-
- Alberto Cesar Pinheiro da Silva

Desempenho das Operações
-
```adicionar_membro```:
possui desempenho $O(n)$, pois para poder adicionar um novo elemento é preciso percorrer a lista até o final para mudar o ponteiro de próximo do último elemeento. Uma forma de tornar $O(1)$ seria criar uma váriavel para apontar para o último elemento.

```proximo_responsavel```: 
possui desempenho de $O(1)$, pois apenas acessa o ponteiro de um elemento.

```remover_membro```: 
possui desempenho $O(n)$, pois precisa percorrer cada elemento da lista para saber se ele é igual ao elemento que deseja-se remover.