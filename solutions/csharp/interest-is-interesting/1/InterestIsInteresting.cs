static class SavingsAccount
{
    public static float InterestRate(decimal balance)
    {
        float rate = 0;
        if (balance < 0) {
            rate = 3.213F;
        } else if (balance < 1000) {
            rate = 0.5F;
        } else if (balance < 5000) {
            rate = 1.621F;
        } else {
            rate = 2.475F;
        }
        return rate;
    }

    public static decimal Interest(decimal balance) => balance * (Decimal)InterestRate(balance) / 100;

    public static decimal AnnualBalanceUpdate(decimal balance) => balance + Interest(balance);

    public static int YearsBeforeDesiredBalance(decimal balance, decimal targetBalance)
    {
        int years = 0;
        decimal working = balance;
        while (working < targetBalance) {
            working = AnnualBalanceUpdate(working);
            years = years + 1;
        }
        return years;
    }
}
