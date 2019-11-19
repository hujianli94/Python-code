#!/usr/bin/env python
# -*- coding:utf8 -*-
import csv

# with open("some.csv",'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['Column1', 'Column2', 'Column3'])      #写单行
#     writer.writerows([range(3) for i in range(5)])          #写多行，列表套列表


# villains = [['Doctor', 'No'],
#     ['Rosa','Klebb'],
#     ['Mister','Big'],
#     ['Auric','Goldfinger'],
#     ['Ernst','Blofeld'],
# ]
# with open('villains','wt') as fout:
#     csvout = csv.writer(fout)
#     csvout.writerows(villains)


# import csv
# villains = [
# {'first': 'Doctor', 'last': 'No'},
# {'first': 'Rosa', 'last': 'Klebb'},
# {'first': 'Mister', 'last': 'Big'},
# {'first': 'Auric', 'last': 'Goldfinger'},
# {'first': 'Ernst', 'last': 'Blofeld'},
# ]
# with open('villains1', 'wt') as fout:
#     cout = csv.DictWriter(fout, ['first', 'last'])
#     cout.writeheader()
#     cout.writerows(villains)


with open("villains", "r", encoding="gbk") as f:
    reader = csv.reader(f)
    with open("villains_bak", "w", newline="", encoding="gbk") as wf:
        writer = csv.writer(wf,delimiter='\t')
        for row in reader:
            print("|".join(row))
            writer.writerow(row)
