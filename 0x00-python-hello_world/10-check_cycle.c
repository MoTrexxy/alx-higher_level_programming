#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - a funct that checks
 * @list: pointer
 *
 * Return: 0 or 1
 *
 */
int check_cycle(listint_t *list)
{
	listint_t *back, *front;

	if (list == NULL || list->next == NULL)
		return (0);

	back = list->next;
	front = list->next->next;

	while (back && front && back->next)
	{
		if (back == front)
			return (1);

		back = back->next;
		front = front->next->next;
	}

	return (0);
}
