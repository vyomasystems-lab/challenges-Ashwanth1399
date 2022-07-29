// Code your design here
module apb_v3_sram(P_clk,P_rst,P_addr,P_selx,P_enable,P_write,P_wdata,P_ready,P_rdata);
  input P_clk;
  input P_rst;
  input [31:0]P_addr;
  input P_selx;
  input P_enable;
  input P_write;
  input [31:0]P_wdata;
  input P_ready;
  output reg [31:0]P_rdata;
  
  parameter [1:0] idle=2'b00;
  parameter [1:0] setup=2'b01;
  parameter [1:0] access=2'b10;
  
  reg [1:0] present_state,next_state;
  memory m1(P_clk,P_enable,P_ready,P_write,P_addr,P_wdata,P_rdata);
  always @(posedge P_clk) begin
    if(P_rst) present_state <= idle;
    else
      present_state <= next_state;
  end
  always @(posedge P_clk) begin
  case (present_state)
    idle:begin
      if (P_selx   & !P_enable) 	
				next_state = setup;
      else
                next_state = idle;
    end

    setup:begin
      if (!P_enable | !P_selx) 
						next_state = idle; 
      else 
						next_state =access;          
    end
    access :begin
      if(P_ready == 1 && P_selx == 0)
                  next_state <= idle;
      else if(P_ready == 1 && P_selx == 1)
                	next_state <= setup;
      else if(P_ready == 0)
                  next_state <= access;
    end
  endcase 
end
endmodule

module memory(P_clk,P_enable,P_ready,P_write,P_addr,P_wdata,P_rdata);
  input [31:0] P_wdata,P_addr;
  input P_write, P_ready, P_enable, P_clk;
  output reg [31:0] P_rdata;
  
  reg [3:0] mem [0:31];
  
  always@(posedge P_clk)begin
    if(P_enable && P_ready)
      begin
        if(P_write==1)
          mem[P_addr]=P_wdata;          
  		else 
          P_rdata=mem[P_addr];
      end
  end  
endmodule