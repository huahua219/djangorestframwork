from functools import partial
from operator import add

# 深度优先

def find_path(x1, y1, x2, y2):
    """
    运用栈寻找迷宫路径

    迷宫中 0 表示可以通过，1 表示无法通过，-1 表示已经走过的路
    左上角坐标为 (0, 0)，横轴为 y 轴，纵轴为 x 轴
    迷宫四周必须用 1 围起来

    :param int x1:起点 x 轴坐标
    :param int y1:起点 y 轴坐标
    :param int x2:终点 x 轴坐标
    :param int y2:终点 y 轴坐标
    :return: 是否找到出口
    :rtype: bool
    """
    paths = [lambda x, y: (x - 1, y),  # 上
             lambda x, y: (x, y + 1),  # 右
             lambda x, y: (x + 1, y),  # 下
             lambda x, y: (x, y - 1)]  # 左

    # 从起点进入迷宫
    stack = list()
    maze[x1][y1] = -1
    stack.append((x1, y1))

    while len(stack) > 0:

        cur_node = stack[-1]  # 当前位置
        if cur_node[0] == x2 and cur_node[1] == y2:
            # 到达终点
            for p in stack:
                print(p)
            return True
        for path in paths:
            # 按照 dirs 顺序寻找路径
            next_node = path(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:  # 如果可以走
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = -1  # 标记为已经走过，防止死循环
                break
        else:  # 四个方向都没找到
            stack.pop()  # 回溯
    print("没有出口")
    return False

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

if __name__ == '__main__':
    find_path(1, 1, 8, 8)
    pickle.loads(one.cost.encode())[0]