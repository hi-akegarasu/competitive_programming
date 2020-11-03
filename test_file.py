# PAST 2 H - 1-9 Grid

### ref Sakai Python Algorythm Introduction (2020) my_dijkstra.py
import heapq

# 無限大の定義
INFTY = 2**31 - 1

class MyVertex:
    def __init__(self, id):
        self.id = id
        self.adj = {} # dict型
        self.dist = INFTY
        self.pred = None
    
    # = の定義
    def __eq__(self, v):
        return self.dist == v.dist

    # != の定義
    def __ne__(self, v):
        return self.dist != v.dist

    # < の定義
    def __lt__(self, v):
        return self.dist < v.dist
    
    # <= の定義
    def __le__(self, v):
        return self.dist <= v.dist
    
    # > の定義
    def __gt__(self, v):
        return self.dist > v.dist
    
    # >= の定義
    def __ge__(self, v):
        return self.dist >= v.dist

    # 頂点の情報を表示
    def to_string(self):
        str_pred = "None"
        if self.pred != None:
            str_pred = str(self.pred)
        
        return str(self.id) + ", adj = " + str(self.adj) + ", " + str(self.dist) + ", " + str_pred

# 最短経路となる先行頂点の変更
def relax(u, v):
    if v.dist > u.dist + u.adj[v.id]:
        v.dist = u.dist + u.adj[v.id]
        v.pred = u.id
        return True
    else:
        return False

# ダイクストラ法
def dijdkstra(vertices, src):
    # 初期化
    src.dist = 0
    q = [] # 優先度付きキュー
    for u in vertices:
        heapq.heappush(q, u)
    
    # 探索開始
    while len(q) > 0:
        # print_heap(q) # ヒープの中身を表示
        u = heapq.heappop(q)
        for i in u.adj.keys():
            if relax(u, vertices[i]):
                heapq.heapify(q)

# 経路を表示
def print_path(vertices, src, v):
    if src.id == v.id:
        print(src.id, end = " ")
    elif v.pred == None:
        print("\n経路が存在しません。")
    else:
        print_path(vertices, src, vertices[v.pred])
        print(v.id, end = " ")

# 頂点を接続
def connect(vertices, i, j, weight):
    vertices[i].adj[j] = weight

# ヒープの中身を表示
def print_heap(q):
    print("[", end="")
    for i in q:
        print(i.id, end=" ")
    print("]")

### ref end

n, m = map(int, input().split())
a = [input() for _ in range(n)]
nodes = [[] for i in range(10)]

for i in range(n):
    for j in range(m):
        if a[i][j] in '0123456789':
            k = int(a[i][j])
            #print(k)
            nodes[k].append((i,j))
        elif a[i][j] =='S':
            start = (i,j)
        else:
            goal = (i,j)

# for i in range(10): print(nodes[i])
# 0~9どのnodesにいるかで、配列に格納する。これを使って、グラフの最短路を求める。
# 先に例外処理をする

if not(all(nodes[i] for i in range(1,10))):
    print(-1)
    exit()

# make vertices
vertices = []
for i in range(0, n*m): # (i,j)nodeに対応するverticesはi*m+j番
    vertices.append(MyVertex(i))

# connect 1-2,2-3,...,8-9
for k in range(1, 8):
    for pairA in nodes[k]:
        for pairB in nodes[k+1]:
            Ai, Aj = pairA[0], pairA[1]
            Bi, Bj = pairB[0], pairB[1]
            det = abs(Ai - Bi) + abs(Aj - Bj)
            connect(vertices, Ai*m+Aj, Bi*m+Bj, det)
for pairB in nodes[1]:
    Ai, Aj = start[0], start[1]
    Bi, Bj = pairB[0], pairB[1]
    det = abs(Ai - Bi) + abs(Aj - Bj)
    connect(vertices, Ai*m+Aj, Bi*m+Bj, det)
for pairA in nodes[9]:
    Ai, Aj = pairA[0], pairA[1]
    Bi, Bj = goal[0], goal[1]
    det = abs(Ai - Bi) + abs(Aj - Bj)
    connect(vertices, Ai*m+Aj, Bi*m+Bj, det)

dijdkstra(vertices, vertices[start[0]*m+start[1]])
print_path(vertices, vertices[start[0]*m+start[1]], vertices[goal[0]*m+goal[1]])

'''
～～～～～～～～
inputに対する途中出力例
print(nodes,start,goal)

3 4
1S23
4567
89G1
[[], [(0, 0), (2, 3)], [(0, 2)], [(0, 3)], [(1, 0)], [(1, 1)], [(1, 2)], [(1, 3)], [(2, 0)], [(2, 1)]] (0, 1) (2, 2)
～～～～～～～～
input
8
13245678
23456789
34657890
78901234
45672389
59285376
09561732
96204394
'''
