#include <stdio.h>

int	d(int n)
{
	int	ans;

	ans = n;
	while (n)
	{
		ans += n % 10;
		n /= 10;
	}
	return (ans);
}

int	main()
{
	int	n;
	int	i;

	n = 1;
	while (n < 10000)
	{
		i = 0;
		while(++i < n)
			if (n == d(i))
				break ;
		if (i == n)
			printf("%d\n", n);
		n++;
	}
}