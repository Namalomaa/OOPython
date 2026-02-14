NAME = libftprintf.a

CC	= cc
CFLAGS	= -Wall -Wextra -Werror

SRCS = ft_printf.c \
       printform.c \
       printstr.c \
       printptr.c \
       printd.c \
       printu.c \
       printhx_l.c \
       printhx_u.c \
       print_unsigned_base.c

OBJS = $(SRCS:.c=.o)

all: $(NAME)

$(NAME): $(OBJS)
	ar rcs $(NAME) $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

clean:
	rm -f $(OBJS)

fclean: clean
	rm -f $(NAME)

re: fclean all

.PHONY: all clean fclean re
