package industry

type Bank struct {
	Accounts map[uint64]*Account
	Fee      int64
	History  map[int64][]Event
}

type Account struct {
	Balance      int64
	Transactions []Entry
}

func (a *Account) AddTransaction(timestamp, delta int64) {
	newBalance := a.Balance + delta
	a.Transactions = append(a.Transactions, Entry{
		Timestamp: timestamp,
		Delta:     delta,
		Balance:   newBalance,
	})
	a.Balance = newBalance
}

type Event struct {
	AccountID uint64
	Delta     int64
}

type Entry struct {
	Timestamp int64
	Delta     int64
	Balance   int64
}

func NewBank() *Bank {
	return &Bank{
		Accounts: make(map[uint64]*Account),
		Fee:      1,
		History:  make(map[int64][]Event),
	}
}

func (b *Bank) AddEvent(accountID uint64, delta, timestamp int64) {
	b.History[timestamp] = append(b.History[timestamp], Event{
		AccountID: accountID,
		Delta:     delta,
	})
}

func (b *Bank) Create(accountID uint64) {
	if _, ok := b.Accounts[accountID]; ok {
		return
	}
	b.Accounts[accountID] = &Account{Balance: 0, Transactions: make([]Entry, 0)}
}

func (b *Bank) Deposit(accountID uint64, amount int64, timestamp int64) bool {
	if amount <= 0 {
		return false
	}
	account, ok := b.Accounts[accountID]
	if !ok {
		return false
	}

	account.AddTransaction(timestamp, amount)
	b.AddEvent(accountID, amount, timestamp)
	return true
}

func (b *Bank) Withdraw(accountID uint64, amount int64, timestamp int64) bool {
	if amount <= 0 {
		return false
	}
	account, ok := b.Accounts[accountID]
	if !ok || account.Balance < amount+b.Fee {
		return false
	}

	account.AddTransaction(timestamp, -amount-b.Fee)
	b.AddEvent(accountID, -amount-b.Fee, timestamp)
	return true
}

func (b *Bank) Transfer(fromID, toID uint64, amount int64, timestamp int64) bool {
	if amount <= 0 {
		return false
	}

	from, okFrom := b.Accounts[fromID]
	to, okTo := b.Accounts[toID]
	if !okFrom || !okTo {
		return false
	}

	if from.Balance < amount+b.Fee {
		return false
	}

	from.AddTransaction(timestamp, -amount-b.Fee)
	to.AddTransaction(timestamp, amount)

	b.AddEvent(fromID, -amount-b.Fee, timestamp)
	b.AddEvent(toID, amount, timestamp)
	return true
}

func (a *Account) BalanceAt(timestamp int64) int {
	left, right := 0, len(a.Transactions)

	for left < right {
		mid := (left + right) / 2
		if a.Transactions[mid].Timestamp <= timestamp {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left - 1
}

func (a *Account) UndoSince(timestamp int64) int {
	left, right := 0, len(a.Transactions)
	for left < right {
		mid := (left + right) / 2
		if a.Transactions[mid].Timestamp < timestamp {
			left = mid + 1
		} else {
			right = mid
		}
	}
	return left
}

func (a *Account) Undo(timestamp, delta int64) {
	idx := a.UndoSince(timestamp)

	if idx >= len(a.Transactions) {
		return
	}

	a.Balance += (-delta)

	// remove the original entry
	a.Transactions = append(a.Transactions[:idx], a.Transactions[idx+1:]...)

	// rebalance forward
	for i := idx; i < len(a.Transactions); i++ {
		a.Transactions[i].Balance += (-delta)
	}
}

func (b *Bank) BalanceAt(accountID uint64, timestamp int64) *int64 {
	account, ok := b.Accounts[accountID]
	if !ok {
		return nil
	}
	idx := account.BalanceAt(timestamp)
	if idx < 0 {
		return nil
	}
	return &account.Transactions[idx].Balance
}

func (b *Bank) Undo(timestamp int64) bool {
	events, ok := b.History[timestamp]
	if !ok {
		return false
	}

	for _, e := range events {
		if _, ok := b.Accounts[e.AccountID]; !ok {
			return false
		}
	}

	for _, event := range events {
		a, ok := b.Accounts[event.AccountID]
		if !ok {
			continue
		}
		a.Undo(timestamp, event.Delta)
	}

	delete(b.History, timestamp)
	return true
}
