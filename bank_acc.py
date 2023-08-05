import threading
import time


class BankAccount():
    balance = 0
    def __init__(self, name:str, init_balance:float = 0):
        if init_balance < 0:
            raise Exception("init balance should be positive")
        self.balance = init_balance
        self.name = name
        self.balance_lock = threading.Lock()

    def withdraw(self, amount: float):
        if amount < 0:
            raise Exception("withdraw amount should be positive")
        self.balance_lock.acquire()
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.2)
            self.balance = new_balance
            self.balance_lock.release()
            return True
        else:
            print("not enough funds!")
            self.balance_lock.release()
            return False


    def deposit(self, amount: float):
        if amount < 0:
            raise Exception("depositi amount should be positive")

        self.balance_lock.acquire()
        self.balance += amount
        self.balance_lock.release()


if __name__ == "__main__":
    david_ba = BankAccount("david", 10_000)
    N = 20
    thrds = []
    for i in range(N):
        t1 = threading.Thread(target=david_ba.withdraw, args=(1, ))
        t1.start()
        thrds.append(t1)
        t2 = threading.Thread(target=david_ba.deposit, args=(1, ))
        t2.start()
        thrds.append(t2)

    [t.join() for t in thrds]
    print(david_ba.balance)