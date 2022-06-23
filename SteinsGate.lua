-- UI rework in progress (0%)
-- TODO: Hire somebody who can actually make a GUI

--[[
Update log: 
    Removed update log until UI v2 has been completed.
--]]

local Sync = task.synchronize
local dSync = task.desynchronize
local pixelDepth = 1
local pixelDepthSpacing = .45

_G.Dampen = 1
_G.EasingStyle = Enum.EasingStyle.Circular

assert(_G.Dampen > 0 and _G.Dampen < 8,"Invalid value.")

_G.ParallelTween = true
_G.TweenPositionTime = .05
_G.TweenRotateTime = 0

local x = -15 -- Side
local y = -15 -- Down/Up
local z = 0 -- Forward/Back

_G.RotateX = 0
_G.RotateY = 0
_G.RotateZ = 0

local SignScale = (2/3-.05)
local Tracking = (4/3)

_G.DeleteKey = "Q"
_G.RefreshUI = "P"
_G.ContextDelete = "F"
_G.ContextMove = "E"
_G.ContextRotate = "R"
_G.ContextRotateDegrees = 20

_G.Signs = _G.Signs or {}
_G.Generator = true

local service = setmetatable({ }, {
	__index = function(self, key)
		return game:GetService(key)
	end
})
