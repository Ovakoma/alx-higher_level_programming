#include "lists.h"

/*
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: head pointer to singly linked list
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	
	while (current != NULL)
	{
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return (0);
}
