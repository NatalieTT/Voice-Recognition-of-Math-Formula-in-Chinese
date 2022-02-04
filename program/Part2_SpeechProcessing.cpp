/**********************************
  User:Kevin DENG
  Lang:C++
  Scho:UIC
  Prog:FYP_Part2 Speech Processing
  Date:2020.07.16 - 2020.11.08
**********************************/
#include<iostream>
#include<fstream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<ctime>
#include<algorithm>
#include<queue>
#include<vector>
#include<map>
#include<set>
using namespace std;
#define ufor(i,j,k) for (int i=j,_i=k;i<=_i;i++)
#define dfor(i,j,k) for (int i=j,_i=k;i>=_i;i--)
#define uxfor(i,j,k) for (int i=j;i<k;i++)
#define rep(i,j) for(int i=0;i<j;i++)
#define m_int 2147483647
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define pi 3.1415926535897
#define re return 0
#define pn printf("\n") 
#define pk printf(" ")
#define ll long long
#define real double
#define mem(a) memset(a,0,sizeof(a))
#define qfor(k) for(int i=d[k],j;j=a[i].node,i;i=a[i].next)
#define ra(a) rand()%a
#define N 1000000
char s[N];
char t[N];
char ans[N];
int len;
void preprocessing()
{
	freopen("onebest.txt","r",stdin);
	gets(t);
	fclose(stdin);
}	 
void file_o()
{
	freopen("Outresult.txt","r",stdin);
	freopen("Chinese.txt","w",stdout);
}
void file_c()
{
	fclose(stdin);fclose(stdout);
}
void init()
{
	gets(s);
}
void work()
{
	int x = 0, y, z, ok;
	len = 0;
	while (x < strlen(s)){
		y = 0; z = x; ok = 0;
		while (s[z] == t[y]){
			z++; y++;
			if (y == strlen(t)) {
				ok = 1; break;
			}
		}
		if (ok == 1){
			ok = 0;
			x = z;
			while (s[x] != '\"'){
				ans[len++] = s[x];
				x++;
			}
			x--;
		}	
		x++;
	}
	if (ans[len-2] == '.')
		len-=2;
	ans[len]='\0';
}
void outp()
{
	puts(ans);
}
int main()
{
	preprocessing();
	file_o();
	init();
	work();
	outp();
	file_c();
	re;
}
