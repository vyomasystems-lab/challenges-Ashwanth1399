# Coprocessor Design Verification

The verification environment for coprocessor 
![gitpodid](https://user-images.githubusercontent.com/109474211/181935316-b74d8be0-6380-44ba-848f-da2ee5325f86.JPG)


## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mkbitmanip module here) which takes in 32-bit inputs *src1**src2**src3**instr* and 33-bit output *mav_putvalue*

The values are assigned to the input port using 
```
mav_putvalue_src1  = 0x0200ffff
mav_putvalue_src2  = 0xf1020000
mav_putvalue_src3  = 0x00023400
mav_putvalue_instr = 0x40007033

dut.mav_putvalue_src1.value = mav_putvalue_src1
dut.mav_putvalue_src2.value = mav_putvalue_src2
dut.mav_putvalue_src3.value = mav_putvalue_src3
dut.EN_mav_putvalue.value = 1
dut.mav_putvalue_instr.value = mav_putvalue_instr
```
The assert statement is used for comparing the mkbitmanip's outut to the model_out.

The following errors is seen:
```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x1 does not match MODEL = 0x401ffff
```
```
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0x401ffff does not match MODEL = 0x3
```
## Test Scenario 1
- Test Inputs: mav_putvalue_src1  = 0x0200ffff mav_putvalue_src2  = 0xf1020000 mav_putvalue_src3  = 0x00023400 mav_putvalue_instr = 0x40007033
- Expected Output: out=0x401ffff
- Observed Output in the DUT dut.out=0x1
## Test Scenario 2
- Test Inputs: mav_putvalue_src1  = 0x0200ffff mav_putvalue_src2  = 0xf1020000 mav_putvalue_src3  = 0x00023400 mav_putvalue_instr = 0x28005033
- Expected Output: out=0x3
- Observed Output in the DUT dut.out=0x401ffff

Output mismatches for the above inputs proving that there is a design bug

## Verification Strategy
Exercising all the opcode instr and comparison with model output logic.

## Is the verification complete ?
Verification in complited by checking all the combination input and compared with model out.
