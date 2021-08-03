#Requires -Modules @{ ModuleName='Pester'; ModuleVersion='5.0.2' }

BeforeAll {
    $MedalResults = @(
        @{
            'sport' = 'cycling'
            'podium' = @('1.China', '2.Germany', '3.ROC')
        }
        @{
            'sport' = 'fencing'
            'podium' = @('1.ROC', '2.France', '3.Italy')
        }
        @{
            'sport' = 'high jump'
            'podium' = @('1.Italy', '1.Qatar', '3.Belarus')
        }
        @{
            'sport' = 'swimming'
            'podium' = @('1.USA', '2.France', '3.Brazil')
        }
    )

    $ExpectedTable = @{
        Italy = 4
        France = 4
        ROC = 4
        USA = 3
        Qatar = 3
        China = 3
        Germany = 2
        Brazil = 1
        Belarus = 1
    }

}

Describe -Name 'Validate Medal Table' {
    BeforeAll {
        $ActualTable = Build-MedalTable -Medals $MedalResults
    }
    it 'has the right number of countries' {
        $ActualTable.Count -eq $ExpectedTable.Count | should -Be true
    }
    it 'has the right score for each country' {
        ForEach ($Country in $ActualTable.keys) {
            $ExpectedTable[$Country] -eq $ActualTable[$Country] | should -Be true
        }
    }
}