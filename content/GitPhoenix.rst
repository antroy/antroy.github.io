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

The typical setup for this is as follows. For each machine you want to deploy to:

1. Set up an empty git repo with `git init --bare`.
2. Write a git post-receive hook that will archive the current state of the repos master branch and unpack it in the puppet location, and then run puppet apply::

   cd /etc/puppet
   git archive | tar -xz


