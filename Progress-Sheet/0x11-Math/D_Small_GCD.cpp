/*
Author - Fahmi Dinsefa
Date - 03/29/2024
*/
#pragma GCC target("avx2")
#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#include <bits/stdc++.h>
using namespace std;
template<class T, class S>
ostream& operator << (ostream &o, const pair<T, S> &p) {
    return o << '(' << p.first << ", " << p.second << ')';
}
template<template<class, class...> class T, class... A>
typename enable_if<!is_same<T<A...>, string>(), ostream&>::type
operator << (ostream &o, T<A...> V) {
	o << '[';
	for(auto a : V) o << a << ", ";
	return o << ']';
}
 
typedef int ll;
typedef long double ld;
typedef pair<ll, ll> pl;
typedef vector<ll> vl;
 
#define INP(x) ll x; cin >> x;
#define INPD(x) ld x; cin >> x;
#define insr(s) string s; cin >> s;
#define F(i, l, r) for(ll i = l; i < (r); ++i)
#define FD(i, r, l) for(ll i = r; i > (l); --i)
#define P(a, n) { cout << "{ "; F(_, 0, n) cout << a[_] << " "; cout << "}\n"; }
#define EX(x) { cout << x << '\n'; exit(0); }
#define A(a) (a).begin(), (a).end()
#define K first
#define V second
#define M 1000000007 //998244353
#define N 100010
 
vl fact[N];
ll a[N], ct[N], b[N];





int main() {
    F(i, 1, N) for(ll j = i; j < N; j += i) fact[j].push_back(i);
    F(i, 1, N) reverse(A(fact[i]));
    INP(tc) while(tc--) {
        INP(n) F(i, 0, n) cin >> a[i];
        fill_n(ct, N, 0);
        sort(a, a + n);
        long long int ans = 0, cur = 0;
        F(i, 0, n) {
            ans += cur;
            for(ll x : fact[a[i]]) {
                b[x] = ct[x];
                for(ll y : fact[a[i]]) if(y <= x) break; else if(!(y % x)) b[x] -= b[y];
                cur += x * (long long int)b[x];
            }
            for(ll x : fact[a[i]]) ct[x]++;
        }
        cout << ans << '\n';
    
     
    }
}
