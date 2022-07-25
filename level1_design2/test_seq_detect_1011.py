# See LICENSE.vyoma for details

# SPDX-License-Identifier: CC0-1.0

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    inp_bit=[1,0,1,1,1,0,1,1,1]
    exp_out=[0,0,0,0,1,0,0,0,1]
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    for i in range(9):
        dut.inp_bit.value=inp_bit[i]
        await RisingEdge(dut.clk)
        cocotb.log.info(f'input={dut.inp_bit.value} Epected_out={exp_out[i]:2}  DUT={int(dut.seq_seen.value):2}')
        assert dut.seq_seen.value == exp_out[i], "sequence not detected"

@cocotb.test()
async def test_seq_bug2(dut):
    """Test for seq detection """
    clock = Clock(dut.clk, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    inp_bit=[1,0,1,1,0,1,1,1]
    exp_out=[0,0,0,0,1,0,0,1,0]
    # reset
    dut.reset.value = 1
    await FallingEdge(dut.clk)  
    dut.reset.value = 0
    await FallingEdge(dut.clk)
    
    for i in range(8):
        dut.inp_bit.value=inp_bit[i]
        await RisingEdge(dut.clk)
        cocotb.log.info(f'input={dut.inp_bit.value} Epected_out={exp_out[i]:2}  DUT={int(dut.seq_seen.value):2}')
        assert dut.seq_seen.value == exp_out[i], "Overlap sequence not detected"

