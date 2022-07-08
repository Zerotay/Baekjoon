#include <stdio.h>

int	main()
{
	int	tmp, num, max;

	max = 0;
	for (int i = 0; i < 9; i++)
	{
		scanf("%d", &tmp);
		if (tmp > max)
		{
			max = tmp;
			num = i;
		}
	}
	printf("%d\n%d", max, num + 1);
	return (0);
}