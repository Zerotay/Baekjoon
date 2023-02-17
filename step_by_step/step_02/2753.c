#include <stdio.h>

int	main()
{
	int	i;

	scanf("%d", &i);
	if (i % 4)
		printf("0");
	else if (!(i % 100) && (i % 400))
		printf("0");
	else
		printf("1");
	return (0);
}