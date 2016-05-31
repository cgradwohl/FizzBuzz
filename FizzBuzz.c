#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
    int i;
    for( i=1; i<=100; i++){
        if( i%3==0 ) printf("%d%s\n", i, ": Fizz");
        else if( i%5==0 ) printf("%d%s\n", i, ": Buzz");
        else printf("%d\n", i);
    }
}
