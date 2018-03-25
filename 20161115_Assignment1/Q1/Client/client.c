#include <sys/socket.h>
#include <sys/types.h>
#include <netinet/in.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <arpa/inet.h>

void gotoxy(int x,int y)
{
 printf("%c[%d;%df",0x1B,y,x);
}

int main(int argc, char *argv[])
{
    system("clear");
    int sockfd = 0;
    int bytesReceived = 0;
    char recvBuff[1024];
    memset(recvBuff, '0', sizeof(recvBuff));
    struct sockaddr_in serv_addr;

    if((sockfd = socket(AF_INET, SOCK_STREAM, 0))< 0)
    {
        printf("\n Error : Could not create socket \n");
        return 1;
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(5000); // port
    char ip[50];
if (argc < 2)
{
    printf("Enter IP address to connect: ");
    gets(ip);
}
else
  strcpy(ip,argv[1]);
  char filename[50];
if(argc<3)
{
  printf("Enter the file to download: ");
  gets(filename);
}
else
{
  strcpy(filename,argv[2]);
}
printf("%s\n",filename );
    serv_addr.sin_addr.s_addr = inet_addr(ip);

    if(connect(sockfd, (struct sockaddr *)&serv_addr, sizeof(serv_addr))<0)
    {
        printf("\n Error : Connect Failed \n");
        return 1;
    }

    printf("Connected to ip: %s : %d\n",inet_ntoa(serv_addr.sin_addr),ntohs(serv_addr.sin_port));

  
  char * pch;
  pch = strtok (filename," ");
  while (pch != NULL)
  {
    FILE *fp;
    char fname[100];
    printf ("pch :%s\n",pch);
    send(sockfd, pch, 256,0);
    read(sockfd, fname, 256);
  //strcat(fname,"AK");
  char ok[100];
  printf("File Name: %s\n",fname);
  printf("Receiving file...");
    long double sz=1;
    int flag=0;
    /* Receive data in chunks of 256 bytes */
    while((bytesReceived = read(sockfd, recvBuff, 1024)) > 0)
    {
      if(bytesReceived>8){
          fp = fopen(fname, "ab");
         if(NULL == fp)
         {
            printf("Error opening file");
            return 1;
         }
        sz++;
        gotoxy(0,4);
        printf("Received: %llf Mb\n",(sz/1024));
        fflush(stdout);
        fwrite(recvBuff, 1,bytesReceived,fp);
    }
    else{
      flag=1;
      printf("\nError: File not present in server's directory\n");
    }
    }
    if(bytesReceived < 0)
    {
        printf("\n Read Error \n");
    }
    if(flag==0)
    printf("\nFile OK....Completed\n");
    pch = strtok (NULL, " ");
  }

  return 0;
}
