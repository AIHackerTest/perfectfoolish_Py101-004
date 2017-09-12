~ 用于存放本周任务成果。

### 程序使用说明
在mac环境的使用说明，Windows环境的原理一样，只是使用工具有所不同

 1. 使用 [pyenv](https://github.com/pyenv/pyenv) 进行 Python 版本管理，也可使用其他工具来提供 Python 3 环境

  ```
  $ pyenv versions
    system
    2.7.13
  * 3.6.2 (set by /Users/cow/Projects/Py101-004/.python-version)
    3.6.2/envs/venv36
    venv36
  ```

2. 使用 [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) 创建和管理虚拟环境，创建一个虚拟环境，在这个环境里面安装需要使用的包。如果有多个项目都在自己的电脑上开发，每个项目在自己的环境里安装需要的包，互不影响。

  ```
  $ pyenv virtualenvs
    3.6.2/envs/venv36 (created from /Users/cow/.pyenv/versions/3.6.2)
    venv36 (created from /Users/cow/.pyenv/versions/3.6.2)
  ```

3. 安装程序需要的包

  ```
  $ pip install request
  $ pip install Flask-WTF
  ```

4. 运行程序程序

  ```
  $ python check-weather-v2.py
  ```

5. 在浏览器中输入 0.0.0.0:8080
