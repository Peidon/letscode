package tree

import (
	"testing"
)

func TestKthSmallest(t *testing.T) {
	root := &TreeNode{
		Val:   1,
		Right: &TreeNode{Val: 4},
	}

	if 4 != kthSmallest(root, 2) {
		t.Error("expect output = 4")
	}
}
