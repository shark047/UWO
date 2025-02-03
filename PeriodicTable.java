/*
CS1027B - Assignment 1
Name: Yiwei Dong
Student Number: 251419881
Email: ydong445@uwo.ca
Created: Feb 2, 2025
*/

public class PeriodicTable {

    private Element[][] mainTable;
    private Element[] lanthanides;
    private Element[] actinides;

    //Constructor
    public PeriodicTable(String filename){

        mainTable = new Element[7][18];
        lanthanides = new Element[15];
        actinides = new Element[15];
        loadData(filename);

    }

    public void loadData(String filename){

        TextFileReader fr = new TextFileReader(filename);
        fr.readString(); //read title(first line) to skip it

        while (!fr.endOfFile()) {
            String line = fr.readString();
            if (line == null || line.isEmpty()) continue;

            String[] data = line.split(",");

            //process raw data
            int atomicNo = Integer.parseInt(data[0]);
            String name = data [1];
            String symbol = data[2];
            float atomicWeight = Float.parseFloat(data[3]);
            String state = data[15];
            String type = "empty";


            if (data[12].equals("yes")){
                type = "Metal";
            } else if (data[13].equals("yes")) {
                type = "Nonmetal";
            } else if (data[14].equals("yes")) {
                type = "Metalloid";
            }

            Element element = new Element(atomicNo, atomicWeight, symbol, name, state, type);

            if (atomicNo >= 57 && atomicNo <= 71) {
                lanthanides[atomicNo - 57] = element;
            } else if (atomicNo >= 89 && atomicNo <= 103) {
                actinides[atomicNo - 89] = element;
            } else {
                int period = Integer.parseInt(data[7]);
                int group = Integer.parseInt(data[8]);
                mainTable[period - 1][group - 1] = element;
            }


        }
        fr.close();

    }

    public String toString() {
        StringBuilder sb = new StringBuilder();

        // look mainTable
        for (int i = 0; i < 7; i++) {
            for (int j = 0; j < 18; j++) {
                if (mainTable[i][j] == null) {
                    sb.append("    ");
                } else {
                    sb.append(String.format("%4s", mainTable[i][j].getSymbol()));
                }
            }
            sb.append("\n");
        }
        sb.append("\n");

        // Output Lanthanides
        sb.append("         ");
        for (Element e : lanthanides) {
            if (e != null) {
                sb.append(String.format("%4s", e.getSymbol())).append("");
            }
        }
        sb.append("\n");

        // Output Actinides
        sb.append("            ");
        for (Element e : actinides) {
            if (e != null) {
                sb.append(String.format("%4s", e.getSymbol())).append("");
            }
        }

        return sb.toString();
    }


    //getElement
    public Element getElement(String sym){
        for (Element[] row : mainTable) {
            for (Element e : row) {
                if (e != null && e.getSymbol().equals(sym)) {
                    return e;
                }
            }
        }

        for (Element e : lanthanides) {
            if (e != null && e.getSymbol().equals(sym)) return e;
        }
        for (Element e : actinides) {
            if (e != null && e.getSymbol().equals(sym)) return e;
        }
        return null;
    }

    //getPeriod
    public Element[] getPeriod(int per) {
        if (per < 1 || per > 7) return null;
        int count = 0;

        for (Element e : mainTable[per - 1]) {
            if (e != null) count++;
        }

        Element[] periodElements = new Element[count];
        int index = 0;

        for (Element e : mainTable[per - 1]) {
            if (e != null) {
                periodElements[index++] = e;
            }
        }
        return periodElements;
    }


    // getGroup
    public Element[] getGroup(int grp) {
        if (grp < 1 || grp > 18) return null;
        int count = 0;

        for (int i = 0; i < mainTable.length; i++) {
            if (grp - 1 >= 0 && grp - 1 < mainTable[i].length && mainTable[i][grp - 1] != null) {
                count++;
            }
        }

        Element[] groupElements = new Element[count];
        int index = 0;

        for (int i = 0; i < mainTable.length; i++) {
            if (grp - 1 >= 0 && grp - 1 < mainTable[i].length && mainTable[i][grp - 1] != null) {
                groupElements[index++] = mainTable[i][grp - 1];
            }
        }
        return groupElements;
    }



    // getLanthanides
    public Element[] getLanthanides() {
        return lanthanides;
    }

    // getActinides
    public Element[] getActinides() {
        return actinides;
    }

}
