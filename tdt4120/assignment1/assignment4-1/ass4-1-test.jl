function chartodigit(character)
    #Dette er en hjelpefunksjon for å få omgjort en char til tall
    #Den konverterer 'a' til 1, 'b' til 2 osv.
    #Eksempel: chartodigit("hei"[2]) gir 5 siden 'e' er den femte bokstaven i alfabetet.
    return character - '`'
end

println( chartodigit('2') )

#=
A = ["ccc", "cba", "ca", "ab", "abc"]
position = 2

#println(A[1][2])

n = length(A)
#print(n)
B = zeros(Int64, n) #Array(Int64, n)
max = 0
print(max)
#println(A[1][2])
for j = 1:n 
    println( B[j] )
    B[j] = chartodigit(A[j][position])
    if max < B[j]
        max = B[j]
    end
end
#print(B)
print(max)

index = zeros(Int64, max)
sum = zeros(Int64, max)
print("index array: ", index)
totalsum = 0
for l in 1:n
    index[ B[l] ] += 1 
end

for i in 1:max
    totalsum += index[i]
    sum[i] = totalsum
end
print(sum)

temp = A 

for m in n:-1:1
    temp[ sum[ B[m] ] ] = A[m]
    sum[ B[m] ] -= 1
end
print(temp)
return temp

=#