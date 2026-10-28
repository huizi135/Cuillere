# 在 Windows 上打开 Cuillère 原型

当前分支：`docs/product-foundation`。这是设计原型，还不是 Android / iOS 安装包。

## 第一次获取仓库

在 PowerShell 里逐行执行：

```powershell
Set-Location C:\Users\Admin\Documents\GitHub
git clone --branch docs/product-foundation https://github.com/huizi135/Cuillere.git
Set-Location .\Cuillere
Start-Process .\prototype\index.html
```

clone 会创建 Cuillere 文件夹；最后一行用默认浏览器打开原型。如果这个文件夹已经存在，不要重复 clone。

## 已经克隆过

先查看当前分支和未提交的修改：

```powershell
Set-Location C:\Users\Admin\Documents\GitHub\Cuillere
git status
git branch --show-current
```

如果当前就是 docs/product-foundation，执行：

```powershell
git pull --ff-only
Start-Process .\prototype\index.html
```

如果当前是 main 且没有本地修改，执行：

```powershell
git fetch origin
git switch docs/product-foundation
git pull --ff-only
Start-Process .\prototype\index.html
```

本地有修改时，先保留自己的工作；不要用 reset --hard 或覆盖文件来解决。

## 文件用途

- `prototype/source.html`：可编辑的原型源码。
- `prototype/index.html`：可以直接打开的完整预览页，由源码生成。
- `tools/build_prototype.py`：重新生成预览页，只需要 Python，无需安装依赖。
- `tools/prototype-shell.html`：预览运行外壳，一般不用修改。
- `docs/`：产品定位与每次设计调整的记录。

修改 source.html 后运行：

```powershell
py .\tools\build_prototype.py
Start-Process .\prototype\index.html
```

浏览器已经打开时，刷新即可。不要只修改 index.html，否则下次生成会覆盖它。

## 现在能体验什么

打开后先显示 My Recipes 首页。点示例作品进入阅读，再点 Edit 编辑；底部 Recipes 返回首页并在本次会话中保留内容。底部 + 创建空白作品；Templates 可以选择 Everyday、Baking、Minimal 三个起始结构。可以搜索、按分类/标签筛选，并在编辑页 Categories & tags 中整理分类和标签。个人模板保存及真实数据持久化尚未实现。

## 当前边界

- 内容只在本次打开的页面内存中；刷新或关闭后会丢失。请勿把原型当作真实食谱存储。
- 图标及外壳辅助资源从 CDN 加载，首次打开需要联网；页面无后台服务。
- 曲库只有示例条目，没有连接音乐服务，也不播放歌曲。
- 营养和人数是有限通用食材的演示估算，没有品牌识别或完整营养数据库。
- 没有真实账户、云同步、应用商店构建或手机安装包。
- 已检查脚本语法与热量/人数缩放算术；触摸拖动、照片选择和整体浏览器布局尚未全面验证。
