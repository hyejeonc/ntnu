function usegreed(coins)
    # din kode her
    # 그리디 알고리즘으로 풀었을 때랑, 
    # 실제 최적화 문제와 해결하는 답이 다른 경우 > 거짓
    # 그리디 알고리즘으로 가능 한 경우 > 참 
    result = true
    for i in 1:length(coins)-1
        if coins[i] % coins[i+1] != 0
            result = false
        end
    end
    return result
end

function mincoinsgreedy(coins, value)
    # din kode her
    sum = 0
    #value = value2
    for i in 1:length(coins)
        println("i th iteration, and value ", i, " and ", value, " and sum ", sum)
        sum += fld(value, coins[i]) # 몫을 구한 후 몫을 더한다. 
        if rem(value, coins[i]) == 0 # 만약 나누어 떨어질 경우 
            break # 반복을 멈춘다. 
        else
            value = value % coins[i] # rem 함수와 같다 
            # 0으로 나눠 떨어지지 않을 때는 나머지를 새로 value 에 넣는다 
        end  
    end
    return sum
end

### Tester ###
# Disse testene blir kjørt når du kjører filen
# Du trenger ikke å endre noe her, men du kan eksperimentere!

printstyled("\n\n\n---------------\nKjører tester\n---------------\n"; color = :magenta)

using Test
@testset "Tester" begin
  @test mincoinsgreedy([1000,500,100,20,5,1],1226) == 6
  @test mincoinsgreedy([20,10,5,1],99) == 10
  @test mincoinsgreedy([5,1],133) == 29
end

println("\nFungerte alt? Prøv å kjør koden i inginious!")
println("Husk at disse testene ikke alltid sjekker alle edge-cases")
println("---------------------------------------------------------\n\n")

