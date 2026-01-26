package graph

import (
	"container/list"
)

type Course struct {
	Indegree int
	Subseq   []int
}

func canFinish(numCourses int, prerequisites [][]int) bool {

	G := make([]Course, numCourses)

	for _, prerequisity := range prerequisites {
		id := prerequisity[0]
		pr := prerequisity[1]
		G[id].Indegree++
		G[pr].Subseq = append(G[pr].Subseq, id)
	}

	Q := list.New()
	for k, v := range G {
		if v.Indegree == 0 {
			Q.PushBack(k)
		}
	}

	for courseID := Q.Front(); courseID != nil; courseID = courseID.Next() {
		id := courseID.Value.(int)
		for _, seq := range G[id].Subseq {
			G[seq].Indegree--
			if G[seq].Indegree == 0 {
				Q.PushBack(seq)
			}
		}
	}

	return Q.Len() == len(G)
}
