#include <stdio.h>

int	room(int k, int n)
{
	if (k == 0)
		return (n);
	if (n == 1)
		return (1);
	return (room(k - 1, n) + room(k, n - 1));
}

int	main()
{
	int	t, k, n;
	int	ans;

	scanf("%d", &t);
	while (t--)
	{
		scanf("%d %d", &k, &n);
		ans = room(k, n);
		printf("%d\n", ans);
	}
	return (0);
}