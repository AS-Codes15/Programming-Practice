#include <stdio.h>
#define N 5
int stack[N];
int top=-1;
void push()
{
	int x;
	printf("enter the data");
	scanf("%d",&x);
	if(top==N-1)
	{
		printf("overflow");
	}
	else
	{
		top++;
		stack[top]=x;
	}
}
void pop()
{
	int item;
	if(top==-1)
	{
		printf("underflow");
	}
	else{
		item=stack[top];
		top--;
		printf("deleted item is:%d",item);
	}
}
void peek()
{
	if(top==-1)
	{
		printf("stack is empty");
	}
	else
	{
		printf("%d",stack[top]);
	}
}
void display()
{
	int i;
	for(i=top;i>=0;i--)
	{
		printf("%d",stack[i]);
	}
}
int main()
{
	int choice;
	do
	{
		printf("enter your choice:  1: push()  2: pop()  3: peek()  4: display()");
		scanf("%d",&choice);
		switch(choice)
		{
			case 1:  push();
			break;
			case 2:  pop();
			break;
			case 3:  peek();
			break;
			case 4:  display();
			break;
			dafault:  printf("invalid position");
		}
	}
	while(choice!=0);
}