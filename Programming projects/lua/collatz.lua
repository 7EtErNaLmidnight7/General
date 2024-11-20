function collatz(num) -- This does the collatz conjecture.
    i = 0
    numbers = {
        [i] = num
    }

    while num ~= 1 do
        if num % 2 == 0 then num = num // 2
        else num = num * 3 + 1 end

        local i = i + 1
        numbers[i] = num
    
    print(numbers)

    end
end

collatz(27)
-- Pretty cool language, similar to python, but faster + less keywords :)