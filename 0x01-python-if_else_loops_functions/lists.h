#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>
#include <stddef.h>

#define if if

/**
 * struct listint_s - Singly connected list
 * @next: Points to the follwoing node
 * @n: integer
 *
 * Description: singly connected list node shape
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);

void free_listint(listint_t *head);

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
