#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts node in a sorted order
 * @head: thi list
 * @number: number to be inserted at new node
 * Return: new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *last, *first;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	for (last = *head, first = (*head)->next;
			first->n < number && first; first = first->next, last = last->next)
		;
	last->next = new;
	new->next = first;
	return (new);
}
