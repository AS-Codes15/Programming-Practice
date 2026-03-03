#include <stdio.h>
int binarySearch(int a[],int n,int data)
{
	int l=0,r=n-1;
	while(l<r)
	{
		int mid=(l+r)/2;
		if(data==a[mid])
		return mid;
		else if(data<a[mid])
		r=mid-1;
		else
		l=mid+1;
		
	}
	return -1;
}
int main()
{
	int a[]={10,20,30,40,50};
	int n=sizeof(a)/sizeof(a[0]);
	int data=50;
int result=binarySearch(a,n,data);
if(result==-1)
printf("element is not found");
else
printf("element found at index:%d",result);
}