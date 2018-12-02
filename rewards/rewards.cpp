#include <iostream>
#include <vector>
#include <random>

#include "./account.hpp"
#include "./reward.hpp"

using namespace std;

double get_account_rewards(Rewards *rewards, Account *account, bool print) {
  double power = rewards->get_power(*account);
  account->set_power(power);
  double reward = rewards->get_reward(*account);
  if(reward > 1) {
    cout << "WTF" << endl;
  }
  account->set_reward(reward);
  if(print && account->get_reward() > 0 ) {
    account->print();
  }
  return account->get_reward();
}

int main() {
  Rewards rewards;

  std::random_device rd;     // only used once to initialise (seed) engine
  std::mt19937 gen(rd());
  std::mt19937 rng(rd());    // random-number engine used (Mersenne-Twister in this case)
  std::discrete_distribution<> d({70, 50, 40, 30, 20, 10, 4, 3, 2, 1, 1, 1});

  vector<Account> accounts;

  // Random
  for (int i = 0; i < 10000; i++) {
    std::uniform_int_distribution<int> deposit_multiple(1, 2000);
    std::uniform_int_distribution<int> deposit_multiple_decimal(100, 200000);
    std::uniform_int_distribution<int> stake_multiple(50, 200);

    int pledge = d(gen);
    double deposit = pledge * deposit_multiple(rng) + (double) deposit_multiple_decimal(rng) / 10000;
    double stake = pledge * stake_multiple(rng);
    Account *user = new Account(i, pledge, deposit, stake);
    accounts.push_back(*user);
  }

  // Manual
  /*
  Account *user1 = new Account(1000, 3, 200, 20000);
  accounts.push_back(*user1);
  Account *user2 = new Account(1001, 3, 2000, 20000);
  accounts.push_back(*user2);
  Account *user3 = new Account(1002, 3, 20000, 20000);
  accounts.push_back(*user3);
  Account *user4 = new Account(1003, 13, 20000, 20000);
  accounts.push_back(*user4);
  Account *user5 = new Account(1004, 100, 1000000, 5000000);
  accounts.push_back(*user5);
  Account *user6 = new Account(1005, 9999999, 5000000, 5000000);
  accounts.push_back(*user6);
  Account *user7 = new Account(1006, 1, 5000000, 5000000);
  accounts.push_back(*user7);
  */

  const double SECONDS_IN_YEAR = 31557600;
  const double BLOCKS_PER_SECOND = 2;
  const int MAX_ANNUAL_INFLATION = 40000000;
  const double MAX_INFLATION_PER_BLOCK = 0.633762;

  double reward_pool;
  double adjusted_reward_pool;
  vector<Account>::iterator it;
  for(it = accounts.begin(); it != accounts.end(); ++it ) {
    reward_pool += get_account_rewards(&rewards, &(*it), false);
  }
  bool normalize = false;
  if(reward_pool > MAX_INFLATION_PER_BLOCK) {
    normalize = true;
  }

  for(it = accounts.begin(); it != accounts.end(); ++it ) {
    double reward = get_account_rewards(&rewards, &(*it), true);
    if(normalize) {
      double adjusted_reward = (reward / reward_pool) * MAX_INFLATION_PER_BLOCK;
      adjusted_reward_pool += adjusted_reward;
      cout << "INFLATION REWARD (adjusted) IS " << adjusted_reward << " PTR\n\n" << endl;
    } else {
      cout << "INFLATION REWARD IS " << reward << " PTR\n\n" << endl;
    }
  }

  cout << "Paying out MAX of " << MAX_ANNUAL_INFLATION / ( SECONDS_IN_YEAR * BLOCKS_PER_SECOND) << " PAT a block" << endl;
  cout << "Total Rewards: " << reward_pool << ", Adjusted Rewards " << adjusted_reward_pool << endl;
  return 0;
}
