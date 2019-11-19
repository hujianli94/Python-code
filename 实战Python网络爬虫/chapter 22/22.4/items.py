import scrapy
#Product类继承自Item类
class Product(scrapy.Item): 
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
	# last_updated指明了该字段的序列化函数
    last_updated = scrapy.Field(serializer=str)

if __name__=="__main__":
	# 数据存储一
	product = Product(name='Desktop PC',price=1000)
	print (product)
	# 数据存储二
	item = Product()
	item['name'] = 'Mac'
	item['price'] = 2000
	print(item)
	# 读取数据内容一，若不存在会输出None
	print(item.get('name', 'None'))
	print(item.get('stock', 'None'))
	# 读取数据内容二，使用该方法读取，若不存在会提示keyerror
	print(item['name'])
	# print(item['stock'])
	# 判断是否存在字段，输出True，False
	print('name' in item)
	print('stock' in item)
	# 获取键值对
	print(item.keys())
	print(item.items())