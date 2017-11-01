# CML
这个文档主要是写给开发人员的， 在mac下部署


## 准备工作
###python 2.7<br/>
电脑自带的2.7<br/> 
###virtualenv<br/>
在python2.7的环境下运行<br/>
检查是否已经安装<br/>
运行```virtualenv --version```<br/>
如果安装成功会显示版本号 <br/>
如果没有安装<br/>
运行   ```pip install virtualenv```<br/>

## 本地部署
### 下载<br/>
命令行运行：<br/>
```git clone https://github.com/wshwbluebird/CML.git```<br/>
最好直接在github destop 打开<br/><br/>
### 创建python虚拟环境<br/>
下载目录到本地文件夹，然后从命令行进入CML文件夹下<br/>
```cd CML```<br/>
创建虚拟环境，并命名为venv<br/>
```virtualenv venv```<br/>
使用创建的虚拟环境<br/>
```source venv/bin/activate```<br/>
若要退出直接执行```deactivate```命令<br/>
程序的开发部署和调试都需要次虚拟环境下运行<br/><br/>
### 下载flask所需要的依赖<br/>
在虚拟环境venv下，执行
```pip install -r  requirements.txt```<br/>
如果以后你在开发过程中用到了flask的新插件，请运行<br/>
```pip freeze > requirements.txt```<br/>
命令使新的依赖自动添加到requirements.txt中<br/>

### 配置环境变量
将configure.sh文件放在CML文件夹子下<br/>
在虚拟环境venv中运行<br/>
<pre><code>chmod +x configure.sh
./configure.sh
source configure.sh
</code></pre>
执行完毕后,执行<br/>
```echo $CML_MYSQL_USER```<br/>
如果才出现结果为```cml```则说明部署成功<br/>

## 开发测试
###集成开发运行服务器<br/>
在虚拟环境venv下运行<br/>
``` python manage.py runserver```<br/>
之后在本地浏览器输入http://localhost:5000    进入运行网站<br/>
运行默认是debugger模式，可以不用终止服务器进程，直接修改代码进行调试。<br/>
###运行shell命令行<br/>
在虚拟环境venv下运行<br/>
``` python manage.py shell```<br/>
可以通过何种情况直接向数据库输入数据，以及创建表<br/>
###运行单元测试<br/>
在虚拟环境venv下运行<br/>
``` python manage.py test```<br/>
可以运行所有test文件夹下的单元测试代码<br/>
`注意：开发，测试，部署所用数据库均不相同，如果希望使用相同数据库请修改configure.py文档`


## 项目结构
	-CML
      -app 项目开发目录
			-main主模块
				__init__.py   
				errors.py 异常页面路由
				forms.py 主模块表单
				view.py 主模块路由
			-static 静态资源css等
			-templates 界面（一定放在这个文件夹下）
			-xxxx 其他待开发的模块
			__init__.py
			models.py 存储数据模型
		-migrations 数据库迁移目录（这个不用管）
		-tests 测试集
		-venv 虚拟环境（自己配置的）
		config.py 配置信息
		manage.py 部署管理文件
		requirement.txt 项目所需依赖
		










