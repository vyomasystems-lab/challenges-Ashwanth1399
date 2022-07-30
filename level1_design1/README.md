# Mux Design Verification

The verification environment for 31:1 MUX 
![gitpodid](https://user-images.githubusercontent.com/109474211/181925564-cebad5ba-21c3-4790-973d-b63d51a1329a.JPG)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (mux module here) which takes in 2-bit 31-inputs *inp0-inp30* and 5-bit input *sel* and gives 2-bit output *out*

The values are assigned to the input port using 
```
dut.inp0.value = random.randint(1,3)
    :
dut.inp30.value = random.randint(1,3)
```

The assert statement is used for comparing the mux's outut to the expected_out.

The following error is seen:
```
assert dut.out.value == inp[sel], "Test failed with:= sel={sel}  expected_out= {expected_out} DUT={out}".format(out=dut.out.value, expected_out=inp[sel],sel=dut.sel.value)
             AssertionError: Test failed with:= sel=01100  expected_out= 1 DUT=00
```
## Test Scenario 
- Test Inputs: inp12=2 Sel=12
- Expected Output: out=2
- Observed Output in the DUT dut.out=0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
5'b01101: out = inp12;//->bug 5'b1100: out = inp12
5'b01101: out = inp13;
```
For the select line, the logic 12 should be ``01100`` instead of ``01101`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.
5'b1100: out = inp12;



## Verification Strategy
Randomizing all the input pins to values between 1 and 3, testing the expected_out and out by checking all the combination of sel pin.

## Is the verification complete ?
Verification in complited by checking all the combination input and compared with expected_out.
