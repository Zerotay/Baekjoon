#include <stdio.h>
#include <stdlib.h>

int	main()
{
	int	n, sum;
	char	*str;

	scanf("%d", &n);
	str = (char *)malloc(sizeof(char) * n + 1);
	if (!str)
		return (0);
	str[n] = 0;
	sum = 0;
	scanf("%s", str);
	while (n--)
		sum += str[n] - 48;
	printf("%d", sum);
	free(str);
	return (0);
}