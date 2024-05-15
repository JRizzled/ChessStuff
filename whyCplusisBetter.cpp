#include <iostream>


using namespace std;

typedef int bitboard[8][8];

/* 
In Python:
...Literally fucking cant even
maybe like this..?

bitboard = [['','','','','','','',''],...(8 more fucking times))]
ok actually...
bitboard = [[' ' for j in range(8)] for i in range(8)]
But I would have do this every time I wanted to instantiate a new bitboard unless I made a class 
which would involve overriding the [] operator probably taking up about 25 gBs of memory for a fucking 8 by 8 array!!!
*/


enum Side{
	WHITE,
	BLACK
};
/*
In Python:

from enum import Enum

class(Enum):
	WHITE = 0
	BLACK = 1
	// Also racist as fuck 

*/




int main(int argc, char** argv)
{

}