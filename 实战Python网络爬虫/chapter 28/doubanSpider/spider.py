from pyReptile import request, dataPattern
from fields import MovieComment, MovieInfo
import time

# 基本设置
CONNECTION = 'mysql+pymysql://root:1234@localhost/spiderdb?charset=utf8mb4'
# 实例化数据存储类，定义映射类以及创建数据表
movieComment = MovieComment(CONNECTION, databaseType='SQL')
movieInfo = MovieInfo(CONNECTION, databaseType='SQL')


# 爬取电影信息
def get_movie(movieId):
    # URL以字符串格式传入
    r = request.get(movieUrl % (movieId))
    name = dataPattern.cssSelector(r['text'], 'h1 > span')[0]
    summary = dataPattern.cssSelector(r['text'], '#link-report')[0].strip()
    movieDic = dict(movieId=movieId, name=name, summary=summary)
    # 查询数据表是否已存在数据
    queryMovie = movieInfo.DBSession.query(movieInfo.table).filter_by(movieId=movieId).all()
    # 存在数据则作更新处理
    if queryMovie:
        condition = {'movieId': movieId}
        movieInfo.update(movieDic, condition)
    # 不存在就插入新的数据
    else:
        movieInfo.insert(movieDic)


# 爬取电影评论
def get_comment(movieId):
    # URL以列表格式传入
    urlList = []
    for page in range(10):
        urlList.append(commentUrl % (movieId, str(page * 20)))
    valueList = []
    responseList = request.get(urlList)
    for response in responseList:
        commentList = dataPattern.cssSelector(response['text'], 'div.comment > p > span')
        userList = dataPattern.cssSelector(response['text'], 'span.comment-info > a')
        for comment, user in zip(commentList, userList):
            valueList.append(dict(movieId=movieId, user=user, comment=comment))
    # 数据入库
    movieComment.insert(valueList)


if __name__ == '__main__':
    # 开始时间
    localTime = time.localtime(time.time())
    beginTime = time.strftime("%H:%M:%S", localTime)
    print('程序开始时间：' + beginTime)
    # 爬虫程序
    movieUrl = 'https://movie.douban.com/subject/%s/?from=showing'
    commentUrl = 'https://movie.douban.com/subject/%s/comments?start=%s&limit=20&sort=new_score&status=P'
    movieId = '3168101'
    get_movie(movieId)
    get_comment(movieId)
    # 结束时间
    localTime = time.localtime(time.time())
    endTime = time.strftime("%H:%M:%S", localTime)
    print('程序结束时间：' + endTime)
