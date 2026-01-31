package tree

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type BST struct {
	stack *Stack[TreeNode]
	point *TreeNode
}

func NewBST(root *TreeNode) *BST {
	return &BST{
		stack: &Stack[TreeNode]{},
		point: root,
	}
}

/*
- -. --.- -.-- -> - >
	\	\ 	\
	 \
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
