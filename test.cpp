#include <iostream>

void rectMaker(int width, int height){
    std::string topAndBottom = "# ";
    std::string mid = "#";
    for (int i = 0; i < width - 1; i++){
         topAndBottom += "# ";
    }
    std::cout << topAndBottom << std::endl;
    for (int i = 0; i < topAndBottom.size() - 3; i++){
        mid += " ";
    }
    mid += "#";
    for (int i = 0; i < height - 2; i++){
        std::cout << mid << std::endl;
    }
    std::cout << topAndBottom;
}

int main()
{
    rectMaker(5, 5);
}