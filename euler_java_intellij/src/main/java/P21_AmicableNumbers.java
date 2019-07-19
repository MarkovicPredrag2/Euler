public class P21_AmicableNumbers {
    private int n = 1000;
    private int sumOfAllAmicableNumbersBelowN = 0;

    public P21_AmicableNumbers(int n) {
        this.n = n;
    }

    public P21_AmicableNumbers() {

    }

    public void solution_1() {
        for (int number = 2; number <= n; number++) {
            int sumOfDivisors = 0;

            // Only need to iterate to it's half,
            // since this is the highest possible divisor unequal to number
            for (int divisor = 1; divisor <= number / 2; divisor++)
                if ( isDivisorOfNumber(number, divisor) )
                    sumOfDivisors += divisor;
            if ( isAmicableNumber(number, sumOfDivisors) )
                sumOfAllAmicableNumbersBelowN += number;
        }
    }

    private boolean isDivisorOfNumber(int number, int divisor) {
        return number % divisor == 0;
    }

    private boolean isAmicableNumber(int number, int sumOfDivisors) {
        return number == sumOfDivisors;
    }

    @Override
    public String toString() {
        return "P21_AmicableNumbers{" +
                "sumOfAllAmicableNumbersBelowN=" + sumOfAllAmicableNumbersBelowN +
                '}';
    }
}
