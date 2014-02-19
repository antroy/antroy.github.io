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

I will start with the bash part of the script. This can be copied replacing just the name of your completion program and the commands to complete. It focuses on getting the important information out of bash completion and into your code.

.. code-block:: bash

    _complete () {
        local cur prev
        cur=${COMP_WORDS[COMP_CWORD]}
    
        words=`./comp_blog.py "$COMP_CWORD" ${COMP_WORDS[*]}` 
    
        COMPREPLY=( $(compgen -W "${words}" -- ${cur}) )
    }
    
    
    blog(){
        echo "blog $*"
    }

complete -F _complete blog
    
The above script is boilerplate code that gets the right values out of the competion variables and sends them through to your script. The arguments passed in are the current word, the previous word and then all of the arguments. The current and previous could probably be left out, as all of the information required will be in that final list of "COMP_WORDS".

The Python Part
===============

Time for the Python script. This will just implement a multi-level completion where previous terms dictate what future terms look like.

.. code-block:: python

    #!/usr/bin/python
    import sys
    
    options = {
            'add': ['--name', '--date', '--content'],
            'delete': ['--name', '--force']
    }
    commands = options.keys()
    
    index = int(sys.argv[1])
    all = sys.argv[2:]
    
    cur = "" if len(all) <= index else all[index]
    prev = all[index - 1]
    all = all[1:]
    
    if prev not in all:
        print " ".join(commands)
    else:
        command_list = [word for word in all if word in commands]
        if command_list:
            opts = options[command_list[0]]
            print " ".join([opt for opt in opts if opt not in all])
        else:
            print ""
    
Note.
