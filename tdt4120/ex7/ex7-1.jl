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



### Tester ###
# Disse testene blir kjørt når du kjører filen
# Du trenger ikke å endre noe her, men du kan eksperimentere!

printstyled("\n\n\n---------------\nKjører tester\n---------------\n"; color = :magenta)

using Test
@testset "Tester" begin
  @test usegreed([20, 10, 5, 1]) == true
  @test usegreed([20, 15, 10, 5, 1]) == false
  @test usegreed([100, 1]) == true
  @test usegreed([5, 4, 3, 2, 1]) == false
  @test usegreed([1]) == true

end

println("\nFungerte alt? Prøv å kjør koden i inginious!")
println("Husk at disse testene ikke alltid sjekker alle edge-cases")
println("---------------------------------------------------------\n\n")

