#include <iostream>
#include <opencv2/opencv.hpp>

using namespace std;
using namespace cv;

int main() {

    Mat3b img = imread("test1.jpg");

    Mat1b bin;
    cvtColor(img, bin, COLOR_BGR2GRAY);
    bin = bin < 200;

    vector<Point> pts;
    findNonZero(bin, pts);

    RotatedRect box = minAreaRect(pts);

    cout << box.size.width << ", " << box.size.height << endl; 

    Point2f vertices[4];
    box.points(vertices);

    for(int i=0; i<4; i++)
        line(img, vertices[i], vertices[(i + 1) % 4], Scalar(0, 255, 0));

    Mat1b rotated;
    Mat M = getRotationMatrix2D(box.center, box.angle, 1.0);
    warpAffine(bin, rotated, M, bin.size());

    Mat1f horProj;
    reduce(rotated, horProj, 1, CV_REDUCE_AVG);

    // Remove noise in histogram. White bins identify space lines, black bins identify text lines
    float th = 0;
    Mat1b hist = horProj <= th;

    // Get mean coordinate of white white pixels groups
    vector<int> ycoords;
    int y = 0;
    int count = 0;
    bool isSpace = false;
    for (int i = 0; i < rotated.rows; ++i)
    {
        if (!isSpace)
        {
            if (hist(i))
            {
                isSpace = true;
                count = 1;
                y = i;
            }
        }
        else
        {
            if (!hist(i))
            {
                isSpace = false;
                ycoords.push_back(y / count);
            }
            else
            {
                y += i;
                count++;
            }
        }
    }

    // Draw line as final result
    Mat3b result;
    cvtColor(rotated, result, COLOR_GRAY2BGR);
    for (int i = 0; i < ycoords.size(); ++i)
    {
        line(result, Point(0, ycoords[i]), Point(result.cols, ycoords[i]), Scalar(0, 255, 0));
    }

    imwrite("bin.jpg", result);

    return 0;    
}