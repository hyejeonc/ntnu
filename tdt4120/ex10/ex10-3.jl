# Psuedocode is on page 
function floyd_warshall(adjacency_matrix, nodes, f, g)
    new_matrix = adjacency_matrix
    #n = size(adjacency_matrix)[1][1]

    for k in 1:nodes
        for i in 1:nodes
            for j in 1:nodes
                adjacency_matrix[i, j] = min(adjacency_matrix[i, j], adjacency_matrix[i, k] + adjacency_matrix[k, j])
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

    new_matrix = floyd_warshall(adjacency_matrix, nodes, max, multiple)
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



