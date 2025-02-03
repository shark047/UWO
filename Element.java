/*
CS1027B - Assignment 1
Name: Yiwei Dong
Student Number: 251419881
Email: ydong445@uwo.ca
Created: Feb 2, 2025
*/


public class Element {

    private int atomicNo;
    private float atomicWeight;
    private String symbol;
    private String name;
    private String state;
    private String type;

    //Constructor
    public Element(int num, float wt, String sym, String nm, String st, String ty){

        this.atomicNo = num;
        this.atomicWeight = wt;
        this.symbol = sym;
        this.name = nm;
        this.state = st;
        this.type = ty;

    }

    //Getters
    public int getAtomicNo(){
        return atomicNo;
    }

    public float getAtomicWeight(){
        return atomicWeight;
    }

    public String getSymbol(){
        return symbol;
    }

    public String getName(){
        return name;
    }

    public String getState(){
        return state;
    }

    public String getType(){
        return type;
    }

    //Setters
    public void setName(String name) {
        this.name = name;
    }

    public void setState(String state) {
        this.state = state;
    }

    public void setType(String type) {
        this.type = type;
    }

    //toString
    public String toString(){
        return symbol + "(" + name + ")";
    }

    //equals
    public boolean equals(Element other) {
        return atomicNo == other.atomicNo;
    }
}