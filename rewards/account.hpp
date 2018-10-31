#include <iostream>

using namespace std;

class Account
{
  int pledge;
  double deposit;
  double stake;
  double power;
  double reward;
public:

  Account(int pledge, double deposit, double stake) {
    this->pledge = pledge;
    this->deposit = deposit;
    this->stake = stake;
  }

  int get_pledge() {
    return this->pledge;
  }

  double get_deposit() {
    return this->deposit;
  }

  double get_stake() {
    return this->stake;
  }

  void set_power(double power) {
    this->power = power;
  }

  double get_power() {
    return this->power;
  }

  void set_reward(double reward) {
    this->reward = reward;
  }

  double get_reward() {
    return this->reward;
  }

  void print(int account_id) {
    cout << account_id << " Account Summary:" << "\npledge: " << this->pledge << "\ndeposit: " << this->deposit << "\nstake: " << this->stake << "\npower: " << this->power << "\nreward: " << this->reward << "\n\n" << endl;
  }

};
