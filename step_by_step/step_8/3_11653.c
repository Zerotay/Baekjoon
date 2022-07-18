#include <stdio.h>

int	main()
{
	int	n;

	scanf("%d", &n);
	for (int i = 2; i <= n; i++)
	{
		while (!(n % i))
		{
			n /= i;
			printf("%d\n", i);
		}
		if ((n < 2) || (i > n))
			break ;
	}
	return (0);
}