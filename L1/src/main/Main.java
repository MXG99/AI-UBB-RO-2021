package main;

import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    /**
     * Complexitate: O(1)
     * @param p1 - prima pereche de numere
     * @param p2 - a doua pereche de numere
     * @return distanta euclideana a celor doua locatii identificate prin cele doua perechi
     */
    public static float distanta_euclediana(Float[] p1, Float[] p2) {
        return (float) Math.sqrt(((p1[0] - p2[0]) * (p1[0] - p2[0])) + (p1[1] - p2[1]) * (p1[1] - p2[1]));
    }

    /**
     * Complexitate: O(n)
     * @param n - nr de numere binare de generat
     * @return array de numere binare
     */
    public static Integer[] generateBinary(Integer n) {
        Integer[] array = new Integer[n];
        Queue<String> binaryNumbers = new LinkedList<>();
        binaryNumbers.add("1");
        int k = 0;
        while (n > 0) {
            String s1 = binaryNumbers.peek();
            binaryNumbers.remove();
            array[k++] = Integer.parseInt(s1);
            String s2 = s1;
            binaryNumbers.add(s1 + "0");
            binaryNumbers.add(s2 + "1");
            n--;
        }
        return array;
    }



    public static void main(String[] args) {
        Float[] p1 = new Float[] {1f, 5f};
        Float[] p2 = new Float[] {4f, 1f};
        if ((distanta_euclediana(p1, p2) != 5.0f)) throw new AssertionError();

        if ((!Arrays.equals(generateBinary(4), new Integer[]{1, 10, 11, 100}))) {
            throw new AssertionError();
        }
        if ((!Arrays.equals(generateBinary(6), new Integer[]{1, 10, 11, 100, 101, 110}))) {
            throw new AssertionError();
        }
        if ((!Arrays.equals(generateBinary(10), new Integer[]{1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010}))) {
            throw new AssertionError();
        }
    }
}
