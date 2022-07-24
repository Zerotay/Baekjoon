#include <stdio.h>
#include <stdlib.h>

int	compare(char **arr, int n, int m)
{
	char	arr_w[8][8], arr_b[8][8];
	int		cnt1, cnt2;

	for (int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++)
			arr_w[i][j] = (i + j) % 2 ? 'W' : 'B';
	for (int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++)
			arr_b[i][j] = (i + j) % 2 ? 'B' : 'W';
	cnt1 = 0;
	cnt2 = 0;
	for (int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++)
			if (arr_w[i][j] != arr[i + n][j + m])
				cnt1++;
	for (int i = 0; i < 8; i++)
		for (int j = 0; j < 8; j++)
			if (arr_b[i][j] != arr[i + n][j + m])
				cnt2++;
	return (cnt1 > cnt2 ? cnt2 : cnt1);
}

int	main()
{
	int		n, m, ans, k;
	char	**arr;

	scanf("%d %d", &n, &m);
	if (!(arr = (char **)malloc(sizeof(char *) * n)))
		return (0);
	for (int i = 0; i < n; i++)
		if (!(arr[i] = (char *)malloc(sizeof(char) * (m + 2))))
			return (0);
	for (int i = 0; i < n; i++)
		scanf("%s", arr[i]);
	ans = 64;
	for (int i = 0; i <= n - 8; i++)
		for (int j = 0; j <= m - 8; j++)
		{
			k = compare(arr, i, j);
			if (ans > k)
				ans = k;
		}
	printf("%d", ans);
	for (int i = 0; i < n; i++)
		free(arr[i]);
	free(arr);
	return (0);
}