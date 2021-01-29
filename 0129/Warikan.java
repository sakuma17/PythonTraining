import java.util.*;
public class Warikan{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		System.out.print("料金を入力>>");
		int price=sc.nextInt();
		System.out.print("人数を入力>>");
		int number=sc.nextInt();
		int payment=price/number;
		System.out.printf("お支払いは%d円です",payment);
	}
}
