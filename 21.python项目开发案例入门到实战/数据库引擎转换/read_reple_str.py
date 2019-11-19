#!/usr/bin/env python
# -*- coding:utf8 -*-
# auther; 18793
# Date：2019/8/13 14:36
# filename: read_reple_str.py
import re

# ENGINE=MyISAM改为 ENGINE=innodb;

import re, os, shutil

filename = "Full_backuk-2019-08-13_09_28_42.sql"


def alter(file, old_str, new_str):
    old_fname = "%s_bak.sql" % file.split('.')[0]

    with open(file, "r", encoding='utf-8', errors='ignore') as f1, open(old_fname, "w",
                                                                        encoding='utf-8',
                                                                        errors='ignore') as f2:
        for line in f1:
            f2.write(re.sub(old_str, new_str, line, re.I))

    old_path_dir = old_fname.split('-')[0]

    if not os.path.exists(old_path_dir):
        os.mkdir(old_path_dir)
        shutil.move(file, old_path_dir)
    else:
        shutil.rmtree(old_path_dir)
        os.mkdir(old_path_dir)
        shutil.move(file, old_path_dir)

    os.rename(old_fname, file)


alter(filename, "ENGINE=MyISAM", "ENGINE=InnoDB")
# alter(filename, "ENGINE=InnoDB", "ENGINE=MyISAM")
