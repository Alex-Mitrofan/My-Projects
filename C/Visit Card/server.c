
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/time.h>
#include <netinet/in.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>
#include <arpa/inet.h>
#include <string.h>
#include <sqlite3.h>
#include <stdlib.h>
#include <signal.h>
#include <pthread.h>


/* portul folosit */

#define PORT 2728
sqlite3 *db;

int quit=0;
 
 
static void *thread(void *);

 
 
static int  callback(void *x, int nr, char **data, char **col)
{   
    int i;
    strcat(x,"\n");
    for (i = 1; i < nr; i++) {
       strcat(x,col[i]);
       strcat(x,": ");
       strcat(x,data[i]);
       strcat(x,"\n");
  
    }
      
     return 0;
 
}

static int  callback2(void *x, int nr, char **data, char **col)
{   
     strcat(x,data[0]);
     return 0;
 
}

 /*
 void EXIT(int fd)
 {
   printf ("[server] S-a deconectat clientul cu descriptorul %d.\n",fd);
   fflush (stdout);
   close (fd);		/* inchidem conexiunea cu clientul  
   FD_CLR (fd, &actfds);/* scoatem si din multime  	  
  }
*/

struct vcard{
   char nume[51];
   char prenume[51];
   char email[21];
   char companie[21];
   char profesie[21];
   char mobil[21];
   char adresa[51];
   char tara[21];
   char website[21];
   char username[21];
   char password[21];
};

 typedef struct thData
{
  int id; //id unic thread 
  int cl;       //descriptor 
  sqlite3 *db;  //baza de date
 
  int nume, prenume, email, companie, profesie, mobil, adresa, tara, website; //useless
                   
  int start,login,registerr, meniu, adauga, search, edit, sterge;          //usefull
  int confirm;
  int loggedin;
  
} thData;


extern int errno;		/* eroarea returnata de unele apeluri */

/* functie de convertire a adresei IP a clientului in sir de caractere */
char * conv_addr (struct sockaddr_in address)
{
  static char str[25];
  char port[7];

  /* adresa IP a clientului */
  strcpy (str, inet_ntoa (address.sin_addr));	
  /* portul utilizat de client */
  bzero (port, 7);
  sprintf (port, ":%d", ntohs (address.sin_port));	
  strcat (str, port);
  return (str);
}

/* programul */
int main ()
{
  struct sockaddr_in server;	/* structurile pentru server si clienti */
  struct sockaddr_in from;
  fd_set readfds;		/* multimea descriptorilor de citire */
 
  struct timeval tv;		/* structura de timp pentru select() */
  int sd, client;		/* descriptori de socket */
  int optval=1; 			/* optiune folosita pentru setsockopt()*/ 
  int fd;			/* descriptor folosit pentru parcurgerea listelor de descriptori */
  int nfds;			/* numarul maxim de descriptori */
  int len;			/* lungimea structurii sockaddr_in */
  
  pthread_t th[100]; 
  int i=0;   //contor pt threaduri

  sqlite3_open("DATA.db", &db);

  /* creare socket */
  int on=1;
  if ((sd = socket (AF_INET, SOCK_STREAM, 0)) == -1)
    {
      perror ("[server] Eroare la socket().\n");
      return errno;
    }

  /*setam pentru socket optiunea SO_REUSEADDR */ 
  setsockopt(sd, SOL_SOCKET, SO_REUSEADDR,&on,sizeof(on));

  /* pregatim structurile de date */
  bzero (&server, sizeof (server));

  /* umplem structura folosita de server */
  server.sin_family = AF_INET;
  server.sin_addr.s_addr = htonl (INADDR_ANY);
  server.sin_port = htons (PORT);

  /* atasam socketul */
  if (bind (sd, (struct sockaddr *) &server, sizeof (struct sockaddr)) == -1)
    {
      perror ("[server] Eroare la bind().\n");
      return errno;
    }

  /* punem serverul sa asculte daca vin clienti sa se conecteze */
  if (listen (sd, 2) == -1)
    {
      perror ("[server] Eroare la listen().\n");
      return errno;
    }
 
        
  /* servim in mod concurent clientii... */
  while (1)
    {
      int client;    
      thData *td;
      int len=sizeof(from);
      
      printf ("[server] Asteptam la portul %d...\n", PORT);
      fflush (stdout); 
      
      if ((client = accept(sd, (struct sockaddr *)&from, &len)) < 0)
      {
         perror("[server]Eroare la accept().\n");
         continue;
      }
     
     
       printf("[server] S-a conectat clientul cu descriptorul %d, de la adresa %s.\n",client, conv_addr (from));
       fflush (stdout);
	 
	
      	
	   td = (struct thData *)malloc(sizeof(struct thData));
           td->id = i++;
           td->cl = client;
           td->db = db;
           td->start=0; 
           td->meniu=0;
           td->nume=0; td->prenume=0; td->email=0; td->companie=0; td->profesie=0; td->mobil=0;
           td->adresa=0; td->tara=0; td->website=0; 
           td->adauga=0; td->search=0; td->edit=0; td->sterge=0, td->login=0, td->registerr=0;
           td->confirm=0;
           td->loggedin=0;

    pthread_create(&th[i], NULL, &thread, td);

	}

};
static void *thread(void *arg)
{
   struct thData t;
   char buffer[1000];		 // mesajul  
   int bytes;			 // numarul de octeti cititi/scrisi  
   char msg[1000];	        //mesajul primit de la client 
   char msgrasp[1000]=" ";      //mesaj de raspuns pentru client
   struct vcard info;        //structura client
   int ok=0;                    
   char sql[1000];             //query pt baza de date
   char *err_msg = 0;         //pt sql
   int rasp;                  //al 2lea callback
   char msgpass[1000]=" ";     //mesajul de la parole pt parole gresite
   
   while (1)
   {
     t = *((struct thData *)arg);
     printf("[thread]- %d - Asteptam mesajul...\n", t.id);
     fflush(stdout);
     pthread_detach(pthread_self());
     
 
     bytes = read (t.cl, msg, sizeof (buffer));
     if (bytes < 0)
     {
        printf("[Thread %d]\n", t.id);
        perror ("Eroare la read() de la client.\n");
        return 0;
     }   
     
  
                     //################START############################
      if(t.start==0)
     {
       
         if(strncmp(msg,"start",5)==0)
         {
            t.start=1;
            printf("[Thread %d]Am primit mesajul start.\n",t.id);
         }
         else if (strncmp(msg, "quit", 4) == 0)
         {
          close(t.cl);
          break;
         }
      } 
   //###############################login register####################
LOGIN:
   if(t.start==1 && t.login==0)
   {
    bzero(msgrasp,1000);
    strcat(msgrasp,msgpass);
    strcat(msgrasp,"[client][client]Introduceti cifra corespunzatoare comenzii:\n1.login;\n2.register.\n");
    if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
    {
       perror ("[server] Eroare la write() catre client.\n");
       return 0;
    }
    bytes = read (t.cl, msg, sizeof (buffer));
    if (bytes < 0)
    {
       perror ("Eroare la read() de la client.\n");
       return 0;
    }
    if (strncmp(msg, "quit", 4) == 0)
    {
       close(t.cl);
       break;
    }
    if(msg[0]=='1' || msg[0]=='2')
    {
      printf("[server]Comanda meniu valida.\n");
      if(msg[0]=='1') t.login=1;
      else if(msg[0]=='2') t.registerr=1;
    
    }
    else while(t.login==0 && t.registerr==0)            //#############CIFRA GRESITA MENIU#####################
          {
           bzero(msgrasp,1000);
           strcat(msgrasp,"[client]Ati introdus o cifra gresita.\n");
           if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
           {
                perror ("[server] Eroare la write() catre client.\n");
                return 0;
           }
           bytes = read (t.cl, msg, sizeof (buffer));
           if (bytes < 0)
           {
                 perror ("Eroare la read() de la client.\n");
                 return 0;
           }
          if (strncmp(msg, "quit", 4) == 0)
           {
                 close(t.cl);
                 break;
           }
         if(msg[0]=='1' || msg[0]=='2')
         {
          t.login=1; 
          if(msg[0]=='1')t.login=1;
          else if(msg[0]=='2') t.registerr=1;
         }
       }   
      
      
  if(t.registerr==1)
  {                         //#######USERNAME###########
    bzero(msgrasp,1000);
    strcat(msgrasp,"[client]Introduceti un username:\n");
    if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
    {
      perror ("[server] Eroare la write() catre client.\n");
      return 0;
    }
    bytes = read (t.cl, msg, sizeof (buffer));
    if (bytes < 0)
    {
      perror ("Eroare la read() de la client.\n");
      return 0;
    }
   if (strncmp(msg, "quit", 4) == 0)
   {
      close(t.cl);
      break;
   }
   
   
   bzero(msgrasp,1000);
   msg[strcspn(msg, "\n")] = 0;
   strcpy(info.username,msg);
   sprintf(sql, "select count(*) from users where username like '%s';",info.username);
   sqlite3_exec(t.db, sql, callback2, msgrasp, &err_msg);
   //msgrasp[strcspn(msgrasp, "\n")] = 0;
  
   printf("%s\n",msgrasp);
 
    if(msgrasp[0] !='0')   //#####################USERNAME DEJA EXISTENT#####################
    {
     int ok=0;
     while(ok==0)
     {
	     bzero(msgrasp,1000);
	     strcat(msgrasp,"[client]Username deja existent. Alege alt username:\n");
	     if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
	     {
		perror ("[server] Eroare la write() catre client.\n");
		return 0;
	     }
	     bytes = read (t.cl, msg, sizeof (buffer));
	     if (bytes < 0)
	     {
		perror ("Eroare la read() de la client.\n");
		return 0;
	     }
	     if (strncmp(msg, "quit", 4) == 0)
	     {
		 close(t.cl);
		 break;
	     }
	     bzero(msgrasp,1000);
	     msg[strcspn(msg, "\n")] = 0;
	     strcpy(info.username,msg);
	     sprintf(sql, "select count(*) from users where username like '%s';",info.username);
	     sqlite3_exec(t.db, sql, callback2, msgrasp, &err_msg);
             if(msgrasp[0] =='0') ok=1;
            
            printf("%s\n",msgrasp);
      }
    }
      if(msgrasp[0] =='0')   //####################USERNAME VALID#################
         {                              //#############PAROLA######################
          msg[strcspn(msg, "\n")] = 0;
          strcpy(info.username,msg);
          bzero(msgrasp,1000);
	   strcat(msgrasp,"[client]Username valid. Introduceti parola:\n");
	   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
	     {
		perror ("[server] Eroare la write() catre client.\n");
		return 0;
	     }
	     bytes = read (t.cl, msg, sizeof (buffer));
	     if (bytes < 0)
	     {
		perror ("Eroare la read() de la client.\n");
		return 0;
	     }
	     if (strncmp(msg, "quit", 4) == 0)
	     {
		 close(t.cl);
		 break;
	     } 
	    msg[strcspn(msg, "\n")] = 0;
            strcpy(info.password,msg);  
     
                                                    //#############CONFIRMARE CREARE CONT###############
          bzero(msgrasp,1000);
          strcat(msgrasp,"[client]Confirmati crearea contului [Y/n]\n");
          if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
	     {
		perror ("[server] Eroare la write() catre client.\n");
		return 0;
	     }
	     bytes = read (t.cl, msg, sizeof (buffer));
	     if (bytes < 0)
	     {
		perror ("Eroare la read() de la client.\n");
		return 0;
	     }
	     if (strncmp(msg, "quit", 4) == 0)
	     {
		 close(t.cl);
		 break;
	     } 
	    msg[strcspn(msg, "\n")] = 0;
	    ok=0;
		   while(ok==0)                                 //################ALTA LITERA IN AFARA DE N SI Y###############
		   {
		     if(msg[0]=='y' || msg[0]=='Y' || msg[0]=='n' || msg[0]=='N' )
		       ok=1;
		     else {
		              bzero(msgrasp,1000);
		              strcat(msgrasp,"[client]Ati introdus o comanda gresita.\n");
		              if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		              {
		                perror ("[server] Eroare la write() catre client.\n");
		                return 0;
		              }
		              bytes = read (t.cl, msg, sizeof (buffer));
		              if (bytes < 0)
		              {
		                perror ("Eroare la read() de la client.\n");
		                return 0;
		              }  
		              if (strncmp(msg, "quit", 4) == 0)
                               {
                                close(t.cl);
                                break;
                               }
                              
		               printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
		     
		           }		     
		   }
		   if(msg[0]=='y' || msg[0]=='Y')
		    {
		       sprintf(sql, "insert into users values('%s','%s')",info.username, info.password);
		       sqlite3_exec(t.db, sql, 0, 0, &err_msg);
		 
		      printf("[Thread %d]Am salvat in baza de date.\n",t.id);
		      printf("%s\n",sql);  
                     
                     t.registerr=0;
		      goto LOGIN;  
		    }
		   else if(msg[0]=='n' || msg[0]=='N')
		        {
                        t.registerr=0;
		         goto LOGIN; 
		        }		     
	    }
		  		  
            
                         
         }
  
   
   
     
  
  }
                         //###############################LOGIN###########################
 
     if(t.login==1)
     {
      bzero(msgrasp,1000);
      strcat(msgrasp,"[client]Introduceti username-ul:\n");
      if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
      {
        perror ("[server] Eroare la write() catre client.\n");
        return 0;
      }
      bytes = read (t.cl, msg, sizeof (buffer));
      if (bytes < 0)
      {
         perror ("Eroare la read() de la client.\n");
         return 0;
      }
      if (strncmp(msg, "quit", 4) == 0)
      {
         close(t.cl);
         break;
      }
      
      bzero(msgrasp,1000);
      msg[strcspn(msg, "\n")] = 0;
      strcpy(info.username,msg);
      sprintf(sql, "select count(*) from users where username like '%s';",info.username);
      sqlite3_exec(t.db, sql, callback2, msgrasp, &err_msg);
      
      if(msgrasp[0] =='0')
      {
        ok=0;
        while(ok==0)                //#########LOGIN##########INTRODUCETI USERNAME#################
        {
	     bzero(msgrasp,1000);
	     strcat(msgrasp,"[client]Acest username nu exista. Incearca din nou:\n");
	     if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
	     {
		perror ("[server] Eroare la write() catre client.\n");
		return 0;
	     }
	     bytes = read (t.cl, msg, sizeof (buffer));
	     if (bytes < 0)
	     {
		perror ("Eroare la read() de la client.\n");
		return 0;
	     }
	     if (strncmp(msg, "quit", 4) == 0)
	     {
		 close(t.cl);
		 break;
	     }
	     bzero(msgrasp,1000);
	     msg[strcspn(msg, "\n")] = 0;
	     strcpy(info.username,msg);
	     sprintf(sql, "select count(*) from users where username like '%s';",info.username);
	     sqlite3_exec(t.db, sql, callback2, msgrasp, &err_msg);
             if(msgrasp[0] !='0') ok=1;
            
            printf("%s\n",msgrasp);
       }
      }
       if(msgrasp[0] !='0')                    //##########LOGIN#############INTRODUCETI PAROLA######################
       {
         bzero(msgrasp,1000);
         strcat(msgrasp,"[client]Introduceti parola:\n");
         if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
         {
           perror ("[server] Eroare la write() catre client.\n");
           return 0;
         }
         bytes = read (t.cl, msg, sizeof (buffer));
         if (bytes < 0)
         {
           perror ("Eroare la read() de la client.\n");
           return 0;
          } 
         if (strncmp(msg, "quit", 4) == 0)
         {
             close(t.cl);
             break;
          }
         msg[strcspn(msg, "\n")] = 0;
         strcpy(info.password,msg);
         bzero(msgrasp,1000);
         sprintf(sql, "select count(*) from users where username like '%s' and password like '%s';",info.username, info.password);
	 sqlite3_exec(t.db, sql, callback2, msgrasp, &err_msg);
       }
        if(msgrasp[0]=='0')
        {
         bzero(msgpass,1000);
         strcat(msgpass,"[client]Ati introdus o parola gresita.\n");
         t.login=0;
         goto LOGIN;
                 
        }     
      
      
     } 
      
                      //##################################MENIU##################################
MENIU:      //label goto
     if ( t.start==1 &&  t.meniu==0)
               {
               
             //#############################MENIU############################
                   bzero(msgrasp,1000);
                   strcat(msgrasp,"[client]Introduceti cifra corespunzatoare comenzii:\n1.adaugare;\n2.vizualizare;\n");
                   strcat(msgrasp,"3.editare;\n4.stergere.\n");
                   strcat(msgrasp,"Folositi comanda \"home\" pentru a reveni la meniul principal.\n");
                   strcat(msgrasp,"Folositi comanda \"log out\" pentru a va deconecta.\n");
                    if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
                    {
                      perror ("[server] Eroare la write() catre client.\n");
                      return 0;
                    }
                    bytes = read (t.cl, msg, sizeof (buffer));
                    if (bytes < 0)
                    {
                      perror ("Eroare la read() de la client.\n");
                      return 0;
                    }
                    if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                    if (strncmp(msg, "log out", 7) == 0)
                    {
                     goto LOGIN;
                     break;
                    }
                    if(msg[0]=='1' || msg[0]=='2' || msg[0]=='3' || msg[0]=='4')
                    {
                      t.meniu=1;   
                      printf("[server]Comanda meniu valida.\n");
                      
                      if(msg[0]=='1') t.adauga=1;
                      else if(msg[0]=='2') t.search=1;
                      else if(msg[0]=='3') t.edit=1;
                      else if(msg[0]=='4') t.sterge=1;
                    }
                    else while(t.meniu==0)            //#############CIFRA GRESITA MENIU#####################
                            {
                              bzero(msgrasp,1000);
                              strcat(msgrasp,"[client]Ati introdus o cifra gresita.\n");
                              if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
                                {
                                 perror ("[server] Eroare la write() catre client.\n");
                                 return 0;
                                }
                              bytes = read (t.cl, msg, sizeof (buffer));
                              if (bytes < 0)
                                {
                                 perror ("Eroare la read() de la client.\n");
                                 return 0;
                                }
                              if (strncmp(msg, "quit", 4) == 0)
                               {
                                close(t.cl);
                                break;
                               }
                               if (strncmp(msg, "log out", 7) == 0)
                               {
                                goto LOGIN;
                                break;
                               }
                              if(msg[0]=='1' || msg[0]=='2' || msg[0]=='3' || msg[0]=='4')
                                {
                                 t.meniu=1; 
                                 if(msg[0]=='1')t.adauga=1;
                                 else if(msg[0]=='2') t.search=1;
                                 else if(msg[0]=='3') t.edit=1;
                                 else if(msg[0]=='4') t.sterge=1;  
                                 printf("[server]Comanda meniu valida.\n");
                                }
                            }  
                }
       //#########################FUNCTIA DE ADAUGARE####################################################################
     
        if(t.meniu==1 && t.adauga==1)
        {
               if(t.nume==0)       //##################NUME#####################
		  {
		   bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Introduceti numele:\n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
		   if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.adauga=0;
                   goto LOGIN;
                   break;
                   }
		   msg[strcspn(msg, "\n")] = 0;
		   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
		   
		   strcpy(info.nume,msg);          //salvam in struct-ul de tip vcard numele
		   //t.nume=1;
		  }
		  
		  if(t.prenume==0)       //##################PRENUME#####################
		  {
		   bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Introduceti prenumele:\n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
                  if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.adauga=0;
                   goto LOGIN;
                   break;
                   }
		   msg[strcspn(msg, "\n")] = 0;
		   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
		   
		   strcpy(info.prenume,msg);           
		   //t.prenume=1;
		  }
		  if(t.email==0)       //##################EMAIL#####################
		  {
		   bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Introduceti adresa de email:\n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
                  if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.adauga=0;
                   goto LOGIN;
                   break;
                   }
		   msg[strcspn(msg, "\n")] = 0;
		   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
		   
		   strcpy(info.email,msg);           
		   //t.prenume=1;
		  }
		  if(t.mobil==0)       //##################MOBIL#####################
		  {
		   bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Introduceti numarul de telefon mobil:\n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
                  if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.adauga=0;
                   goto LOGIN;
                   break;
                   }
		   msg[strcspn(msg, "\n")] = 0;
		   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
		   
		   strcpy(info.mobil,msg);           
		   //t.prenume=1;
		  }
		  if(t.adresa==0)       //##################adresa#####################
		  {
		   bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Introduceti adresa:\n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
                  if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.adauga=0;
                   goto LOGIN;
                   break;
                   }
		   msg[strcspn(msg, "\n")] = 0;
		   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
		   
		   strcpy(info.adresa,msg);           
		   //t.prenume=1;
		  }
		  if(t.website==0)       //##################WEBSITE#####################
		  {
		   bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Introduceti websiteul:\n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
                  if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.adauga=0;
                   goto LOGIN;
                   break;
                   }
		   msg[strcspn(msg, "\n")] = 0;
		   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
		   
		   strcpy(info.website,msg);           
		 
		  }
		  if(t.confirm==0)         //#################CONFIRMA SALVAREA IN BAZA DE DATE##############
		  {
		   bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Confirma salvarea vCardului: [Y/n] \n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
                  if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.adauga=0;
                   goto LOGIN;
                   break;
                   }
		   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
		   
		   ok=0;
		   while(ok==0)                                 //################ALTA LITERA IN AFARA DE N SI Y###############
		   {
		     if(msg[0]=='y' || msg[0]=='Y' || msg[0]=='n' || msg[0]=='N' )
		       ok=1;
		     else {
		              bzero(msgrasp,1000);
		              strcat(msgrasp,"[client]Ati introdus o comanda gresita.\n");
		              if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		              {
		                perror ("[server] Eroare la write() catre client.\n");
		                return 0;
		              }
		              bytes = read (t.cl, msg, sizeof (buffer));
		              if (bytes < 0)
		              {
		                perror ("Eroare la read() de la client.\n");
		                return 0;
		              }  
		              if (strncmp(msg, "quit", 4) == 0)
                               {
                                close(t.cl);
                                break;
                               }
                             if(strncmp(msg,"home",4)==0)
                             {
				 t.meniu=0;
				 t.adauga=0;
				 t.search=0;
				 t.edit=0;
				 t.sterge=0;
				 goto MENIU;                  
			      }
			      if (strncmp(msg, "log out", 7) == 0)
                             {
                                t.adauga=0;
                                goto LOGIN;
                                break;
                              }
		               printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
		     
		           }		     
		   }
		   if(msg[0]=='y' || msg[0]=='Y')
		    {
		      msg[strcspn(msg, "\n")] = 0;
                
		      
		       sprintf(sql,"insert into vcard values('%s','%s','%s','%s','%s','%s','%s')", info.username,info.nume,info.prenume,info.email,info.mobil,info.adresa,info.website);
		       sqlite3_exec(t.db, sql, callback, msgrasp, &err_msg);
		       
		       printf("%s\n",info.username);
		       printf("%s\n",info.nume);
		       printf("%s\n",info.prenume);
		       printf("%s\n",info.email);
		       printf("%s\n",info.mobil);
		       printf("%s\n",info.adresa);
		       printf("%s\n",info.website);
		 
		      printf("[Thread %d]Am salvat in baza de date.\n",t.id);
		      printf("%s\n",sql);  
		         t.meniu=0;
		         t.adauga=0;
		         t.search=0;
		         t.edit=0;
		         t.sterge=0;
		      goto MENIU;  
		    }
		   else if(msg[0]=='n' || msg[0]=='N')
		        {
		         t.meniu=0;
		         t.adauga=0;
		         t.search=0;
		         t.edit=0;
		         t.sterge=0;
		         goto MENIU; 
		        }		     
		  }
		  		  
       }
        //####################################FUNCTIA DE VIZUALIZARE############################
        
     int gresit=0;
     char msgerror[1000]=" ";    //folosit pentru AGAIN cand se introduce un nume necorelat cu userul
       if(t.meniu==1 && t.search==1)
       {        
   

  AGAIN:     
            bzero(msgrasp,1000);     
            if(gresit==1)
                   strcpy(msgrasp,msgerror);
          //  printf("%s\n",msgerror);
        //    printf("%s\n",msgrasp);
	    strcat(msgrasp,"[client]Introduceti numele vcardului.\n");
	    if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
	   bytes = read (t.cl, msg, sizeof (buffer));
	   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
	   if (strncmp(msg, "quit", 4) == 0)
                  {
                     close(t.cl);
                     break;
                  }
           if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
           if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.search=0;
                   goto LOGIN;
                   break;
                   }	   
	   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
	   
	    bzero(msgrasp,1000);
	    msg[strcspn(msg, "\n")] = 0;
	    strcpy(info.nume,msg);             
	    sprintf(sql, "select count(*) from vcard where username like '%s' and trim(nume) like '%s';",info.username,info.nume);
	    sqlite3_exec(t.db, sql, callback2, msgrasp, &err_msg);
	 //   printf("USER SI NUME: %s %s\n",info.username,info.nume);
            if(msgrasp[0] =='0')  
                 {
                   bzero(msgerror,1000);
                   sprintf(msgerror,"[client]Nu exista niciun vcard cu numele %s in baza de date a utilizatorului %s.\n",info.nume,info.username);
                 //  printf("NUME USER %s %s\n",info.nume,info.username);
                   gresit=1;
                    printf("%s\n",msgerror);
                   goto AGAIN;
                 }
	 
	 //############################
	   gresit=0;
	   msg[strcspn(msg, "\n")] = 0;
	   strcpy(info.nume,msg);
	   printf("%s",info.nume);
	   sprintf(sql,"select * from vcard where trim(nume) like '%s' and username like '%s';",info.nume,info.username);
 
 	  
           bzero(msgrasp,1000);
	   sqlite3_exec(t.db, sql, callback, msgrasp,NULL);
	   
	   
	    if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   } 
	  printf("\n%s",msgrasp );	
	  bytes = read (t.cl, msg, sizeof (buffer));
	   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
	   if (strncmp(msg, "quit", 4) == 0)
                  {
                     close(t.cl);
                     break;
                  }
           if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
           if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.search=0;
                   goto LOGIN;
                   break;
                   }	   
	   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);    
	   
	   //##########asteapta o comanda valida#######
	   ok=0;
	   while(ok==0)
	   {
	    bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Introduceti una dintre comenzile \"quit\",\"home\" sau \"log out\".\n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
                  if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.search=0;
                   goto LOGIN;
                   break;
                   }
	   
	   }
	       
       
       }
         //########################################FUNCTIA DE EDITARE#########################################
       if(t.meniu==1 && t.edit==1)
       {
         bzero(msgrasp,1000);
	  strcat(msgrasp,"[client]Introdu cifra corespunzatoare campului pe care vrei sa-l editezi:\n");
	  strcat(msgrasp,"1.nume;\n2.prenume;\n3.email;\n4.mobil;\n5.adresa;\n6.website;\n");
          if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
	   bytes = read (t.cl, msg, sizeof (buffer));
	   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
	   if (strncmp(msg, "quit", 4) == 0)
                  {
                     close(t.cl);
                     break;
                  }
           if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
           if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.search=0;
                   goto LOGIN;
                   break;
                   }	   
	   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
	   
	   
	   char camp[21];       
           if(msg[0]=='1') strcpy(camp,"nume");
           else if(msg[0]=='2') strcpy(camp,"prenume");
           else if(msg[0]=='3') strcpy(camp,"email");
           else if(msg[0]=='4') strcpy(camp,"mobil");
           else if(msg[0]=='5') strcpy(camp,"adresa");
           else if(msg[0]=='6') strcpy(camp,"website");
	  
	    bzero(msgrasp,1000);
	    strcat(msgrasp,"[client]Introdu modificarea:\n");
	    if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
	   bytes = read (t.cl, msg, sizeof (buffer));
	   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
	   if (strncmp(msg, "quit", 4) == 0)
                  {
                     close(t.cl);
                     break;
                  }
      	
          printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg); 
          msg[strcspn(msg, "\n")] = 0;
          strcpy(info.password,msg);         //warning la sprintf
          bzero(msgrasp,1000);
          
          sprintf(sql,"update vcard set '%s' = '%s' where username='%s';",camp,info.password,info.username);
	  sqlite3_exec(t.db, sql, callback2, msgrasp, &err_msg);
	  
	  
	  bzero(msgrasp,1000);
	  strcat(msgrasp,"[client]Modificare efectuata cu succes:\n");
	  if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
	  
	  bytes = read (t.cl, msg, sizeof (buffer));
	   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
	   if (strncmp(msg, "quit", 4) == 0)
                  {
                     close(t.cl);
                     break;
                  }
           if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
           if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.search=0;
                   goto LOGIN;
                   break;
                   }	   
	   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
          
           //##########asteapta o comanda valida#######
	   ok=0;
	   while(ok==0)
	   {
	    bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Introduceti una dintre comenzile \"quit\",\"home\" sau \"log out\".\n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
                  if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.search=0;
                   goto LOGIN;
                   break;
                   }
	   
	   }
	   
       }
       
       if(t.meniu==1 && t.sterge==1)   //#########################FUnCTIA DE STERGERE####################
       {
       
    AGAIN2:             //Daca se introduce un nume care nu exista in bd   
          bzero(msgrasp,1000);     
          if(gresit==1)
              strcpy(msgrasp,msgerror);
     
         
	 strcat(msgrasp,"[client]Introdu numele vcardului pe care vrei sa-l stergi:\n");
	 if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
	   bytes = read (t.cl, msg, sizeof (buffer));
	   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
	   if (strncmp(msg, "quit", 4) == 0)
                  {
                     close(t.cl);
                     break;
                  }
           if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
           if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.sterge=0;
                   goto LOGIN;
                   break;
                   }	   
	   printf("[Thread %d]Am primit mesajul %s.\n",t.id,msg);
	   
	   
	    bzero(msgrasp,1000);
	    msg[strcspn(msg, "\n")] = 0;
	    strcpy(info.nume,msg);
	    sprintf(sql, "select count(*) from vcard where username like '%s' and nume like '%s';",info.username,info.nume);
	    sqlite3_exec(t.db, sql, callback2, msgrasp, &err_msg);
            if(msgrasp[0] =='0')  
                 {
                   bzero(msgerror,1000);
                   sprintf(msgerror,"[client]Nu exista niciun vcard cu numele %s in baza de date a utilizatorului %s.\n",info.nume,info.username);
                 //  printf("NUME USER %s %s\n",info.nume,info.username);
                   gresit=1;
                    printf("%s\n",msgerror);
                   goto AGAIN2;
                 }
	   gresit =0;
                               //###########stergere##########
          
           bzero(msgrasp,1000);
	   msg[strcspn(msg, "\n")] = 0;
	   strcpy(info.nume,msg);
	   sprintf(sql, "delete from vcard where username like '%s' and nume like '%s';",info.username,info.nume);
	   sqlite3_exec(t.db, sql, callback2, msgrasp, &err_msg);   
	   
	               
       
       
        ok=0;
	   while(ok==0)
	   {
	    bzero(msgrasp,1000);
		   strcat(msgrasp,"[client]Introduceti una dintre comenzile \"quit\",\"home\" sau \"log out\".\n");
		   if (write (t.cl, msgrasp, bytes) < 0)                 //trimitem mesajul cu meniu la client
		   {
		      perror ("[server] Eroare la write() catre client.\n");
		      return 0;
		   }
		   bytes = read (t.cl, msg, sizeof (buffer));
		   if (bytes < 0)
		   {
		       perror ("Eroare la read() de la client.\n");
		       return 0;
		   }  
		   if (strncmp(msg, "quit", 4) == 0)
                    {
                     close(t.cl);
                     break;
                    }
                  if(strncmp(msg,"home",4)==0)
                  {
                   t.meniu=0;
		    t.adauga=0;
		    t.search=0;
		    t.edit=0;
		    t.sterge=0;
		    goto MENIU;                  
                  }
                  if (strncmp(msg, "log out", 7) == 0)
                  {
                   t.sterge=0;
                   goto LOGIN;
                   break;
                   }
	   
	   }
       
       }
     }
	     
   
    
}


 



