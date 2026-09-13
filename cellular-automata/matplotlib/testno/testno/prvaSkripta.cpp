#include <glad.h>
#include <glfw3.h>
#include <vector>
#include <SDL.h>
using namespace std;
GLuint createShaderProgram() {
    // Vertex shader source code
    const char* vertexShaderSource = R"glsl(
        #version 330 core
        layout (location = 0) in vec2 position;
        uniform vec3 color;
        out vec3 Color;
        void main() {
            gl_Position = vec4(position, 0.0, 1.0);
            Color = color;
        }
    )glsl";

    // Fragment shader source code
    const char* fragmentShaderSource = R"glsl(
        #version 330 core
        in vec3 Color;
        out vec4 FragColor;
        void main() {
            FragColor = vec4(Color, 1.0);
        }
    )glsl";

    // Create and compile the vertex shader
    GLuint vertexShader = glCreateShader(GL_VERTEX_SHADER);
    glShaderSource(vertexShader, 1, &vertexShaderSource, NULL);
    glCompileShader(vertexShader);

    // Create and compile the fragment shader
    GLuint fragmentShader = glCreateShader(GL_FRAGMENT_SHADER);
    glShaderSource(fragmentShader, 1, &fragmentShaderSource, NULL);
    glCompileShader(fragmentShader);

    // Create the shader program and link the shaders
    GLuint shaderProgram = glCreateProgram();
    glAttachShader(shaderProgram, vertexShader);
    glAttachShader(shaderProgram, fragmentShader);
    glLinkProgram(shaderProgram);

    // Delete the shaders as they're linked into our program now and no longer necessary
    glDeleteShader(vertexShader);
    glDeleteShader(fragmentShader);

    return shaderProgram;
}



// This is where you can put your OpenGL code
void draw(const vector<vector<int>>& b) {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);
    glClear(GL_COLOR_BUFFER_BIT);

    float width = 2.0f / b[0].size(); // Calculate the width of each cell
    float height = 2.0f / b.size(); // Calculate the height of each cell

    // Create a shader program and use it
    GLuint shaderProgram = createShaderProgram(); // You need to implement this function
    glUseProgram(shaderProgram);

    for (int i = 0; i < b.size(); i++) {
        for (int j = 0; j < b[i].size(); j++) {
            float x = -1.0f + j * width;
            float y = 1.0f - i * height;

            // Create a VAO and VBO, bind them, upload vertex data
            GLuint VAO, VBO;
            glGenVertexArrays(1, &VAO);
            glGenBuffers(1, &VBO);
            glBindVertexArray(VAO);
            glBindBuffer(GL_ARRAY_BUFFER, VBO);

            float vertices[] = {
                x, y - height, // bottom left corner
                x + width, y - height, // bottom right corner
                x + width, y, // top right corner
                x, y // top left corner
            };
            glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

            // Specify the layout of the vertex data
            GLint posAttrib = glGetAttribLocation(shaderProgram, "position");
            glEnableVertexAttribArray(posAttrib);
            glVertexAttribPointer(posAttrib, 2, GL_FLOAT, GL_FALSE, 0, 0);

            if (b[i][j] == 1) {
                glUniform3f(glGetUniformLocation(shaderProgram, "color"), 1.0f, 0.5f, 0.0f); // White for cells with value 1
            }
            else {
                glUniform3f(glGetUniformLocation(shaderProgram, "color"), 0.0f, 1.0f, 0.5f); // Black for cells with value 0
            }

            // Draw the rectangle
            glDrawArrays(GL_QUADS, 0, 4);

            // Delete the VAO and VBO
            glDeleteBuffers(1, &VBO);
            glDeleteVertexArrays(1, &VAO);
        }
    }
}

int SDL_main(int argc, char* argv[]) {
    // Initialize the library
    if (!glfwInit())
        return -1;

    // Create a windowed mode window and its OpenGL context
    GLFWwindow* window = glfwCreateWindow(1920, 1080, "Hello World", NULL, NULL);//
    // GLFWwindow* window = glfwCreateWindow(640, 480, "Hello World", NULL, NULL);
    if (!window) {
        glfwTerminate();
        return -1;
    }

    // Make the window's context current
    glfwMakeContextCurrent(window);

    // Initialize GLAD
    if (!gladLoadGLLoader((GLADloadproc)glfwGetProcAddress)) {
        return -1;
    }

    //CRTANJE AUTOMATONA

    int sir = 501;
    vector<int> a(sir, 0);//array with length sir
    for (int i = 0; i < sir; i++) {
        a[i] = 0;
    }
    a[sir / 2] = 1;

    int dub = 300;
    vector<vector<int>> b(dub, vector<int>(sir));//array visine dub i sirine sir

    for (int j = 0; j < sir; j++) {
        b[0][j] = a[j];
    }

    for (int i = 0; i < dub; i++) {
        for (int j = 0; j < sir ; j++) {
            int left, right;
            if (i != dub - 1) {
                if (j == 0) {
                     left = b[i][sir-1];
                }
                else {
                     left = b[i][j - 1];
                }
                
                if (j == sir - 1) {
                     right = b[i][0];
                }
                else {
                     right = b[i][j + 1];
                }
                int current = b[i][j];

                if (left == 0 && current == 0 && right == 0) {
                    b[i + 1][j] = 0;
                }
                else if (left == 0 && current == 0 && right == 1) {
                    b[i + 1][j] = 1;
                }
                else if (left == 0 && current == 1 && right == 0) {
                    b[i + 1][j] = 1;
                }
                else if (left == 0 && current == 1 && right == 1) {
                    b[i + 1][j] = 1;
                }
                else if (left == 1 && current == 0 && right == 0) {
                    b[i + 1][j] = 1;
                }
                else if (left == 1 && current == 0 && right == 1) {
                    b[i + 1][j] = 0;
                }
                else if (left == 1 && current == 1 && right == 0) {
                    b[i + 1][j] = 0;
                }
                else if (left == 1 && current == 1 && right == 1) {
                    b[i + 1][j] = 0;
                }
            }
        }
    }




    // Loop until the user closes the window
    while (!glfwWindowShouldClose(window)) {
        // Call the draw function
        draw(b);

        // Swap front and back buffers
        glfwSwapBuffers(window);

        // Poll for and process events
        glfwPollEvents();
    }



    glfwTerminate();
    return 0;
}
