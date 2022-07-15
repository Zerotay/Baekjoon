#include <stdio.h>

int	main()
{
	int	a, b, v, x = 0;

	scanf("%d %d %d", &a, &b, &v);
	x = (v - a) / (a - b) + !(!((v - a) % (a - b))) + 1;
	printf("%d", x);
	return (0);
}