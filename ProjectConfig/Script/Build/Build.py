#!/usr/bin/python
# coding=utf-8
import zipfile
import shutil
import os
import os.path
import time
import datetime
import sys

# include AppInfo.py
# sys.path.append('./common')
import AppInfo 

o_path = os.getcwd()  # 返回当前工作目录
# 当前工作目录 Common/PythonLaya/ProjectConfig/Script 
sys.path.append('../../') 
sys.path.append('./')  
from Config.Config import mainConfig
from Common import Source
from Config.AdConfig import mainAdConfig  
from Project.Resource import mainResource
from Common.File.FileUtil import FileUtil  
from AppInfo.AppChannel import mainAppChannel
from Common.Platform import Platform
from AppInfo.AppInfo import mainAppInfo

# https://docs.cocos.com/creator/3.0/manual/en/editor/publish/publish-in-command-line.html

class Build(): 
    builder:None
    listChannel = [] 
    def BuildClean(self): 
        targetDir = mainResource.GetRootDirAndroidStudio()
        # build
        dir2 = targetDir + "/build"
        flag = os.path.exists(dir2)
        if flag:
            shutil.rmtree(dir2)

        print("apk_build_clean sucess")


    def BuildApk(self):
        if Platform.isWindowsSystem():
            # dir1 = "C:\Program Files\Android\Android Studio\gradle"
            dir2 = "C:/moon/gradle/gradle-4.10.1"
            flag = os.path.exists(dir2)
            if not flag:
                # shutil.copytree(dir1,dir2)
                dir2 = "E:/Program Files/Android/Android Studio/gradle/gradle-4.10.1"
                flag = os.path.exists(dir2)
                if not flag:
                    # aliyun
                    dir2 = "C:/Program Files/Unity/Hub/Editor/"+source.UNITY_VERSION_WIN+"/Editor/Data/PlaybackEngines/AndroidPlayer/Tools/gradle"

    
            os.system(dir2+"/bin/gradle assembleRelease")
        else:
            dir2 = "/Users/moon/sourcecode/gradle/gradle-4.10.1/bin"
            flag = os.path.exists(dir2) 
            if flag:
                # os.system("chmod 777 "+dir2+"/gradle")
                os.system(dir2+"/gradle assembleRelease")
            else:
                os.system("gradle assembleRelease")
        


    def CopyApk(self,channel):
        gameName = mainResource.getGameName()
        gameType = mainResource.getGameType()
    # copy2 同时复制文件权限
        dirapk = mainResource.GetProjectOutPutApp() + "/apk"
        if mainResource.AppForPad(False):
            dirapk+="/heng"
            gameName += "_hd"
        else:
            dirapk+="/shu"

        if not os.path.exists(dirapk):
            os.makedirs(dirapk)

        shutil.copy2(mainResource.getAndroidProjectApk(), dirapk + "/" +
                    gameType + "_" + gameName + "_" + channel + ".apk")
    def Init(self,channel): 
        self.listChannel.clear()
        if channel==Source.HUAWEI:
            self.listChannel.append(Source.HUAWEI)
        if channel==Source.TAPTAP:
            self.listChannel.append(Source.TAPTAP)
        if channel==Source.GP:
            self.listChannel.append(Source.GP)
        if channel=="all":
            self.listChannel.append(Source.HUAWEI)
            self.listChannel.append(Source.TAPTAP)
            self.listChannel.append(Source.GP)
 
    def GetProjectName(self,channel):  
        name = ""
        if channel==Source.Oppo:
            name = Source.ProjectNameMiniGameOppo
        if channel==Source.Vivo:
            name = Source.ProjectNameMiniGameVivo 
        if channel==Source.XIAOMI:
            name = Source.ProjectNameMiniGameXiaomi
        if channel==Source.HUAWEI:
            name = Source.ProjectNameMiniGameHuawei
        if channel==Source.Facebook:
            name = Source.ProjectNameMiniGameFacebook
        if channel==Source.BYTE:
            name = Source.ProjectNameMiniGameByte
        if channel==Source.WEIXIN:
            name = Source.ProjectNameMiniGameWeixin 
        if channel==Source.QQ:
            name = Source.ProjectNameMiniGameWeixin 
        return name
 

    def DeleteCloudRes(self):  
        dir = mainResource.GetRootUnityAssetsResource()+"/GameRes/CloudRes" 
        FileUtil.RemoveDir(dir)
        file = mainResource.GetRootUnityAssetsResource()+"/GameRes/CloudRes.zip" 
        FileUtil.RemoveFile(file)


#  
# cocos creator 3.0 打包 qq 编译出错问题 
# VM20:254 文件game.js执行出现异常
#  ReferenceError: System is not defined
#     at game.js? [sm]:37
#     at f (QGame.js:1)
#     at QGame.js:1
# https://zhuanlan.zhihu.com/p/265033132?ivk_sa=1024320u
# //game.js 此行为加入代码,赋值globalThis.System
# globalThis.System = global.System;

#  

    def BuildProject(self,isHD,channel):  
        name =  self.GetProjectName(channel)
        dirproject = mainResource.GetRootCocosBuildOutput()+"/"+name
        appid = mainAppInfo.GetAppId(isHD, channel)
        if name == Source.ProjectNameMiniGameWeixin or name == Source.ProjectNameMiniGameByte:
            filepath = mainResource.GetProjectConfigDefault()+ "/"+name+"/game.json"
            strfile = FileUtil.GetFileString(filepath)
            strfile = strfile.replace("_Orientation_","portrait")
            filepath = dirproject+ "/game.json"
            FileUtil.RemoveFile(filepath)
            FileUtil.SaveString2File(strfile,filepath)


            filepath = mainResource.GetProjectConfigDefault()+ "/"+name+"/project.config.json"
            strfile = FileUtil.GetFileString(filepath)  
            print("BuildWeixin  appid="+appid)
            # wx3e44af039aee1b96
            strfile = strfile.replace("_APPID_",appid)
            # print("BuildWeixin  strfile="+strfile)
            filepath = dirproject + "/project.config.json"
            FileUtil.RemoveFile(filepath)
            FileUtil.SaveString2File(strfile,filepath)


        # python 里无法直接执行cd目录，要用chdir改变当前的工作目录
        if os.path.exists(dirproject):
            os.chdir(dirproject) 
        print("dirproject:" + dirproject)
        if name == Source.ProjectNameMiniGameVivo: 
            os.system("npm install")
            os.system("npm run build")
      

    def GenerateProject(self,isHD,channel):  
        name =  self.GetProjectName(channel)
        # cloudres 
        # output 
        dir = mainResource.GetRootCocosBuildOutput()+"/"+name
        FileUtil.RemoveDir(dir)
 
        # 0f6 2f1
        UNITYPATH=""
        if Platform.isWindowsSystem():
            # UNITYPATH="E:/Unity/"+Source.UNITY_VERSION_WIN+"/Editor/Unity.exe"
            UNITYPATH= "CocosCreator.exe"
        else:
            # UNITYPATH="/Applications/Unity/Hub/Editor/"+Source.UNITY_VERSION_MAC+"/Unity.app/Contents/MacOS/Unity" 
            UNITYPATH="/Applications/CocosCreator/Creator/"+Source.Cocos_Version+"/CocosCreator.app/Contents/MacOS/CocosCreator"
            #  --project projectPath--build "platform=web-desktop;debug=true"


        appid = mainAppInfo.GetAppId(isHD, channel)
        PROJECT_PATH= mainResource.GetRootProjectUnity()
        # cmd = UNITYPATH+" --project "+ PROJECT_PATH+" --build "+ "\"platform=wechatgame;debug=false\""

        # package = "packages: { wechatgame: {appid: '*****',}}"
        package = "packages: { wechatgame: {appid: '"+appid+"',}}"
        # cmd = UNITYPATH+" --project "+ PROJECT_PATH+" --build "+ "\"platform="+name+";debug=false;packages="+package+"\""
        cmd = UNITYPATH+" --project "+ PROJECT_PATH+" --build "+ "\"platform="+name+";debug=false"+"\""
        
        print("BuildWeixin  cmd="+cmd)
        # ps = subprocess.Popen(cmd)
        # ps.wait()#让程序阻塞
        os.system(cmd)
 
        print("BuildWeixin  end")

      

# 主函数的实现
    def Run(self,platform,channel,isHD):  
        print("Build Run platform="+platform+" channel="+channel+" isHD="+str(isHD))
        self.Init(channel)
        gameName = mainResource.getGameName()
        gameType = mainResource.getGameType() 
        print("gameName="+gameName)
        print ("gameType="+gameType) 
        if platform==Source.ANDROID:
        # python 里无法直接执行cd目录，想要用chdir改变当前的工作目录
            android_studio_dir = mainResource.GetRootDirAndroidStudio()
            # python 里无法直接执行cd目录，要用chdir改变当前的工作目录
            os.chdir(android_studio_dir)
            for channel in self.listChannel:
                print("apk_build:" + channel)
                self.BuildClean()
                mainAppChannel.UpdateChannel(channel,isHD) 
                self.BuildApk()
                self.CopyApk(channel)


        if platform==Source.MinProgram:
            self.DeleteCloudRes()

            if channel == Source.WEIXIN2:
                self.BuildProject(isHD,Source.WEIXIN)
            else:
                self.GenerateProject(isHD,channel)
                self.BuildProject(isHD,channel)

 
  

        print("Build sucess channel="+channel)

mainBuild = Build()
