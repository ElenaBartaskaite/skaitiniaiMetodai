## Copyright (C) 2019 Vilius
## 
## This program is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see
## <https://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} CholeskioD (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: Vilius <Vilius@LAPBOT>
## Created: 2019-10-20

function L = CholeskioD (A)
  ALength = length(A);
  L = zeros(ALength);
  L(1, 1) = A(1, 1) ^ 0.5;
  for i = 2:ALength
    L(i, 1) = A(i, 1) / L(1, 1);
  endfor
  for i = 2:ALength
    L(i, i) = (A(i, i) - L(i, 1:(i - 1)) * L(i, 1:(i - 1))') ^ 0.5;
    for j = (i + 1):ALength
      L(j, i) = (A(j, i) - L(j, 1:(j - 1)) * L(i, 1:(j - 1))') / L(i, i);
    endfor
  endfor
endfunction
