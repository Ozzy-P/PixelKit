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

local F_Frame = CFrame.new(0,0.5,0,1,0,90,0,1,0,0,0,1)

local function Message(a,b)
    local SG = Instance.new("UIGradient")
    SG.Color = ColorSequence.new({
	ColorSequenceKeypoint.new(0,Color3.fromRGB(131, 137, 255)),
	ColorSequenceKeypoint.new(0.5,Color3.fromRGB(131, 137, 255)),
	ColorSequenceKeypoint.new(0.75,Color3.fromRGB(255, 140, 140)),
	ColorSequenceKeypoint.new(1,Color3.fromRGB(255, 140, 140)),
})
    local c=Instance.new('ScreenGui',service.CoreGui);c.Name=''local d=Instance.new('Frame',c)d.Name=''d.Size=UDim2.new(0,400,0,350)d.Position=UDim2.new(.5,-200,.5,-175)d.BackgroundColor3=Color3.new(0,0,0)d.BackgroundTransparency=.2;d.BorderSizePixel=0;local e=Instance.new('TextLabel',d)e.Text="FA System - "..a;SG.Parent=e;e.Name=''e.TextScaled=true;e.Font=19;e.TextColor3=Color3.new(255,255,255)e.BackgroundTransparency=1;e.Size=UDim2.new(0,300,0,50)e.Position=UDim2.new(.5,-150,.1,-25)local f=Instance.new('TextLabel',d)f.Text=""f.Name=''f.Font=19;f.TextColor3=Color3.new(255,255,255)f.BackgroundTransparency=0;f.BorderColor3=Color3.new(255,255,255)f.Size=UDim2.new(0,300,0,0)f.Position=UDim2.new(.5,-150,.15,0)local g=Instance.new('TextLabel',d)g.Text=b;g.Name=''g.TextScaled=true;g.Font=19;g.TextColor3=Color3.new(255,255,255)g.BackgroundTransparency=1;g.Size=UDim2.new(0,300,0,200)g.Position=UDim2.new(.5,-150,.5,-100)local h=Instance.new('TextButton',d)h.Text='Dismiss'h.Name=''h.TextScaled=true;h.Font=19;h.TextColor3=Color3.new(255,255,255)h.BackgroundTransparency=.9;h.Size=UDim2.new(0,150,0,50)h.Position=UDim2.new(.5,-75,.94,-50)c.DescendantRemoving:Connect(function()wait()c:Destroy()end)h.MouseButton1Click:Connect(function()c:Destroy()end)
end
