#include <stdio.h>
#include <stdlib.h>

#include "array.h"


void shiftR(int begin, int  end, int factor) {
	for (int i = end; i >= begin; i--) {
		put(i + factor, get(i));
	}
}

void shiftL(int begin, int  end, int factor) {
	for (int i = begin; i <= end; ++i) {
		put(i - factor, get(i));
	}
}


char op; // u for push, o for pop
int id, val; // id determines which stack to operate on, val is what to push to stack
int pos[] = { -1, -1, -1, 21 };
// first stack is 0 to i, third stack 21 to j, second in the middle
// pos[0] = top of first stack
// pos[3] = top of third stack
// pos[1] = begin of second stack
// pos[2] = top of second stack 

int main() {

	
	//printf("%c\n", op);
	//if (op == '\n') {
		//main();
	//}
	//else
	if (scanf("%c", &op) == EOF) {
		return 0;
	}
	else if (op == 'u') {
		scanf("%d", &id);
		scanf("%d", &val);

		//printf("%c, %d, %d\n", op, id, val);
		if (id == 0) {
			if (pos[0]+1 == pos[1]) { //conflict
				int sfactor = (pos[3] - pos[2]) / 2;
				//shift 2nd stack right to center
				shiftR(pos[1], pos[2], sfactor);
				//adjust start and end of 2nd
				pos[1] += sfactor;
				pos[2] += sfactor;

				//put in the value
				pos[0] += 1;
				put(pos[0], val);

				//restart
				//stack();
			}
			else {
				pos[0] += 1;
				put(pos[0], val);

				//stack();
			}
		}
		else if (id == 1 || id == 2) {

			if (pos[2] + 1 == pos[3]) {//conflict
				int sfactor = (pos[1] - pos[0]) / 2;
				//shift left to center
				shiftL(pos[1], pos[2], sfactor);
				//adject start and end of second stack
				pos[1] -= sfactor;
				pos[2] -= sfactor;

				//put in the value
				if (id == 1) {
					if (pos[2] == -1) {
						pos[1] = pos[0] + 1;
						pos[2] = pos[0] + 1;
					}
					else {
						pos[2] += 1;
					}
					put(pos[2], val);
							
					//stack();
				}
				else if (id == 2) {
					pos[3] -= 1;
					put(pos[3], val);
							
					//stack();
				}
			}
			else { //no conflict
				if (id == 1) {
					if (pos[2] == -1) {
						pos[1] = pos[0] + 1;
						pos[2] = pos[0] + 1;
					}
					else {
						pos[2] += 1;
					}
					put(pos[2], val);
					//stack();
				}
				else if (id == 2) {
					pos[3] -= 1;
					put(pos[3], val);

					//stack();
				}
				else {
					printf("identifier error 1,2");
				}
			}
		}
		else {
			printf("identifier error main");
		}
	}

		else if (op == 'o') {
			scanf("%d", &id);
			//printf("pop %d\n", id);
			if (id == 0) {
				int out = get(pos[0]);
				printf("%d\n", out);
				//ignore old val, pretend it's empty (will be overwritten anyway)
				pos[0] -= 1;

				main();
				//stack();
			}
			else if (id == 1) {
				printf("%d\n", get(pos[2]));
				if (pos[1] == pos[2]) {
					pos[1] = -1;
					pos[2] = -1;
				}
				else {
					pos[2] -= 1;
				}

				main();
				//stack();
			}
			else if (id == 2) {
				printf("%d\n", get(pos[3]));
				pos[3] += 1;

				main();
				//stack();
			}
		}
		main();
	
	
	

	return 0;
}