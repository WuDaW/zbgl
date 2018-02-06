# GitHub使用方法简易说明
## 一、生成SSH Key
1. 在终端输入下面的命令，一路回车，使用默认设置。
```bash
ssh-keygen -t rsa -C "wdw_shen@hotmail.com"
```
2. 在当前目录中会出现.ssh文件夹（在Linux中是隐藏文件夹）
3. 打开.ssh文件夹中的id_rsa.pub文件，这个文件里的内容就是生成的SSH Key。
4. 将SSH Key与GitHub账户绑定。

## 二、同步使用GitHub仓库
1. 在GitHub网站上创建仓库，仓库名为zbgl
2. 在本地终端输入下面的命令，将远程仓库克隆到本地
```bash
git clone https://github.com/WuDaW/zbgl.git
```
3. 在本地修改zbgl文件夹中文件（添加、删除、修改）
4. 使用下面的命令将修改的文件放到暂存区
```bash
git add <filename>
```
5. 使用下面的命令将暂存区的文件提交到当前分支中
```bash
git commit -m "说明/备注"
```
6. 使用下面的命令与远程仓库同步
```bash
git push origin master(分支名)
```
7. 使用下面的命令将远程修改的代码拉取到本地分支上
```bash
git pull origin master
```

## 三、分支的使用
1. 说明
   * 分支相对独立，互不影响
2. 创建并使用分支
```bash
git checkout -b wdw(分支名)
```
   * 上面命令的意思是创建名为wdw分支，并使用，相当于下面两条命令
   ```bash
   git branch wdw #创建wdw分支
   git checkout wdw #使用wdw分支
   ```
3. 查看当前分支
```bash
git branch
```
   * 当前使用的分支前有“*”号标注
4. 合并分支
```bash
git merge wdw
```
   * 将名为wdw的分支合并到当前分支里
   * 如果要将B分支合并到A分支里，要先进入A分支再执行上面的命令
