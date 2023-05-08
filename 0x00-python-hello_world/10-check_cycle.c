#include "lists.h"

/**
  * check_cycle - will check if linked list has a cycle
  * @list: head of the list
  * Return: will return 1 if there is a cycle 0 if not
  */

int check_cycle(listint_t *list)
{
	listint_t *frist = list;
	listint_t *second = list;

	if (list == NULL)
		return (0);

	while (frist && second && frist->next && second->next->next)
	{
		frist = frist->next;
		second = second->next->next;
		if (frist == second)
			return (1);
	}
	return (0);
}
