### Denne må med når en tester lokalt ###
# (try-catch er bare for å unngå feilmelding om redefinition of constant struct)
try
	mutable struct Node
    	children::Dict{Char,Node}
    	count::Int
	end
catch
	println("Node() allerede definert")
end

#==
To go to a child, one can write , 
given that one is in a node called and that node has a 
currentnode = currentnode.children['A']

gives a node currentnode with child 'A'
==#



### Du skal implementere denne funksjonen ###
function searchtree(root, dna)
    # din kode
    size = 0
    count = 0
    ex = false
    for i in 1:length(dna)
        if haskey(root.children, dna[i]) == true
            root = root.children[dna[i]]
            count = root.count
            size += 1
        end
    end

    if size == length(dna)
        return count
    else
        return 0
    end
    
end




### Konstruert testdata, la stå ###
root1 = Node(Dict('A' => Node(Dict{Char,Node}(), 1),'G' => Node(Dict('A' => Node(Dict{Char,Node}(), 2)), 1)), 0)
root2 = Node(Dict('A' => Node(Dict{Char,Node}(), 1),'G' => Node(Dict('A' => Node(Dict{Char,Node}(), 1),'G' => Node(Dict{Char,Node}(), 1)), 1),'T' => Node(Dict('G' => Node(Dict('T' => Node(Dict{Char,Node}(), 1)), 0),'T' => Node(Dict('G' => Node(Dict{Char,Node}(), 1)), 0)), 0),'C' => Node(Dict('C' => Node(Dict('A' => Node(Dict{Char,Node}(), 1)), 1)), 1)), 0)

s1 = "AG"
s2 = "GA"
s3 = "TGT"




### Tester ###
# Disse testene blir kjør når du kjører filen
# Du trenger ikke å endre noe her, men du kan eksperimentere!

printstyled("\n\n\n---------------\nKjører tester!!\n---------------\n"; color = :magenta)

using Test
@testset "Tester" begin
	@test searchtree(root1, s1) == 0
	@test searchtree(root1, s2) == 2
	@test searchtree(root1, s3) == 0
	@test searchtree(root2, s1) == 0
	@test searchtree(root2, s2) == 1
	@test searchtree(root2, s3) == 1
end

println("\nFungerte alt? Prøv å kjør koden i inginious!")
println("Husk at disse testene ikke alltid sjekker alle edge-cases")
println("---------------------------------------------------------\n\n")