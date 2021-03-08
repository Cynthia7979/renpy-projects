from sys import argv


def main():
    globals()['log_enabled'] = True

    if len(argv) >= 3:
        renpy, output = argv[1], argv[2]
    else:
        renpy, output = "./script.rpy", "朗读女.txt"

    script = open(renpy, 'r', encoding='utf-8')
    langdunv = open(output, 'w', encoding='utf-8')

    predefined_characters = []
    all_characters = set()
    # Start reading file
    for line in script.readlines():
        # Read predefined characters
        if line.startswith('define ') and slice_between(line, '= ', '(') == 'Character':
            character_name = slice_between(line, 'define ', ' =')
            predefined_characters.append(character_name)

        # Read lines
        if line.startswith('    ') and '"' in line:
            character_seg = slice_between(line, '    ', ' "', rfind=True)
            if '"' in character_seg:
                character_name = slice_between(character_seg, '"', '"', rfind=True)
            else:
                character_name = character_seg
                if character_name not in predefined_characters:  # Nonexistent character
                    log(f'Warning: Ignoring nonexistent character "{character_name}" and their dialogue.')
                    continue
            log('Character:', character_name)
            all_characters.add(character_name)

            # Get dialogue
            dialogue = slice_between(line, f'    {character_seg} "', '"', rfind=True)
            dialogue = dialogue.strip('\\')
            log('Dialogue:', dialogue)
            if not should_pass(dialogue):
                # Write character tag
                langdunv.write(f'[{character_name}]\n')
                # Write dialogue
                langdunv.write(dialogue)
                langdunv.write('\n\n')
            else:
                log('Dialogue passed.')
    log('-------')
    log('Characters:')
    for name in all_characters:
        log('    '+name)
    log('-------\nDone.')


def slice_between(s, start=None, end=None, rfind=False):
    if not start: start = s[0]
    if not end: end = s[-1]
    if rfind:
        return s[s.find(start)+len(start):s.rfind(end)]
    else:
        return s[s.find(start) + len(start):s.find(end)]


def should_pass(dialogue):
    pass_keywords = ('SAN CHECK', '检定', '成功', '失败', '1d100 =', )
    for kw in pass_keywords:
        if kw in dialogue:
            return True
    return False


def log(*args):
    if globals()['log_enabled']:
        print(*args)


if __name__ == '__main__':
    main()
