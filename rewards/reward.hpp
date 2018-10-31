#include <math.h>
#include <iostream>

using namespace std;

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
