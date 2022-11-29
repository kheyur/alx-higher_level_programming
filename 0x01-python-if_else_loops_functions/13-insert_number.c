#include "lists.h"
/**
 * insert_node - insert a number into a sorted linked list
 * @head: beginning of list
 * @number: index for new node
 * Return: address of new node, NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new;
	listint_t *h;

	h = *head;
	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);

	while (h != NULL)
	{
		if (h->n > number)
			break;
		h_prev = h;
		h = h->next;
	}

	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = h;
		if (h == *head)
			*head = new;
		else
			h_prev->next = new;
	}

	return (new);
}
