#include <stdio.h>

int	main()
{
	int	n, num, i, j;
	int	arr[10000] = {0, };
	int	prime[10000] = {0, };
	int	ans[2];

	i = 1;
	while (++i < 101)
		if (!arr[i])
			for (j = i; j * i < 10000; j++)
				arr[j * i] = 1;
	j = 0;
	for (i = 2; i < 10000; i++)
		if (!arr[i])
			prime[j++] = i;
	scanf("%d", &n);
	while (n--)
	{
		scanf("%d", &num);
		for (i = 0; prime[i] <= num / 2; i++)
			for (j = 0; prime[i] + prime[j] <= num; j++)
				if (prime[i] + prime[j] == num)
				{
					ans[0] = prime[i];
					ans[1] = prime[j];
				}
		printf("%d %d\n", ans[0], ans[1]);
	}
	return (0);
}