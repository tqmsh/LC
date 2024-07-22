class Account:
    def __init__(self, account_id): # Action 1a: Create an account The account ID was a parameter and the data behind  
        self.id = account_id        # it was sensible defaults (balance and transaction total set to 0). The function 
        self.balance = 0            # itself just shoved that into the storage dictionary. 
        self.transaction_total = 0
    def deposit(self, deposit_amount):      # Action 1b: Create a deposit by account ID Update the balance by doing something    
        self.balance += deposit_amount      # like storage_dict[account_id]["balance"] += deposit_amount 
        self.add_transaction(deposit_amount)
    def transfer_to(self, transfer_amount, other_account): # Action 2: Create a transfer This handler was built in two pieces. 
        if transfer_amount < 0: raise ValueError("Transfer amount cannot be negative") 
        if self.balance >= transfer_amount:                # First, make sure the transfer can happen by ensuring that both accounts 
            self.balance -= transfer_amount                # exist and that the "from" account's balance was >= the transfer amount. 
            other_account.balance += transfer_amount       # Second, decrease the from account's balance by the transfer amount and 
            self.add_transaction(transfer_amount)          # increase the to accounts balance by the transfer amount.   
            other_account.add_transaction(transfer_amount)
        else: raise ValueError("Insufficient funds")
    def add_transaction(self, amount):           # Action 3a: Add a transaction total to the accounts Whenever a deposit or transfer 
        self.transaction_total += amount         # happened for an account, that accounts transaction total would increase by the 
                                                 # amount of money moved. The trick here is to always add the "amount" in play to the
                                                 # transaction total, even if the money is being moved out of an account, the transaction total gets increased.   
class Bank:
    def __init__(self):
        self.accounts = {}
    def create_account(self, account_id):
        if account_id not in self.accounts: self.accounts[account_id] = Account(account_id)
        else: raise ValueError("Account already exists")
    def deposit(self, account_id, amount):
        if account_id in self.accounts: self.accounts[account_id].deposit(amount) 
        else: raise ValueError("Account does not exist")
    def transfer(self, from_id, to_id, amount):
        if from_id in self.accounts and to_id in self.accounts: self.accounts[from_id].transfer_to(amount, self.accounts[to_id]) 
        else: raise ValueError("One or both accounts do not exist")
    def get_top_active_accounts(self, n):
        if n <= 0: raise ValueError("Number of accounts must be positive")  
        return sorted(self.accounts.values(), key = lambda x: (-x.transaction_total, x.id))[:n] # 从大到小排序
    
def test_create_account():
    bank = Bank()
    bank.create_account("123")
    assert "123" in bank.accounts
    print("test_create_account passed")
    try:
        bank.create_account("123")
    except ValueError as e:
        assert str(e) == "Account already exists"
        print("test_create_account duplicate passed")

def test_deposit():
    bank = Bank()
    bank.create_account("123")
    bank.deposit("123", 100)
    assert bank.accounts["123"].balance == 100
    assert bank.accounts["123"].transaction_total == 100
    print("test_deposit passed")
    try:
        bank.deposit("1234", 100)
    except ValueError as e:
        assert str(e) == "Account does not exist"
        print("test_deposit account not exist passed")
    try:
        bank.deposit("123", -50)
    except ValueError as e:
        assert str(e) == "Deposit amount cannot be negative"
        print("test_deposit negative amount passed")

def test_transfer():
    bank = Bank()
    bank.create_account("123")
    bank.create_account("456")
    bank.deposit("123", 200)
    bank.transfer("123", "456", 100)
    assert bank.accounts["123"].balance == 100
    assert bank.accounts["456"].balance == 100
    assert bank.accounts["123"].transaction_total == 300
    assert bank.accounts["456"].transaction_total == 100
    print("test_transfer passed")
    try:
        bank.transfer("123", "4567", 50)
    except ValueError as e:
        assert str(e) == "One or both accounts do not exist"
        print("test_transfer non-existing account passed")
    try:
        bank.transfer("123", "456", 150)
    except ValueError as e:
        assert str(e) == "Insufficient funds"
        print("test_transfer insufficient funds passed")
    try:
        bank.transfer("123", "456", -50)
    except ValueError as e:
        assert str(e) == "Transfer amount cannot be negative"
        print("test_transfer negative amount passed")

def test_get_top_active_accounts():
    bank = Bank()
    bank.create_account("123")
    bank.create_account("456")
    bank.create_account("789")
    bank.deposit("123", 300)
    bank.deposit("456", 200)
    bank.deposit("789", 100)
    bank.transfer("123", "456", 50)
    bank.transfer("456", "789", 25)
    top_accounts = bank.get_top_active_accounts(2)
    assert top_accounts[0].id == "123"
    assert top_accounts[1].id == "456"
    print("test_get_top_active_accounts passed")
    try:
        bank.get_top_active_accounts(0)
    except ValueError as e:
        assert str(e) == "Number of accounts must be positive"
        print("test_get_top_active_accounts non-positive n passed")

if __name__ == "__main__":
    test_create_account()
    test_deposit()
    test_transfer()
    test_get_top_active_accounts()
    print("All tests passed")
