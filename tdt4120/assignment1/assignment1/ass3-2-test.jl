function binaryintervalsearch(x, delta, coordinate)
    co = coordinate
    col = x[:, co] 
    med = 0.5 * (col[1] + col[length(col)])
    min = med - delta
    max = med + delta
    println("min = ", min)
    println("max = ", max)
    a = -1
    b = -1
    
    for i = 1:length(col)
        if (col[i] >= min) && (col[i] <= max)
            a = i
            break
        end
    end
    
    for j in length(col):-1:1
        if (col[j] >= min) && (col[j] <= max)
            b = j
            break
        end
    end
    
    if ((a == -1) || (b == -1)) || ((a == b) || (col[1] == col[length(col)]))
        return(-1, -1)
#    elseif a == b
#        return(-1, -1)
    else
        return(a, b)
    end
        
end

a = [1 2; 2 3; 3 0; 4 0; 5 1]
b = [1.0 -1.0; 2.0 2.0; 3.0 3.0]
c = [1 2; 2 0; 3 3; 4 4]
d = [1 0; 2 0; 2 0; 3 0; 4 0; 5 0; 5 0]
e = [1.0 -1.0; 2.0 2.0; 3.0 3.0] #delta=1.0
f = [1.0 0.0; 2.0 0.0; 3.0 0.0] # delta = 1.0
#println(binaryintervalsearch(a, 1.5, 1))
#println(binaryintervalsearch(b, 1, 1))
#println(binaryintervalsearch(c, 0.25, 1)) # -1, -1
#println(binaryintervalsearch(d, 1, 1)) # 2, 5
println(binaryintervalsearch(e, 1, 1)) 
println(binaryintervalsearch(e, 1, 2)) 
println(binaryintervalsearch(f, 0.5, 1)) 
g = [1.0 0.0; 2.0 0.0; 3.0 0.0] # d = 0.5
println(binaryintervalsearch(g, 0.5, 1)) 
println(binaryintervalsearch(g, 0.5, 2)) 