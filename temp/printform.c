/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printform.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: namaloma <namaloma@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/24 14:27:15 by namaloma          #+#    #+#             */
/*   Updated: 2025/12/24 15:39:01 by namaloma         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	printform(char c, va_list *args)
{
	if (c == 'c')
	{
		c = (char)va_arg(*args, int);
		return (write (1, &c, 1));
	}
	else if (c == 's')
		return (printstr(va_arg(*args, char *)));
	else if (c == 'p')
		return (printptr(va_arg(*args, void *)));
	else if (c == 'd' || c == 'i')
		return (printd(va_arg(*args, int)));
	else if (c == 'u')
		return (printu(va_arg(*args, unsigned int)));
	else if (c == 'x')
		return (printhx_l(va_arg(*args, unsigned int)));
	else if (c == 'X')
		return (printhx_u(va_arg(*args, unsigned int)));
	else if (c == '%')
		return (write (1, "%", 1));
	return (0);
}
