#include <stdio.h>

int	main()
{
	int	a, b;
	int	ar, br;

	scanf("%d %d", &a, &b);
	ar = a / 100 + a / 10 % 10 * 10 + a % 10 * 100;
	br = b / 100 + b / 10 % 10 * 10 + b % 10 * 100;
	printf("%d", ar > br ? ar : br);
	return (0);
}