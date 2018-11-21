#include <stdio.h>
#include <stdlib.h>

struct Node {
	int data;
	struct Node *next;
};

struct Node *reverse(struct Node *lst) {
	struct Node *prev = NULL; //pointer to previous node
	struct Node *cur = lst; //pointer to current node
	struct Node *next;

	while (cur != NULL) {
		next = (*cur).next;

		(*cur).next = prev;

		//proceed to next node
		prev = cur;
		cur = next;
	}

	return prev;
}

