var maxProfit = function(prices) {
  var profit = 0;
  function buy (day_index) {
    profit -= prices[day_index];
  }
  function sell (day_index) {
    profit += prices[day_index];
  }

  for (var i = 0; i <= prices.length-2; i++) {
    if (prices[i] < prices[i+1]) {
      buy(i);
      sell(i+1);
    }
  }
  return profit;
}
