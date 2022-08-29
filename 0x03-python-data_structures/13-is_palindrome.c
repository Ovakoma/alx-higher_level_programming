#include "lists.h"
#define STACK_SIZE 100
/**
 * is_palindrome -  check if the linked list forward transvers is the same when
 * back transvers backward
 * @head: address of the head pointer
 *
 * Return: return 1 if it's palindrome and 0 otherwise
 */
int is_palindrome(listint_t **head)
{
	int stack[STACK_SIZE], count = 0;
	listint_t *dir  = *head;

	if (!head)
		return (0);
	while (dir)
	{
		stack[count] = dir->n;
		count++;
		dir = dir->next;
	}
	stack[count] = '\0';
	dir = *head;
	count--;
	while (dir)
	{
		if (dir->n != stack[count])
			return (0);
		dir = dir->next;
		count--;
	}
	return (1);
}
