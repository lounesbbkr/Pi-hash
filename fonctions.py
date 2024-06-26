import json

def get_characters(number):
    with open('dictionary.json', 'r') as f:
        data = json.load(f)
    return data.get(str(number), None)

def calculate_ascii_sum(text):
    ascii_sum = 0
    for char in text:
        ascii_sum += ord(char)
    return ascii_sum

def convert_bit_to_hex(bit_string):
    decimal_sequence = []
    for i in range(0, len(bit_string), 8):
        binary_char = bit_string[i:i+8]
        decimal_number = int(binary_char, 2)
        decimal_sequence.append(decimal_number)
    
    hex_sequence = ""
    for decimal_number in decimal_sequence:
        hex_char = hex(decimal_number)[2:].zfill(2)
        hex_sequence += hex_char
    
    return hex_sequence[:64]  

def convert_integer(integer): 
    character_sequence = str(integer) 
    return ''.join(character_sequence)

def md_compres(text, key):
    # Convert text and key to binary strings
    text_binary = ''.join(format(ord(c), '08b') for c in text)
    key_binary = ''.join(format(ord(c), '08b') for c in key)

    # Calculer le nombre de zéros de remplissage nécessaires
    padding_zeros = (len(key_binary) - len(text_binary) % len(key_binary)) % len(key_binary)

    # Ajouter les zéros de remplissage au texte
    text_binary += '0' * padding_zeros

    # Diviser le texte en blocs de la taille de la clé
    blocks = [text_binary[i:i+len(key_binary)] for i in range(0, len(text_binary), len(key_binary))]

    # Effectuer le XOR entre les blocs 
    result = ""
    for i in range(len(blocks)):
        block_xor = ""
        for j in range(len(blocks[i])):
            block_xor += str(int(blocks[i][j]) ^ int(key_binary[(j + i) % len(key_binary)]))
        result += block_xor

    # Pad the result to a length of 256 bits
    result = result[:256].ljust(256, '0')

    return result

def get_next_32_numbers(sequence):
    def read_sequence_from_file(filename):
        try:
            with open(filename, 'r') as file:
                for line in file:
                    yield line.strip()
        except FileNotFoundError:
            print("File not found.")
            yield ""

    def find_sequence_in_file(user_sequence, filename):
        user_sequence = ''.join(user_sequence)  # Convert list to string
        while user_sequence:
            for file_sequence in read_sequence_from_file(filename):
                if not file_sequence:
                    return None
                if user_sequence in file_sequence:
                    index = file_sequence.index(user_sequence)
                    sequence_end = index + len(user_sequence)
                    next_32_numbers = file_sequence[sequence_end:sequence_end + 32]
                    return next_32_numbers
            user_sequence = user_sequence[:-1]  # Remove the last character

        return None

    filename = "pi.txt"
    next_32_numbers = find_sequence_in_file(sequence, filename)
    return next_32_numbers



def next_generation(bit_string):
    next_bit_string = ""
    length = len(bit_string)

    for i in range(length):
        # Determine the range of neighbors
        left_range = max(0, i - 3)
        right_range = min(length, i + 4)

        # Count the number of live neighbors
        if i == 0:
            live_neighbors = bit_string[-3:] + bit_string[i+1:right_range]
        elif i == length - 1:
            live_neighbors = bit_string[left_range:i] + bit_string[:3]
        else:
            live_neighbors = bit_string[left_range:i] + bit_string[i+1:right_range]

        live_count = live_neighbors.count('1')

        # Apply rules
        if bit_string[i] == '0' and live_count < 1:
            next_bit_string += '1'
        elif bit_string[i] == '1' and live_count > 4:
            next_bit_string += '0'
        else:
            next_bit_string += bit_string[i]

    return next_bit_string


def convert_text_to_bits(text):
    bit_string = ""
    for char in text:
        ascii_value = ord(char)
        binary_value = format(ascii_value, '08b')
        bit_string += binary_value
    return bit_string