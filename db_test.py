from watchlist.app import db, User, Movie  # 导入模型类


def create():
    # 创建
    user = User(name='Grey Li')  # 创建一个 User 记录
    m1 = Movie(title='Leon', year='1994')  # 创建一个 Movie 记录
    m2 = Movie(title='Mahjong', year='1996')  # 再创建一个 Movie 记录
    db.session.add(user)  # 把新创建的记录添加到数据库会话
    db.session.add(m1)
    db.session.add(m2)
    db.session.commit()  # 提交数据库会话，只需要在最后调用一次即可


def query():
    # 读取 查询语句：<模型类>.query.<过滤方法（可选）>.<查询方法>
    movie = Movie.query.first()  # 获取 Movie 模型的第一个记录（返回模型类实例）
    print(movie.title)  # 对返回的模型类实例调用属性即可获取记录的各字段数据
    print(movie.year)
    print(Movie.query.all())  # 获取 Movie 模型的所有记录，返回包含多个模型类实例的列表
    print(Movie.query.count())  # 获取 Movie 模型所有记录的数量
    print(Movie.query.get(1))  # 获取主键值为 1 的记录
    print(Movie.query.filter_by(title='Mahjong').first())  # 获取 title 字段值为 Mahjong 的记录
    print(Movie.query.filter(Movie.title == 'Mahjong').first())  # 等同于上面的查询，但使用不同的过滤方法


def updata():
    # 下面的操作更新了 Movie 模型中主键为 2 的记录
    movie = Movie.query.get(2)
    movie.title = 'WALL-E'
    movie.year = '2008'
    db.session.commit()

def delete():
    # 下面的操作删除了 Movie 模型中主键为 1 的记录
    movie = Movie.query.get(1)
    db.session.delete(movie)
    db.session.commit()

if __name__ == '__main__':
    pass
