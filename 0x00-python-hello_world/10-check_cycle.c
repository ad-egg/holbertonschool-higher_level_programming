#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to a listint_t list
 * Return: 1 if there is a cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *walk;

	if (list == NULL)
		return (0);
	walk = list;
	while (walk != NULL)
	{
		walk = walk->next;
		if (walk == list)
			return (1);
	}
	return (0);
}
