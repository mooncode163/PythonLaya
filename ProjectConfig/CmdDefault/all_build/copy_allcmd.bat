@echo  apk_build_gp
@set filepath = %~dp0 
 
cd ../../../Common/PythonLaya/ProjectConfig/Script
python ProjectManager.py %~dp0 CopyAllCmd
  
@Pause
