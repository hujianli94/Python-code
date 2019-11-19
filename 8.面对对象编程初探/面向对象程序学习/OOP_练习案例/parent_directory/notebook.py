#!/usr/bin/env python
# -*- coding:utf8 -*-
import datetime

# 为所有新的备注存储下一个可用的id
last_id = 0


class Note:
    '''
    备注
    创建时间
    标签
    '''

    def __init__(self, memo, tags=''):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags


class Notebook:
    """
    笔记本类
    """

    def __init__(self):
        '''
        初始化笔记本
        '''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''创建一个新的笔记本，new一个新list'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''
        Locate the note with the given id.
        :param note_id:
        :return:
        '''
        for note in self.notes:
            if note.id == note_id:
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''
        find the note and change memo to the given value
        :param note_id:
        :param memo:
        :return:
        '''
        self._find_note(note_id).memo = memo

    def modify_tags(self, node_id, tags):
        '''
         find the note and change tags to the given value
        :param node_id:
        :param tags:
        :return:
        '''
        self._find_note(node_id).tags = tags

    def search(self, filter):
        '''
        find all notes that match the given filter string
        :param filter:
        :return:
        '''
        return [note for note in self.notes if note.match(filter)]
