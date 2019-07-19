import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringJoiner;

public class P16_PowerDigitSum {
    private List<Integer> numberSequence = new ArrayList<>();
    private int base = 2;
    private int exponent = 1000;

    public P16_PowerDigitSum() {

    }

    public P16_PowerDigitSum(int base, int exponent) {
        this.base = base;
        this.exponent = exponent;
    }

    public void solution_1() {
        // The number is stored from left (first index) to right (last index)
        initializeSequence();
        for (int i = 0;  i < exponent; i++) {
            Integer firstDigit = numberSequence.get(0);
            if ( firstDigit != 0 )
                appendLeadingZero();
            int digits = numberSequence.size();
            performMultiplicationOnNumberSequence(digits);
        }
    }

    private void initializeSequence() {
        // Leading zero makes the algorithm easier
        appendLeadingZero();
        numberSequence.add(1);
    }

    private void appendLeadingZero() {
        numberSequence.add(0, 0);
    }

    private void performMultiplicationOnNumberSequence(int digits) {
        for (int j = 1; j < digits; j++) {
            Integer currentDigit = numberSequence.get(j);
            Integer beforeDigit = numberSequence.get(j - 1);

            multiplyCurrentDigitAndAddRemainderToDigitBefore(currentDigit, beforeDigit, j);
        }
    }

    private void multiplyCurrentDigitAndAddRemainderToDigitBefore(Integer currentDigit, Integer beforeDigit, int j) {
        currentDigit *= base;
        beforeDigit += Math.floorDiv(currentDigit, 10);
        currentDigit %= 10;
        numberSequence.set(j, currentDigit);
        numberSequence.set(j - 1, beforeDigit);
    }

    @Override
    public String toString() {
        if ( numberSequence.get(0) == 0 )
            numberSequence.remove(0);
        StringBuilder number = new StringBuilder();
        for (Integer digit : numberSequence)
            number.append(digit);

        return number.toString();
    }
}
