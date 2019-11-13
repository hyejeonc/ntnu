A = [1, 4, 3, 4, 7, 2, 1]
println(A)
for j = 2:length(A)
    key = A[j]
    i = j-1
    while A[i] > key
        A[i+1] = A[i]
        i = i-1  
        if j == 0
            break
        end
    end
    A[i+1] = key
end

println(A)



