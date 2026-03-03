#include <stdio.h>
#include <string.h>

struct student{
    char name[100];
    int roll_no;
    float cgpa;
};

int main(){

    struct student s1;
    strcpy(s1.name, "John Doe");
    s1.roll_no = 25;
    s1.cgpa = 8.5;
    printf("Name: %s\nRoll No: %d\nCGPA: %.2f\n", s1.name, s1.roll_no, s1.cgpa);
    printf("\n");

    struct student s2;
    strcpy(s2.name, "Ram");
    s2.roll_no = 50;
    s2.cgpa = 8.8;
    printf("Name: %s\nRoll No: %d\nCGPA: %.2f\n", s2.name, s2.roll_no, s2.cgpa);
    printf("\n");

    struct student s3;
    strcpy(s3.name, "Shiv");
    s3.roll_no = 65;
    s3.cgpa = 9.1;
    printf("Name: %s\nRoll No: %d\nCGPA: %.2f\n", s3.name, s3.roll_no, s3.cgpa);
    printf("\n");
}