import sys
import re


class Dialogue(object):
    def __init__(self, character, msg, isRoll=False, success=None):
        self.character = character
        self.msg = msg
        self.isRoll = isRoll
        self.success = success

    def __repr__(self):
        repr_str = ''
        repr_str += self.character + ': '
        if self.isRoll:
            repr_str += '<roll> '
            if self.success:
                repr_str += '(√) '
            else:
                repr_str += '(x) '
        repr_str += self.msg
        return repr_str

    def __str__(self):
        return f'{self.character}: {self.msg}'


def main():
    argv = sys.argv
    if len(argv) > 1:  # Designated file path
        try:
            log_file = open(argv[1])
        except FileNotFoundError:
            log_file = open('./log.txt', encoding='utf-8')
    else:
        log_file = open('./log.txt', encoding='utf-8')

    dialog_list = raw2py(log_file)
    print(''.join(str(dialog_list)))


def raw2py(raw_fh):
    all_dialogues = []
    line_no = 0
    while True:
        isRolling = False
        success = None
        infoline = raw_fh.readline()
        msgline = raw_fh.readline()
        line_no += 2

        if not msgline:  # EOF
            break
        elif not msgline.startswith('    '):
            print(f'Warning: Line number {line_no} does not start with an indent. Please check if it is really a msgline')
            print('Line:', msgline)
        elif msgline.startswith('    .r'):  # Rolling dice
            infoline = raw_fh.readline()
            msgline = raw_fh.readline()
            line_no += 2
            isRolling = True
            if '成功' in msgline:
                success = True
            elif '失败' in msgline:
                success = False
        character = infoline[:re.search('\s\d\d\d\d/\d\d/\d\d', infoline).span()[0]]
        msg = msgline.replace('    ', '').replace('\n', '')
        all_dialogues.append(Dialogue(character, msg, isRoll=isRolling, success=success))

    return all_dialogues


if __name__ == '__main__':
    main()
