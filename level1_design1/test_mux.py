# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
import random
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    inp=[]
    inp=[random.randint(1,3) for i in range(31)]
    dut.inp0.value=inp[0]
    dut.inp1.value=inp[1]
    dut.inp2.value=inp[2]
    dut.inp3.value=inp[3]
    dut.inp4.value=inp[4]
    dut.inp5.value=inp[5]
    dut.inp6.value=inp[6]
    dut.inp7.value=inp[7]
    dut.inp8.value=inp[8]
    dut.inp9.value=inp[9]
    dut.inp10.value=inp[10]
    dut.inp11.value=inp[11]
    dut.inp12.value=inp[12]
    dut.inp13.value=inp[13]
    dut.inp14.value=inp[14]
    dut.inp15.value=inp[15]
    dut.inp16.value=inp[16]
    dut.inp17.value=inp[17]
    dut.inp18.value=inp[18]
    dut.inp19.value=inp[19]
    dut.inp20.value=inp[20]
    dut.inp21.value=inp[21]
    dut.inp22.value=inp[22]
    dut.inp23.value=inp[23]
    dut.inp24.value=inp[24]
    dut.inp25.value=inp[25]
    dut.inp26.value=inp[26]
    dut.inp27.value=inp[27]
    dut.inp28.value=inp[28]
    dut.inp29.value=inp[29]
    dut.inp30.value=inp[30]
    for i in range (31):
        sel=i
        dut.sel.value=sel
        await Timer(2, units='ns')
        dut.log.info(f'Sel={sel:2} Expected_out={inp[sel]:2}  DUT={int(dut.out.value):2}')
        assert dut.out.value == inp[sel], "Randomised test failed with:= {out} = {expected_out} ".format(out=dut.out.value, expected_out=inp[sel])