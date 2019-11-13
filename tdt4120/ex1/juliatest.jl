#!/usr/bin/env julia
println("hello world")

function f(x, y)
     return x + y
end

function g(x, y)
    x - y
end 

#f(x::Float64, y::Float64)::Float64 = x / y

function main!()
    for i in length(l)
        print(l[i], ' ')
    end
    a::Int = 14
    b::Int = 7
    c::Int a + b


    @show typeof(c)  # debug print

    c = div(a, b)
    c = fld(a, b)
end

main()

l = Array{Int, 1}(undef, 100)

l = zeros(Int, 100)
l = ones(Int, 100)
push!(l, 5) # l.append(5)
sort!(l)
l = sort(l)

l2 = view(l, 3:-1:1, 1:4)
display(l2)
a = rand(Int64)
a = rand(Float64)
a = rand(1 : 10)
l = rand(1 : 10, 3, 4)

push!(d, "foo" => 1//2)
println(haskey(d, "foo")
println(d[])

@show l


@show union(s1, s2)
@show intersect(s1, s2)

@show setdiff(s1, s2)
@show symdiff(s1, s2)