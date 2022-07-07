#include <stdio.h>

int	main()
{
	int	n;
	int	b, c;
	int	t;
	int	tmp;

	scanf("%d", &n);
	t = 1;
	b = n % 10;
	c = n / 10 + b;
	while (n != b * 10 + c % 10)
	{
		tmp = c;
		c = b + c % 10;
		b = tmp % 10;
		t++;
	}
	printf("%d", t);
	return (0);
}