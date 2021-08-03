# Grad Tech Test - PowerShell

## Clone this repository

Use `git clone` to clone the repository locally, then change the remote, please do not fork this repository. To change the remote, use

```powershell
git remote set-url origin <path-to-your-blank-repository>
git push -u origin <branch-name>
```

## Setup

Install the pester module for testing: `install-module pester -MinimumVersion 5.0.2 -MaximumVersion 5.0.2`

## Challenge

In the file [medals.ps1](medals.ps1), there's a function for creating a medal table based on sports result. Update the function with your implementation, you'll find input data and expected output data in [medals.test.ps1](medals.test.ps1)

To run the tests:

1. `cd powershell`
1. Run `. .\medals.ps1` (change filepath delimiter as relevant for your system)
1. Run `invoke-pester`

## Tips

When the test passes clean up your code.
It's worth spending time formatting and simplifing things.
It's more important that humans can read your code than computers.
