#include <stdio.h>

int	check(int n)
{
	int	i;

	if (n < 100)
		return (1);
	while (n >= 100)
	{
		i = n % 10 - n / 10 % 10;
		n /= 10;
		if (i != n % 10 - n / 10 % 10)
			return (0);
	}
	return (1);
}

int	main()
{
	int	n;
	int	i = 0;
	int count = 0;

	scanf("%d", &n);
	while (++i <= n)
		if (check(i))
			count++;
	printf("%d", count);
	return (0);
}