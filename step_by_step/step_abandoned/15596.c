#include <stdio.h>
#include <stdlib.h>

long long	sum(int *a, int n)
{
	long long	ans;

	ans = 0;
	while (n--)
		ans += (long long)a[n];
	return	(ans);
}

int	main()
{
	int	n;
	int	*arr;

	scanf("%d", &n);
	arr = (int *)malloc(sizeof(int) * n);
	if (!arr)
		return (0);
	for (int i = 0; i < n; i++)
		scanf("%d", (arr + i));
	sum(arr, n);
	return (0);
}