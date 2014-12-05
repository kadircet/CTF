#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netdb.h>
using namespace std;

int main()
{
	addrinfo hints, *res;
	int sockfd;

	memset(&hints, 0, sizeof hints);
	hints.ai_family = AF_UNSPEC;
	hints.ai_socktype = SOCK_STREAM;

	getaddrinfo("vortex.labs.overthewire.org", "5842", &hints, &res);

	sockfd = socket(res->ai_family, res->ai_socktype, res->ai_protocol);

	connect(sockfd, res->ai_addr, res->ai_addrlen);
	//int recv(int sockfd, void *buf, int len, int flags);
	char* buff=new char[1024];
	int size;
	/*while((size=recv(sockfd, buff, sizeof(buff), 0))>0)
	{
		for(int i=0;i<size;i++)
			cout << buff[i];
	}
	
	return 0;*/
	unsigned int a[4],i=0;
	for(int i=0;i<4;i++)
		recv(sockfd, a+i, sizeof(a[i]), 0), cout << a[i] << endl;
	
	unsigned int tres=0;
	for(int i=0;i<4;i++)
		tres+=a[i];
	
	send(sockfd, &tres, sizeof(int), 0);
	
	while((size=recv(sockfd, buff, 1024, 0))>0)
	{
		for(int i=0;i<size;i++)
			cout << buff[i];
	}
	cout << endl;
	return 0;
}
