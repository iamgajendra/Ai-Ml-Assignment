class jug:
    jugs = (0, 0)
    jug1 = jugs[0]
    jug2 = jugs[1]
    maxjug = [0, 0]
    goal_amount = []
    visited_nodes = [(0, 0)]
    j=(0,0)

    def set_jugs(self):
        jug1_cap = 0
        jug2_cap = 0
        jug1_cap = int(input("Enter first jug capacity"))
        while jug1_cap < 1:
            print("Enter valid capacity")
            jug1_cap = int(input("Enter first jug capacity"))
        jug2_cap = int(input("Enter second jug capacity"))
        while jug2_cap < 1:
            print("Enter valid capacity")
            jug2_cap = int(input("Enter second jug capacity"))
        self.maxjug = [jug1_cap, jug2_cap]
        print("Capacity set successfully")
        self.set_goals()

    def set_goals(self):
        temp = int(input("Enter the goal amount"))
        while temp > max(self.maxjug[0], self.maxjug[1]):
            print("Enter valid value")
            temp = int(input("Enter the goal amount"))
        for g in range(max(self.maxjug[0],self.maxjug[1]+1)):
            self.goal_amount.append((0, temp))
            self.goal_amount.append((temp, 0))
        print("Goal amount successfully set")
        self.searchtype()

    def searchtype(self):
        ch = 3
        while ch > 2 or ch < 0:
            print("Enter the type of search:")
            print("1. DFS")
            print("0. Exit")
            ch = int(input(ch))
            if ch > 2 or ch < 0:
                print("Enter valid choice")
        if ch == 1:
            self.dfs(self.jugs)
            exit(0)
    def print_solution(self):
        print("steps")
        for i in self.visited_nodes:
            print(i)
        print("Graph: ",graph)
        exit(0)

    def dfs(self, jugs):
        if jugs in self.goal_amount:
            print("Solution is:")
            self.print_solution()
        else:
            if not self.visited_nodes.__contains__((0, jugs[1])):
                graph[jugs].append([0, jugs[1]])
                graph[0, jugs[1]] = []
                flag = 1
                self.visited_nodes.append((0, jugs[1]))
                j = (0, jugs[1])
                self.dfs(j)
            if not self.visited_nodes.__contains__((jugs[0], 0)):
                graph[jugs].append([jugs[0], 0])
                graph[jugs[0], 0] = []
                flag = 1
                self.visited_nodes.append((jugs[0], 0))
                j = (jugs[0], 0)
                self.dfs(j)
            if not self.visited_nodes.__contains__((self.maxjug[0], jugs[1])):
                graph[jugs] = [(self.maxjug[0], jugs[1])]
                graph[(self.maxjug[0], jugs[1])]=[]
                self.visited_nodes.append((self.maxjug[0], jugs[1]))
                j = ((self.maxjug[0], jugs[1]))
                self.dfs(j)
            if not self.visited_nodes.__contains__((jugs[0],self.maxjug[1])):
                graph[jugs] = [(jugs[0],self.maxjug[1])]
                graph[(jugs[0],self.maxjug[1])]=[]
                self.visited_nodes.append((jugs[0],self.maxjug[1]))
                j = (jugs[0],self.maxjug[1])
                self.dfs(j)
            jug2_left=self.maxjug[1]-jugs[1]
            if jugs[0]<= jug2_left:
                if not self.visited_nodes.__contains__((0,jugs[0]+jugs[1])):
                    graph[jugs] = [(0,jugs[0]+jugs[1])]
                    graph[(0,jugs[0]+jugs[1])] = []
                    self.visited_nodes.append((0,jugs[0]+jugs[1]))
                    j = (0, jugs[0] + jugs[1])
                    self.dfs(j)
            else:
                if not self.visited_nodes.__contains__((jugs[0]-jug2_left,jugs[1]+jug2_left)):
                    graph[jugs] = [(jugs[0]-jug2_left,jugs[1]+jug2_left)]
                    graph[(jugs[0]-jug2_left,jugs[1]+jug2_left)] = []
                    self.visited_nodes.append((jugs[0]-jug2_left,jugs[1]+jug2_left))
                    j = ((jugs[0]-jug2_left,jugs[1]+jug2_left))
                    self.dfs(j)
            jug1_left = self.maxjug[0] - jugs[0]
            if jugs[1] <= jug1_left:
                if not self.visited_nodes.__contains__((jugs[0] + jugs[1],0)):
                    graph[jugs] = [(jugs[0] + jugs[1],0)]
                    graph[(jugs[0] + jugs[1],0)] = []
                    self.visited_nodes.append((jugs[0] + jugs[1],0))
                    j = ((jugs[0] + jugs[1],0))
                    self.dfs(j)
            else:
                if not self.visited_nodes.__contains__((jugs[0] + jug1_left, jugs[1] - jug1_left)):
                    graph[jugs] = [(jugs[0] + jug1_left, jugs[1] - jug1_left)]
                    graph[(jugs[0] + jug1_left, jugs[1] - jug1_left)] = []
                    self.visited_nodes.append((jugs[0] + jug1_left, jugs[1] - jug1_left))
                    j = ((jugs[0] + jug1_left, jugs[1] - jug1_left))
                    self.dfs(j)
j = jug()
graph = {}
maxjug = j.set_jugs()
