#include <stdio.h>

int	main()
{
	int	arr[1000001] = {0, };
	int	m, n, i = 1;

	scanf("%d %d", &m, &n);
	while (++i * i <= n)
		if (!arr[i])
			for (int j = i; i * j <= n; j++)
				arr[i * j] = 1;
	i = m == 1 ? m : m - 1;
	while (++i <= n)
		if (!arr[i])
			printf("%d\n", i);
	return (0);
}