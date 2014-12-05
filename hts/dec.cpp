#include <iostream>
#include <cstdio>
#include <vector>
using namespace std;

bool maybe(vector<int>& a)
{
	for(int i=0;i<a.size();i++)
		if(a[i]<10 || a[i]>127)
			return false;
	return true;
}

vector<int> decrypt(vector<int>& a, int key)
{
	vector<int> res;
	for(int i=0;i<a.size();i++)
		res.push_back(a[i]-key);
	return res;
}

int main()
{
	freopen("enc.txt", "r", stdin);
	int a,b,c,m=0;
	char d;
	vector<int> chars;
	while(!cin.eof())
	{
		cin >> d >> a >> d >> b >> d >> c;
		chars.push_back(a+b+c);
		m=max(m, a+b+c);
		if(cin.eof())
			break;
	}
	cout << m << endl;
	cout << chars.size() << endl;
	
	for(int i=0;i<=m;i++)
	{
		vector<int> res=decrypt(chars, i);
		if(maybe(res))
		{
			for(int i=0;i<res.size();i++)
				cout << (char)res[i];
			cout << endl;
		}
	}
}

