#!/usr/bin/env python
#-*- coding:utf8 -*-
u"""
封装pymongodb 的操作
https://docs.mongodb.com/manual/tutorial/query-documents/
https://api.mongodb.com/python/current/
"""
import pymongo
from db.mongodb.pymongo import settings


class PyMongoClient(object):
    u"""
    pymongo client
    """
    _client = pymongo.MongoClient(settings.MONGO_URI)

    def __init__(self, database, collections):
        self._collection = self._client[database][collections]

    def get_collections(self):
        return self._collection

    def find_all_collections(self):
        u"""
        查看mongodb该db下的所有collection
        :return:
        """
        return self._collection.collection_names(
            include_system_collections=False)

    def add(self, document_map):
        u"""
        添加一个文档操作
        :param document_map:
        :return:
        """
        return self._collection.insert_one(document_map).inserted_id

    def batch_add(self, document_list):
        u"""
        批量添加
        :param document_list:
        :return:
        """
        if not isinstance(document_list, list):
            raise Exception("document_list should be list type")
        return self._collection.insert_many(document_list).inserted_ids

    def update_one(self, filter, document_map):
        u"""
        更新一条数据
        :param condition:
        :param document_map:
        :return:
        """
        # upsert：True表示如果不存在则执行insert操作,默认设置不做insert操作
        return self._collection.\
            update_one(filter, document_map, upsert=False).modified_count

    def replace_one(self, source_map, dist_map):
        u"""
        :param source_map:  更新条件
        :param dist_map:    根据条件进行替换
        :return:
        """
        return self._collection.replace_one(source_map, dist_map).modified_count

    def update_many(self, filter, document_map):
        u"""
        更新多条数据
        :param filter:
        :param document_map:
        :return:
        """
        return self._collection.\
            update_many(filter, document_map, upsert=False).modified_count

    def delete_one(self, condition):
        u"""
        根据条件查询并删除一条数据
        :param condition:
        :return:
        """
        return self._collection.delete_one(condition).deleted_count

    def delete_many(self, condition):
        u"""
        根据条件删除数据
        :param condition:
        :return:
        """
        return self._collection.delete_many(condition).deleted_count

    def query_by_id(self, _id, keys=[]):
        u"""
        根据mongodb的查询指定的keys数据
        :param _id:ObjectId
        :param keys:
        :return:
        """
        if keys:
            _search_keys = {}
            for key in keys:
                _search_keys[key] = 1
            return self._collection.find_one({"_id": _id},
                                             _search_keys)
        return self._collection.find_one({"_id": _id})

    def query_one(self, filed, value):
        u"""
        根据指定的field查询mongodb中一条数据
        :param filed:
        :param value:
        :return:
        """
        return self._collection.find_one({filed: value})

    def query_sort_limit(self, condition, sorted={}, offset=None, size=None):
        u"""
        根据查询排序分页查询数据
        :param condition:{f1:v1, f2:v2, f3:v3},查询条件这些都是f1 = v1
        :param sorted:{f1:1,f2:-1}，1表示顺序排序，-1表示倒序排序
        :param offset:分页,从第offset条记录开始查询
        :param size:分页显示的大小
        :return:
        """
        _sorted_list = []
        if sorted:
            for key, value in sorted.items():
                if value == 1:
                    _sorted_list.append({key, pymongo.ASCENDING})
                elif value == -1:
                    _sorted_list.append({key, pymongo.DESCENDING})
        if offset is not None and size is not None:
            if offset < 0 or size < 0:
                raise Exception("pass the offset and size is not invalidated,"
                                "the offset[%d],the size[%d]" % (offset, size))
            _result = self._collection.find(condition).sort(_sorted_list).\
                skip(offset).limit(size)
        else:
            _result = self._collection.find(condition).sort(_sorted_list)
        if _result:
            return list(_result)
        return []

    def query_by_conditions(self, condition):
        u"""
        根据条件查询
        :param condition:{f1:v1, f2:v2, f3:v3},查询条件这些都是f1 = v1
        :return:
        """
        return self.query_sort_limit(condition)

    def query_by_sort(self, condition, sorted={}):
        u"""
        根据条件并按照指定的顺序排序输出
        :param condition:{f1:v1, f2:v2, f3:v3},查询条件这些都是f1 = v1
        :param sorted:
        :return:
        """
        return self.query_sort_limit(condition, sorted)

    def query_counter(self, condition):
        u"""
        根据条件查询记录个数
        :param condition:查询条件,{f1:v1, f2:v2, f3:v3},查询条件这些都是f1 = v1
        :return:
        """
        return self._collection.find(condition).count()

    def create_index(self, keys={}, **kwargs):
        u"""
        创建一个索引,一个索引下可以有多个key
        :param index_fileds:{f1: idx_policy, ...}
        :return:
        """
        if not keys:
            raise Exception("have not any fields to create index")
        _index_list = []
        for key, policy in keys.items():
            if not isinstance(key, str):
                raise Exception("the key[%s] must be str type" % str(key))
            if policy not in (pymongo.DESCENDING,
                              pymongo.ASCENDING,
                              pymongo.GEO2D,
                              pymongo.GEOHAYSTACK,
                              pymongo.GEOSPHERE,
                              pymongo.HASHED,
                              pymongo.TEXT):
                raise Exception("the index policy type is error")
            _index_list.append({key, policy})
        if kwargs:
            for key, value in kwargs.items():
                if key not in ["name", "unique", "sparse", "bucketSize",
                               "min", "max", "expireAfterSeconds",
                               "partialFilterExpression", "collation"]:
                    raise Exception("the key name is not invalidated .")
        self._collection.create_index(_index_list, **kwargs)

    def show_index_information(self):
        return self._collection.index_information()

    def create_indexes(self, mutil_indexes):
        u"""
        创建多个索引数据
        :param mutil_indexes:
        :return:
        """
        if not isinstance(mutil_indexes, dict):
            raise Exception("mutil_indexes should be dict instance ..")
        _index_items = []
        for index_name, index_keys in mutil_indexes:
            if not isinstance(index_keys, dict):
                raise Exception("the index is not dict instance ")
            _index_keys = []
            for key, policy in index_keys.items():
                if not isinstance(key, str):
                    raise Exception("the key should be str type")
                if policy not in (pymongo.DESCENDING,
                                  pymongo.ASCENDING,
                                  pymongo.GEO2D,
                                  pymongo.GEOHAYSTACK,
                                  pymongo.GEOSPHERE,
                                  pymongo.HASHED,
                                  pymongo.TEXT):
                    raise Exception("the index policy type is error")
                _index_keys.append({key, policy})
            _item = pymongo.IndexModel(_index_keys, name=index_name)
            _index_items.append(_item)
        self._collection.create_indexes(_index_items)

    def query_by_null_fields(self, fields=[]):
        if not fields:
            _query_comdition = {}
            for fileld in fields:
                _query_comdition[fileld] = "NONE"
            return self._collection.find(_query_comdition)

    def get_field_exist(self, filed):
        u"""
        查询当前field字段在document中存在的数据
        :param filed:
        :return:
        """
        return self._collection.find({filed, {"$exist": True}})

    def get_filed_not_exist(self, filed):
        u"""
        查询当前field字段不在document中的数据
        :param filed:
        :return:
        """
        return self._collection.find(filed, {"$exist": False})