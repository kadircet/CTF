#include <stdio.h>
#include <string.h>
#define SIZE ('Z'-'A'+1)

char org[15] = "AAAAAAAAAAAAA";
char cry[15] = "AXMDNNPKTEKUL";
char dif[15] = "             ";
int map[13];
char cip[15] = "MEQMTYXLDHKZN";
char ocp[15] = "ABCDEFGHIJKLM";
char pic[15] = "HRXDZNWEAWWCP";

int main()
{
	int i,j;
	for(i=0;i<strlen(org);i++)
		dif[i] = (cry[i]-org[i]+SIZE)%SIZE;
	
	for(i=0;i<strlen(cry);i++)
	{
		cry[i] = (cry[i]-'A'-dif[i]+SIZE)%SIZE+'A';
		cip[i] = (cip[i]-'A'-dif[i]+SIZE)%SIZE+'A';
		pic[i] = (pic[i]-'A'-dif[i]+SIZE)%SIZE+'A';
	}
	
	for(i=0;i<strlen(org);i++)
		for(j=0;j<strlen(cry);j++)
			if(ocp[i]==cip[j])
			{
				map[i]=j;
				break;
			}
			
	for(i=0;i<strlen(cry);i++)
		printf("%c", pic[map[i]]);
	puts("");
	
	return 0;
}

