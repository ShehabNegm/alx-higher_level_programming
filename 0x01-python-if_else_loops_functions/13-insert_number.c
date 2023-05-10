#include "lists.h"

/**
  * insert_node - function to insert node in sorted linked list
  * @head: head of the sorted linked list
  * @number: number to be inserted
  * Return: address of the new node or null if failed
  */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp;
	listint_t *new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	if (!head || !*head)
		return (NULL);

	tmp = *head;

	while (tmp)
	{
		if (number < tmp->next->n)
		{
			new->next = tmp->next;
			new->n = number;
			tmp->next = new;
			break;
		}
		tmp = tmp->next;
	}
	return (new);
}
