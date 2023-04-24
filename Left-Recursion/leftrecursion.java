import java.util.*;
import java.io.*;

public class leftrecursion {
    public static void main(String args[]) throws IOException {
        File file = new File("left-recursion.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String s = "";
        while((s=br.readLine()) != null) {
            char NT = s.charAt(0);
            String prod = s.substring(3);
            String[] rules = prod.split("\\|");
            ArrayList<String> alpha = new ArrayList<String>();
            ArrayList<String> beta = new ArrayList<String>();

            for(int i=0; i<rules.length; i++) {
                String rule = rules[i];
                char start = rule.charAt(0);

                if(start == NT) { alpha.add(rule.substring(1)+NT+"'"); }
                else { beta.add(rule+NT+"'"); }
            }

            if(alpha.size() > 0) {
                System.out.print(NT+"->");
                for(int i=0; i<beta.size(); i++) {
                    System.out.print(beta.get(i));
                    if(i+1 != beta.size()) System.out.print("|");
                }
                System.out.println();

                System.out.print(NT+"'->");
                for(int i=0; i<alpha.size(); i++) {
                    System.out.print(alpha.get(i)+"|");
                }
                System.out.print("E\n");
            }
            else {
                System.out.println(s);
            }
        }
    }
}