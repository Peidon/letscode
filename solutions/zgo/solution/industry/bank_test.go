package industry

import (
	"testing"
)

func TestBinSearch(t *testing.T) {
	a := &Account{
		Transactions: []Entry{
			{Timestamp: -7, Balance: 1},
			{Timestamp: 0, Balance: 2},
			{Timestamp: 1, Balance: 3},
			{Timestamp: 2, Balance: 5},
			{Timestamp: 5, Balance: 6}},
	}

	testsData := []struct {
		queryTime int64
		expectVal int
	}{
		{
			queryTime: -8,
			expectVal: -1,
		},
		{
			queryTime: -7,
			expectVal: 0,
		},
		{
			queryTime: 0,
			expectVal: 1,
		},
		{
			queryTime: 1,
			expectVal: 2,
		},
		{
			queryTime: 2,
			expectVal: 3,
		},
		{
			queryTime: 3,
			expectVal: 3,
		},
		{
			queryTime: 4,
			expectVal: 3,
		},
		{
			queryTime: 5,
			expectVal: 4,
		},
		{
			queryTime: 6,
			expectVal: 4,
		},
	}

	for i, d := range testsData {
		v := a.BalanceAt(d.queryTime)
		if v != d.expectVal {
			t.Error(v)
		} else {
			t.Logf("#%d pass", i)
		}
	}

}
