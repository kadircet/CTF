#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <fcntl.h>

#define PORT "24000"
#define HOST "semtex.labs.overthewire.org"

void fatal(char *s)
{
	puts(s);
	exit(0);
}

int main()
{
	struct addrinfo hints, *res;
	memset(&hints, 0, sizeof(hints));
	hints.ai_family = AF_INET;
	hints.ai_socktype = SOCK_STREAM;
	
	if(getaddrinfo(HOST, PORT, &hints, &res)!=0)
		fatal("getaddrinfo");
		
	int sd=socket(AF_INET, SOCK_STREAM, 0);
	if(sd==-1)
		fatal("socket");
		
	if(connect(sd, res->ai_addr, res->ai_addrlen)==-1)
		fatal("connect");
		
	freeaddrinfo(res);
	
	int fd=open("semtex0.bin", O_WRONLY|O_CREAT);
	
	unsigned char rd;
	int nread,i;
	int tot=0;
	while((nread=read(sd, &rd, sizeof(rd)))>0)
	{
		write(fd, &rd, sizeof(rd));
		tot+=nread;
		nread=read(sd, &rd, sizeof(rd));
		if(nread==-1)
			break;
		tot+=nread;
	}
	printf("Tot: %d bytes read\n", tot);
	return 0;
}

