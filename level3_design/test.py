import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge

@cocotb.test()
async def test_seq_bug1(dut):
    """Test for seq detection """
    clock = Clock(dut.PCLK, 10, units="us")  # Create a 10us period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    addr=22
    wdata=23
    # reset
    dut.PRESETn.value = 1
    await FallingEdge(dut.PCLK)  
    dut.PRESETn.value = 0
    await FallingEdge(dut.PCLK)
    
    dut.PADDR.value = addr
    dut.PWRITE.value= 1
    dut.PSEL.value  = 1
    dut.PWDATA.value= wdata
    await RisingEdge(dut.PCLK)

    dut.PENABLE.value=1
    dut.PREADY.value =1
    await RisingEdge(dut.PCLK)

    dut.PENABLE.value=0
    dut.PREADY.value =0
    await RisingEdge(dut.PCLK)

    dut.PADDR.value = 0
    dut.PWRITE.value= 0
    dut.PSEL.value  = 0
    dut.PWDATA.value= 0
    await RisingEdge(dut.PCLK)

    dut.PADDR.value = addr
    dut.PSEL.value  = 1
    await RisingEdge(dut.PCLK)

    dut.PENABLE.value=1
    dut.PREADY.value =1
    await RisingEdge(dut.PCLK)

    cocotb.log.info(f'Wdata={dut.PWDATA.value}  Rdata={int(dut.PRDATA.value):2}')
    assert dut.PRDATA.value == wdata, "wdata is not same as rdata"