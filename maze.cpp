#include<iostream>

using namespace std;

bool solvemaze(int a[4][4],int n, int i, int j, int path[4][4]){
    if(i < 0 || i >=n || j < 0 || j >= n ){   //don't go out of bound
        return false;
    }

    if( i == n && j == n){                 // if jou reach the end of the maze
        return true;
    }

    if(a[i][j] == 0 || path[i][j] == 1){ //we cant go there
        return false;
    }

    path[i][j] = 1;

    // right move
    if(solvemaze(a, n, i, j + 1, path)){
        path[i][j] = 0;
        return true;
    }
    // left move
    if(solvemaze(a, n, i , j -1, path)){
        path[i][j] = 0;
        return true;
    }

    // top move
    if (solvemaze(a, n, i - 1, j, path)){
        path[i][j] = 0;
        return true;
    }
    // bottom move
    if(solvemaze(a, n, i + 1, j, path)){
        path[i][j] = 0;
        return true;
    }

    return false;
}



bool solve(int a[4][4],int n){
    int path[4][4] {0};
    return solvemaze(a,n,0,0,path);
}



int main() {
    int n = 4;
    int a[4][4] ={  { 1, 1, 0, 0 },
                    { 1, 1, 1, 1 },
                    { 0, 1, 0, 1 },
                    { 1, 1, 1, 1 } };

    if(solve(a,n)) cout << "There is a path \n";
    else cout << "No path \n";
    return 0;
}
