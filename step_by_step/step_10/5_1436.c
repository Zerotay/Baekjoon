#include <stdio.h>

int	main()
{
	int	n;
	int	i, j, count, flag;

	scanf("%d", &n);
	i = 665;
	count = 0;
	while (1)
	{
		j = ++i;
		flag = 0;
		while (j == 666 || j > 1000)
		{
			if (j % 1000 == 666)
				flag++;
			j /= 10;
		}
		if (flag)
			count++;
		if (n == count)
			break ;
	}
	printf("%d", i);
	return (0);
}