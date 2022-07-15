#include <stdio.h>

int	main()
{
	int	n;
	int	cycle = 1;
	int	hex = 1;

	scanf("%d", &n);
	while (1)
	{
		if (n <= cycle)
			break ;
		cycle += 6 * hex++;
	}
	printf("%d", hex);
	return (0);
}