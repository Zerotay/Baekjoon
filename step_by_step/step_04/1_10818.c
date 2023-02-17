#include <stdio.h>

int	main()
{
	int	n;
	int	min, max;
	int	tmp;

	scanf("%d", &n);
	min = 1000001;
	max = -1000001;
	while (n--)
	{
		scanf("%d", &tmp);
		if (tmp > max)
			max  = tmp;
		if (tmp < min)
			min = tmp;
	}
	printf("%d %d", min, max);
	return (0);
}