import java.util.*;
import java.io.*;
import java.time.*;
import java.time.format.*;

class StarBucks {
    String custName;
    double totPrice = 0;
    ArrayList<String> addCoffeeName = new ArrayList<String>();
    ArrayList<Double> addCoffeePrice = new ArrayList<Double>();
    ArrayList<String> addCoffeeSize = new ArrayList<String>();

    void getMenu() {
        try {
            FileReader reader = new FileReader("menu.txt");
            BufferedReader br = new BufferedReader(reader);

            String line;
            line = br.readLine();

            while(line != null) {
                System.out.println(line);

                line = br.readLine();
                line = br.readLine();
                line = br.readLine();
                line = br.readLine();
                line = br.readLine();
            }

            br.close();
            reader.close();
        } catch (IOException e) {
            System.out.println("Error: " + e);
        }
    }

    void order(String coffeeName) {
        try {
            FileReader reader = new FileReader("menu.txt");
            BufferedReader br = new BufferedReader(reader);
            double small, medium, large;
            char ch;
            String line, coffeeSize;
            Scanner k = new Scanner(System.in);
        
            while((line = br.readLine()) != null) {
                if(line.equals(coffeeName))
                    break;
            }

            small = Double.parseDouble(line = br.readLine());
            medium = Double.parseDouble(line = br.readLine());
            large = Double.parseDouble(line = br.readLine());

            System.out.print("\n\nEnter size of coffee: ");
            coffeeSize = k.nextLine();

            if(coffeeSize.toLowerCase().equals("small")) {
                addCoffeeName.add(coffeeName);
                addCoffeeSize.add("small");
                addCoffeePrice.add(small);
            } else if(coffeeSize.toLowerCase().equals("medium")) {
                addCoffeeName.add(coffeeName);
                addCoffeeSize.add("medium");
                addCoffeePrice.add(medium);
            } else if(coffeeSize.toLowerCase().equals("large")) {
                addCoffeeName.add(coffeeName);
                addCoffeeSize.add("large");
                addCoffeePrice.add(large);
            }

        } catch (IOException e) {
            System.out.println("Error: " + e);
        }
    }

    void confirmOrder() {
        System.out.println("Customer Name: " + this.custName);
        System.out.println();
        for(int i=0; i<addCoffeeSize.size(); i++) {
            System.out.println(addCoffeeName.get(i) + "(" + addCoffeeSize.get(i) + ")" + "   " + addCoffeePrice.get(i));
            totPrice += addCoffeePrice.get(i);
        }

        System.out.println("Total Price: " + totPrice);
    }
}

public class restaurant {
    public static void main(String args[]) {
        Scanner k = new Scanner(System.in);
        StarBucks obj = new StarBucks();
        String ch, buy;
        
        while(true) {
            System.out.println("Enter your name: ");
            obj.custName = k.nextLine();
            obj.getMenu();
            
            while(true) {
                System.out.print("Enter to add Coffee: (type stop for stop order)");
                ch = k.nextLine();
                if(ch.equals("stop"))
                    break;
                
                obj.order(ch);
            }

            obj.confirmOrder();
            System.out.print("Confirm Bill: " );
            buy = k.nextLine();
            if(buy.equals("yes")) {
                System.out.println("Thank you for buy!");
            } else {
                System.out.println("NExt Time to buy");
            }

            break;
        }
        
    }
}