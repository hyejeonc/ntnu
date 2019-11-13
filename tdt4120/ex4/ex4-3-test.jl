## Hvis du bruker denne, kan jeg desverre ikke gi ut LF
## Da må du fylle den ut selv
function countingsortletters(A, position)
    #TODO
    n = length(A)
    B = zeros(Int64, n) #Array(Int64, n)
    max = 0
    for j = 1:n 
        B[j] = chartodigit(A[j][position])
        if max < B[j]
            max = B[j]
        end
    end


    index = zeros(Int64, max)
    sum = zeros(Int64, max)
    totalsum = 0
    for l in 1:n
        index[ B[l] ] += 1 
    end
    for i in 1:max
        totalsum += index[i]
        sum[i] = totalsum
    end
    temp = Array{String, 1}(undef, n)
    for m = n:-1:1
        temp[ sum[ B[m] ] ] = A[m]
        sum[ B[m] ] -= 1

    end
    return temp
end

function chartodigit(character)
    #Dette er en hjelpefunksjon for å få omgjort en char til tall
    #Den konverterer 'a' til 1, 'b' til 2 osv.
    #Eksempel: chartodigit("hei"[2]) gir 5 siden 'e' er den femte bokstaven i alfabetet.

    return character - '`'
end

## Hvis du bruker denne, kan jeg desverre ikke gi ut LF
## Da må du fylle den ut selv
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
        temp[ sum[ B[m] + 1 ]  ] = A[m]
        sum[ B[m] + 1 ] -= 1
    end
    return temp
end

## Du skal implementere denne funksjonen 
function flexradix(A, maxlength)
    # TODO
    # 먼저 각 알파벳을 숫자로 바꿀 수 있다. 이때 빈 칸인 숫자는 ` 으로 바꾼다. 
    n = length(A)
    B = A
    #B = Array{String, 1}(undef, n)
    for w in 1:n
        for q in maxlength:-1:maxlength-length(A[w])
            if length(A[w]) < maxlength
                println("w = ", w)
                println("q = ", q)
                B[w] = string(B[w], "`")
                #push!(B[w], "`")
                println("B[w][q] = ", B[w][q])
                #
            end
        end
    end

    println("old A = ", A)   
    println("old B = ", B)   

    temp = Array{String, 1}(undef, n)

    for i in maxlength:-1:1
        temp = B
        println("temp = ", temp)  
        B = countingsortletters(temp, i)
    end
    println("new B = ", B)  

    for e in 1:n
        for r in maxlength:-1:1
            if B[e][r] == "`"
                replace(B[e][r], "`" => "")
            end
        end
    end

    println("result B = ", B)  
    #=
    for m in 1:length(temp2)
        println("temp2[m]", temp2[m])
        for u in 1:length(temp2[m])
            replace(temp2[m][u], "" => "")
        end

        #if contains(val2, "z")
    end
    =#

    
    return B
    
end





### Tests ###
# Disse testene blir kjør når du kjører filen
# Du trenger ikke å endre noe her, men du kan eksperimentere! 

printstyled("\n\n\n---------------\nKjører tester!!\n---------------\n"; color = :magenta)

using Test
@testset "Basic tests" begin
    #@test flexradix(["d", "c", "b", "a"], 1) == ["a", "b", "c", "d"]
    @test flexradix(["d", "c", "b", ""], 1) == ["", "b", "c", "d"]
    #@test flexradix(["jeg", "elsker", "deg"], 6) == ["deg", "elsker", "jeg"]
    #@test flexradix(["denne", "oppgaven", "mangler", "emojies"], 8) == ["denne", "emojies", "mangler", "oppgaven"]
    #@test flexradix(["kobra", "aggie", "agg", "kort", "hyblen"], 6) == ["agg", "aggie", "hyblen", "kobra", "kort"] # Fra oppgaven
end

println("\nFungerte alt? Prøv å kjør koden i inginious!")
println("Husk at disse testene ikke alltid sjekker alle edge-cases")
println("---------------------------------------------------------\n\n")