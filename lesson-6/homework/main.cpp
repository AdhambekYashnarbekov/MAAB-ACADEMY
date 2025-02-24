#include <QApplication>
#include <QLabel>

int main(int argc, char *argv[])  // Corrected parameter names
{
    QApplication app(argc, argv); // Fixed class name
    QLabel label("Hello Qt!");    // Stack allocation (auto-managed)
    label.show();
    
    return app.exec();  // Corrected event loop function
}
