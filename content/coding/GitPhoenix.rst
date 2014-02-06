The Git Phoenix
===============

:date: 2014-02-04 08:14
:modified: 2014-02-04 08:14
:tags: git, coding, deployment, puppet
:category: Programming
:slug: Git push for code deployment using Puppet
:author: Anthony Roy
:summary: A technique for managing a small number of machines using Puppet and git
:status: published

Git is a great tool for managing source code, and is very flexible in what you can do with it. Puppet is great for configuration management, and can be used to great effect for automating the provisioning of software onto machines.

I have been using puppet at work for a year or so now in the automation of server builds in our internal cloud. A few months ago I decided that it would make sense to use it at home to standardise my PC builds and make it easy to make changes to one machine and have that change propagate out to the others. I use git at home for my personal projects (Bitbucket for private stuff, GitHub for stuff I share) and one of the Puppet deployment methods that has come about in the last year or so is the so called Masterless Puppet, where code is pushed to a bunch of machines using git.

Incidentally this also works great for deploying arbitrary code - for example a website - to a bunch of servers.

The typical setup for this is as follows. For each machine you want to deploy to:

1. Set up an empty git repo with ``git init --bare``.
2. Write a git post-receive hook that will archive the current state of the repos master branch and unpack it in the puppet location, and then run puppet apply
   
::

    git archive --format=tar master | (cd /etc/puppet; tar -x)

On your "master" machine - which with git being distributed can be any machine you happen to be developing on, you need to set up your remote. Add the following to the ``.git/config`` file::

    [remote webservers]
        url = ssh://git@server1/puppet
        url = ssh://git@server2/puppet

This works pretty well. You deploy to each of the machines in your remotes list by simply running ``git push webservers``.

The downside to this approach is if you want to roll back code. It would be nice to be able to roll back the master branch to a particular commit without a horde of messy revert commits. With git you can move the head back to a particular commit easily using ``git reset --hard a4d779c`` for example, or to a tag if you have been tagging your code - ``git reset --hard 1.4.2``.

The issue is that git's post-receive hooks don't fire for this sort of change. Nothing is received, hence no hook is fired.

The Phoenix Script
------------------

Cue the Pheonix script, a post commit hook that destroys itself before rebuilding itself again from the ashes. It is in essence a post-receive hook which is held outside of the git repo and symlinked in, which performs the following steps when run.

1. Archive off the code to the relevant location as above.
2. Run puppet.
3. Delete the git repository.
4. Create a new bare repository in the same location.
5. Symlink itself into the .git/hooks directory.

The code itself looks like this::

    #!/bin/bash
    PHEONIX=/var/repos/phoenix.sh
    PUPPET_DIR=/etc/puppet
    GIT_REPO=/var/repos/puppet_code

    rm -rf $PUPPET_DIR/*
    cd $GIT_REPO
    git archive --format=tar master | (cd $PUPPET_DIR; tar -x)
    puppet apply $PUPPET_DIR/manifests/site.pp

    rm -rf $GIT_REPO
    mkdir $GIT_REPO
    cd $GIT_REPO
    git init --bare
    ln -s $PHEONIX $GIT_REPO/.git/hooks/post-receive

This has the advantage that whenever you push, the code will get checked out and placed in the appropriate directory, even if no commits have been made, just references (i.e. the master pointer) has been moved.

The main disadvantage to this approach is that you are having to send the entire repo over to each server every time you push. This is not a major issue if your codebase is small, but with a large infrastructure and large puppet deployment this could take quite a lot of time.

Puppet Librarian and R10K
-------------------------

There are two tools which can mitigate this overhead, and have the advantage of organising your puppet modules in a better way than keeping everything in one repository. This method has three parts.

Firstly, you need to create a git repo for each module in your codebase. This step has several advantages by itself. Teams can work on different modules without treading on each others toes. Modules can be shared on github or the like for other developers to use and enhance.

The second step is to create a Puppetfile which is effectively a shopping list of the modules you are interested in. You tell it which modules you want, their git locations if pulling directly from git (they are downloaded from the Puppetforge otherwise), and which version you want (for git repos this can be any arbitrary commit hash, branch or tag).

You then add a call to r10k from your Phoenix script. r10k reads the puppetfile and will download all modules referenced into your modules directory.
In practice, the repo that I push to each server isn't the entire puppet codebase, but a small repo which contains a Puppetfile readable by the r10k tool and some hiera configuration. This means that the push always delivers the correct puppetfile and hiera data, but the other modules that are brought in by r10k are cached. See https://github.com/adrienthebo/r10k for more details on r10k and https://github.com/rodjek/librarian-puppet for librarian puppet.
