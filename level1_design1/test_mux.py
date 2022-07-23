# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    dut.inp0.value=1
    dut.inp1.value=2
    dut.inp2.value=3
    dut.inp3.value=1
    dut.inp4.value=2
    dut.inp5.value=3
    dut.inp6.value=1
    dut.inp7.value=2
    dut.inp8.value=3
    dut.inp9.value=1
    dut.inp10.value=2
    dut.inp11.value=3
    dut.inp12.value=1
    dut.inp13.value=2
    dut.inp14.value=3
    dut.inp15.value=1
    dut.inp16.value=2
    dut.inp17.value=3
    dut.inp18.value=1
    dut.inp19.value=2
    dut.inp20.value=3
    dut.inp21.value=1
    dut.inp22.value=2
    dut.inp23.value=3
    dut.inp24.value=1
    dut.inp25.value=2
    dut.inp26.value=3
    dut.inp27.value=1
    dut.inp28.value=2
    dut.inp29.value=3
    dut.inp30.value=1
    for i in range (31):
        dut.sel.value=i
        await Timer(2, units='ns')
        dut.log.info(f' DUT={int(dut.out.value):31}')
