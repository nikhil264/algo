#include <iostream>
#include <vector>

using namespace std;

template<class RandomAccessIterator>
void quickSort(RandomAccessIterator first, RandomAccessIterator last){
    --last;
    if(first < last){
        auto pivot = first;
        for(auto i = first; i < last; ++i)
            if(*i < *last) swap(*i, *pivot++);
        swap(*last, *pivot);
        quickSort(first,pivot);
        quickSort(pivot+1,++last);
    }
}

int main(void){
    int n;
    cin >> n;
    vector<int> v;
    for(int i = 0, temp; i < n; ++i){
        cin >> temp;
        v.emplace_back(temp);
    }
    quickSort(v.begin(), v.end());
    for(const auto i : v) cout << i << " ";
    cout << endl;

}