===============
Bash Completion
===============

:date: 2014-02-04 17:24
:modified: 2014-02-04 17:24
:tags: coding, bash, autocomplete, python, ruby
:category: Programming
:slug: Complex commandline completion in the bash shell
:author: Anthony Roy
:summary: Command line completion can be awkward in bash. Make it easier by shelling out to a more powerful language.
:status: draft

Bash completion can be awkward to program in bash. The docs aren't great, and the language esoteric. It would be nice to be able to use your favorite language to do the heavy lifting. This article shows how to acheive this in Python and Ruby and provides an example of how you can call in to your own application to get the completion data.

The Bash Part
=============

I will start with the bash part of the script. This can be copied replacing just the name of your completion program and the commands to complete. It focuses on getting the important information out of bash completion and into your code::

    _woof () {
        local cur prev
        cur=${COMP_WORDS[COMP_CWORD]}
        prev=${COMP_WORDS[COMP_CWORD - 1]}
        all=$( IFS=$' '; echo "${COMP_WORDS[*]}" )
    
        words=`./dog.py "$cur" "$prev" ${COMP_WORDS[*]}` 
    
        COMPREPLY=( $(compgen -W "${words}" -- ${cur}) )
    }
    
    
    dog(){
        echo "Woof. $*"
    }
    
    complete -F _woof dog
    
The above script is boilerplate code that gets the right values out of the competion variables and sends them through to your script. The arguments passed in are the current word, the previous word and then all of the arguments. The current and previous could probably be left out, as all of the information required will be in that final list of "COMP_WORDS".

The Python Part
===============

Time for the Python script. This will just implement a multi-level completion where previous terms dictate what future terms look like.


