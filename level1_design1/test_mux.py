# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
inp0=random.randint(0,3)
inp1=random.randint(0,3)
inp2=random.randint(0,3)
    cocotb.log.info('##### CTB: Develop your test here ########')
