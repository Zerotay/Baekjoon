#include <stdio.h>
#include <stdlib.h>

int	main()
{
	int	n;
	int	tmp;
	int	sum;
	char s[80];

	scanf("%d", &n);
	while (n--)
	{
		scanf("%s", s);
		tmp = 0;
		sum = 0;
		for (int i = 0 ; *(s + i); i++)
		{
			if (*(s + i) == 'O')
			{
				tmp++;
				sum += tmp;
			}
			else
				tmp = 0;
		}
		printf("%d\n", sum);
	}
	return (0);
}