####1,git基本命令
    查看每次提交的内容差异 并显示两条内容:git log -p -2
    查看作者提交日志:git log --author='xxxx'
    显示前N条记录:git log -n
    显示简要的增改行的统计，做代码审核或这快速浏览其他协作者提交的改动:git log --stat
    回退到上个版本: git reset --hard HEAD^
    回退到某个版本: git reset --hard ID

    git reflog 可以查看所有分支的所有操作记录（包括已经被删除的 commit 记录和 reset 的操作）
    git log [--pretty=oneline] 命令可以显示所有提交过的版本信息

    1,回退个历史版本的id
    git reset --hard ID

    2,回退上个版本：
        git reset --hard HEAD^
    
    3,删除本地分支：
        git branch -d [branchname]
    
    4,删除远程分支
        git push origin --delete [branchname]
