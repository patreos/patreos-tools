#include <math.h>
#include <iostream>

using namespace std;

class Rewards
{
public:

  double safe_log(double value) {
    if(value < 1) {
      return 0;
    }
    return log(value);
  }

  double safe_quadrt(double value) {
    if(value < 1) {
      return 0;
    }
    return sqrt(sqrt(value));
  }

  double safe_sqrt(double value) {
    if(value < 1) {
      return 0;
    }
    return sqrt(value);
  }

  // [0, 1]
  double shelf(double value) {
    if(value < 1) {
      return 0;
    }
    return 2 / M_PI * atan( safe_log(value) );
  }

  // [0, 1]
  double pareto(double value) {
    return (exp(value) - 1) / M_E;
  }

  // [0, 1]
  double get_power(Account account) {
    int pledge = 4 * account.get_pledge();
    double deposit = account.get_deposit();
    double power = 0;
    if( account.get_pledge() > 0 && account.get_deposit() > 0) {
      power = shelf( pledge * deposit / (pledge + deposit) );
    }
    return power;
  }

  double get_reward(Account account) {
    double power_mod = pareto(account.get_power());
    double max_total = 1 * safe_sqrt(2000000000) + safe_quadrt(2000000000) + 1;
    double total = power_mod * safe_sqrt(account.get_stake()) + safe_quadrt(account.get_stake()) + power_mod;
    double normalized_total = pareto(total / max_total);
    return normalized_total;
  }

};
