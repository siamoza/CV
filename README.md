# Установка библиотеки
(скопировано с https://pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/)

Step #1: Install OpenCV 4 dependencies on Ubuntu

I’ll be using Ubuntu 18.04 to install OpenCV 4 with Python 3 bindings on my machine.
To get the OpenCV 4 install party started, fire up your Ubuntu machine and open a terminal. Alternatively, you may SSH into the box for the install portion.
From there, let’s update our system:

$ sudo apt-get update
$ sudo apt-get upgrade

And then install developer tools:

$ sudo apt-get install build-essential cmake unzip pkg-config

Next, let’s install a handful of image and video I/O libraries.

$ sudo apt-get install libjpeg-dev libpng-dev libtiff-dev
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
$ sudo apt-get install libxvidcore-dev libx264-dev

These libraries enable us to load image from disk as well as read video files.
From there, let’s install GTK for our GUI backend:

$ sudo apt-get install libgtk-3-dev

Followed by installing two packages which contain mathematical optimizations for OpenCV:

$ sudo apt-get install libatlas-base-dev gfortran

And finally, let’s install the Python 3 development headers:

$ sudo apt-get install python3-dev

Once you have all of these prerequisites installed you can move on to the next step.

Step #2: Download OpenCV 4

Our next step is to download OpenCV.
Let’s navigate to our home folder and download both opencv and opencv_contrib. The contrib repo contains extra modules and functions which we frequently use here on the PyImageSearch blog. You should be installing the OpenCV library with the additional contrib modules as well.
When you’re ready, just follow along to download both the opencv and opencv_contrib code:

$ cd ~
$ wget -O opencv.zip https://github.com/opencv/opencv/archive/4.0.0.zip
$ wget -O opencv_contrib.zip https://github.com/opencv/opencv_contrib/archive/4.0.0.zip

From there, let’s unzip the archives:

$ unzip opencv.zip
$ unzip opencv_contrib.zip

I also like to rename the directories:

$ mv opencv-4.0.0 opencv
$ mv opencv_contrib-4.0.0 opencv_contrib

If you skip renaming the directories, don’t forget to update the CMake paths.
Now that opencv and opencv_contrib are downloaded and ready to go, let’s set up our environment.

Step #3: Configure your Python 3 virtual environment for OpenCV 4

Let’s install pip, a Python Package Manager. To install pip, simply enter the following in your terminal:

$ wget https://bootstrap.pypa.io/get-pip.py
$ sudo python3 get-pip.py

Make use of virtual environments for Python development

Python virtual environments allow you to work on your Python projects in isolation. They are a best practice for Python development.
For example, maybe you have a Python + OpenCV project that requires an older version of scikit-learn (v0.14), but you want to keep using the latest version of scikit-learn (0.19) for all of your newer projects.
Using virtual environments, you could handle these two software version dependencies separately, something that is not possible using just the system install of Python.
If you would like more information about Python virtual environments take a look at this article on RealPython or read the first half of the this blog post on PyImageSearch.
Note: My preferred way to work with Python virtual environment is via the virtualenv and virtualenvwrapper packages; however if you are more familiar with conda or PyEnv, feel free to use them and skip this part.
Let’s go ahead and install virtualenv and virtualenvwrapper — these packages allow us to create and manage Python virtual environments:

$ sudo pip install virtualenv virtualenvwrapper
$ sudo rm -rf ~/get-pip.py ~/.cache/pip

To finish the install of these tools, we need to update our ~/.bashrc file.
Using a terminal text editor such as vi /vim or nano , add the following lines to your ~/.bashrc :

# virtualenv and virtualenvwrapper
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source /usr/local/bin/virtualenvwrapper.sh

Alternatively, you can append the lines directly via bash commands:

$ echo -e "\n# virtualenv and virtualenvwrapper" >> ~/.bashrc
$ echo "export WORKON_HOME=$HOME/.virtualenvs" >> ~/.bashrc
$ echo "export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3" >> ~/.bashrc
$ echo "source /usr/local/bin/virtualenvwrapper.sh" >> ~/.bashrc

Next, source the ~/.bashrc file:

$ source ~/.bashrc

Create a virtual environment to hold OpenCV 4 and additional packages
Now we’re at the point where we can create your OpenCV 4 + Python 3 virtual environment:

$ mkvirtualenv cv -p python3

This command simply creates a Python 3 virtual environment named cv .
You can (and should) name your environment(s) whatever you’d like — I like to keep them short and sweet while also providing enough information so I’ll remember what they are for. For example, I like to name my environments like this:

* py3cv4
* py3cv3
* py2cv2
* etc

Here my py3cv4 virtual environment can be used for Python 3 + OpenCV 4. My py3cv3 virtual environment is used for Python 3 and OpenCV 3. And my py2cv2 environment can be used to test legacy Python 2.7 + OpenCV 2.4 code. These virtual environment names are easy to remember and allow me to switch between OpenCV + Python versions (nearly) seamlessly.
Let’s verify that we’re in the cv environment by using the workon command:

$ workon cv

Install NumPy

The first package and only Python prerequisite we’ll install is NumPy:

$ pip install numpy

We can now prepare OpenCV 4 for compilation on our Ubuntu machine.

Step #4: CMake and compile OpenCV 4 for Ubuntu

For this step, we’re going to setup our compile with CMake followed by running make to actually compile OpenCV. This is the most time-consuming step of today’s blog post.
Navigate back to your OpenCV repo and create + enter a build directory:

$ cd ~/opencv
$ mkdir build
$ cd build

Run CMake for OpenCV 4

Now let’s run CMake to configure the OpenCV 4 build:

$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
	-D CMAKE_INSTALL_PREFIX=/usr/local \
	-D INSTALL_PYTHON_EXAMPLES=ON \
	-D INSTALL_C_EXAMPLES=OFF \
	-D OPENCV_ENABLE_NONFREE=ON \
	-D OPENCV_EXTRA_MODULES_PATH=~/opencv_contrib/modules \
	-D PYTHON_EXECUTABLE=~/.virtualenvs/cv/bin/python \
	-D BUILD_EXAMPLES=ON ..
  
Notice the -D OPENCV_ENABLE_NONFREE=ON flag. Setting this flag with OpenCV 4 ensures that you’ll have access to SIFT/SURF and other patented algorithms.
Be sure to update the above command to use the correct OPENCV_EXTRA_MODULES_PATH and PYTHON_EXECUTABLE in your virtual environment that you’re working in. If you’re using the same directory structure Python virtual environment names these paths should not need to be updated.
Take a second now to ensure that the Interpreter points to the correct Python 3 binary. Also check that numpy points to our NumPy package which is installed inside the virtual environment.
Be sure to check the CMake output to ensure that the “Non-free algorithms” will be installed (YES).

Compile OpenCV 4

Now we’re ready to compile OpenCV 4:

$ make -j4

Note: In the make command above, the -j4 argument specifies that I have 4 cores for compilation. Most systems will have 2, 4, or 8 cores. You should update the command to use the number of cores on your processor for a faster compile. If you encounter compilation failures, you could try compiling with 1 core to eliminate race conditions by skipping the optional argument altogether.
Here you can see OpenCV 4 has compiled without any errors.
And from there, let’s install OpenCV 4 with two additional commands:

$ sudo make install
$ sudo ldconfig

Step #5: Link OpenCV 4 into your Python 3 virtual environment

Before we make a symbolic link to link OpenCV 4 into our Python virtual environment, let’s determine our Python version:

$ workon cv
$ python --version
Python 3.5

Using the Python version, we can easily navigate to the correct site-packages directory next (although I do recommend tab-completion in the terminal).
Update 2018-12-20: The following paths have been updated. Previous versions of OpenCV installed the bindings in a different location (/usr/local/lib/python3.5/site-packages ), so be sure to take a look at the paths below carefully.
At this point, your Python 3 bindings for OpenCV should reside in the following folder:

$ ls /usr/local/python/cv2/python-3.5
cv2.cpython-35m-x86_64-linux-gnu.so

Let’s rename them to simply cv2.so :

$ cd /usr/local/python/cv2/python-3.5
$ sudo mv cv2.cpython-35m-x86_64-linux-gnu.so cv2.so

Pro-tip: If you are installing OpenCV 3 and OpenCV 4 alongside each other, instead of renaming the file to cv2.so , you might consider naming it cv2.opencv4.0.0.so and then in the next sub-step sym-link appropriately from that file to cv2.so as well.
Our last sub-step is to sym-link our OpenCV cv2.so bindings into our cv virtual environment:

$ cd ~/.virtualenvs/cv/lib/python3.5/site-packages/
$ ln -s /usr/local/python/cv2/python-3.5/cv2.so cv2.so

Step #6: Test your OpenCV 4 install on Ubuntu

Let’s do a quick sanity test to see if OpenCV is ready to go.
Open a terminal and perform the following:

$ workon cv
$ python
>>> import cv2
>>> cv2.__version__
'4.0.0'
>>> quit()

The first command activates our virtual environment. Then we run the Python interpreter associated with the environment.
Note: It is not necessary to specify python3 as Python 3 is the only Python executable in the environment.
If you see that you have version 4.0.0 installed, then a “Congratulations!” is in order. Have a swig of your favorite beer or bourbon and let’s get to something more fun than installing libraries and packages.

Источник: https://pyimagesearch.com/2018/08/15/how-to-install-opencv-4-on-ubuntu/
