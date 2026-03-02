#!/bin/bash
# 生成Anthropic文章封面

PROMPT='Text overlay at top left: "对总统说\"不\"" in large bold white text with black outline, Subtitle below: "3800亿公司的底线" in smaller orange text. 

A determined tech CEO standing on the right side of the frame, looking confidently forward with arms crossed. Professional photography style, realistic human face with subtle "uncompromising" expression. Wearing a dark navy blazer over a simple t-shirt.

Background: dramatic gradient from deep blue (left) to powerful red (right), symbolizing the clash between tech principles and political power. Subtle AI circuit patterns and digital elements fading into the background.

Style: high-contrast cinematic lighting, professional portrait photography, MrBeast-style YouTube thumbnail, 2.35:1 aspect ratio. Non-cartoon, non-3D render, must be photorealistic. Chinese text must be rendered directly in the image, clearly readable, high contrast against background. Small text "老里" in bottom right corner.'

/root/.openclaw/workspace/scripts/gen-image.sh "$PROMPT" "articles/anthropic-trump-standoff-cover"
