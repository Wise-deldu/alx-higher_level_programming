#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - A function that checks if a singly-linked list contains a cycle.
 * @list: A singly-linked list.
 *
 * Return: 0 - no cycle
 *         1 - There is a cycle
 */

int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	turtle = list->next;
	hare = list->next->next;

	while (turtle && hare && hare->next)
	{
		if (turtle == hare)
			return (1);

		turtle = turtle->next;
		hare = hare->next->next;
	}

	return (0);
}
