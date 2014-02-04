The Git Phoenix
===============

:date: 2014-02-04 08:14
:modified: 2014-02-04 08:14
:tags: git, coding, deployment, puppet
:category: Programming
:slug: Git push for code deployment using Puppet
:author: Anthony Roy
:summary: A technique for managing a small number of machines using Puppet and git
:status: draft

Git is a great tool for managing source code, and is very flexible in what you can do with it. Puppet is great for configuration management, and can be used to great effect for automating the provisioning of software onto machines.

I have been using puppet at work for a year or so now in the automation of server builds in our internal cloud. A few months ago I decided that it would make sense to use it at home to standardise my PC builds and make it easy to make changes to one machine and have that change propagate out to the others. I use git at home for my personal projects (Bitbucket for private stuff, GitHub for stuff I share) and one of the Puppet deployment methods that has come about in the last year or so is the so called Masterless Puppet, where code is pushed to a bunch of machines using git.

Incidentally this also works great for deploying arbitrary code - for example a website - to a bunch of servers.

The typical setup for this is as follows. For each machine you want to deploy to:

1. Set up an empty git repo with ``git init --bare``.
2. Write a git post-receive hook that will archive the current state of the repos master branch and unpack it in the puppet location, and then run puppet apply::

   cd /etc/puppet
   git archive | tar -xz

On your "master" machine - which with git being distributed can be any machine you happen to be developing on, you need to set up your remote. Add the following to the ``.git/config`` file::

    [remote webservers]
    blah.balh
    blah.balh

This works pretty well. You deploy to each of the machines in your remotes list by simply running ``git push webservers``.

The downside to this approach is if you want to roll back code. It would be nice to be able to roll back the master branch to a particular commit without a horde of messy revert commits. With git you can move the head back to a particular commit easily using ``git reset --hard a4d779c`` for example, or to a tag if you have been tagging your code - ``git reset --hard 1.4.2``.

The issue is that git's post-receive hooks don't fire for this sort of change. Nothing is received, hence no hook is fired. A solution to this is to have a post-receive hook which is held outside of the git repo and symlinked in, which performs the following steps when run.

1. Archive off the code to the relevant location as above.
2. Run puppet.
3. Delete the git repository.
4. Create a new bare repository in the same location.
5. Symlink itself into the .git/hooks directory.

The code itself looks like this::

    #!/bin/bash
    rm -rf /etc/puppet/*
    cd /etc/puppet
    git archive | tar -xz
    puppet apply --modulepath /etc/puppet/manifests/site.pp

    rm -rf /var/repos/puppet_code
    mkdir /var/repos/puppet_code
    cd /var/repos/puppet_code
    git init --bare
    ln -s /var/repos/phoenix.sh /var/repos/puppet_code/.git/hooks/post-receive

This has the advantage that whenever you push, the code will get checked out and placed in the appropriate directory, even if no commits have been made, just references (i.e. the master pointer) has been moved.


