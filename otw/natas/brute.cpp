#include <iostream>
#include <string>
using namespace std;

int main()
{
	//generateKey("         ", 0);
	
	string a = "EICTDGYIYZKTHNSIRFXYCPFUEOCKRN";
	for(int i=0;i<a.size();i++)
		a[i]-='A';
	
	string b = /*"EICTDGYIYZKTHNSIRFXYCPFUEOCKRN";*/"PNUKLYLWRQKGKBE";
	for(int i=0;i<b.size();i++)
	{
		b[i]-='A';
		b[i] = (b[i]-a[i]+26)%26+'A';
	}
		
	cout << b << endl;
	return 0;
}

