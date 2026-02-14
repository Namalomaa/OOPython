#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>

char *get_next_line(int fd);

/* ---------- Utils ---------- */

static void	print_result(char *line, int expect_null)
{
	if (expect_null)
	{
		if (line == NULL)
			printf("✅ OK (NULL as expected)\n");
		else
		{
			printf("❌ KO (Expected NULL, got \"%s\")\n", line);
			free(line);
		}
	}
	else
	{
		if (!line)
			printf("❌ KO (Unexpected NULL)\n");
		else
		{
			size_t len = strlen(line);
			if (len > 0 && line[len - 1] != '\n')
				printf("⚠️  EOF line without \\n: \"%s\"\n", line);
			else
				printf("✅ \"%s\"", line);
			free(line);
		}
	}
}

/* ---------- Error Tests ---------- */

static void	test_invalid_fd(void)
{
	printf("\n=== Invalid FD Test ===\n");
	char *line = get_next_line(42);
	print_result(line, 1);
}

static void	test_closed_fd(void)
{
	printf("\n=== Closed FD Test ===\n");
	int fd = open("test_files/simple.txt", O_RDONLY);
	close(fd);
	char *line = get_next_line(fd);
	print_result(line, 1);
}

/* ---------- File Tests ---------- */

static void	test_file(const char *name)
{
	printf("\n=== File: %s ===\n", name);
	int fd = open(name, O_RDONLY);
	if (fd < 0)
	{
		perror("open");
		return;
	}

	char *line;
	while ((line = get_next_line(fd)))
		print_result(line, 0);

	close(fd);
}

/* ---------- STDIN ---------- */

static void	test_stdin(void)
{
	printf("\n=== STDIN Test (Ctrl+D to stop) ===\n");
	char *line;
	while ((line = get_next_line(STDIN_FILENO)))
		print_result(line, 0);
}

/* ---------- Entry ---------- */

int main(void)
{
	printf("=====================================\n");
	printf(" get_next_line STRESS TEST\n");
	printf(" BUFFER_SIZE = %d\n", BUFFER_SIZE);
	printf("=====================================\n");

	/* Error handling */
	test_invalid_fd();
	test_closed_fd();

	/* Files */
	test_file("test_files/empty.txt");          // empty file
	test_file("test_files/one_char.txt");       // "a"
	test_file("test_files/short.txt");          // < 4 chars
	test_file("test_files/exact.txt");          // line == BUFFER_SIZE
	test_file("test_files/plus_one.txt");       // BUFFER_SIZE + 1
	test_file("test_files/minus_one.txt");      // BUFFER_SIZE - 1
	test_file("test_files/multiple.txt");       // multiple lines
	test_file("test_files/long.txt");           // 2k+ chars
	test_file("test_files/no_newline.txt");     // EOF without \n
	test_file("test_files/empty_lines.txt");    // multiple empty lines

	/* STDIN */
	test_stdin();
	printf("\n=== END OF TEST ===\n");
	return 0;

}
