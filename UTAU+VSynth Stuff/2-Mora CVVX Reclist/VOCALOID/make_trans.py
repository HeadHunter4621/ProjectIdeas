info_lines = []

with open("info.txt", "r") as info_file:
    info_lines = info_file.readlines()

final_list = []

for line in info_lines:
    filename = line.split("\t")[0]
    transcription = line.split("\t")[1]
    old_phonemes = line.split("\t")[2].split("]")
    new_phonemes = []
    for phoneme in old_phonemes:
        print(f"old: {phoneme}")
        if phoneme != "\n":
            phoneme = phoneme.replace("[", "").replace("]", "")
            phoneme = "[" + phoneme + "]"
            new_phonemes.append(phoneme.replace("[ ", "["))
            print(f"new: {phoneme}")
    with open(f"./trans/{filename}.trans", "w+") as file:
        file.write(f"{transcription}\n")
        for phoneme in new_phonemes:
            file.write(f"{phoneme}\n")
