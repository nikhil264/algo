package main

import "fmt"

var parent map[int]int

func main() {
	var graph map[int][]int
	graph = make(map[int][]int)
	parent = make(map[int]int)
	graph[0] = []int{1, 2}
	graph[1] = []int{0, 3}
	graph[2] = []int{0}
	graph[3] = []int{1, 4, 5}
	graph[4] = []int{3, 5, 6}
	graph[5] = []int{3, 4, 6, 7}
	graph[6] = []int{4, 5, 7}
	graph[7] = []int{6, 5}
	graph[8] = []int{9, 10}

	for k := range graph {
		if _, ok := parent[k]; ok == false {
			parent[k] = -1
			dfs(k, graph, parent)
			fmt.Printf("%v\nparent = %v\n", k, parent)
		}
	}

}

func dfs(k int, graph map[int][]int, parent map[int]int) {
	for _, v := range graph[k] {
		if _, ok := parent[v]; ok == false {
			parent[v] = k
			dfs(v, graph, parent)
		}
	}
}
