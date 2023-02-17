#include <stdio.h>

int	main()
{
	int	m, n, i, min, sum = 0;

	scanf("%d %d", &m, &n);
	while (m <= n)
	{
		i = n;
		while (--i > 1)
		{
			if (!(n % i))
				break ;
		}
		if (i == 1)
		{
			min = n;
			sum += n;
		}
		n--;
	}
	if (!sum)
		printf("-1");
	else
		printf("%d\n%d", sum, min);
	return (0);
}