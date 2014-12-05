#include <iostream>
#include <cstdio>
using namespace std;

int decrypt(char source, char dest)
{
	for(int key=0;key<128;key++)
		if((source ^ key) == dest)
			return key;
			
	return -1;
}

int main()
{
	FILE *f = fopen("t.txt", "wb");
	char first;
	char buf[1024];
	
	string to = "{\"showpassword\":\"yes\",\"bgcolor\":\"#000000\"}";
	string key = "qw8J";
	for(int i=0;i<to.size();i++)
		buf[i] = to[i]^key[i%key.size()];
	fwrite(buf, 1, to.size(), f);
	
	/*for(int i=0;i<to.size();i++)
	{
		fread(&first, 1, 1, f);
		cout << (char)decrypt(first, to[i]);
	}*/
	cout << endl;
	return 0;
}

