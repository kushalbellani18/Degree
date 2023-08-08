import java.util.*;
import java.io.*;
import java.time.*;
import java.time.format.*;

interface file {
    public abstract void addNewAccount(String n, double a, int no);
    public abstract void modifyAccount(int aNo, double updateMoney);
    public abstract boolean checkAccount(int aNo);
    public abstract String getName(int aNo);
    public abstract double getAmount(int aNo);
    public abstract String getFileName(int aNo);
    public abstract void addHistoryTransaction(int aNo, String status, double newMoney, double subMoney);
}

interface bank extends file{
    public abstract void deposit();
    public abstract void withdraw();
    public abstract void signUp();
    public abstract void signIn();
    public abstract void disHistoryTransaction();
}

class bankOfBaroda implements bank {
    String name, fileName;
    int accountNumber;
    double amount;
    Scanner k = new Scanner(System.in);

    public void disHistoryTransaction() {
        try {
            String lineLoc = "transactionHistory/" + Integer.toString(this.accountNumber) + ".txt";
            FileReader reader = new FileReader(lineLoc);
            BufferedReader br = new BufferedReader(reader);
            String line;

            System.out.println("\t\tTransaction History: \n");
            while((line = br.readLine()) != null) {
                System.out.println(line);
            }
        } catch (IOException e) {
            System.out.println("Error: " + e);
        }
    }

    public void deposit() {
        double addAmount;
        System.out.print("Enter amount money for deposit: ");
        addAmount = k.nextDouble();
        amount += addAmount;

        modifyAccount(this.accountNumber, amount);
        addHistoryTransaction(this.accountNumber, "DEPOSIT", amount, addAmount);
    }

    public void withdraw() {
        double getAmount, totalAmount;

        System.out.print("Enter amount money for withdraw: ");
        getAmount = k.nextDouble();

        totalAmount = getAmount(this.accountNumber);

        if(getAmount <= totalAmount) {
            amount -= getAmount;

            modifyAccount(this.accountNumber, amount);
            addHistoryTransaction(this.accountNumber, "WITHDRAW", amount, getAmount);
        } else {
            System.out.println("Sorry Bye!!!");
        }
    }

    public void modifyAccount(int aNo, double updateMoney){
        try {
            FileReader reader = new FileReader("bankAccountList.txt");
            BufferedReader  br = new BufferedReader(reader);

            String line, oldSub, newSub, oldContext, newContext;
            oldContext = "";
            oldSub = "";
            newSub = "";

            while((line = br.readLine()) != null) 
                oldContext += line + "\n";
            
            reader = new FileReader("bankAccountList.txt");
            br = new BufferedReader(reader);
            String line2, line3;

            while((line2 = br.readLine()) != null) {
                if(line2.equals(Integer.toString(aNo))) {
                    line2 = br.readLine();
                    line2 = br.readLine();
                    break;
                }
            }

            reader = new FileReader("bankAccountList.txt");
            br = new BufferedReader(reader);
            line3 = br.readLine();
            while(line3 != null) {
                if(line3.equals(Integer.toString(aNo)))
                    break;
                line3 = br.readLine();
            }

            while(line3 != null) {
                if(line3.equals("----"))
                    break;

                if(line3.equals(line2)) {
                    newSub += Double.toString(updateMoney) + "\n";
                } else {
                    newSub += line3 + "\n";
                }
                oldSub += line3 + "\n";

                line3 = br.readLine();
            }


            newContext = oldContext.replaceAll(oldSub, newSub);

            FileWriter writer = new FileWriter("bankAccountList.txt");
            writer.write(newContext);

            br.close();
            reader.close();
            writer.close();
        } catch (IOException e) {
            System.out.println("Error:  " + e);
        }
    }

    public void addHistoryTransaction(int aNo, String status, double newMoney, double subMoney) {
        try {
            String lineLoc;
            lineLoc = "transactionHistory/" + Integer.toString(aNo) + ".txt";
            FileWriter writer = new FileWriter(lineLoc, true);
            BufferedWriter bw = new BufferedWriter(writer);
            DateTimeFormatter myFormatDate = DateTimeFormatter.ofPattern("dd-MM-yyyy HH:mm:ss");
            LocalDateTime myObjDate = LocalDateTime.now();
            String formattedDate = myObjDate.format(myFormatDate);

            bw.append(status + ": ( " + formattedDate + " )");
            bw.append("\n");
            if(status.equals("DEPOSIT"))
                bw.append("Old Money: " + Double.toString(newMoney - subMoney));
            else if(status.equals("WITHDRAW"))
                bw.append("Old Money: " + Double.toString(newMoney + subMoney));
            bw.append("\n");
            bw.append("Update Money: " + Double.toString(newMoney));
            bw.append("\n");
            bw.append("----");
            bw.append("\n");

            bw.close();
            writer.close();

        } catch (IOException e) {
            System.out.println("Error: " + e);
        }
    }

    public void signIn() {
        int aNo;

        System.out.println("Enter your account number:  ");
        aNo = k.nextInt();

        if(checkAccount(aNo)) {
            System.out.println("Found\n");
            this.accountNumber = aNo;
            this.name = getName(aNo);
            this.amount = getAmount(aNo);
            this.fileName = getFileName(aNo);

            System.out.println("\n\nHi, " + this.name + "\n\n");
            int choice;

            do{
                System.out.println("    1) Deposit");
                System.out.println("    2) Withdraw");
                System.out.println("    3) Display");
                System.out.println("    4) Transaction History");
                System.out.println("    0) Exit");
                System.out.print("Enter your choice? ");
                choice = k.nextInt();

                switch(choice) {
                    case 0: System.out.println("Exit!!!"); break;
                    case 1: deposit(); break;
                    case 2: withdraw(); break;
                    case 3: System.out.println("\n\n\tYour totally amount: " + this.amount); break;
                    case 4: disHistoryTransaction(); break;
                    default: System.out.println("INVALID TRY AGAIN!!");
                }
            }while (choice != 0);

        } else {
            System.out.println("\t\t Error your account number\n \tPlease Try again!");
        }
    }

    public boolean checkAccount(int aNo) {
        try {
            FileReader reader = new FileReader("bankAccountList.txt");
            BufferedReader br = new BufferedReader(reader);

            String line;

            while((line = br.readLine()) != null) {
                if(line.equals(Integer.toString(aNo))) {
                    br.close();
                    reader.close();
                    return true;
                }
            }

            br.close();
            reader.close();
        } catch (IOException e) {
            System.out.println("Error: " + e);
        }
        return false;
    }

    public String getName(int aNo) {
        try {
            FileReader reader = new FileReader("bankAccountList.txt");
            BufferedReader br = new BufferedReader(reader);

            String line;

            while((line = br.readLine()) != null) {
                if(line.equals(Integer.toString(aNo))) {
                    line = br.readLine();
                    return line;
                }
            }    

            br.close();
            reader.close();

        } catch (IOException e) {
            System.out.println("Error: " + e);
        }

        return "";
    }

    public double getAmount(int aNo) {
        try {
            FileReader reader = new FileReader("bankAccountList.txt");
            BufferedReader br = new BufferedReader(reader);

            String line;

            while((line = br.readLine()) != null) {
                if(line.equals(Integer.toString(aNo))) {
                    line = br.readLine();
                    line = br.readLine();
                    return Double.parseDouble(line);
                }
            }    

            br.close();
            reader.close();

        } catch (IOException e) {
            System.out.println("Error: " + e);
        }

        return 0.0;
    }

    public String getFileName(int aNo) {
        try {   
            FileReader reader = new FileReader("bankAccountList.txt");
            BufferedReader br = new BufferedReader(reader);
            String line;

            while((line = br.readLine()) != null) {
                if(line.equals(Integer.toString(aNo))) {
                    line = br.readLine();
                    line = br.readLine();
                    line = br.readLine();
                    break;
                }
            }

            return line;
        } catch (IOException e) {
            System.out.println("Error: " + e);
        }

        return "";
    }

    public void signUp() {
        String n;
        double am;
        int an;
        
        System.out.print("Enter your name:  ");
        n = k.nextLine();
        System.out.print("Enter you have money in your new bank:  ");
        am = k.nextDouble();
        Random rand = new Random();
        an = rand.nextInt(900000000) + 1;
        System.out.println("\n\tYour account Number is " + an);
        System.out.print("\tNote:- Please dont share to everyone");

        addNewAccount(n, am, an);
    }

    public void addNewAccount(String n, double a, int no) {
        try {
            FileWriter writer = new FileWriter("bankAccountList.txt", true);
            BufferedWriter bw = new BufferedWriter(writer);

            bw.append(Integer.toString(no));
            bw.append("\n");
            bw.append(n);
            bw.append("\n");
            bw.append(Double.toString(a));
            bw.append("\n");
            bw.append(Integer.toString(no)+".txt");
            bw.append("\n");
            bw.append("----");
            bw.append("\n");


            bw.close();
            writer.close();

            try {
                File obj = new File("transactionHistory/" + Integer.toString(no) + ".txt");
                if(obj.createNewFile())
                    System.out.println("DONE");
                else 
                    System.out.print("OOPS!");
            } catch (IOException e) {
                System.out.println("Error: " + e);
            }

        } catch (IOException e) {
            System.out.println("Error: " + e);
        }
    }
}

public class bankAcc {
    public static void main(String args[]) {
        bankOfBaroda bob = new bankOfBaroda();
        Scanner k = new Scanner(System.in);
        int choice;
        int count=0;

        System.out.println("\t\t +-------------------+");
        System.out.println("\t\t |                   |");
        System.out.println("\t\t |  Welcome to Bank !|");
        System.out.println("\t\t |                   |");
        System.out.println("\t\t +-------------------+");

        do {
            System.out.println("1) Sign In");
            System.out.println("2) Sign Up");
            System.out.println("0) Shutdown");
            System.out.print("Enter your choice? ");
            choice = k.nextInt();

            switch(choice) {
                case 0: System.out.println("\t\tExit!!\n"); break;
                case 1: bob.signIn(); 
                        if(count == 3) {
                            choice = 0;
                            System.out.println("\n\t\tSorry!!! Exit\n");
                            break;
                        }

                        count++; 
                        break;
                case 2: bob.signUp(); break;
                default: System.out.println("\t Invalid Try Again\n");
            }

        } while (choice != 0);
    }
}