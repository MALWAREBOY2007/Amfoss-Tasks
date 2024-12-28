## Task 1:Terminal Wizard

### 1.Enter the maze:

**Command**: git clone https://github.com/KshitijThareja/TerminalWizard.git`

**Explaination**: This will clone the repository into our computer..

**Command**: mkdir Codes

**Explaination**: This will create a new directory named "Codes".

**Command**: cd Codes

**Explaination**: This will change the present working directory.

### 2.First Challenge:

**Cracking x**: First perfect number is 6,as the sum of the factors of 6 is equal to 6.

**Cracking y**: After differentiating x^2-7x we get "y" equal to 5.

**Command**: cd 06

**Command**: cat spell_05.txt

**Output**: Impedimenta.py

**Command**: cd ..

**Explaination**: Goes to previously used directory

**Command**: cd spellbook

**Command**: python3 Impedimenta.py

**Explaination**: Executing the Impedimenta.py file

**Output**: aHR0cHM6Ly9naX

### 3.Second Challenge:

**Cracking x,y**: Atomic number of the element first used to make semicondutors is Germanium(32)

**MIstake**: At first after Googling this,it gave me the answer as silicon(14) But,after some serious Googling in depth..i was able to find out that the answer is Germanium(32).

**Command**: cd 02

After this the same process is done as above challenge.

### 4.Third Challenge:

**Explaination**: After Googling the riddle..the answer is Riddikulus

**Command:** git checkout defenseAganistTheDarkArts

**Explaination**: Now,by using this command we are going to change into a new branch

**Command:** cd spellbook

**Result**: we found the Riddikulus.py which was not in the main branch

**Command**:git checkout main

**Result:** Going to the main branch.

**Command**: git checkout defenseAganistTheDarkArts spellbook/Riddikulus.py

**Result:** This command will copy the Riddikulus.py file from defenseAganistTheDarkArts branch to main branch.

After this the same process as the above challenges..

### 5.Fourth challenge

**Command**: git log

**Explaination**: Shows the previous commits done by all the members

After searching for the spell which is hidden in the commits logs of this repositary..

**Result**: Hey there! The last spell is in path 0x/Spell_0y" of thegraveyard...where x is the number of horcruxes made by Voldemort and y is the number that has same alphabets as the number

**Cracking x:** no of horcruxes made by the voldemort are 7

**Cracking y**: The number which has same no of alphabets as the number is 4

After this the process is same as the above challenges..

### 6.The end

After Getting all the codes,I combined the codes into one base64 encoded string..

**Command**:echo aHR0cHM6Ly9naXRodWIuY29tL1RoZUh1bnRzbWFuNC9UaGVGaW5hbFNwZWxs | base64 --decode

**Result**: https://github.com/TheHuntsman4/TheFinalSpell

### Pushing Solution.md to git repo

**Command**: git add

**Explaination**: Adding the file(Solution.md)

**Command:** git commit -m "Comitted the file Solution.md"

**Explaination**: Saving the changes done to the file content

**Command**: git push origin main

**Explaination**: Pusing the changes into the git repositary(Amfoss-Tasks)

# 
