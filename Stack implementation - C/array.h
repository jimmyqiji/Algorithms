#include <stdlib.h>

#ifndef ARRAY
#define ARRAY

#define DEBUG
enum { ArraySize = 21 };

int put_count, get_count;
int* array = NULL;

int* data() {
    if (array == NULL) array = malloc(ArraySize * sizeof(int));
    return array;
}

void put(int index, int num) {
    int* array = data();
    put_count++;
    array[index] = num;
}

int get(int index) {
    int* array = data();
    get_count++;
    return array[index];
}

#endif
