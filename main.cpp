#include <iostream>

#include "glm\glm.hpp"
#include "glm\gtc\matrix_transform.hpp"
#include "glm\gtc\type_ptr.hpp"


int main(){
    float a, b, c, d;
    std::cout << "x^1 = "; 
    std::cin >> a;
    std::cout << "y^1 = ";
    std::cin >> b;
    std::cout << "x^2 = ";
    std::cin >> c;
    std::cout << "y^2 = ";
    std::cin >> d;
     
    glm::vec2 x = glm::vec2(a, b);
    glm::vec2 y = glm::vec2(c, d);
    float lmao = glm::distance(x, y);
    std::cout << lmao;
    return 0;
}