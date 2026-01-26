package graph

import "testing"

func TestCanFinish(t *testing.T) {

	var testsData = []struct {
		numCourses    int
		prerequisites [][]int
		expect        bool
	}{
		{
			numCourses:    2,
			prerequisites: [][]int{{1, 0}},
			expect:        true,
		},
		{
			numCourses:    2,
			prerequisites: [][]int{{1, 0}, {0, 1}},
			expect:        false,
		},
		{
			numCourses:    2,
			prerequisites: [][]int{},
			expect:        true,
		},
	}

	for i, d := range testsData {
		if d.expect != canFinish(d.numCourses, d.prerequisites) {
			t.Errorf("#%d example failed. ", i)
		}
	}
}
