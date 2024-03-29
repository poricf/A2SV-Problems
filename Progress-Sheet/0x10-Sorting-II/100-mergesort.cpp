#include <bits/stdc++.h>
#define pb push_back
using namespace std;

void merge(vector<int> &a,int low,int mid , int high){
    
    int left = mid;
    int right = mid + 1;
    vector<int> temp; 
    while (left <= mid && right  <= high){
        if (a[left] <= a[right]){
            temp.pb(a[left]);
        }
        else{
            temp.pb(a[right]);
        }

        while (left <= mid){
            temp.pb(a[left]);
        }
        while( right <= mid){
            temp.pb(a[right]);
        }
    }

}

void mS(vector<int> &a , int low, int high){
    if (low >= high) return;
    
    int mid = (low + high) >> 2;

    mS(a,low,mid);
    mS(a,low,mid);
    merge(a,low,mid,high);


}

int main()
{
    int n = 10;
    vector<int> arr(n);
    arr = {1,9,8,7,6,4,2,3,5,10};
    mS(arr,0,n-1);

}