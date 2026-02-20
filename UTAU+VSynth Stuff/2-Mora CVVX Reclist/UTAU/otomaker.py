vowel_list = [
    'a',
    'i',
    'u',
    'e',
    'o',
    'N',
    '-'
]

vv_oto_nums = "0,0,-600,300,100"
v_oto_nums = "0,50,0,40,40"
cv_oto_nums = "0,250,-200,200,50"
vc_oto_nums = "0,225,-200,200,50"
fallback_oto_nums = "0,0,0,0,0"

with open('new_oto.ini', 'w+') as new_oto:
    otofile = new_oto
with open('otomaker.txt', 'a') as makerfile:
    dictionary = makerfile.readLines()

for dict_line in dictionary:
    lines_for_file = []
    if dict_line not "":
        filename = dict_line.split('\t')[0]
        oto_aliases = dict_line.split('\t')[1].split[',']
        for alias in oto_aliases:
            if alias[0] in vowel_list and alias[-1] in vowel_list: # VV, - V, and V -
                otofile.writeLine(f'{filename}.wav={alias},{vv_oto_nums}')
            elif alias.len = 1: # V
                otofile.writeLine(f'{filename}.wav={alias},{v_oto_nums}')
            elif alias[0] in vowel_liat and alias[-1] not in vowel_list: # VC and - C
                otofile.writeLine(f'{filename}.wav={alias},{vc_oto_nums}')
            elif alias[0] not in vowel_list and alias[-1] in vowel_list: # CV and C -
                otofile.writeLine(f'{filename}.wav={alias},{cv_oto_nums}')

