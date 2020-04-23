#include <iostream>
#include <cstring>

int main()
{
	char* name = "Joshua";
	for(int i = 0; i < strlen(name); i++)
	{
		std::cout << name[i] << std::endl;
	}
}
