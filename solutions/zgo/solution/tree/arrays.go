package tree

type Stack[T any] struct {
	entries []*T
	size    int
}

func (s *Stack[T]) PushBack(elem *T) {

	top := s.size
	s.size += 1

	if len(s.entries) > top {
		s.entries[top] = elem
	} else {
		s.entries = append(s.entries, elem)
	}
}

func (s *Stack[T]) Pop() *T {
	if s.size == 0 {
		return nil
	}
	peek := s.entries[s.size-1]
	s.size -= 1
	return peek
}
