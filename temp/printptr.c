/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   printptr.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: namaloma <namaloma@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 14:57:07 by namaloma          #+#    #+#             */
/*   Updated: 2025/12/21 16:06:11 by namaloma         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

int	printptr(void *addr)
{
	int	count;

	if (addr == 0)
		return (write (1, "(nil)", 5));
	count = 0;
	count += write(1, "0x", 2);
	count += print_unsigned_base((unsigned long)addr, "0123456789abcdef");
	return (count);
}
