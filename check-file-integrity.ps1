# Commands to check integrity of file with SHA-256

# (!) Create method to input filePath and target
$filePath = "C:\Users\Caio Sergio\Downloads\gpg4win-4.1.0.exe"

# will be the target sha-256 string from the font
$target = "e0fddc840808eef9531f14a515f8b3b6c46511977f00569161129c1dee413b38"

# Display details in list format
Get-FileHash $filePath | Format-List

# Compare, if True all ok
(Get-FileHash $filePath).Hash -eq $target.ToUpper()