#include <stdio.h>

int	main()
{
	int	n, num, i, count = 0;

	scanf("%d", &n);
	while (n--)
	{
		scanf("%d", &num);
		if (num == 1)
			continue ;
		i = 2;
		while (num % i)
			i++;
		if (i == num)
			count++;
	}
	printf("%d", count);
	return (0);
}