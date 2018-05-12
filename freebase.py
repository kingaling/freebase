# Copyright (C) 2018  Shane King <kingaling at meatchicken dot net>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

def __free_base(src, sc, dc):
    src_base = len(sc)
    dst_base = len(dc)
    len_src = len(src)
    sv = 0

    # Need value of input before we can begin conversion
    for i in range(0, len_src):
        multiplier = sc.index(src[i])
        power = len_src - i - 1
        sv += (src_base ** power) * multiplier
    # sv contains decimal (base 10) version of the input

    # Begin conversion
    if sv == 0:
        return dc[0]
    dv = ''
    while True:
        if sv == 0:
            break
        tmp_int = int(sv / dst_base)
        dv = dc[(sv % dst_base)] + dv
        sv = tmp_int

    return dv


# convert a number of any base to a number of any base.
# max base = 94 due to current defined charsets
# However, you could easily use base 256 if you wanted. :)

# Defined charsets
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
punct = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{',
         '}', ':', '"', '<', '>', '?', '-', '=', '[', ']', ';', '\'', ',',
         '.', '/', '|', '\\', '~', '`']

# Must be a string
src_val = 'ADF54ED'

# Define charset used by source
src_charset = ints + upper[:6]

# Define charset used by destination
dst_charset = ints

# Convert all the things
res = __free_base(src_val, src_charset, dst_charset)

print 'Input: %s' % src_val
print 'Converting from base: %s' % len(src_charset)
print 'Converting to base: %s' % len(dst_charset)
print 'Output: %s' % res
