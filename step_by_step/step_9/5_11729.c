#include <stdio.h>

int	get_count(int n)
{
	if (n == 1)
		return (1);
	return (2 * get_count(n - 1) + 1);
}

void	hanoi(int a, int b, int n)
{
	if (n == 1)
		printf("%d %d\n", a, b);
	else
	{
		hanoi(a, 6 - a - b, n - 1);
		printf("%d %d\n", a, b);
		hanoi(6 - a - b, b, n - 1);
	}
}

int	main()
{
	int	n;

	scanf("%d", &n);
	printf("%d\n", get_count(n));
	hanoi(1, 3, n);
	return (0);
}