# Mux Design Verification

The verification environment for 1011 sequence detector 
![gitpodid](https://user-images.githubusercontent.com/109474211/181925564-cebad5ba-21c3-4790-973d-b63d51a1329a.JPG)

## Verification Environment

The [CoCoTb](https://www.cocotb.org/) based Python test is developed as explained. The test drives inputs to the Design Under Test (seq_detect_1011 module here) which takes in 1-bit input *inp_bit*  and change to next state, finall gives 1-bit output *seq.seen*

The values are assigned to the input port using 
```
inp_bit=[1,0,1,1,1,0,1,1,1]
for i in range(9):
        dut.inp_bit.value=inp_bit[i]
```

The assert statement is used for comparing the seq_seen to the expected_out.

The following error is seen:
Error1
```
assert dut.seq_seen.value == exp_out[i], "sequence not detected"
                     AssertionError: sequence not detected
```
Error2
```
assert dut.seq_seen.value == exp_out[i], "Overlap sequence not detected"
                     AssertionError: Overlap sequence not detected
```

## Test Scenario 1 
- Test Inputs:inp_bit=1,0,1,1,1,0,1,1,1
- Expected Output: seq_seen=0,0,0,0,1,0,0,0,1
- Observed Output in the DUT dut.seqseen=0,0,0,0,1,0,0,0,0
## Test Scenario 
- Test Inputs:inp_bit=1,0,1,1,0,1,1,1
- Expected Output: seq_seen=0,0,0,0,1,0,0,1,0
- Observed Output in the DUT dut.seqseen=0,0,0,0,1,0,0,0,0

Output mismatches for the above inputs proving that there is a design bug

## Design Bug
Based on the above test input and analysing the design, we see the following

```
SEQ_1011:
      begin
        next_state = IDLE;//->bug 
      end
```
For the select line, the logic 12 should be ``01100`` instead of ``01101`` as in the design code.

## Design Fix
Updating the design and re-running the test makes the test pass.
SEQ_1011:
      begin
        if(inp_bit==1) 
          next_state=SEQ_1;
        else 
          next_state=SEQ_10;
      end
![seq](https://user-images.githubusercontent.com/109474211/181935050-43d341f1-4ccc-43aa-b72d-08787b7e4889.JPG)

## Verification Strategy
Input sequence is given as array , testing the expected_out array match with seq_seen outputs.

## Is the verification complete ?
Verification in complited by checking all the possible transition of state and verified with expected out.
