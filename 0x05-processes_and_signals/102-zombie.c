#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * main - Creates 5 zombie processes
 * Return: void
 */

int main(void)
{
	int i;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child == 0)
		{
			printf("Zombie process created, PID: %i\n", getpid());
			exit(0);
		}
	}

	while (1)
	{
		sleep(1);
	}
	return (0);
}
