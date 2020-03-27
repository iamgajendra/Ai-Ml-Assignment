graph={}
class graphs:
    def switch(self):
        ch=8
        while ch!=0:
            print("Enter the task you wanna do:")
            print("1. To insert a new node")
            print("2. To delete a new node")
            print("3. To insert a new edge")
            print("4. To delete a new edge")
            print("5. To print graph")
            print("6. To traverse BFS")
            print("7. To traverse DFS")
            print("0. Exit")
            ch=int(input(ch))
            if ch==1:
                self.addnode()
            elif ch==2:
                self.delnode()
            elif ch==3:
                self.addedge()
            elif ch==4:
                self.deledge()
            elif ch==5:
                self.prigraph()
            elif ch==6:
                self.bfs()
            elif ch==7:
                self.dfs()
            elif ch==0:
                self.exit()
            else:
                pass
    def addnode(self):
        print("Enter node you want to add")
        node=int(input())
        if node not in graph:
            graph[node]=[]
            print("Node added")
        else:
            print("Node already exists")
        self.switch()
    def prigraph(self):
        print(graph)
        self.switch()
    def delnode(self):
        print("Enter node you want to delete")
        n=int(input())
        if n in graph:
            for node in graph:
                for neighbor in graph[node]:
                    graph[node].remove(neighbor)
            graph.__delitem__(n)
            print("Node deleted")
            self.switch()
        else:
            print("Node not found")
            self.switch()
    def addedge(self):
        print("Enter starting node:")
        s=int(input())
        print("Enter ending node:")
        e=int(input())
        if s in graph:
            if e in graph:
                graph[s].append(e)
                print("Edge added")
            else:
                print("Invalid node")
        else:
            print("Invalid node")
        self.switch()
    def deledge(self):
        print("Enter starting node:")
        s = int(input())
        print("Enter ending node:")
        e = int(input())
        if s in graph:
            if e in graph:
                graph[s].remove(e)
                print("Edge removed")
            else:
                print("Invalid node")
        else:
            print("Invalid node")
        self.switch()
    def bfs(self):
        print("Enter starting node:")
        s=int(input())
        if s in graph:
            visited = [False] * len(graph)
            queue=[]
            queue.append(s)
            visited[s]=True
            while queue:
                s=queue.pop(0)
                print(s,end=" ")
                for i in graph[s]:
                    if visited[i]== False:
                        queue.append(i)
                        visited[i]= True
                        print(queue)
            self.switch()

    # def bfs(self):
    #     g={1:[2,3],2:[4,5],3:[6,7]}
    #     print("Enter starting vertex")
    #     s=int(input())
    #     for i in g:
    #         for neighbor in g[i]:
    #             # Mark all the vertices as not visited
    #             visited = [False] * (len(graph))
    #
    #             # Create a queue for BFS
    #             queue = []
    #
    #             # Mark the source node as
    #             # visited and enqueue it
    #             queue.append(s)
    #             visited[s] = True
    #             print(queue)
    #             # while queue:
    #                 # print("Hello")
    #                 # Dequeue a vertex from
    #                 # queue and print it
    #                 # s = queue.pop(0)
    #                 # print(s, end=" ")
    #                 #
    #                 # # Get all adjacent vertices of the
    #                 # # dequeued vertex s. If a adjacent
    #                 # # has not been visited, then mark it
    #                 # # visited and enqueue it
    #                 # for i in graph[s]:
    #                         # if visited[i] == False:
    #                         #     queue.append(i)
    #                         #     visited[i] = True

m=graphs()
m.switch()
