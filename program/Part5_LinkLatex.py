# -*- coding: utf-8 -*-
"""

User: Kevin DENG Yichun TAO
Lang: Python
Scho: UIC
Proj: FYP_Part5 Link Latex 
Date: 2020.11.02 - 2020.11.08
    
"""

from IPython.display import Latex
import os
def lat():
    dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(dir);
    fin = open("Latex.txt", "r", encoding = 'utf-8')
    S = fin.read()
    fin.close()
    fin1 = open("Outresult.txt", "r", encoding = 'utf-8')
    one = fin1.read()
    fin1.close()
    fin2 = open("Chinese.txt", "r", encoding = 'utf-8')
    two = fin2.read()
    fin2.close()
    fin3 = open("Pinyin.txt", "r", encoding = 'utf-8')
    three = fin3.read()
    fin3.close()
    fin4 = open("Formula4.5.txt", "r", encoding = 'utf-8')
    four = fin4.read()
    fin4.close()
    html = open("Formula.html", "w")
    ans = """
    <!-- Yichun TAO -->
    <html>
        <head>
            <title>Formula Output</title>
            <!-- Link CSS -->
            <link rel="stylesheet" href="css/base.css">
            <link rel="stylesheet" href="css/main.css">
            <script type="text/x-mathjax-config">
                MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\(','\)']]}});
            </script>
            <script type="text/javascript"  src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
        </head>
        <body>
            <div class="header">
                <div class="title">
                    <!-- 销售大数据分析 -->
                </div>
            </div>
            <!-- <div class="menu"> -->
                <!-- 预留菜单位置 -->
            <!-- </div> -->
            <div class="main clearfix">
                <div class="main-left fleft">
                    <div class="box bg-title">
                        <div class="title text-center">1.语音识别结果</div>
                        <div class="content" style="font-size: 20px; height: 360px; overflow: hidden; padding:0 13px; color: white;">
                            <br>
                            <center>
    """ + one + """

                            </center>
                        </div>
                    </div>
                    <br><br>>
                    <div class="box bg-title">
                        <div class="title text-center">2.提取中文文本</div>
                        <div class="content" style="font-size: 30px; height: 360px; overflow: hidden; padding:0 13px; color: white;">
                            <br><br>
                            <center>
    """ + two + """

                            </center>
                        </div>
                    </div>
                </div>
                <div class="main-center fleft">
                        <br><br><br><br><br><br><br><br><br><br>
                        <div class="box bg-title">
                            <div class="title text-center">5.最终结果</div>
                            <div class="content" style="font-size: 50px; height: 360px; overflow: hidden; padding:0 13px; color: white;">
                                <br>
                                <center>
    """ + S + """
                                </center>
                            </div>
                        </div>
                </div>
                <div class="main-right fright">
        
                    <div class="box bg-title">
                        <div class="title text-center">3.中文文本转拼音文本</div>
                        <div class="content" style="font-size: 30px; height: 360px; overflow: hidden; padding:0 13px; color: white;">
                            <br><br>
                            <center>
    """ + three + """

                            </center>
                        </div>
                    </div>
                    <br><br>
                    <div class="box bg-title">
                        <div class="title text-center">4.拼音文本转公式</div>
                        <div class="content" style="font-size: 30px; height: 360px; overflow: hidden; padding:0 13px; color: white">
                            <br><br>
                            <center>
    """ + four + """

                            </center>
                        </div>
                    </div>
                </div>
            </div>
        
            <!-- JS -->
            <script src="js/jquery.min.js"></script>
            <script src="js/echarts.min.js"></script>
            <script src="js/world.js"></script>
            <script src="js/main.js"></script>
        </body>
    </html>
    """
    html.write(ans)
    html.close()
    os.system("Formula.html")

