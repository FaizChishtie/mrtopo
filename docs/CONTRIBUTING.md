# Contribution Guide
One of the best ways to contribute is to participate in discussions and discuss issues. 
You can also contribute by submitting pull requests with code changes.

## General Contributing Guide
> Unless it is a trivial change, make sure that there is a corresponding issue for your change first. 
If there is none, create one.

**Create a fork in GitHub**

Create a branch off the master branch. Name it something that that makes sense, such as ```issue-123``` or ```githubhandle-issue```. 
This makes it easy for everyone to figure out what the branch is used for. 
It also makes it easier to isolate your change from incoming changes from the origin.

```
// after forking: 

git clone https://github.com/YourUserName/mrtopo.git
git pull origin master
git checkout -b my-guideline-abiding-branch-name
git branch

// your branch name should show up!
```

**Commit your changes and push your changes to GitHub**

Some quick commands to help you get started!

```
git status
git add -A
// ^ use at your own risk
git commit -m "my message that follows the guidelines"
git push -u origin my-guideline-abiding-branch-name
```

**Create a pull request against the origin's master branch**

If you don't know what a pull request is [read this article](https://help.github.com/en/articles/creating-a-pull-request).
Before submitting a feature or substantial code contribution please discuss it with the team (contact information is found in the README). 

You should also take a look at these two blogs posts on contributing code: 
[Open Source Contribution Etiquette](https://tirania.org/blog/archive/2010/Dec-31.html) by Miguel de Icaza 
and [Don't "Push" Your Pull Requests](https://www.igvita.com/2011/12/19/dont-push-your-pull-requests/) by Ilya Grigorik.

## Commits
Please format commit messages as follows:

```
Summarize change in 50 characters or less

Provide more detail after the first line. Leave one blank line below the
summary and wrap all lines at 72 characters or less.

If the change fixes an issue, leave another blank line after the final
paragraph and indicate which issue is fixed in the specific format
below.

Fix #42
```

## Formatting
Do your best to factor commits appropriately, i.e not too large with unrelated things in the same commit, and not too small with the same small change applied N times in N different commits. 
If there was some accidental reformatting or whitespace changes during the course of your commits, please rebase them away before submitting the PR.
