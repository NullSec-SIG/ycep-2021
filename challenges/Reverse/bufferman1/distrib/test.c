#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int changethis;
  char buffer[64];

  changethis = 0;
  gets(buffer);

  if(changethis != 0) {
    printf("Congrats!\n");
    FILE *fp;
    char txt[64];
    fp =fopen("flag.txt","r");
    fscanf(fp,"%s",&txt);
    printf(txt);
    fclose(fp);
  } else {
    printf("Try again!!!\n");
  }
}

