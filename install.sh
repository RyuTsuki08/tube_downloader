#!/bin/bash

env=./tube

found_program(){
     which $1 > /dev/null 2>&1 &&
          echo -e "\e[0;32mfound\e[0m" || 
          echo -e "\e[0;31mnot found\e[0m"
}

echo -n "Checking for required programs: "
if found_program python; then echo  -n "python..."; else  echo -e "\e[0;31mFAIL\e[0m"; fi
if found_program node;  then echo -n "node..."; else echo -e "\e[0;31mFAIL\e[0m"; fi
if found_program npm;   then echo -n "npm..."; else echo -e "\e[0;31mFAIL\e[0m"; fi
if found_program git;   then echo -e "git...\e[0;32mfound\e[0m"; else echo -e "\e[0;31mFAIL\e[0m"; fi

# if test find . -type d -name tube ; then echo -n -e"enviroment.. \e[0;32mok\e[0m"; else echo -e "enviroment... \e[0;31SFAILED\e[0m"; fi

# exitcode=$?
# if [ $exitcode !=  0 ]; then echo "[FAIL]"; exit 1; fi
# echo "[OK]"