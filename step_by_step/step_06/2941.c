#include <stdio.h>

int	main()
{
	char	str[101];
	int		count = 0;

	scanf("%s", str);
	for (int i = 0; str[i]; i++)
	{
		if (str[i] == 'c' && (str[i + 1] == '=' || str[i + 1] == '-'))
			continue;
		else if (str[i] == 'l' && (str[i + 1] == 'j'))
			continue;
		else if (str[i] == 'n' && (str[i + 1] == 'j'))
			continue;
		else if (str[i] == 's' && (str[i + 1] == '='))
			continue;
		else if (str[i] == 'z' && (str[i + 1] == '='))
			continue;
		else if (str[i] == 'z' && i && (str[i - 1] == 'd'))
			count++;
		else if (str[i] == 'd' && (str[i + 1] == '-' || str[i + 1] == 'z'))
			continue;
		count++;
	}
	printf("%d", count);
	return (0);
}