class TIMIT_Constants:
    vowels: list[str] = ['iy', 'ih', 'eh', 'ey', 'ae',
                         'uw', 'uh', 'ow', 'ao', 'aa', 'ax', 'ah', 'er']
    # ['iy', 'ih', 'eh', 'ey', 'ae', 'aa', 'aw', 'ay', 'ah',
    # 'ao', 'oy', 'ow', 'uh', 'uw', 'ux', 'er', 'ax', 'ix', 'axr', 'ax-h']
    # Quick note about the vowels list, `aa` refers to `/a/` whereas `ao` refers to /ɔ/, `ax` refers to /ə/
    liquids_and_glides: list[str] = ['l', 'r', 'w', 'y']

    semivowels: list[str] = ['hh']  # ['hh', 'hv', 'el']

    nasals: list[str] = ['m', 'n', 'ng']

    fricatives: list[str] = ['s', 'sh',  'z', 'zh', 'f',  'v', 'th', 'dh']
    # Note: `zh` refers to `/ʒ/` and `dh` refers to `/ð/`

    stops: list[str] = ['b', 'd', 'g', 'p', 't', 'k']

    def getCommonSegments() -> list[str]:
        common_segs: list[str] = TIMIT_Constants.vowels + TIMIT_Constants.liquids_and_glides + \
            TIMIT_Constants.semivowels + TIMIT_Constants.nasals + \
            TIMIT_Constants.fricatives + TIMIT_Constants.stops
        return common_segs
