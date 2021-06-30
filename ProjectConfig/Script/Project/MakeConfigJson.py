#!/usr/bin/python
# coding=utf-8
import sys
import zipfile
import shutil
import os
import os.path
import time,  datetime
import json 

o_path = os.getcwd()  # 返回当前工作目录
# 当前工作目录 Common/PythonLaya/ProjectConfig/Script
sys.path.append('../../') 
sys.path.append('./')  
from Config.Config import mainConfig
from Common import Source
from Config.AdConfig import mainAdConfig  
from Project.Resource import mainResource
from Common.File.FileUtil import FileUtil 

class MakeConfigJson(): 
    
    dirCloudResHead = "Resources/GameRes/CloudRes/"
 

    def ScanImageFile(self,dir,filejson):
        # if not os.path.exists(dir):
        #     return

        listFile = []
        if os.path.exists(dir):
            FileUtil.GetFileList(dir,"png",listFile)
            FileUtil.GetFileList(dir,"jpg",listFile)
            print("listFile len="+str(len(listFile)))
        dataRootOld = None
        if os.path.exists(filejson)==True:
            print("filejson = "+filejson)
            strfile = FileUtil.GetFileString(filejson)
            # print("strfile = "+strfile)
            dataRootOld = json.loads(strfile)
            if dataRootOld is  None:
                print("dataRootOld is  none")
                print("strfile = "+strfile)
            # remove
            os.remove(filejson)

        dataRoot = json.loads("{}") 
    #        "BtnIconPlay" : {
    #     "path" : "App/UI/Common/Button/BtnIconPlay.png"
    # },
        for fileimage in listFile:
            
            item= json.loads("{}")
            filepath = fileimage.replace(mainResource.GetRootUnityAssets() + "/", "")
            filepath = filepath.replace(self.dirCloudResHead, "")
            
            item["path"]=filepath 
            name = FileUtil.GetPathNameWithoutExt(fileimage)


            # 从原来的json中恢复board
            if dataRootOld is not None:
                # print("dataRootOld is not none")
                if name in dataRootOld:
                    # print("dataRootOld  name="+name)
                    dataitem = dataRootOld[name]
                    key = "board"
                    # key = "path"
                    # if name =="BtnCommon":
                    #     # key = "board"
                    #     print("dataitem[key] = "+dataitem[key]+" name="+name)

                    if key in dataitem:
                        print("key = "+key+" name="+name)
                        item[key] = dataitem[key] 
    
            dataRoot[name]=item 


        json_str = json.dumps(dataRoot,ensure_ascii=False,indent=4,sort_keys = True)
        FileUtil.SaveString2File(json_str,filejson)

    def ScanPrefabFile(self,dir,filejson):
        if not os.path.exists(dir):
            return
        listFile = []

        dirsave = FileUtil.GetLastDirofDir(filejson)
        FileUtil.CreateDir((dirsave))

        FileUtil.GetFileList(dir,"prefab",listFile) 
        

        dataRoot = json.loads("{}") 
    #        "BtnIconPlay" : {
    #     "path" : "App/UI/Common/Button/BtnIconPlay.png"
    # },
        for fileimage in listFile:
            # item= json.loads("{}")
            filepath = fileimage.replace(mainResource.GetRootUnityAssets() + "/", "")
            # item["path"]=filepath 
            name = FileUtil.GetPathNameWithoutExt(fileimage)
            dataRoot[name]=filepath  

        json_str = json.dumps(dataRoot,ensure_ascii=False,indent=4,sort_keys = True)
        FileUtil.SaveString2File(json_str,filejson)



    def ScanAudioFile(self,dir,filejson):
        if not os.path.exists(dir):
            return
        listFile = []

        dirsave = FileUtil.GetLastDirofDir(filejson)
        FileUtil.CreateDir((dirsave))

        FileUtil.GetFileList(dir,"mp3",listFile) 
        FileUtil.GetFileList(dir,"wav",listFile) 
        FileUtil.GetFileList(dir,"ogg",listFile) 

        dataRoot = json.loads("{}") 
    #        "BtnIconPlay" : {
    #     "path" : "App/UI/Common/Button/BtnIconPlay.png"
    # },
        for fileimage in listFile:
            filepath = fileimage.replace(mainResource.GetRootUnityAssets() + "/", "")
            filepath = filepath.replace(self.dirCloudResHead, "")
                        # item= json.loads("{}")
            # item["path"]=filepath 
            name = FileUtil.GetPathNameWithoutExt(fileimage)
            dataRoot[name]=filepath  

        json_str = json.dumps(dataRoot,ensure_ascii=False,indent=4,sort_keys = True)
        FileUtil.SaveString2File(json_str,filejson)


    def MakeConfigImage(self):
        dir1 = mainResource.GetRootUnityAssetsResource()+"/App/UI"    
        filepathJson = mainResource.GetRootUnityAssetsResource() + "/ConfigData/Image/" + "ImageResApp.json"
        self.ScanImageFile(dir1, filepathJson)

        dir2 = mainResource.GetRootUnityAssetsResource()+"/AppCommon/UI"  
        filepathJson = mainResource.GetRootUnityAssetsResource() + "/ConfigData/Image/" + "ImageResAppCommon.json"
        self.ScanImageFile(dir2, filepathJson)

        dircommon = mainResource.GetRootUnityAssetsResource()+"/Common/UI"  
        filepathJson = dircommon + "/ImageRes.json"
        self.ScanImageFile(dircommon, filepathJson)


        # # CloudRes
        dircommon = mainResource.GetRootUnityAssetsResource()+"/GameRes/CloudRes" 
        filepathJson = dircommon + "/ImageResCloudRes.json"
        self.ScanImageFile(dircommon, filepathJson)
        filedst = mainResource.GetResourceDataApp()+"/GameRes/CloudRes/ImageResCloudRes.json" 
        FileUtil.CopyFile(filepathJson,filedst)
 

    def MakeConfigPrefab(self): 

        dir1 = mainResource.GetRootUnityAssetsResource()+"/App/Prefab"    
        filepathJson = mainResource.GetRootUnityAssetsResource() + "/ConfigData/Prefab/" + "ConfigPrefabApp.json"
        self.ScanPrefabFile(dir1, filepathJson)

        dir2 = mainResource.GetRootUnityAssetsResource()+"/AppCommon/Prefab"  
        filepathJson = mainResource.GetRootUnityAssetsResource() + "/ConfigData/Prefab/" + "ConfigPrefabAppCommon.json"
        self.ScanPrefabFile(dir2, filepathJson)

        dircommon = mainResource.GetRootUnityAssetsResource()+"/Common/Prefab" 
        filepathJson = dircommon + "/ConfigPrefab.json"
        self.ScanPrefabFile(dircommon, filepathJson)

    def MakeConfigAudio(self): 

        # dir1 = mainResource.GetRootUnityAssetsResource()+"/App/Audio"    
        # filepathJson = mainResource.GetRootUnityAssetsResource() + "/ConfigData/Audio/" + "ConfigAudioApp.json"
        # self.ScanAudioFile(dir1, filepathJson)

        # dir2 = mainResource.GetRootUnityAssetsResource()+"/AppCommon/Audio"  
        # filepathJson = mainResource.GetRootUnityAssetsResource() + "/ConfigData/Audio/" + "ConfigAudioAppCommon.json"
        # self.ScanAudioFile(dir2, filepathJson)

              # # CloudRes
        dircommon = mainResource.GetRootUnityAssetsResource()+"/GameRes/CloudRes" 
        filepathJson = dircommon + "/AudioCloudRes.json"
        self.ScanAudioFile(dircommon, filepathJson)
        filedst = mainResource.GetResourceDataApp()+"/GameRes/CloudRes/AudioCloudRes.json" 
        FileUtil.CopyFile(filepathJson,filedst)

     
#主函数的实现
    def Run(self): 
        # gameType = mainResource.getGameType()
        # gameName = mainResource.getGameName()
        self.MakeConfigImage() 
        self.MakeConfigPrefab() 
        self.MakeConfigAudio() 
        
        print ("MakeConfigJson sucess")    

mainMakeConfigJson = MakeConfigJson()  