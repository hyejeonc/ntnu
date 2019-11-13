co = 1
delta = 1.5

x = [1 2; 2 3; 3 0; 4 0; 5 1]

col = x[:, co]
med = 0.5 * (col[1] + col[length(col)])
min = med - delta
max = med + delta

a = -1
b = -1

a_var = 0
b_var = 0


for i = 1:length(col)
    println("i is !! ", i)
    if (col[i] >= min) && (col[i] <= max)
        a_var = i
        a = i
        println("a = ", a)
        break
    end
end
println("a = !!!! ", a_var)
for j in length(col):-1:1
    println("j is !! ", j)
    if (col[j] >= min) && (col[j] <= max)
        b = j
        b_var = j
        println("b = ", b)
        break
    end
end
println(a_var, b_var)
#=
if (a == nothing) || (b == nothing)
    println(-1, -1)
else
    println(a, b)
end
=#




