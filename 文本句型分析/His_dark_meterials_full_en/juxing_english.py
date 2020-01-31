import re
import random

with open('Pullman, Philip - His Dark Materials, Book 2.txt', 'r', encoding='GB18030') as f:
    doc = f.read().replace('\n', '')
sentences = re.split('(。|！|\!|\.|？|\?)', doc)  # 保留分割符

new_sents = []
num = 0
l_label = []
for i in range(int(len(sentences) / 2)):
    if random.random() > 0.3 and sentences[2 * i].strip() != '':
        num += 1
        sent = sentences[2 * i].strip() + sentences[2 * i + 1]
        new_sents.append(sent)
        l = sent.lower().split()
        if ('and' in l)or('or' in l)or('so' in l)or('but' in l):
            l_label.append('并列句')
        elif sentences[2 * i + 1] in ['!', '！']:
            l_label.append('陈述句')
        elif sentences[2 * i + 1] in ['？', '?']:
            l_label.append('疑问句')
        else:
            l_label.append('陈述句')

        if num == 5000:
            break
with open('Pullman, Philip - His Dark Materials, Book 2_juxing.txt', 'w', encoding='utf-8') as f:
    for sent, label in zip(new_sents, l_label):
        f.write('{}\t{}\n'.format(sent, label))


