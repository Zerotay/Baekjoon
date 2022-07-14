#include <stdio.h>

int	is_group(char *str)
{
	char	abc[26] = {0, };

	for (int i = 0; str[i]; i++)
		if (str[i] != str[i + 1])
			abc[str[i] - 97]++;
	for (int j = 0; j < 26; j++)
		if (abc[j] > 1)
			return (0);
	return (1);
}

int	main()
{
	int	n;
	char	str[101];
	int	count = 0;

	scanf("%d", &n);
	while (n--)
	{
		scanf("%s", str);
		count += is_group(str);
	}
	printf("%d", count);
	return (0);
}