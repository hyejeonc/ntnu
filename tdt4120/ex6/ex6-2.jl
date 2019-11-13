function cumulative(weights)
    rows, cols = size(weights)
    path_weights = zeros(Int64, rows, cols)
    print(rows, cols)
    path_weights[1,:] = weights[1,:]

    for r = 2:rows
        for c = 1:cols
            above = [path_weights[r-1, c]]

            if c > 1
                push!(above, path_weights[r-1, c-1])
            end


            if c < cols
                push!(above, path_weights[r-1, c+1])
            end

            path_weights[r, c] = weights[r, c] + minimum(above)
        end
    end

    return path_weights
end

# weights = [3  6  8 6 3;
#            7  6  5 7 3;
#            4  10 4 1 6;
#            10 4  3 1 2;
#            6  1  7 3 9]

# println(cumulative(weights))

function backtrack(pathweights)
    rows, cols = size(pathweights)
    lower, upper = 2, cols

    path = Array{Tuple{Int, Int}, 1}()

    for r = rows:-1:1

        smallest = pathweights[r, lower]
        index = lower
        for c = lower:upper
            if pathweights[r, c] < smallest
                smallest = pathweights[r, c]
                index = c
            end
        end

        push!(path, (r, index))

        lower, upper = maximum([1, index-1]), minimum([cols, index+1])
    end

    return path
end

pathweights = [3  6  8  6  3
              10 9  11 10 6
              13 19 13 7  12
              23 17 10 8  9
              23 11 15 11 17]

println(backtrack(pathweights))