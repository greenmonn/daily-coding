public class Account {
  private int balance = 0;
  private int debt = 0;
  private int debtLimit = 300;

  public Account(int balance) {
    this.balance = balance;
  }

  public boolean Receive(int amount) {
    this.balance += amount;
    return true;
  }

  public boolean Borrow(int amount) throws Exception {
    this.debt += amount;
    if (this.debt > this.debtLimit) {
      throw new Exception("Exceed Debt Limit!");
    }
    return true;
  }

  public boolean Repay(int amount) {
    if (this.debt < amount) {
      this.debt = 0;
      this.balance = amount - this.debt;
    }
    this.debt -= amount;
    return true;
  }

  public boolean Send(int amount) throws Exception {
    if (this.balance < amount) {
      this.balance = 0;
      this.debt = amount - this.balance;
      if (this.debt > this.debtLimit) {
        throw new Exception("Exceed Debt Limit!");
      }
      return false;
    }
    this.balance -= amount;
    return true;
  }

}