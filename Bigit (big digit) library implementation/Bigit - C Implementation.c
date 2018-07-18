#include <stdio.h>
#include <stdlib.h>


struct Node {
	int bigit;
	struct Node *next;
};



struct Node *cons_bigit(int bgt, struct Node *nxt);
void free_num(struct Node *blst);
struct Node *copy_num(struct Node *nlst);


void print_num(struct Node *nlst);
void print_num_h(struct Node *nlst);
struct Node *add(struct Node *n1lst, struct Node *n2lst);
struct Node *mult(struct Node *n1lst, struct Node *n2lst);

void testing();

struct Node *cons_bigit(int bgt, struct Node *nxt) {
	//printf("cons_bigit %d\n", bgt);
	struct Node *n = malloc(sizeof(struct Node));
	n->bigit = bgt;
	n->next = nxt;
	return n;
}

void free_num(struct Node *blst){
	while (blst != NULL) {
		struct Node *temp = blst;
		blst = (*blst).next;
		free(temp);
	}
}


struct Node *copy_num(struct Node *nlst) {
	if (nlst == NULL) { return NULL; }

	struct Node *cur = (struct Node *)malloc(sizeof(struct Node));
	struct Node *nxt = malloc(sizeof(struct Node));

	struct Node *root = cur;

	while (nlst->next != NULL) {

		cur->bigit = nlst->bigit;
		cur->next = nxt; //empty

		nlst = nlst->next;
		cur = nxt;
		nxt = malloc(sizeof(struct Node));
	}
	cur->bigit = nlst->bigit;
	cur->next = NULL;
	free(nxt);

	return root;
}



void print_num(struct Node *nlst) {
	if (nlst == NULL) { printf("0"); }
	else {
		struct Node *iter = nlst;
		print_num_h(iter);
	}
}

void print_num_h(struct Node *iter) {
	if (iter->next != NULL) {
		print_num_h(iter->next);
		printf("%04d", iter->bigit);
	}
	else {
		printf("%d", iter->bigit);
	}
}



struct Node *add(struct Node *nlst, struct Node *n2lst) {
	/*
	print_num(nlst);
	printf("\t");
	print_num(n2lst);
	printf("\n");
	*/
	if (nlst == NULL && n2lst == NULL) { return NULL; }

	struct Node *iter1 = nlst;
	struct Node *iter2 = n2lst;

	int inherit = 0; //add to next 
	struct Node *cur = malloc(sizeof(struct Node));
	struct Node *root = cur;
	struct Node *next = NULL;
	struct Node *prev = NULL;

	while (iter1 != NULL || iter2 != NULL) {
		//printf("add %d, %d\n", iter1->bigit, iter2->bigit);

		next = malloc(sizeof(struct Node));

		if (iter1 == NULL) {
			if (iter2->bigit + inherit >= 10000) {
				cur->bigit = 0;
				cur->next = next;

				prev = cur;
				cur = next;
				iter2 = iter2->next;
				inherit = 1;
			}
			else {
				cur->bigit = iter2->bigit + inherit;
				cur->next = next;

				prev = cur;
				cur = next;
				iter2 = iter2->next;
				inherit = 0;
			}
		}
		else if (iter2 == NULL) {
			if (iter1->bigit + inherit >= 10000) {
				cur->bigit = 0;
				cur->next = next;

				prev = cur;
				cur = next;
				iter1 = iter1->next;
				inherit = 1;
			}
			else {
				cur->bigit = iter1->bigit + inherit;
				cur->next = next;

				prev = cur;
				cur = next;
				iter1 = iter1->next;
				inherit = 0;
			}
		}
		else if (iter1->bigit + iter2->bigit + inherit >= 10000) {
			cur->bigit = iter1->bigit + iter2->bigit + inherit - 10000;
			cur->next = next; //points to new, empty node

			//increments
			prev = cur;
			cur = next;
			iter1 = iter1->next;
			iter2 = iter2->next;
			inherit = 1;
		}
		else {
			cur->bigit = iter1->bigit + iter2->bigit + inherit;
			cur->next = next;

			//increments
			prev = cur;
			cur = next;
			iter1 = iter1->next;
			iter2 = iter2->next;
			inherit = 0;
		}
	}

	//if (iter1 == NULL && iter2 == NULL) {
	if (inherit == 1) {
		cur->bigit = 1;
		cur->next = NULL;

		return root;
	}
	else {
		prev->next = NULL;

		free(cur);
		return root;
	}
	//}
	
		/*
	else if (iter1 == NULL) {
		//print_num(iter2);  --> 12
		//printf("\n");
		cur = copy_num(iter2);
		//print_num(cur);  --> 12
		//printf("\n");
		return root;
	}
	else {
		cur = copy_num(iter1);
		return root;
	}
	*/
}

struct Node *mult10knTimes(struct Node *blst, int num) { //produces a new adjusted list, need to free input separately
	struct Node *acc = copy_num(blst);
	if (num == 0) {
		return acc;
	}
	while (num > 0) {
		acc = cons_bigit(0, acc);
		--num;
	}
	return acc;
}



struct Node *mult(struct Node *n1lst, struct Node *n2lst) {
	//multiply with 2 loops, ie. first of a times b, + second of a times b ... a is n1lst, b is n2lst
	//think of a on top
	//  AAA
	//*  BB
	// ----
	// CCCC

	if (n1lst == NULL || n2lst == NULL) { return NULL; }
	struct Node *iter1 = n1lst;
	struct Node *iter2 = n2lst;
	
	struct Node *acc = NULL;

	int count2 = 0;
	
	while (iter2 != NULL) {
		int inherit = 0;

		struct Node *cur = malloc(sizeof(struct Node));
		struct Node *root = cur;
		struct Node *prev = NULL;

		while (iter1 != NULL) {
			struct Node *nxt = malloc(sizeof(struct Node));
			
			int bgt = (iter1->bigit * iter2->bigit + inherit) % 10000;
			inherit = (iter1->bigit * iter2->bigit + inherit) / 10000;
			
			prev = cur;
			cur->bigit = bgt;
			cur->next = nxt;
			cur = nxt;

			iter1 = iter1->next;
		}
		if (inherit == 0) { 
			free(cur);
			prev->next = NULL;
		}
		else { 
			cur->bigit = inherit;
			cur->next = NULL;
		}
		
		//reset iter1 to start of n1lst
		iter1 = n1lst;

		struct Node *rootAdj = mult10knTimes(root, count2);
		struct Node *acctemp = acc;
		acc = add(acc, rootAdj);
		free_num(acctemp);
		free_num(rootAdj);
		free_num(root);

		//inc 
		++count2;
		iter2 = iter2->next;
	}
	return acc;
}


void testing() {
	struct Node *a = cons_bigit(9999, cons_bigit(9999, NULL));
	struct Node *b = cons_bigit(9999, cons_bigit(9999, NULL));
	struct Node *s = add(a, b);
	struct Node *sp = add(b, a);
	struct Node *m = mult(a, b);
	struct Node *mp = mult(b, a);
	print_num(s);
	printf("\n");
	print_num(sp);
	printf("\n");
	print_num(m);
	printf("\n");
	print_num(mp);
	printf("\n");
	free_num(s);
	free_num(m);
	free_num(a);
	free_num(b);
	free_num(sp);
	free_num(mp);
}

//void main() {
	//testing();

	//print_num(cons_bigit(9, cons_bigit(1, NULL)));
	
	/*
	// test for mult10kntimes
	struct Node *tenKTest = cons_bigit(69, NULL);
	struct Node *afterTenK = mult10knTimes(tenKTest, 3);
	print_num(afterTenK);

	free_num(afterTenK);
	*/


/*
	// test for mult
	struct Node *a = cons_bigit(7890, cons_bigit(3456, cons_bigit(12, NULL)));
	struct Node *b = cons_bigit(3456, cons_bigit(12, NULL));
	struct Node *sab = mult(a, b);
	print_num(sab);
	free_num(a);
	free_num(b);
	free_num(sab);
*/

/*
	//10000*10000 test
	struct Node *hundred = cons_bigit(100, NULL);
	struct Node *s10k = mult(hundred, hundred);
	struct Node *s100000000 = mult(s10k, s10k);
	print_num(s10k);
	printf("\n");
	print_num(s100000000);
	printf("\n");
	free_num(s100000000);
	free_num(s10k);
	free_num(hundred);
*/

	//print_num(mult10knTimes(cons_bigit(69, NULL), 3));

	/*
	//print_num(cons_bigit(7890, cons_bigit(3456, cons_bigit(12, NULL)))); //test cons and print
	//printf("\n");

	struct Node *n = cons_bigit(7890, cons_bigit(3456, cons_bigit(12, NULL))); //test cons and print
	//print_num(n);
	//printf("\n");

	struct Node *np = copy_num(n); //test copy
	//print_num(np);
	//printf("\n");

	//print_num(cons_bigit(12, NULL));
	//print_num(copy_num(cons_bigit(12, NULL)));

	
	//struct Node *s = add(n, np); //test add
	//print_num(s);
	//printf("\n");

	struct Node *nh = cons_bigit(3456, cons_bigit(12, NULL)); //add different length
	struct Node *sp = add(nh, n);
	print_num(sp);
	printf("\n");
	
	struct Node *fivek = cons_bigit(5000, NULL); //5k + 5k test
	print_num(add(fivek, fivek));
	printf("\n");
	free_num(fivek);

	free_num(nh);
	free_num(n);
	free_num(np);
	//free_num(s);
	free_num(sp);
	*/
//}
 