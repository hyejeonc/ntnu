function countingsortlength(A)
    # TODO 
    n = length(A)
    B = zeros(Int64, n) #Array(Int64, n)
    max = 0
    zero = false

    for j = 1:n 
        B[j] = length(A[j])
        if max < B[j]
            max = B[j]
        end
    end

    println("This is B ", B)
    index = zeros(Int64, max + 1)
    sum = zeros(Int64, max + 1)
    totalsum = 0

    for l in 1:n
        index[ B[l] + 1 ] += 1 
    end

    for i in 1:max+1
        totalsum += index[i]
        sum[i] = totalsum
    end

    #temp = A 
    temp = Array{String, 1}(undef, n)
    #temp = Array{String}(undef, n)
    
    for m = n:-1:1
        #println("temp[ sum[ B[m] ] ] = ", temp[ sum[ B[m] ] ])
        println("m = ", m)
        println("index ", index)
        println("temp ", temp)
        println("sum ", sum)
        println("B ", B)
        temp[ sum[ B[m] + 1 ]  ] = A[m]
        sum[ B[m] + 1 ] -= 1
    end
    println("##################")
    println(temp)
    return temp

end


### Tests ###
# Disse testene blir kjør når du kjører filen
# Du trenger ikke å endre noe her, men du kan eksperimentere! 

printstyled("\n\n\n---------------\nKjører tester!!\n---------------\n"; color = :magenta)

using Test
@testset "Basic tests" begin
    @test countingsortlength(["ccc", "bb", "a"]) == ["a", "bb", "ccc"]
    @test countingsortlength(["aaa", "bb", "c"]) == ["c", "bb", "aaa"]
    @test countingsortlength(["bb", "a", ""]) == ["", "a", "bb"] # Testen her sjekker om du kan sortere også med emtpy string
    @test countingsortlength(["bbbb", "aa", "aaaa", "ccc"]) == ["aa", "ccc", "bbbb", "aaaa"] # Fra oppgaven
end

println("\nFungerte alt? Prøv å kjør koden i inginious!")
println("Husk at disse testene ikke alltid sjekker alle edge-cases")