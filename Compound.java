/*
CS1027B - Assignment 1
Name: Yiwei Dong
Student Number: 251419881
Email: ydong445@uwo.ca
Created: Feb 2, 2025
*/

public class Compound {
    private Element[] elements;
    private int[] elementCount;

    public Compound(PeriodicTable table, String[][] compoundArray) {
        elements = new Element[compoundArray.length];
        elementCount = new int[compoundArray.length];

        for (int i = 0; i < compoundArray.length; i++) {
            String symbol = compoundArray[i][0];
            Element element = table.getElement(symbol);

            elements[i] = element;
            if (compoundArray[i].length == 2) {
                elementCount[i] = Integer.parseInt(compoundArray[i][1]);
            } else {
                elementCount[i] = 1;
            }
        }
    }

    public String getBondType() {
        if (elements.length != 2) return null;

        String type1 = elements[0].getType();
        String type2 = elements[1].getType();


        if ((type1.equals("Metal") && type2.equals("Nonmetal")) ||
                (type2.equals("Metal") && type1.equals("Nonmetal"))) {
            return "ionic";
        } else if ((type1.equals("Metal") && type2.equals("Metalloid")) ||
                (type2.equals("Metal") && type1.equals("Metalloid")) ||
                (type1.equals("Nonmetal") && type2.equals("Nonmetal"))) {
            return "covalent";
        } else {
            return null;
        }
    }


    public String toString() {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < elements.length; i++) {
            sb.append(elements[i].getName()).append(": ").append(elementCount[i]).append("\n");
        }
        return sb.toString();
    }
}
