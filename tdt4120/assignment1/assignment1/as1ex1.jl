#!/usr/bin/env julia
A = [1, 3, 1, 5, 7, 8, 3 ,9]
for j = 2:size(A)
	key = A(j)
	i = j-1
	while j>0 and A(i)>key
		A(i+1) = A(i)
		i = i-1
	A[i+1] = key


