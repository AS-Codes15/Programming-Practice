#include <stdio.h>
#include <conio.h>
void linearSearch(int a[],int n,int data)
{
    int i;
	for( i=0;i<n;i++)
	{
		if(a[i]==data)
		{
		  printf("element id found at index: %d",i);
		  break;
		}
	}
	if(i==n)
	printf("element is not found");
}
int main()
{
	int a[]={3,5,1,8,9};
	int n=sizeof(a)/sizeof(a[0]);
	int data=8;
    linearSearch(a,n,data);
}
