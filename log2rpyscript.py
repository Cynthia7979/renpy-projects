import sys
import re
import random


class Dialogue(object):
    def __init__(self, character, msg, isRoll=False, status=None):
        self.character = character
        self.msg = msg
        self.isRoll = isRoll
        self.status = status

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

    @property
    def success(self):
        return self.status in ('成功', '大成功')

    # def __str__(self):
    #     return f'{self.character}: {self.msg}'


class Log(object):
    def __init__(self, dialogue_list=()):
        self.log = list(dialogue_list)
        self.characters = {}  # 全名：变量名

        if dialogue_list:
            for dialogue in dialogue_list:
                self._add_character(dialogue.character)

    def add_dialogue(self, dialogue: Dialogue):
        self.log.append(dialogue)
        self._add_character(dialogue.character)

    def _add_character(self, character):
        if character not in self.characters.keys():
            self.characters[character] = ''.join(list(filter(lambda s: s not in (' ',), character))).lower()  # 全部小写当变量名

    @property
    def nickname(self):
        return self.characters  # Syntax sugar

    def __repr__(self):
        return str(list(self.characters.keys())) + '\n'.join([str(d) for d in self.log])

    def __iter__(self):
        return iter(self.log)


def main():
    argv = sys.argv
    if len(argv) > 1:  # Designated file path
        try:
            log_file = open(argv[1])
        except FileNotFoundError:
            log_file = open('./log.txt', encoding='utf-8')
    else:
        log_file = open('./log.txt', encoding='utf-8')

    generated_log_obj = raw2Log(log_file)
    Log2rpy(generated_log_obj)
    Log2LangDuNv(generated_log_obj)


def raw2Log(raw_fh):
    all_dialogues = Log()
    line_no = 0
    while True:
        isRolling = False
        status = None
        infoline = raw_fh.readline()
        msgline = raw_fh.readline()
        line_no += 2

        if not msgline:  # EOF
            break
        elif not msgline.startswith('    '):
            print(f'Warning: Line number {line_no} does not start with an indent. Please check if it is really a msgline')
            print('Line:', msgline)
        elif msgline.startswith('    .r') or msgline.startswith('    .sc'):  # Rolling dice
            infoline = raw_fh.readline()
            msgline = raw_fh.readline()
            line_no += 2
            isRolling = True
            if '大成功' in msgline:
                status = '大成功'
            elif '成功' in msgline:
                status = '成功'
            elif '大失败' in msgline:
                status = '大失败'
            elif '失败' in msgline:
                status = '失败'
        character = infoline[:re.search('\s\d\d\d\d/\d\d/\d\d', infoline).span()[0]]
        msg = msgline.replace('    ', '').replace('\n', '')
        all_dialogues.add_dialogue(
            Dialogue(character, msg, isRoll=isRolling, status=status)
        )

    return all_dialogues


def Log2rpy(log: Log, filename='script.rpy'):
    rpy_file = open(filename, 'wb')
    buffer = ''

    # 初始化人物变量
    for character in log.characters.keys():
        color = '#%02x%02x%02x' % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # TODO 防止重复？
        buffer += f'define {log.nickname[character]} = Character("{character}", color="{color}")\n'

    # 初始化显示
    buffer += """default preferences.afm_enable = True
default preferences.afm_after_click = True

label start:
"""

    last_character = None

    for dlg in log:
        if dlg.character != last_character:
            buffer += f'    hide {log.nickname[last_character]}\n' if last_character is not None else '    scene bg\n'
            buffer += f'    show {log.nickname[dlg.character]} at left\n'

        if dlg.isRoll:
            buffer += '    play sound "roll.mp3"\n'
            if dlg.status == '大成功':
                buffer += '    queue sound "bigsuccess.mp3"\n'
            elif dlg.status == '成功':
                buffer += '    queue sound "success.mp3"\n'
            elif dlg.status == '大失败':
                buffer += '    queue sound "bigfail.mp3"\n'
            elif dlg.status == '失败':
                buffer += '    queue sound "fail.mp3"\n'

        escaped_msg = dlg.msg.replace('\\', '\\\\') \
            .replace('"', '\\"')\
            .replace("'", "\\'")\
            .replace(' ', '\\ ')
        buffer += f'    {log.nickname[dlg.character]} "{escaped_msg}"\n'

        last_character = dlg.character

    rpy_file.write(buffer.encode('utf-8', errors='python-strict'))

    return rpy_file


def Log2LangDuNv(log: Log):
    ldn_file = open('朗读女.txt', 'w', encoding='utf-8')
    for dlg in log:
        if not dlg.isRoll:
            ldn_file.write(f'[{dlg.character}]\n{dlg.msg}\n\n')
    return ldn_file


if __name__ == '__main__':
    main()
