#include <stdio.h>

int	recur(int n)
{
	if (n == 1)
		return (1);
	return (n + recur(n - 1));
}

int	main()
{
	int	n;

	scanf("%d", &n);
	printf("%d", recur(n));
	return (0);
}