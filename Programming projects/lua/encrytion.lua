LETTERS = "abcdefghijklmnopqrstuvwxyz"
KEY = "turnip"

function encrypt(msg)
    local i = 0
    local encrypted_msg = ""

    for letter in msg:gmatch(".") do
        if string.find(LETTERS, letter) then
            local letter_index = string.find(LETTERS, letter) - 1
            local key_index = string.find(LETTERS, KEY[(i % #KEY) + 1]) - 1
            encrypted_msg = encrypted_msg .. LETTERS[((letter_index + key_index) % 26) + 1]
        else
            encrypted_msg = encrypted_msg .. letter
        end
        i = i + 1
    end

    return encrypted_msg
end

function decrypt(msg)
    local i = 0
    local decrypted_msg = ""

    for letter in msg:gmatch(".") do
        if string.find(LETTERS, letter) then
            local letter_index = string.find(LETTERS, letter) - 1
            local key_index = string.find(LETTERS, KEY[(i % #KEY) + 1]) - 1
            decrypted_msg = decrypted_msg .. LETTERS[((letter_index - key_index) % 26) + 1]
        else
            decrypted_msg = decrypted_msg .. letter
        end
        i = i + 1
    end

    return decrypted_msg
end

print(encrypt("Hello, world"))
