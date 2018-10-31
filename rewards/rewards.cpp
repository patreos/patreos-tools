#include <iostream>
#include <vector>
#include <math.h>
#include <random>

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

  void print(int account_id) {
    cout << account_id << " Account Summary:" << "\npledge: " << this->pledge << "\ndeposit: " << this->deposit << "\nstake: " << this->stake << "\npower: " << this->power << "\nreward: " << this->reward << "\n\n" << endl;
  }

};

class Rewards
{
public:

  // [0, 1]
  double shelf(double value) {
    if(value < 1) {
      return 0;
    }
    return 2 / M_PI * atan( log(value) );
  }

  // [0, 1]
  double pareto(double value) {
    return (exp(value) - 1) / M_E;
  }

  // [0, 1]
  double get_power(Account account) {
    int pledge = 2 * account.get_pledge();
    double deposit = account.get_deposit();
    double power = 0;
    if( account.get_pledge() > 0 && account.get_deposit() > 0) {
      power = shelf( pledge * deposit / (pledge + deposit) );
      //cout << "For pledge: " << account.get_pledge() << " and deposit: " << account.get_deposit() << ", power is " << power << endl;
    }
    return power;
  }

  // [0, 1]
  double get_reward(Account account) {
    double power_mod = pareto(account.get_power());
    double total = power_mod * sqrt(account.get_stake()) + account.get_stake() + account.get_power();
    return total;
    //return ( exp( shelf( power * sqrt(account.get_stake()) + account.get_stake() + power ) ) - 1 ) / M_E;
  }

};

int main() {
  Rewards rewards;

  std::random_device rd;     // only used once to initialise (seed) engine
  std::mt19937 gen(rd());
  std::mt19937 rng(rd());    // random-number engine used (Mersenne-Twister in this case)
  std::discrete_distribution<> d({70, 50, 30, 20, 10, 5, 4, 3, 2, 1});

  vector<Account> accounts;
  for (int i = 0; i < 1000; i++) {
    std::uniform_int_distribution<int> deposit_multiple(1,10);
    std::uniform_int_distribution<int> deposit_multiple_decimal(100,99999);

    int pledge = d(gen);
    double deposit = pledge * deposit_multiple(rng) + deposit_multiple_decimal(rng) * 1.0 / 10000;
    double stake = pledge * deposit_multiple(rng);
    Account *user = new Account(pledge, deposit, stake);
    accounts.push_back(*user);
  }

  vector<Account>::iterator it;
  int i = 0;
  for(it = accounts.begin(); it != accounts.end(); ++it ) {
    i++;
    double power = rewards.get_power(*it);
    it->set_power(power);
    double reward = rewards.get_reward(*it);
    it->set_reward(reward);
    it->print(i);
  }

  return 0;
}
