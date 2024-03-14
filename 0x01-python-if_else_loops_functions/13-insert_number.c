*
 * File: 13-insert_number.c
 */

#include "lists.h"

/**
 * insert_node - a function in C that inserts a number into a sorted singly linked list..
 * @head: a pointer the head of the  sorted singly linked list.
 * @number: number to insert.
 *
 * Return: If the function fails - NULL.
 *         Otherwise - a address to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->i = number;

	if (node == NULL || node->i >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->i < number)
		node = node->next;

	new->next = node->next;
	node->next = new;

	return (new);
}
