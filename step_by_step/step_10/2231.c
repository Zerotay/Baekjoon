#include <stdio.h>

int	main()
{
	int	n, ans = 0;

	scanf("%d", &n);
	for (int i = 1; i < n; i++)
	{
		ans = i;
		int j = i;
		while (j / 10)
		{
			ans += j % 10;
			j /= 10;
		}
		ans += j;
		if (ans == n)
		{
			printf("%d", i);
			return (0);
		}
	}
	printf("0");
	return (0);
}