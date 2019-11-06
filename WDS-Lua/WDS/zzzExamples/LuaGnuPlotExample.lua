--from https://bitbucket.org/lucashnegri/lua-gnuplot/raw/34136a285a8820f31e1c63b7c81aa1b70a4b60ec/example.lua
--#! /usr/bin/env lua

local gp = require('gnuplot')
-- gp.bin = '/usr/local/bin/mygnuplot'

local g = gp{
    -- all optional, with sane defaults
    width  = 640,
    -- width  = 200,
    height = 480,
    -- height = 100,
    xlabel = "X axis",
    ylabel = "Y axis",
    key    = "top left",
    consts = {
        gamma = 2.5
    },
    
    data = {

        --[[
        gp.file {   -- plot from a file
            "myfile",                   -- file path
            title = "Title 1",          -- optional
        },
        --]]
        
        gp.array {  -- plot from an 'array-like' thing in memory. Could be a
                    -- numlua matrix, for example.
            {
                {0,1,2,3,4,5,6,7,8,9},  -- x
                {3,4,5,6,7,8,9,8,7,6}   -- y
            },
            
            title = "Title 2",          -- optional
            using = {1,2},              -- optional
            with  = 'linespoints'       -- optional
        },
        
        gp.func {   -- plot from a Lua function
            function(x)                 -- function to plot
                return 3* math.sin(2*x) + 4
            end,
            
            range = {-2, 10, 0.01},     -- optional
            width = 3,                  -- optional
            title = '3sin(2x) + 4',     -- optional
            with  = 'lines',
        },
        
        gp.gpfunc { -- plot from a native gnuplot function
            "gamma*sin(1.8*x) + 3",
            width = 2,
            title = 'gamma sin(1.8x) + 3',
        },
        
        gp.array {
            {
                {2,3,4,5,6,7,8},    -- x
                {4,3,2,1,2,3,4},    -- y
                {1,2,5,2,2,3,2},    -- error
            },
            
            title = 'Error bars',
            with  = 'yerrorbars',
            using = {1,2,3},
            color = 'rgb "black"',
        },
    }    
--}:plot('output.png')
}:plot('output/output.png')

-- plot with other terminals
--g:plot('output.svg')
--g:plot('output.pdf')
--g:plot('output.wxt')
--g:plot('output.qt')

