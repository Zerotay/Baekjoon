#include <stdio.h>

int	main()
{
	int	x;
	int	n = 0;
	int	sum = 0;

	scanf("%d", &x);
	while (1)
	{
		sum += ++n;
		if (x <= sum)
			break ;
	}
	if (n % 2)
		printf("%d/%d", sum - x + 1, n + x - sum);
	else
		printf("%d/%d", n + x - sum, sum - x + 1);
	return (0);
}