#include <stdio.h>
#include <string.h>

int	main()
{
	char	a[10001] = {0,};
	char	b[10001] = {0,};
	char	ans[10002] = {0,};
	int		i, j, k = 0;

	scanf("%s %s", a, b);
	i = strlen(a) - 1;
	j = strlen(b) - 1;
	k = 10001;
	while (1)
	{
		ans[k] += a[i] + b[j] - 96;
		if (ans[k] > 9)
		{
			ans[k] = ans[k] % 10;
			ans[k - 1] += 1;
		}
		if (!i && !j)
			break ;
		if (i)
			i--;
		else
			a[i] = 48;
		if (j)
			j--;
		else
			b[j] = 48;
		k--;
	}
	i = 0;
	while (!ans[i])
		i++;
	while (i < 10002)
		printf("%c", ans[i++] + 48);
	return (0);
}