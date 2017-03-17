package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func main() {
	var graph map[int][]int
	graph = make(map[int][]int)
	graph[0] = []int{1, 2}
	graph[1] = []int{0, 3}
	graph[2] = []int{0}
	graph[3] = []int{1, 4, 5}
	graph[4] = []int{3, 5, 6}
	graph[5] = []int{3, 4, 6, 7}
	graph[6] = []int{4, 5, 7}
	graph[7] = []int{6, 5}

	for k := range graph {
		wg.Add(1)
		go bfs(k, graph)
	}
	wg.Wait()
}

func bfs(k int, graph map[int][]int) {
	defer wg.Done()
	var frontier []int
	var parent, level map[int]int
	parent = make(map[int]int)
	level = make(map[int]int)
	i := 1
	parent[k] = -1
	level[k] = 0

	frontier = append(frontier, k)
	for len(frontier) > 0 {
		var next []int
		for _, k := range frontier {
			for _, v := range graph[k] {
				if _, ok := level[v]; ok == false {
					level[v] = i
					parent[v] = k
					next = append(next, v)
				}
			}
		}
		frontier = next
		i = i + 1
	}

	fmt.Printf("%v\nparent = %v\nlevel = %v\n", k, parent, level)

}
