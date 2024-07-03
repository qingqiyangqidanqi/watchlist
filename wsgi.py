# 在部署程序时，我们不会使用 Flask 内置的开发服务器运行程序，因此，对于写到 .env 文件的环境变量，我们需要手动使用 python-dotenv 导入。下面在项目根目录创建一个 wsgi.py
# 脚本，在这个脚本中加载环境变量，并导入程序实例以供部署时使用：
#
# wsgi.py：手动设置环境变量并导入程序实例

import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

from watchlist import app
