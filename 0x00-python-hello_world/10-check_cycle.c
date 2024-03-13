#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - a function in C that checks if a singly linked list has a cycle in it
 * Return: 0 if no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
	listint_t *quick = list;
	listint_t *lazy = list;

	if (!list)
		return (0);

	while (1)
	{
		/*traverse through nodes as long as linked list node exists*/
		if (quick->next != NULL && quick->next->next != NULL)
		{
			quick = quick->next->next;
			lazy = lazy->next;

			if (quick == lazy) /*if nodes match, cycle found*/
				return (1);
		}
		else
			return (0);
	}

}
