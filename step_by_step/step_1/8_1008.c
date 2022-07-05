#include <stdio.h>

int main()
{
	long double	a, b;
	long double	i;

	scanf("%Lf %Lf", &a, &b);
	i = a / b;
	printf("%.9Lf", i);
}