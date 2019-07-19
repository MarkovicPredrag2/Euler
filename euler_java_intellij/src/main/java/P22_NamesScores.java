import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class P22_NamesScores {
    private String[] arrayOfNames = {
            "ABCD", "ABC", "ABB", "AB", "A"
    };

    public P22_NamesScores() {

    }

    public void solution_1() {
        sortNamesAlphabeticallyInInterval(0, arrayOfNames.length, 0);
    }

    private void sortNamesAlphabeticallyInInterval(int offset, int end, int charPositionToSortBy) {
        List<Integer> sectionOffsetsOfNameList = new ArrayList<>();
        sortIntervalAlphabetically(offset, end, charPositionToSortBy);
        createSectionsOfNamesBasedOnCharPosition(offset, end, charPositionToSortBy, sectionOffsetsOfNameList);
        for (int i = 1; i < sectionOffsetsOfNameList.size(); i++) {
            int newOffset = sectionOffsetsOfNameList.get(i - 1);
            int newEnd = sectionOffsetsOfNameList.get(i);

            sortNamesAlphabeticallyInInterval(newOffset, newEnd, charPositionToSortBy + 1);
        }
    }

    private void sortIntervalAlphabetically(int offset, int end, int charPositionToSortBy) {
        if ( !isInputFor_alphabeticSelectionSort_valid(offset, end, charPositionToSortBy) )
            return;
        // Selection Sort is being used for simplicity, but pretty much any sort algorithm could have been implemented instead
        for (int i = offset; i < end; i++) {
            int indexOfAlphabeticallyHigherName = i;
            for(int currentNameIndex = i; currentNameIndex < end; currentNameIndex++)
                if ( isCurrentNameAlphabeticallyHigher(currentNameIndex, indexOfAlphabeticallyHigherName, charPositionToSortBy) )
                    indexOfAlphabeticallyHigherName = currentNameIndex;
            swapPositionsOfNames(i, indexOfAlphabeticallyHigherName);
        }
    }

    private boolean isInputFor_alphabeticSelectionSort_valid(int offset, int end, int charPositionToSortBy) {
        return ( end > offset ) && ( charPositionToSortBy >= 0 );
    }

    private char getCharAtPositionOfNameOnIndex(int charPositionToSortBy, int i) {
        String name = arrayOfNames[i];
        // It makes the algorithm a lot easier,
        // since it handles out of index cases perfectly by not moving the elements from their positions when comparing
        if (charPositionToSortBy >= name.length())
            return getCharWithHighestNumericValue();

        return arrayOfNames[i].charAt(charPositionToSortBy);
    }

    private char getCharWithHighestNumericValue() {
        return 'Z';
    }

    private int getNumericValueOfChar(char character) {
        return Character.getNumericValue(character);
    }

    private void swapPositionsOfNames(int first, int second) {
        String buffer = arrayOfNames[first];

        arrayOfNames[first] = arrayOfNames[second];
        arrayOfNames[second] = buffer;
    }

    private boolean isCurrentNameAlphabeticallyHigher(int indexOfCurrentName, int indexOfAlphabeticallyHigherName, int charPositionToSortBy) {
        char charOfAlphabeticallyHigherName = getCharAtPositionOfNameOnIndex(charPositionToSortBy, indexOfAlphabeticallyHigherName);
        char charOfCurrentName = getCharAtPositionOfNameOnIndex(charPositionToSortBy, indexOfCurrentName);

        return ( getNumericValueOfChar(charOfAlphabeticallyHigherName) > getNumericValueOfChar(charOfCurrentName));
    }

    private void createSectionsOfNamesBasedOnCharPosition(int offset, int end, int charPositionToSortBy, List<Integer> sectionOffsetsOfNameList) {
        char c = getCharAtPositionOfNameOnIndex(charPositionToSortBy, offset);

        sectionOffsetsOfNameList.add(offset);
        for (int i = offset; i < end; i++) {
            char newChar = getCharAtPositionOfNameOnIndex(charPositionToSortBy, i);

            if ( c != newChar ) {
                sectionOffsetsOfNameList.add(i);
                c = newChar;
            }
        }
        sectionOffsetsOfNameList.add(end);
    }

    @Override
    public String toString() {
        return "P22_NamesScores{" +
                "names=" + Arrays.toString(arrayOfNames) +
                '}';
    }
}
