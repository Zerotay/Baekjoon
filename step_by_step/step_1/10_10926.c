#include <stdio.h>
#include <stdlib.h>

int main()
{
	char	*name;

	if (!(name = (char *)malloc(sizeof(char) * 51)))
		return (0);
	for (int i = 0; i < 50; i++)
	{
		scanf("%c", &name[i]);
		if (name[i] == '\n')
		{
			name[i] = 0;
			break;
		}
	}
	printf("%s\?\?!", name);
	free(name);
	return (0);
}