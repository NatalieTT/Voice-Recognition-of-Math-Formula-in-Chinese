 /**********************************
  User:Kevin DENG
  Lang:C++
  Scho:UIC
  Prog:FYP_Part4 AC automation
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
#include<queue>
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
#define N 2000000
#define NN 50000
#define M 200
char ans[N];
struct standard_formula{
	char p[M],f[M];
}a[NN];
int n, m;
char st[N];
char t[N];

int trie[N][26];
int flag[N];
int cnt[N];
int c;
int fail[N];
int num;

bool cmp(standard_formula S, standard_formula T)
{
	int len = min(strlen(S.p), strlen(T.p));
	uxfor(i,0,len)
		if (T.p[i] > S.p[i])
			return true;
			else if (T.p[i] < S.p[i])
				return false;
	return true;
}

void insert_words(char s[], int x)
{
	int root = 0;
	uxfor(i,0,strlen(s)){
		int next = s[i] - 'a';
		if(!trie[root][next])
			trie[root][next] = ++c;
		root = trie[root][next];
	}
	flag[root] = x; //¸ü¸Ä
}

void getFail()
{
	queue <int>q;
	ufor(i,0,25)
		if(trie[0][i]){
			fail[trie[0][i]] = 0;
			q.push(trie[0][i]);
		}
	while(!q.empty()){
			int now = q.front();
			q.pop();
			ufor(i,0,25){
				if(trie[now][i]){
					fail[trie[now][i]] = trie[fail[now]][i];
					q.push(trie[now][i]);
				}
				else trie[now][i] = trie[fail[now]][i];
			}
	}
}	

int query(char s[]){
	int now = 0, ans = 0;
	mem(cnt);
	uxfor(i,0,strlen(s)){
		now = trie[now][s[i]-'a'];
		for(int j = now; j && cnt[j] != -1; j = fail[j]){
			if (flag[j] > 0)
				return flag[j];
			cnt[j] = -1;
		}
	}
	return 0;
}

void read_standard_formula() 
{
	freopen("AC.txt", "r", stdin);
	m = 0;
	while (scanf("%s\n",a[++m].p)!= EOF)
		gets(a[m].f);
	m--;
	/*ufor(i,1,m){
		puts(a[i].p);
		printf("~%s~\n",a[i].f);
	}*/
	sort(a + 1, a + m + 1, cmp); 
	fclose(stdin);
}

void file_o()
{
	freopen("Pinyin.txt","r",stdin);
	freopen("Latex.txt","w",stdout);
}

void file_c()
{
	fclose(stdin);fclose(stdout);
}

void init()
{
	gets(st);
}

void work()
{
	ufor(i,1,m)
		insert_words(a[i].p, i);
	fail[0] = 0;
	getFail();
	int x = 0, y = 0, z = 0;
	num = 1; ans[0]='$'; ans[1]='$'; 
	
	int bracket = 0;
	int logflag = 0;
	mem(t);
	while (x < strlen(st)) {
		if (st[x] >= '0' && st[x] <= '9'){
			ans[++num] = st[x];
		}
		if (st[x] == ' ' && bracket == 2){
			bracket = 0;
			ans[++num] = ')';
		}
		if (st[x] == ' ' && bracket == 1) 
			bracket = 2;
		if (st[x] >= 'A' && st[x] <= 'Z'){
			ans[++num] = st[x] - 'A' + 'a';
		}
		else if (st[x] >= 'a' && st[x] <= 'z'){
			ufor(i,0,y)
				t[i] = 0;
			y = 0;
			while (st[x] >= 'a' && st[x] <= 'z'){
				t[y++] = st[x];
				x++;
				if (x >= strlen(st))
					break;
			}
			t[y] = '\0';
			x--;
			z = query(t);
			if (z != 0){
				uxfor(i,0,strlen(a[z].f)){
					if(a[z].f[i] != '~')
						ans[++num] = a[z].f[i];
						else ans[++num] = ' ';
					if (ans[num] == '(')
						bracket = 1;
				}
			}
		}
		else if (st[x] == '+' || st[x] == '-' || st[x] == '*' || st[x] == '/' || st[x] == '=' || st[x] == '.' || st[x] == '{' || st[x] == '}'){
			ans[++num] = st[x];
		}
		x++;
	}
	ans[++num] = '$';
	ans[++num] = '$';
	ans[++num] = '\0';
}

void outp()
{
	printf("%s",ans);
}

int main()
{
	read_standard_formula();
	file_o();
	init();
	work();
	outp();
	file_c();
	re;
}
