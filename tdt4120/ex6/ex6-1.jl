### Du skal implementere denne funksjonen ###
function lislength(s)
    mls = zeros(Int, size(s))
    mls[1] = 1
    #a = s[1]
    for i = 2:length(s)    
        max = maximum(s[1:i - 1]) 
        if max < s[i]
            mls[i] = mls[i - 1] + 1 
        else 
            var2 = s[1:i - 1]  
            var = s[1:i - 1] #이전 숫자 까지의 리스트 새로 정의
            for j = 1:length(var)
                max2 = maximum(var)
                println("var is :", var)
                println("var2 is : ", var2)
                println("max2 is  :", max2)
                println("mls is :", mls)
                #println("findnext(var2, max2) :", findnext(var2, max2))
                #println(mls[findnext(var2, max2)] )
                if max2 > s[i]
                    deleteat!(var, var .== max2)
                    continue
                # max2 의 index 를 찾아야 함. 
                
                #try 
                #    num = mls[findnext(var2, max2)]
                #catch
                #    num = 
                #end
                # 오류가 난 이유는 var2 에 ma2가 두개 있을 경우 마지막 index를 반환하기 때문. 첫 인덱스를 어떻게 반환? 
                find(a -> a == max2, var2)
                elseif mls[getindex(var2, max2)] + 1 > mls[i - 1]
                    mls[i] = mls[i - 1] + 1   
                    break
                else
                    deleteat!(var, var .== max2)
                    #pop!(var, max2)
                    mls[i] = mls[i - 1]
                end
            end
        end
        #else
         #   mls[i] = mls[i-1]


    end    
    return maximum(mls) # Returnerer det største tallet i listen
end


### Tester ###
# Disse testene blir kjør når du kjører filen
# Du trenger ikke å endre noe her, men du kan eksperimentere!

printstyled("\n\n\n---------------\nKjører tester!!\n---------------\n"; color = :magenta)

using Test
@testset "Tester" begin
   	@test lislength([5,3,3,6,7]) == 3
	#@test lislength([2,2,2,2]) == 1
	#@test lislength([100,50,25,10]) == 1
	#@test lislength([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]) == 6
	#@test lislength([682, 52, 230, 441, 1000, 22, 678, 695, 0, 681]) == 5
	#@test lislength([441, 1000, 22, 678, 695, 0, 681, 956, 48, 587, 604, 857, 689, 346, 425, 513, 476, 917, 114, 43, 327, 172, 162, 76, 91, 869, 549, 883, 679, 812, 747, 862, 228, 368, 774, 838, 107, 738, 717, 25, 937, 927, 145, 44, 634, 557, 850, 965]) == 12
end

println("\nFungerte alt? Prøv å kjør koden i inginious!")
println("Husk at disse testene ikke alltid sjekker alle edge-cases")
println("---------------------------------------------------------\n\n")