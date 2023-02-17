#include <stdio.h>

int	main()
{
	int	count, i, n = 1;
	int	arr[456913] = {0, };

	i = 1;
	arr[1] = 1;
	while (++i < 676)
		if(!arr[i])
			for(int j = i; i * j <= 456912; j++)
				arr[i * j] = 1;
	while (scanf("%d", &n) && n)
	{
		i = n;
		count = 0;
		while (++i <= 2 * n)
			if (!arr[i])
				count++;
		printf("%d\n", count);
	}
	return (0);
}