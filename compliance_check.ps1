# Check if a package is approved  
param([string]$package)  

# Read approved packages  
$approved = Get-Content "approved_packages.txt"  

if ($approved -contains $package) {  
    Write-Host "SUCCESS: $package is approved."  
    exit 0  
} else {  
    Write-Host "ERROR: $package is NOT approved."  
    exit 1  
}  