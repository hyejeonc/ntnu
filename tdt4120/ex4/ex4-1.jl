function chartodigit(character)
    #Dette er en hjelpefunksjon for å få omgjort en char til tall
    #Den konverterer 'a' til 1, 'b' til 2 osv.
    #Eksempel: chartodigit("hei"[2]) gir 5 siden 'e' er den femte bokstaven i alfabetet.
    return character - '`'
end
## Du skal implementere denne funksjonen 
function countingsortletters(A, position)
    #TODO
    n = length(A)
    #print(n)
    B = zeros(Int64, n) #Array(Int64, n)
    max = 0
    #print(max)
    #println(A[1][2])
    for j = 1:n 
        #println( B[j] )
        B[j] = chartodigit(A[j][position])
        if max < B[j]
            max = B[j]
        end
    end
    #print(B)
    #print(max)

    index = zeros(Int64, max)
    sum = zeros(Int64, max)
    #print("index array: ", index)
    totalsum = 0
    for l in 1:n
        index[ B[l] ] += 1 
    end
    println(B)
    for i in 1:max
        totalsum += index[i]
        sum[i] = totalsum
    end
    println(sum)

    #temp = A 
    temp = Array{String, 1}(undef, n)
    #temp = Array{String}(undef, 1, n)

    println(temp)
    println("%%%%%%%%%%%%%%%%%")
    for m = n:-1:1
        println("###########################")
        println("B(m) = ", B[m])
        #println("temp[ sum[ B[m] ] ] = ", temp[ sum[ B[m] ] ])
        println("A[m] = ", A[m])
        temp[ sum[ B[m] ] ] = A[m]
        println("sum[ B[m] ]", sum[ B[m] ])
        sum[ B[m] ] -= 1
        println(sum)
        println(temp)
        println(A)
    end
    #print(temp)
    return temp
end


# Don't mind me 




### Tests ###
# Disse testene blir kjør når du kjører filen
# Du trenger ikke å endre noe her, men du kan eksperimentere! 

printstyled("\n\n\n---------------\nKjører tester!!\n---------------\n"; color = :magenta)

using Test
@testset "Basic tests" begin
    @test countingsortletters(["aa", "bb", "cc"], 1) == ["aa", "bb", "cc"]
    @test countingsortletters(["cc", "bb", "aa"], 2) == ["aa", "bb", "cc"]
    @test countingsortletters(["ac", "bb", "ca"], 2) == ["ca", "bb", "ac"]
    @test countingsortletters(["ccc", "cba", "ca", "ab", "abc"], 2) == ["ca", "cba", "ab", "abc", "ccc"]
end

println("\nFungerte alt? Prøv å kjør koden i inginious!")
println("Husk at disse testene ikke alltid sjekker alle edge-cases")
println("---------------------------------------------------------\n\n")