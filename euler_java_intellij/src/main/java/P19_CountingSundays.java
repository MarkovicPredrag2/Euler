import java.time.Month;
import java.util.HashMap;

public class P19_CountingSundays {
    private enum Month {
        January,
        February,
        March,
        April,
        May,
        June,
        July,
        August,
        September,
        October,
        November,
        December
    }

    private enum Day {
        Monday,
        Tuesday,
        Wednesday,
        Thursday,
        Friday,
        Saturday,
        Sunday
    }

    private HashMap<Month, Day> beginningOfMonths = new HashMap<>();

    public P19_CountingSundays() {
        initBeginningOfMonths();
    }

    private void initBeginningOfMonths() {
        beginningOfMonths.put(Month.January,    Day.Tuesday);
        beginningOfMonths.put(Month.February,   Day.Friday);
        beginningOfMonths.put(Month.March,      Day.Friday);
        beginningOfMonths.put(Month.April,      Day.Monday);
        beginningOfMonths.put(Month.May,        Day.Wednesday);
        beginningOfMonths.put(Month.June,       Day.Saturday);
        beginningOfMonths.put(Month.July,       Day.Monday);
        beginningOfMonths.put(Month.August,     Day.Thursday);
        beginningOfMonths.put(Month.September,  Day.Sunday);
        beginningOfMonths.put(Month.October,    Day.Tuesday);
        beginningOfMonths.put(Month.November,   Day.Friday);
        beginningOfMonths.put(Month.December,   Day.Sunday);
    }



}
