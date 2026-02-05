package tree

import "github.com/Peidon/studio/list"

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type BST struct {
	stack *list.Stack[TreeNode]
	point *TreeNode
}

func NewBST(root *TreeNode) *BST {
	return &BST{
		stack: new(list.Stack[TreeNode]),
		point: root,
	}
}

/*
- -. --.- -.- - -
	\	\ 	\ __
	 \		|
If we rotate the tree and straighten along one side of it,
then we can see the traversal more obviously.
*/

func (b *BST) Next() *TreeNode {
	for b.point != nil {
		b.stack.PushBack(b.point)
		b.point = b.point.Left
	}

	x := b.stack.Pop()
	b.point = x.Right

	return x
}

func kthSmallest(root *TreeNode, k int) int {
	bst := NewBST(root)
	v := bst.Next().Val
	for i := 0; i < k-1; i++ {
		v = bst.Next().Val
	}
	return v
}
