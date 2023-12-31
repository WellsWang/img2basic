# img2basic
一个用Microsoft BASIC语言来显示BMP文件内容的样例

## 使用方法

### BMP文件准备
首先准备BMP图像文件，需要存储为调色板，并只有黑白两色的格式。本例中有4个BMP样例文件，分别是：
  * BILI.bmp - bilibili Logo图片
  * geeklogic.bmp - GeekLogic Logo图片
  * text1.bmp - 中文文本“这次一定”
  * text2.bmp - 中文文本“一键三连”

### 将BMP文件转换成数据
使用Python程序bmp2arr.py，将图片文件转换成BASIC程序中的图形数据。使用方法

    python3 bmp2arr.py <BMP文件名>

输出的结果为转换后的数据以及数据的长度。

### 将数据转储成BASIC的图形块文件
为了提升BASIC程序显示图形的效率，可以对数据进行预处理，然后将数据存储为BASIC的图形块文件。
修改SAVEBIN.BAS文件，将之前Python程序生成的数据贴入程序末尾的DATA数据段，注意将数据长度（字节数）填写到程序前段数组长度及循环的长度部分。

    100 DIM geek%(1 TO 315)
    ...
    120 FOR i = 3 TO 315 STEP 1
    ...
    5000 DATA 200, 25, 0, 0, 0, 0, 0, ...

程序会生成图形块文件，在本例中，对应之前的BMP文件，一共生成了四个块文件：
 * BILI.BIN
 * GEEK.BIN
 * TEXT1.BIN
 * TEXT2.BIN

### 显示图像
修改SHOWIMG.BAS，将生成的块文件名及数据长度填写进相应位置。执行便可以读取块文件，快速显示图像。

    100 DIM bili%(1 TO 362)
    ...
    210 BLOAD "bili.bin", VARPTR(bili%(1))


## 免责说明
本程序是为复古电脑测试写着玩的，大家可以随便尝试和修改使用，本人不对可能或不可能产生的结果以及任何形式的结果的外延影响承担任何责任和义务。
代码是写着玩的，里面有很多hardcoding，不喜勿喷。

## 许可证
这些代码适用MIT许可证，随便玩吧。
