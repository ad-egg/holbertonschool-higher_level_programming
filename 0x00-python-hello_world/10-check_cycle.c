#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to a listint_t list
 * Return: 1 if there is a cycle, 0 if no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *walk;
	listint_t *zoom;

	if (list == NULL)
		return (0);
	walk = list;
	zoom = list;
	while ((walk != NULL) && (zoom != NULL))
	{
		walk = walk->next;
		zoom = zoom->next->next;
		if (walk == zoom)
			return (1);
	}
	return (0);
}
