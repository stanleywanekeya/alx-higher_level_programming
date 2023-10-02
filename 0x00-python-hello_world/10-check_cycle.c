#include "lists.h"

/**
 * check_cycle - checks for cycles
 * @list: list to check
 *
 * Return: 1 if the list has cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *head = list;
	listint_t *check = list;


	if (!list)
		return (0);


	while (head && check && check->next)
	{
		head = head->next;
		check = check->next->next;
		if (head == check)
			return (1);
	}


	return (0);
}

