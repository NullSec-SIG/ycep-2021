#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
 volatile int changethis;
 char buffer[64];

 changethis = 0;
 gets(buffer);

 if(changethis == 0x51535254) {
  printf("Congrats!\n");
    FILE *fp;
    char txt[64];
    fp =fopen("flag.txt","r");
    fscanf(fp,"%s",&txt);
    printf(txt);
    fclose(fp);
 } else {
  printf("Try again, you got 0x%08x\n", changethis);
 }
}


