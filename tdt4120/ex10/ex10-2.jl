try
    mutable struct Node
        name::String # used to distinguish nodes when debugging
        d::Union{Float64, Nothing} # d for distance
        p::Union{Node, Nothing} # p for predecessor
    end
catch
    println("Node is defined already")
end
Node(name) = Node(name, nothing, nothing) # constructor used for naming nodes

try
    mutable struct Graph
        V::Array{Node} # V for Vertices
        Adj::Dict{Node, Array{Node}} # Adj for Adjacency
    end
catch
    println("Graph is defined already")
end


# Psuedocode is on page 648
function initialize!(G, s) # Graph G 에서, 시작점이 s. 끝점이 v.
    # din kode her
    for v in G.V
        v.d = Inf
        v.p = Nothing
    end
    s.d = 0
end


function update!(u, v, w)
    # din kode her
    if v.d > u.d + w(u, v)
        v.d = u.d + w(u, v)
        v.p = u
    end
end

# Psuedocode is on page 
function floyd_warshall(adjacency_matrix, nodes, f, g)
    new_matrix = adjacency_matrix
    #n = size(adjacency_matrix)[1][1]

    for k in 1:nodes
        for i in 1:nodes
            for j in 1:nodes
                adjacency_matrix[i, j] = f(adjacency_matrix[i, j], g(adjacency_matrix[i, k], adjacency_matrix[k, j]) )
            end
        end
    end
    return adjacency_matrix
end

function add(a, b)
    return a+b
end

test = [0 7 2; Inf 0 Inf; Inf 4 0]
println(floyd_warshall(test, 3, min, add ))

# Pseudocode is in page 633. 
function transitive_closure_test(adjacency_matrix, nodes)
    # din kode her
    new_matrix = adjacency_matrix
    for i in 1:nodes
        for j in 1:nodes
            if (i == j) || (adjacency_matrix[i, j] == 1)
                new_matrix[i, j] == 1
            else
                new_matrix[i, j] == 0
            end
        end
    end
    # new matrix 는 이미 생겼다. 
    for k in 1:nodes
        old_matrix = new_matrix
        for i in 1:nodes
            for j in 1:nodes
                if (old_matrix[i, j] == 0) && (old_matrix[i, k] * old_matrix[k, j] == 0)
                    new_matrix[i, j] = 0
                else
                    new_matrix[i, j] = 1
                end
            end
        end

    end
    return new_matrix
end

function transitive_closure(adjacency_matrix, nodes)
    function multiple(a, b)
        return a * b
    end

    function add(a, b)
        return a + b
    end
    new_matrix = floyd_warshall(adjacency_matrix, nodes, min, add)
    
    for i in 1:nodes
        for j in 1:nodes
            if new_matrix[i, j] == Inf
                new_matrix[i, j] = 0
            else 
                new_matrix[i, j] = 1
            end
        end
    end
    return new_matrix
end

println(transitive_closure(test, 3) )



