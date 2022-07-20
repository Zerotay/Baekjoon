#include <stdio.h>

int	fivo(int a, int b, int n)
{
	if (!n)
		return (a);
	return (fivo(b, a + b, --n));
}

int	main()
{
	int	n;

	scanf("%d", &n);
	printf("%d", fivo(0, 1, n));
	return (0);
}