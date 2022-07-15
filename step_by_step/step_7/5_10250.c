#include <stdio.h>

int	main()
{
	int	t, h, w, n;
	int	ans;

	scanf("%d", &t);
	while (t--)
	{
		scanf("%d %d %d", &h, &w, &n);
		ans = n / h + !(!(n % h)) + 100 * (n % h ? n % h : h);
		printf("%d\n", ans);
	}
	return (0);
}