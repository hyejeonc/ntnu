B = [1, 4, 3, 4, 7, 2, 1]
A = [10, 5, 16, 0]
maxnumber = 8
println(A)

for j = 2:length(A)
    
    
    key = A[j]
    i = j-1
    println("This is the index == ", i)
    println("This is key == ", key)
    while A[i] > key
        A[i+1] = A[i]
        i = i-1  
        if i == 0
            break
        end
    end
    A[i+1] = key
end
println(A)
for k = 1:length(A)
    if A[k] > maxnumber
        A[k] = maxnumber 
    end
end
println(A)



