# APB Protocol Design Verification

The verification environment for APB Protocol 
![gitpodid](https://user-images.githubusercontent.com/109474211/181935316-b74d8be0-6380-44ba-848f-da2ee5325f86.JPG)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (apb_v3_sram module here) which takes input*PRESETn**PADDR**PWDATA**PWRITE**PSEL**PENABLE* and Outpts are *PREADY**PRDATA**PSLVERR*.
The values are assigned to the input port using 
```
dut.PRESETn.value = 0
dut.PWRITE.value= 1
dut.PSEL.value  = 1
dut.PWDATA.value= wdata
dut.PENABLE.value=1
```
The assert statement is used for comparing the apb_v3_sram's outut to the model_out.

The following errors is seen:
```
assert dut.PRDATA.value == wdata, "wdata is not same as rdata"
                     AssertionError: wdata is not same as rdata
```
## Test Scenario 
- Test Inputs: PADDR=22 PWDATA=2147483647
- Operation performed: Write 2147483647 in 22 then read from 22
- Expected Output: out=2147483647
- Observed Output in the DUT dut.PRDATA=0

Output mismatches for the above inputs proving that there is a design bug

## Verification Strategy
APB protocol RAM is tested by writting data into some random address and reading the data from that address 
## Is the verification complete ?
Verification in complited by checking writing and reading from RAM
