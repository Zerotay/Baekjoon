#include <stdio.h>

int	main()
{
	char	str[100];
	int		abc[27];
	int		i = -1;

	while (++i < 26)
		abc[i] = -1;
	scanf("%s", str);
	i = -1;
	while (str[++i])
		if(abc[str[i] - 97] == -1)
			abc[str[i] - 97] = i;
	i = 0;
	while (i < 26)
		printf("%d ", abc[i++]);
	return (0);
}