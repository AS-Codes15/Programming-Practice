#include <stdio.h>

typedef struct account{
    int account_no;
    char name[50];
} acc;

int main(){
    acc acc1 = {101, "Archa"};
    acc acc2 = {102, "Archana"};

    printf("Account No: %d\nName: %s\n", acc1.account_no, acc1.name);
    printf("Account No: %d\nName: %s\n", acc2.account_no, acc2.name);

    return 0;
}
