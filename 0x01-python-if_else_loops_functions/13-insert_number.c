#include "lists.h"

/**
 * insert_node - Input a node to a ranked list
 * @head: Ranked list
 * @number: Number to input
 * Writer: Graham S. Paul
 * Return: Location of new node
 *
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *temp;

	if (!head)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (*head == NULL)
	{
		*head = new;
		(*head)->next = NULL;
		return (new);
	}
	if ((*head)->next == NULL)
	{
		if ((*head)->n < new->n)
			(*head)->next = new;
		else
		{
			new->next = *head;
			*head = new;
		} return (new);
	}
	temp = *head;
	for (; temp->next;)
	{
		if (new->n < temp->n)
		{	new->next = temp;
			*head = new;
			return (new);
		}
		if (((new->n > temp->n) && (new->n < (temp->next)->n)) ||
			(new->n == temp->n))
		{	new->next = temp->next;
			temp->next = new;
			return (new);
		}
		temp = temp->next;
}
temp->next = new;
return (new);
}
