function mergearrays(x, y)
    println("###########################")
   
    a = x
    b = y



    

    a_x = a[:, 1]
    a_y = a[:, 2]
    println("a_y = ", a[:, co + 1])

    b_x = b[:, 1]
    b_y = b[:, 2]
    #println("b_x = ", b_x)

    n = length(a_x) 
    m = length(b_x)
    println("n and m : ", n, m)
    
    temp = zeros(Int64, n+m, 2)
    println("temp ", temp)
    k = 1
    i = 1
    j = 1
  
    while (i <= n)  
        while (j <= m) 
            println("k, i, j = ", k, i, j)
            if a[i, co] <= b[j, co]
                #println("a[i, co] = ", a[i, co])
                if temp[k-1, co] > a[i, co]
                temp[k, co] = a[i, co]
                #println("a[i, co] = ", temp[k, co])
                temp[k, co + 1] = a[i, co + 1]
                i += 1
                k += 1
            else 
                temp[k, co] = b[j, co]
                temp[k, co + 1] = b[j, co + 1]
                j += 1
                k += 1
            end
        end
    end
    println("This is temp = ", temp)

    while i < n
        temp[k, co] = a[i, co]
        temp[k, co + 1] = a[i, co + 1]
        k += 1
        i += 1
    end

    while j < m 
        temp[k, co] = b[j, co]
        temp[k, co + 1] = b[j, co + 1]
        k += 1
        j += 1
    end

    return temp

end



x = [1 2; 4 5; 3 2]
y = [2 2; 4 5; 3 2 ; 2 6]

println( mergearrays(x, y, 1) )


#=
function mergesort(x, coordinate)
    co = coordinate
    col = x[:, co]
    n = length(col)
    mid = int(0.5 * (col[1] + col[n]))
    if 

  

end
=#


