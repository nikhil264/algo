#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

#define ALPHABET_SIZE  26
struct TrieNode{
    int words;
    int prefixes;
    struct TrieNode *children[ALPHABET_SIZE];
};


void addWord(TrieNode *root, string name){
    if (name.empty()){
        ++(root->words);
        ++(root->prefixes);
    }
    else{
        ++(root->prefixes);
        int c = tolower(name[0])-'a';
        auto child = root->children;
        if(child[c]==nullptr){
           child[c] = new TrieNode;
           child[c]->words = child[c]->prefixes = 0;
           for(auto& i : child[c]->children) i = nullptr;   
        }
        name.erase(name.begin());
        addWord(child[c], name);
    }

}


int findPrefix(TrieNode *root, string name, int word=0){
    if(name.empty()){
        if(word) return root->words;
        else return root->prefixes;
    }
    int c = tolower(name[0])-'a';
    auto child = root->children;
    if(child[c]==nullptr) return 0;
    name.erase(name.begin());
    return findPrefix(child[c], name);
    
}

int main() {
    int testCases = 1;
    TrieNode head;
    head.words = head.prefixes = 0;
    for(auto& i : head.children) i = nullptr;
    while(testCases--){
        int n;
        cin >> n;
        while(n--){
            string instr, input;
            cin >> instr >> input;
            if(instr == "add") addWord(&head,input);
            if(instr == "find") cout << findPrefix(&head, input) << endl;
        }
    }
    return 0;
}

