#include <iostream>
#include <vector>
using namespace std;

void merge(int a[], int start, int mid, int end)
{
    vector<int> b1, b2;
    for (int i = start; i <= mid; i++)
    {
        b1.push_back(a[i]);
    }
    for (int i = mid + 1; i <= end; i++)
    {
        b2.push_back(a[i]);
    }
    int p1 = 0, p2 = 0, p3 = start;
    while (p1 < b1.size() && p2 < b2.size())
    {
        if (b1[p1] < b2[p2])
        {
            a[p3++] = b1[p1++];
        }
        else
        {
            a[p3++] = b2[p2++];
        }
    }
    while (p1 < b1.size())
    {
        a[p3++] = b1[p1++];
    }
    while (p2 < b2.size())
    {
        a[p3++] = b2[p2++];
    }
}

void mergesort(int a[], int start, int end)
{
    if (start < end)
    {
        int mid = (start + end) / 2;
        mergesort(a, start, mid);
        mergesort(a, mid + 1, end);
        merge(a, start, mid, end);
    }
}

signed main()
{
    int a[] = {21,2,61,63,50,35,46,42,3,80,14,80,7,65,27,32,23,7,4,72,96,37,10,87,60,61,46,38,85,77,99,38,54,93,35,28,19,52,100,62,67,71,85,78,57,27,45,20,61,22,11,70,100,79,74,27,64,82,7,56,15,73,68,13,30,39,34,94,17,70,32,37,49,34,51,56,3,91,77,62,56,65,98,92,61,75,11,91,35,54,63,16,24,22,11,28,43,15,4,53
};
    mergesort(a, 0, sizeof(a) / sizeof(int) - 1);
    for (int f : a)
    {
        cout << f << " ";
    }
    cout << endl;
}