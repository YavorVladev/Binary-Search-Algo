sec_message = input()
command = input()
while not command == "Decode":
    params = command.split("|")
    action = params[0]
    if action == "Move":
        num_letters = int(params[1])
        sec_message = sec_message[num_letters:] + sec_message[:num_letters]
    elif action == "Insert":
        index = int(params[1])
        value = params[2]
        sec_message = sec_message[:index] + value + sec_message[index:]
    elif action == "ChangeAll":
        substring = params[1]
        replacement = params[2]
        if substring in sec_message:
            sec_message = sec_message.replace(substring, replacement)

    command = input()
print(f"The decrypted message is: {sec_message}")