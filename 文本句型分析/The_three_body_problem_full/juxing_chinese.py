import re
import random
import jieba

with open('The_three_body_problem_full.txt', 'r', encoding='GB18030') as f:
    doc = f.read().replace('\n', '')
sentences = re.split('(。|！|\!|\.|？|\?)', doc)  # 保留分割符

new_sents = []
num = 0
l_label = []
for i in range(int(len(sentences) / 2)):
    if random.random() > 0.5 and sentences[2 * i].strip() != '':
        num += 1
        sent = sentences[2 * i].strip() + sentences[2 * i + 1]
        new_sents.append(sent)
        l_word = jieba.cut(sent)
        if '把' in l_word:
            l_label.append('把字句')
        elif '被' in l_word:
            l_label.append('被字句')
        elif sentences[2 * i + 1] in ['!', '！']:
            l_label.append('陈述句')
        elif sentences[2 * i + 1] in ['？', '?']:
            l_label.append('疑问句')
        else:
            l_label.append('陈述句')

        if num == 5000:
            break
with open('The_three_body_problem_juxing.txt', 'w', encoding='utf-8') as f:
    for sent, label in zip(new_sents, l_label):
        f.write('{}\t{}\n'.format(sent, label))


