#include <stdio.h>

int	main()
{
	int	n, m;
	int	arr[101];
	int	sum, ans;

	scanf("%d %d", &n, &m);
	for (int i = 0; i < n; i++)
		scanf("%d", (arr + i));
	ans = 0;
	for (int i = 0; i < n - 2; i++)
	{
		sum = arr[i];
		for (int j = i + 1; j < n - 1; j++)
		{
			sum = arr[i] + arr[j];
			for (int k = j + 1; k < n; k++)
			{
				sum = arr[i] + arr[j] + arr[k];
				if (sum <= m && ans < sum)
					ans = sum;
			}
		}
	}
	printf("%d", ans);
	return (0);
}