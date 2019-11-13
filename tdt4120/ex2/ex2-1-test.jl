# Importing the struct beeing used
# Inside a try-catch to allow it to be defined multiple times
# (Mostly a workaround for some IDEs, you don't have to care about this)
try
    mutable struct Node
        next::Union{Node, Nothing} # Next can be a new Node or nothing
        value::Int 
    end
catch e end




## Du skal implementere denne funksjonen 
function findindexinlist(linkedlist, index)
    i = index
    node = linkedlist 
    println("1. Start with index == ", index)
    result = nothing
    var = nothing 
    count = 0
    
    try
        for i in 1:index
            println("\n 2. %% Start the loop %% == ", i)
            
            if node.value != nothing
                var = node.next
                println("3. if node.value != nothing ############ HEre!")
                println("4. node === ", node)
            else
                println("5. This?! \n")
                result = -1
            end
            #result = -1
            result = node.value
            node = var
            count += 1
        end
        println("6. Result is : ", result)
        #println("7. node = ", node)
        println("8. Count is ..! ", count)

        return result
        
    catch 
        return -1
    end
end





### Tests ###
# Disse testene blir kjør når du kjører filen
# Du trenger ikke å endre noe her, men du kan eksperimentere! 

## Simple linked chain
n3 = Node(nothing, 100)
n2 = Node(n3, 10)
n1 = Node(n2, 1)

println(findindexinlist(n1,1))


using Test
printstyled("\n\n---------------\nKjører tester!!\n---------------\n"; color = :magenta)
@testset "Basic tests" begin
    @test findindexinlist(n1, 1) == 1
    @test findindexinlist(n1, 2) == 10
    println("this is the problem!!!!!!! \n")
    @test findindexinlist(n1, 3) == 100
    @test findindexinlist(n1, 4) == -1
    @test findindexinlist(n1, 50) == -1
end

println("\nFungerte alt? Prøv å kjør koden i inginious!")
println("Husk at disse testene ikke alltid sjekker alle edge-cases")
println("---------------------------------------------------------\n\n\n\n")

