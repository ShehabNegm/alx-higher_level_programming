#include "lists.h"
/**
  * list_len - will print linked list elements
  * @h: linked list
  * Return: will return number of elements
  */

size_t list_len(listint_t *h)
{
	size_t length = 0;

	listint_t *tmp = h;

	while (tmp != NULL)
	{
		length++;
		tmp = tmp->next;
	}
	return (length);
}

/**
  * reverse_listint - will reverse a singly linked list
  * @head : linked list head
  * Return: will return pointer to last node reversed
  */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *tmp;
	listint_t *pre_tmp = NULL;

	if (*head == NULL)
		return (NULL);

	while ((*head)->next != NULL)
	{
		tmp = *head;
		*head = (*head)->next;
		tmp->next = pre_tmp;
		pre_tmp = tmp;
	}
	(*head)->next = pre_tmp;
	return (*head);
}

/**
  * is_palindrome - function to check if singly linked list is palindrome
  * @head: head of list to be checked
  * Return: will return 1 if palindrome 0 if not
  */

int is_palindrome(listint_t **head)
{
	size_t length, count, i;
	listint_t *r_head, *l_head, *reversed_head, *tmp;

	if (*head == NULL)
		return (1);
	
	if ((*head)->next == NULL)
		return (0);

	tmp = *head;
	length = list_len(tmp);

	if (length == 1)
		return (0);

	if (length % 2 == 0)
		count = length / 2;
	else
		count = (length / 2);

	for (i = 0; i <= count; i++)
		tmp = tmp->next;

	reversed_head = reverse_listint(&tmp);

	r_head = reversed_head;
	l_head = *head;

	while (r_head)
	{
		if (r_head->n != l_head->n)
			return (0);
		r_head = r_head->next;
		l_head = l_head->next;
	}
	return (1);
}
