#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: points to beginning of the linked list to be checked
 * Return: 0 if list is not a palindrome, 1 if list is palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *tail, *half;
	int i, j, k;
	int *intn;

	tail = half = *head;
	if ((head == NULL) || (tail == NULL))
		return (0);
	for (i = 0; tail->next; i++)
		tail = tail->next;
	if (i % 2 == 0)
		k = i / 2;
	else
		k = i / 2 + 1;
	intn = malloc(sizeof(int) * i);
	if (intn == NULL)
		return (0);
	for (j = 0; j < k; j++)
	{
		intn[j] = half->n;
		half = half->next;
	}
	j--;
	for (; (j > 0) && half; j--)
	{
		if (half->n != intn[j])
			return (0);
		half = half->next;
	}
	return (1);
}
