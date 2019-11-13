try 
    mutable struct Node
        i::Int
        j::Int
        floor::Bool
        neighbors::Array{Node}
        color::Union{String,Nothing}
        distance::Union{Int,Nothing}
        predecessor::Union{Node,Nothing}
    end
catch
	println("Node() allerede definert")
end
Node(i, j, floor=true) = Node(i, j, floor, [], nothing, nothing, nothing)


a = Node(1, 2, false)
println(a)



### Du skal implementere denne funksjonen ###
function mazetonodelist(maze)
    # Vi lager en matrise nodearray med størrelse tilsvarende maze,
    # men med Node-objekter isteden
    nodearray = Array{Node}(undef, size(maze, 1), size(maze, 2))
    num = 1
    for i in 1:size(maze, 1) # maze 의 행 수 
        for j in 1:size(maze, 2) # maxe 의 열 수 
            # Fyll inn kode for å oppdatere nodearray 
            # 어레이 노드 각각 어떤게 있는지 일단 쭉 뽑기 
            if maze[i, j] == 1
                nodearray[num] = Node(i, j)
                #push!(nodearray, Node(i, j, true))
                num += 1 # num 은 어레이의 사이즈가 된다. 
            end
            
        end
    end
    # 여기까지 하면, 노드어레이에 노드어레이는 노드 객체 들의 리스트로 구성된다. 
    # 그럼 노드 어레이에 쌓인 리스트에 각각 어떻게 이웃을 수정할 것이냐?
    #=
    num2 = 1
    for i in 1:size(maze, 1)
        for j in 1:size(maze, 2)
            # Fyll inn kode for å oppdatere neighbors til hver node
            # (Husk at naboene alltid er rett over, rett under,
            #  rett til venstre og/eller rett til høyre)
            # 각 노드 객체에 이웃은 어떻게 지정할 것인지 입력하기. 
            list = []
            if maze[i, j] == 1 
                if maze[i, j+1] == 1
                    push!(list, Node(i, j+1, true))
                elseif maze[i+1, j] == 1
                    push!(list, Node(i+1, j, true))
                end
            end
            println(nodearray)
            nodearray[num2].neighbors = list
            num2 += 1
            
        end
    end
    =#
    return nodearray
    # Fyll inn kode for å returnere en nodeliste ut ifra nodearray
end

maze = [0 0 0 0 0
        0 1 1 1 0
        0 1 0 0 0
        0 1 1 1 0
        0 0 0 0 0]
nodelist = mazetonodelist(maze)
println(nodelist)
println("length of nodelist is :", length(nodelist))