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
if found_program git;   then echo -n "git..."; else echo -e "\e[0;31mFAIL\e[0m"; fi
if found_program kitty;   then echo -e "kitty...\e[0;32mfound\e[0m"; else echo -e "\e[0;31mFAIL\e[0m"; fi
if python -c "import venv" > /dev/null 2>&1 ; then
    echo -e "venv...\e[0;32mfound\e[0m"
else
    echo -e "venv...\e[0;31mnot found\e[0m"
    echo "Installing venv..."
    pip install -r venv
fi

if find . -type d -name a > /dev/null 2>&1; 
then 
echo -n -e "enviroment.. \e[0;32mok\e[0m"
else echo -e "enviroment... \e[0;31SFAILED\e[0m"; 
fi

source tube/bin/activate;
pip install -r requirements.txt
kitty -e uvicorn main:app --reload &
git clone "https://github.com/RyuTsuki08/tube_downloader_frontend.git" && cd tube_downloader_frontend
if pwd | grep -q 'tube_downloader_frontend'; then
    echo "Already in the correct directory."
else
    echo "Moving into the downloader directory."
    cd ../tube_downloader_frontend
fi

kitty -e npm install && npm run dev &

# exitcode=$?
# if [ $exitcode !=  0 ]; then echo "[FAIL]"; exit 1; fi
# echo "[OK]"