/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: namaloma <namaloma@learner.42.tech>        +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/20 11:29:39 by namaloma          #+#    #+#             */
/*   Updated: 2025/12/24 16:13:26 by namaloma         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <unistd.h>
# include <stdarg.h>

int	ft_printf(const char *format, ...);
int	printform(char c, va_list *args);
int	printstr(char *s);

int	printptr(void *addr);
int	printd(int n);
int	printu(unsigned int n);
int	printhx_l(unsigned int n);
int	printhx_u(unsigned int n);
int	print_unsigned_base(unsigned long num, char *base);

#endif
