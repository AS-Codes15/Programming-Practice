import java.util.Scanner;

public class power {
    public static int calcPower(int x,int n) {
        if (x==0) {
            return 0;
        }
        if (n==0) {
            return 1;
        }
        int xPownm1=calcPower(x, n-1);
        int xPow=x*xPownm1;
        return xPow;
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
         int n=sc.nextInt();
         int ans=calcPower(x, n);
         System.out.println(ans);
         sc.close();
    }
}
