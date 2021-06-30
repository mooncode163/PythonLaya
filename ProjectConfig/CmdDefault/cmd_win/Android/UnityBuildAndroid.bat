@echo  unity_build
@set filepath = %~dp0 

cd ../../../../../../Common/PythonLaya/ProjectConfig/Script

python ProjectManager.py %~dp0 UnityBuild android
  
@Pause
