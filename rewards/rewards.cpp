#include <iostream>
#include <vector>
#include <random>

#include "./account.hpp"
#include "./reward.hpp"

using namespace std;

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
    if(it->get_reward() > 0 ) {
      it->print(i);
    }
  }

  return 0;
}
