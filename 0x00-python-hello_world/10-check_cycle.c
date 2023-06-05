#include "lists.h"

/**
 * check_cycle - list to be examined for cycles
 * @list: list to be examied
 * Return: 1 list has cycle, 0 list don't have cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *snake = list;
	listint_t *rat = list;

	if (!list)
		return (0);

	for (;;)
	{
		if (rat->next && rat->next->next)
		{
			snake = snake->next;
			rat = (rat->next)->next;
			if (snake == rat)
				return (1);
		}
		else
			return (0);
	}
}
