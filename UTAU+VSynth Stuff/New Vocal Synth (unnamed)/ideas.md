## Ideas
Similar to DeepVocal (CV V VX) but with support for VXVs which act like VX phonemes

a i -> [-a][a][a_i][i][i_-]
a ka (CVVC) -> [-a][a][a_k][ka][a][a_-]
a sa (VCV) -> [-a][a][a_sa][a][a_-]

VCV is not looped and just overlaps into stable vowel, but is there to preserve more realistic fricatives/rhotics (not very helpful for plosives). Treated like a VX phoneme but inclides the next vowel

Feeds diffsrent OTO values to UTAU resamplers OR uses self-developed resampler that is very fast (??)

config.yaml is equivalnt to oto.ini (stores phoneme timing, aliases, pitch, etc), dict.yaml stores data about how phonemes are used by phonemizer
