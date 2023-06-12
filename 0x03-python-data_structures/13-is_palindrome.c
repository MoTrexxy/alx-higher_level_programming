#include <stddef.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - a C funct that checks if a singly list is a palindrome
 *
 * @head: first node
 * Return: zero or one
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp = *head;
	int values[2048], m = 0, cLoop, limit;

	if (head == NULL || *head == NULL)
		return (1);

	while (tmp != NULL)
	{
		values[m] = tmp->n;
		m++;
		tmp = tmp->next;
	}

	limit = (m % 2 == 0) ? m / 2 : (m + 1) / 2;

	for (cLoop = 0; cLoop < limit; cLoop++)
		if (values[cLoop] != values[m - 1 - cLoop])
			return (0);

	return (1);
}
