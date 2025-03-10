// Online Java Compiler
// Use this editor to write, compile and run your Java code online
import java.util.Scanner;
class Node{
    int data;
    Node next;
    
    public Node(int data){
        this.data = data;
        this.next = null;
    }
}
public class HelloWorld {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Try programiz.pro");
        Node head = new Node(sc.nextInt());
        head.next = new Node(sc.nextInt());
        head.next.next = new Node(sc.nextInt());
        Node curr = head;
        while(curr!=null){
            System.out.print(curr.data+" ");
            curr = curr.next;
        }
        sc.close();
    }
}