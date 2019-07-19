
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class SupportiveFunctions {
    public static < T extends Comparable<? super T>> T getMaxValueOfArray(T[] array) {
        List<T> list = Arrays.asList(array);
        return Collections.max(list);
    }

    public static Integer[] convertPrimitiveIntArrayToIntegerArray(int[] array) {
        return IntStream.of( array ).boxed().toArray( Integer[]::new );
    }
}
