import time
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import *
engine = create_engine('mysql+pymysql://root:1234@localhost/spiderdb?charset=utf8')
DBSession = sessionmaker(bind=engine)
SQLsession = DBSession()
Base = declarative_base()

# 定义数据模型，映射数据表
class table_info(Base):
    __tablename__ = 'job_info'
    id = Column(Integer(), primary_key=True)
    job_id = Column(String(100), comment='职位ID')
    company_name = Column(String(100), comment='企业名称')
    company_type = Column(String(100), comment='企业类型')
    company_scale = Column(String(100), comment='企业规模')
    company_trade = Column(String(100), comment='企业经营范围')
    company_welfare = Column(String(1000), comment='企业福利')
    job_name = Column(String(3000), comment='职位名称')
    job_pay = Column(String(100), comment='职位薪酬')
    job_years = Column(String(100), comment='工龄要求')
    job_education = Column(String(100), comment='学历要求')
    job_member = Column(String(100), comment='招聘人数')
    job_location = Column(String(3000), comment='上班地址')
    job_describe = Column(Text, comment='工作描述')
    job_date = Column(String(100), comment='发布日期')
    recruit_sources = Column(String(100), comment='招聘来源')
    log_date = Column(String(100), comment='记录日期')
# 创建数据表
Base.metadata.create_all(engine)

# 写入数据库
def insert_db(info_dict):
    temp_id = info_dict['job_id']
    # 判断是否已存在记录
    info = SQLsession.query(table_info).filter_by(job_id=temp_id).first()
	# 若存在，更新数据
    if info:
        info.job_id = info_dict.get('job_id','')
        info.company_name = info_dict.get('company_name','')
        info.company_type = info_dict.get('company_type','')
        info.company_trade = info_dict.get('company_trade', '')
        info.company_scale = info_dict.get('company_scale','')
        info.company_welfare = info_dict.get('company_welfare','')
        info.job_name = info_dict.get('job_name', '')
        info.job_pay = info_dict.get('job_pay', '')
        info.job_years = info_dict.get('job_years', '')
        info.job_education = info_dict.get('job_education', '')
        info.job_member = info_dict.get('job_member', '')
        info.job_location = info_dict.get('job_location', '')
        info.job_describe = info_dict.get('job_describe', '')
        info.recruit_sources = info_dict.get('recruit_sources', '')
        info.job_date = info_dict.get('job_date', '')
        info.log_date = time.strftime('%Y-%m-%d',time.localtime(time.time()))
	# 不存在则新增数据
    else:
        inset_data = table_info(
        job_id = info_dict.get('job_id',''),
        company_name=info_dict.get('company_name',''),
        company_type=info_dict.get('company_type',''),
        company_trade=info_dict.get('company_trade',''),
        company_scale=info_dict.get('company_scale',''),
        company_welfare=info_dict.get('company_welfare',''),
        job_name=info_dict.get('job_name', ''),
        job_pay=info_dict.get('job_pay', ''),
        job_years=info_dict.get('job_years', ''),
        job_education=info_dict.get('job_education', ''),
        job_member=info_dict.get('job_member', ''),
        job_location=info_dict.get('job_location', ''),
        job_describe=info_dict.get('job_describe', ''),
        job_date=info_dict.get('job_date', ''),
        recruit_sources=info_dict.get('recruit_sources', ''),
        log_date=time.strftime('%Y-%m-%d', time.localtime(time.time()))
        )
        SQLsession.add(inset_data)
    SQLsession.commit()



