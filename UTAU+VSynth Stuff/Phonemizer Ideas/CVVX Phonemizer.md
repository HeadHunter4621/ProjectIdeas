# CVVX Phonemizer (Primarily JA)

Automatically converts CV phonemes (or whatever the lyric is) to a CV and VC/VV phoneme (similar to DeepVocal's method of this)

Uses a config file (probably a YAML, but I don't know how it would be configured. Could be comma-seperated INI file as well?) with phonemes, related V's, related C's, and replacements

config.ini is split into 6 sections. 
* Consonants
  * List of all consonant phonemes used
* Vowels
  * List of all vowel phonemes available in voicebank
* Phonemes
  * List of per-note lyric inputs as [Input]=[Consonant],[Vowel]
    * Consonant and Vowel must be in their respective lists, otherwise an error is thrown (or something, Kona will make a python script to check configs)
  * Output CV+VXs are constructed from these files, with the vowel taken from the previous note's vowel (if no preceding note, it is "-",), and the current note's consonant
* Standalone
  * Aliases that are passed to the resampler on their own, without phonemization.
* Endings
  * VX phonemes where the X is silence. These lyrics are entered as just the `X` part.
* Replacements
  * Phonemes that are replaced (`from=to`), processed in the same way as ARPAsing phonemizers do (maybe? ideally it would be the same, I think)

## Behavior

1. User inputs "[ka][sa]" as lyrics (notes are in brackets)
2. Phonemizer splits these into seperate phonemes ('ka' and 'sa').
3. Phonemization
  a. First, it does "a". It sees that there isn't a preceding note and inserts the [- C] phoneme,in this case "- k". This doesn't exist in this voicebank's oto.ini, so it is skipped and no phoneme is placed (treated the same way as the CVVC+VCV phonemizer I think?)
  b. Then, it inputs "ka", as that is the phoneme that was entered
  c. Next, it sees that tne next consonant is "s", and that "ka"'s vowel is "a", placing the VX phoneme "a s". It then checks the "replacements" section and replaces "a s" with "a2 s" 
  d. Then it places "sa" because that is the phoneme that was entered
  e. Then it sees that "sa"'s vowel is "a" and the next note is silence, so it places the default end phoneme ("-")
4. Outputted phonemes: `[- k](Skipped) [ka] [a2 s](replaced from [a s]) [sa] [a -]`

## Things I don't know

* I am unsure how Hiragana support would work. I think that the best way to do this is to have a `dict.ini` or something which just has lines like `kana=romaji`, but I am unsure about that.
* I also don't know how this would be done properly with a YAML file, as I don't really understand how YAML files are interpreted. I hope that either the `config.ini` file is satisfactory or that it is possible to make a similarly-formatted YAML file.
