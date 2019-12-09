# Face Detect Landmarks 200 Points

## About
本项目使用dlib人脸特征识别，在原来的68点的基础上扩展到200点

### Features
+ 200个特征点，覆盖全脸、眼部、眉毛、嘴及嘴唇、鼻子包含轮廓及鼻梁骨架

## Getting Start
1. 下载[illinois的图片](http://www.ifp.illinois.edu/~vuongle2/helen/)
2. 安装必要的插件,如dlib, opencv
3. 运行python脚本test_shape_predictor.py

在根目录已经提供了一个用如下参数训练出来的预测模型，也可以自己通过train_shape_predictor.py来训练
```
    options.nu = 0.05
    options.tree_depth = 2
    options.be_verbose = True
```

## Demo
![image](./annotated.png)

## Contact
- [Watson Wuh](mailto:watson.wuh@google.com)
-------------------------------------
#face detect landmarks 200 points

## About
base on dlib's face landmarks detecting from 68 exntend to 200 points

## Getting start
Actually, in this project already provide predictor model trained with
```
    options.nu = 0.05
    options.tree_depth = 2
    options.be_verbose = True
```
plese follow below steps:
1. download images at [Helen dataset from illinois](http://www.ifp.illinois.edu/~vuongle2/helen/)
2. install required plugins, like dlib, opencv
3. run the python script test_shape_predictor.py

Actually, in this project already provide predictor model trained by train_shape_predictor.py with
```
    options.nu = 0.05
    options.tree_depth = 2
    options.be_verbose = True
```

## Demo
![image](./annotated.png)

## Contact
- [Watson Wuh](mailto:watson.wuh@google.com)
