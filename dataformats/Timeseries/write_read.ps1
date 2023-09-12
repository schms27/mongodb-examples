function Get-RandomDecimalArray{
    param (
        $numElements
    )

    $decArray = New-Object double[] $numElements

    for ($num = 0 ; $num -lt $numElements ; $num++){
        $numerator = Get-Random -Minimum -100 -Maximum 100
        $denominator = Get-Random -Minimum -100 -Maximum 100
        $decArray[$num] =  [math]::Round($numerator / $denominator, 4)
    }

    return $decArray
}


$h = [ordered]@{
    metadata=[ordered]@{}; 
    axisX=Get-RandomDecimalArray -numElements 10;
    axisY=Get-RandomDecimalArray -numElements 10;
    axisZ=Get-RandomDecimalArray -numElements 10;
}

$h.metadata.version = "1.0.0"
$h.metadata.testbenchName = "Prüfplatz A"
$h.metadata.partNumber = "565097"
$h.metadata.serialNumber = "0001"
$h.metadata.mesurementId = [guid]::NewGuid().ToString()
$h.metadata.sampleRateHz = 10
$h.metadata.series = @{}
$h.metadata.series.axisX = @{}
$h.metadata.series.axisX.unit = "mm"
$h.metadata.series.axisY = @{}
$h.metadata.series.axisY.unit = "mm"
$h.metadata.series.axisZ = @{}
$h.metadata.series.axisZ.unit = "mm"





$json = $h | ConvertTo-Json -Depth 9

$result = python ./python/src/cli/main.py write-object -o $json -d measurements -c ts_max_velocity
Write-Host $result