#B = [1, 4, 3, 4, 7, 2, 1]
A = [10, 5, 16, 0]
X = []
maxnumber = 8
println(A)

for i = 1:length(A)
    var = pop!(A)
    push!(X, var)
end

println(A)
println(X)
for k = 1:length(X)
    if X[k] > maxnumber
        X[k] = maxnumber 
    end
end
println(X)



