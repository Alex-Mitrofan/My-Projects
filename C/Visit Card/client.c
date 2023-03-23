#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <errno.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <netdb.h>
#include <string.h>
#include <arpa/inet.h>

/* codul de eroare returnat de anumite apeluri */
extern int errno;

/* portul de conectare la server*/
int port;

int main (int argc, char *argv[])
{
   int sd;			// descriptorul de socket
  struct sockaddr_in server;	// structura folosita pentru conectare 
  char msg[1000];		// mesajul trimis

  /* exista toate argumentele in linia de comanda? */
  if (argc != 2)
    {
      printf ("[client] Sintaxa: %s <port>\n", argv[0]);
      return -1;
    }

  /* stabilim portul */
  port = atoi (argv[1]);

  /* cream socketul */
  if ((sd = socket (AF_INET, SOCK_STREAM, 0)) == -1)
    {
      perror ("[client] Eroare la socket().\n");
      return errno;
    }
  

  /* umplem structura folosita pentru realizarea conexiunii cu serverul */
  /* familia socket-ului */
  server.sin_family = AF_INET;
  /* adresa IP a serverului */
  server.sin_addr.s_addr = inet_addr("127.0.0.1");
  /* portul de conectare */
  server.sin_port = htons (port);


  /* ne conectam la server */
  if (connect (sd, (struct sockaddr *) &server,sizeof (struct sockaddr)) == -1)
    {
      perror ("[client]Eroare la connect().\n");
      return errno;
    }
int ok;

 
 
 
 

 ok=0; 

 while(ok==0){
       
	 bzero (msg, 1000);
	 printf ("[client]Folositi comanda \"start\" pentru a incepe sau comanda \"quit\" pentru a iesi.\n");
	 fflush (stdout);
	 read (0, msg, 1000);
	 //msg[strcspn(msg, "\n")] = 0;
	 if (strncmp(msg,"quit",4)==0 || strncmp(msg,"start",5)==0)
	   {
	     ok=1;
	     /* trimiterea mesajului la server */
	     if (write (sd, msg, 1000) <= 0)
	      {
	       perror ("[client]Eroare la write() spre server.\n");
	       return errno;
	      }
           }
	 else printf("[client]Ati introdus o comanda gresita.\n %s",msg); 
	 }
	 
	 
	 if(strncmp(msg,"quit",4)==0)    //daca primim mesajul "quit" inchidem clientul
         {
          close(sd);
          return 0;
         } 
         if (read(sd, msg, 1000) < 0)
         {
           perror("[client]Eroare la read() de la server.\n");
           return errno;
         }
         printf("%s\n",msg);	 
     
 //}
// else{
 
while(1){
    //sleep(1);
    bzero (msg, 1000);
     
    fflush (stdout);
    read (0, msg, 1000);
    if(strncmp(msg,"quit",4)==0)    //daca primim mesajul "quit" inchidem clientul
    {
      close(sd);
      return 0;
    }
    if (write (sd, msg, 1000) <= 0)
    {
      perror ("[client]Eroare la write() spre server.\n");
      return errno;
    }
   
   if (read (sd, msg, 1000) < 0)
     {
       perror ("[client]Eroare la read() de la server.\n");
       return errno;
     }
     
    
   printf ("%s\n", msg);
  
  
  
 }
 

  /* inchidem conexiunea, am terminat */
  close (sd);
}
