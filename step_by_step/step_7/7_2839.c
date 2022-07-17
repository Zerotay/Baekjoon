#include <stdio.h>

int	main()
{
	int	n;

	scanf("%d", &n);

	if (n == 4 || n == 7)
		printf("-1");
	else if (n % 5 == 3)
		printf("%d", n / 5 + 1);
	else if (!(n % 5))
		printf("%d", n / 5);
	else if (n % 5 == 1)
		printf("%d", n / 5 + 1);
	else if (n % 5 == 2)
		printf("%d", n / 5 + 2);
	else
		printf("%d", n / 5 + 2);
	return (0);
}