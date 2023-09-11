
$inserted_ids = New-Object Collections.Generic.List[string]

Get-ChildItem -Path ./dataformats/testdata/ | 
Foreach-Object {
    $_.FullName
    $result = python ./python/src/cli/main.py write-file --path $_.FullName
    $inserted_ids.Add($result)
}

foreach ($id in $inserted_ids) {
    python ./python/src/cli/main.py read-file --id $id --verbose
}