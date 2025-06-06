import os
from typing import List, Set, Dict

from loguru import logger

from app.base import APPBase

class InviZible(APPBase):
    def __init__(self, blockList:List[str], unblockList:List[str], filterDict:Dict[str,str], filterList:List[str], filterList_var:List[str], ChinaSet:Set[str], fileName:str, sourceRule:str):
        super(InviZible, self).__init__(blockList, unblockList, filterDict, filterList, filterList_var, ChinaSet, fileName, sourceRule)

    def generate(self, isLite=False):
        try:
            if isLite:
                logger.info("generate adblock InviZible Lite...")
                fileName = self.fileNameLite
                blockList = self.blockListLite
            else:
                logger.info("generate adblock InviZible...")
                fileName = self.fileName
                blockList = self.blockList
            
            if os.path.exists(fileName):
                os.remove(fileName)
            
            # 生成规则文件
            with open(fileName, 'a') as f:
                f.write("!\n")
                if isLite:
                    f.write("! Title: AdBlock InviZible Lite\n")
                else:
                    f.write("! Title: AdBlock InviZible\n")
                f.write("! Homepage: %s\n"%(self.homepage))
                f.write("! Version: %s\n"%(self.version))
                f.write("! Last modified: %s\n"%(self.time))
                f.write("! Blocked domains: %s\n"%(len(blockList)))
                f.write("!\n")
                for domain in blockList:
                    f.write("%s\n"%(domain))
            
            if isLite:
                logger.info("adblock InviZible Lite: block=%d"%(len(blockList)))
            else:
                logger.info("adblock InviZible: block=%d"%(len(blockList)))
        except Exception as e:
            logger.error("%s"%(e))