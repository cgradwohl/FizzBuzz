// prints intergers i such that,  1<=i<=100
// replaces intergers i such that i%3==0 with Fizz and i%5==0 with Buzz
class FizzBuzz{
    public static void main(String[] args){
        int i;
        for( i=1; i<=100; i++ ){
            if( i%3==0 ) System.out.println(i+": "+"Fizz");
            else if( i%5==0 ) System.out.println(i+": "+"Buzz");
            else System.out.println(i);
        }
    }
}
