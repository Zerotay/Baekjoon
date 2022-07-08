#include <stdio.h>

int	main()
{
	int	max, n, sub, sum, i;

	scanf("%d", &n);
	i = n;
	max = 0;
	sum = 0;
	while (i--)
	{
		scanf("%d", &sub);
		if (sub > max)
			max = sub;
		sum += sub;
	}
	printf("%f", (float)sum * 100 / (max * n));
	return (0);
}