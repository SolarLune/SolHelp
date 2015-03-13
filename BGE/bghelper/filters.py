__author__ = 'SolarLune'

# This is a library of 2D filters that either
# 1) I made, or
# 2) I Adapted from other scripts (I don't think any were direct copies, just re-adaptation. If I am wrong, though,
# please point it out to me).
#
# Hopefully someone can use them.

# As a note to myself, the 2D filter system in the BGE has access to the following samplers:
# bgl_RenderedTexture (The usual screen grab)
# bgl_LuminanceTexture (The luminosity)
# bgl_DepthTexture (The depth of each pixel (fragment))

from bge import logic

# Filters


def read_depths():
    script = """

    uniform sampler2D bgl_DepthTexture;

    float linearize(float depth)
    {

        float near = 1.0;  // Near plane
        float far = 100.0; // Far plane
        return (-far * near) / (depth * (far - near) - far);

    }

    void main(void)
    {
        gl_FragColor = linearize(texture2D(bgl_DepthTexture, gl_TexCoord[0]).x);
    }

    """

    return script


def chromatic(dist=1.0):
    """
    Chromatic aberration screen filter. Received from someone from the BlenderArtists forums.

    Author: Someone from BlenderArtists.org, Modified by SolarLune

    Date Updated: 6/6/11
    """

    return ("""
    uniform sampler2D bgl_RenderedTexture;

    void main()
    {

    vec2 texcoord = gl_TexCoord[0].xy;

    vec3 sum = vec3(0.0);

    float d = 0.01 * """ + str(dist) + """;

    sum.r = vec3(texture2D(bgl_RenderedTexture, texcoord)).r;
    sum.g = vec3(texture2D(bgl_RenderedTexture, (texcoord * (1 + d)) - vec2(d / 2, d / 2) )).g;
    sum.b = vec3(texture2D(bgl_RenderedTexture, (texcoord * (1 - d)) + vec2(d / 2, d / 2) )).b;

    gl_FragColor = vec4(sum, 1.0);
    }
    """)


def digitaldistort():
    script = """

    uniform sampler2D bgl_RenderedTexture;

    float Round(float value){	// Rounds off the specified number

        if (ceil(value) - value < 0.5)
            return ceil(value);
        else
            return floor(value);

        }

    void main(void)
    {
        vec2 glst = gl_TexCoord[0].st;
        vec4 wtc = gl_TexCoord[3];

        vec2 step;

        vec4 dc = vec4(1, 1, 1, 1);
        float ps = 32.0;

        if ((wtc.y > 0.1) && (wtc.y < 0.2)){
            step = glst + vec2(0.1, 0.0);
            dc = vec4(0.4, 0.2, 0.1, 1.0);
            }
        else
            step = glst;

        if ((wtc.y > 0.4) && (wtc.y < 0.41)){
            dc = vec4(0.3, 0.5, 0.8, 1.0);
            step = glst - vec2(0.1, 0.0);
            }

        if ((wtc.y > 0.4) && (wtc.y < 0.41)){
            dc = vec4(0.9, 0.5, 0.1, 1.0);
            step = glst + vec2(0.1, 0.05);
            }

        if ((wtc.y > 0.6) && (wtc.y < 0.7)){
            dc = vec4(.3, .3, .3, 1.0);
            step = glst + vec2(0.3, 0.0);
            }

        if ((wtc.x > 0.7) && (wtc.x < 0.71)){
            dc = vec4(.3, .3, .3, 1.0);
            step = glst + vec2(-0.3, 0.0);
            }

        if ((wtc.y > 0.3) && (wtc.y < 0.35)){
            dc = vec4(.3, .3, .3, 1.0);
            step = glst + vec2(0.0, 0.2);
            }

        if (wtc.y > 0.9){
            dc = vec4(.3, .3, .3, 1.0);
            step = glst + vec2(0.0, -0.2);
            }

        //if ((wtc.x < 0.25) && (wtc.y < 0.5))
        //{
        //	step.x = floor(step.x / ps) * ps;
        //	step.y = floor(step.y / ps) * ps;
        //}

        if ((wtc.x < 0.15) || (wtc.x > 0.95))
        {
            step.x = Round(step.x * ps) / ps;
            step.y = Round(step.y * ps) / ps;
        }

        if (wtc.y > 0.85)
        {
            step.x = Round(step.x * (ps*2)) / (ps*2);
            step.y = Round(step.y * (ps*2)) / (ps*2);
        }

        vec4 color = texture2D(bgl_RenderedTexture, step);

        color /= dc;

        if (step.x < 0.0)
            step.x += wtc.x;
        else if (step.x > 1.0)
            step.x -= 1.0;

        gl_FragColor = color;
        }

    """

    return script


def reduce(coloramt=1.0):
    """
    Color Reduction - Reduces number of colors that are outputted (rounds all values down).

    Author: SolarLune
    Date Updated: 6/6/11

    coloramt = severity of colors to output;
    3.0 = like 32-bit
    2.0 = like 16-bit
    1.5 = like old-school computer level graphics (VGA?)
    1.0 = (default) is basic colors (only red, green, blue, or a complete combination thereof)
    """
    return ("""

    vec4 colround(float value, vec4 color){

    vec4 c = color;

    c *= value;

    c = vec4( ceil(c.r), ceil(c.g), ceil(c.b), ceil(c.a) );

    c /= value;

    return c;

    }

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {

        vec4 color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

        color = colround(""" + str(float(coloramt)) + """, color);

        gl_FragColor = color;
    }
        """
    )


def gameboy():
    filt = """

        uniform sampler2D bgl_RenderedTexture;

        void main(void)
        {
            vec4 color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

            float lum = max(max(color.r, color.g), color.b);

            if (lum > .75)
                color = vec4(0.816, 0.9909, 0.0675, color.a);
            else if (lum > .5)
                color = vec4(0.542, 0.671, 0.05, color.a);
            else if (lum > .25)
                color = vec4(0.187, 0.382, 0.187, color.a);
            else
                color = vec4(0.058, 0.218, 0.058, color.a);

            gl_FragColor = color;
        }
            """

    return filt


def scanlines(scandarkness=0.0, scanwidth=1.0, pixelcount=4.0, samplesize=1, scancontrast=1.0):
    """
    CRT Scan-line effect filter.

    Combine with Bloom to get something like the glow CRT monitors give to pixelated sprites.

    scandarkness = how strong (dark) the scanlines are
    scanwidth = how large each scanline should be
    scannumber = how many pixels to have between scanlines
    samplesize = how wide of an area to sample for the contrast effect
    scancontrast = how much contrast there is between dark areas (where the scanlines are darkest) and bright areas (where they're not)
    """

    scan = """

        // CRT scanline effect

        uniform sampler2D bgl_RenderedTexture;

        void main()
        {
            vec4 sum = vec4(0);
            vec2 texcoord = vec2(gl_TexCoord[0]);
            vec4 center = texture2D(bgl_RenderedTexture, texcoord);

            float width = 0.002 * """ + str(float(samplesize)) + """;	// width = how wide of a sample to use (is repeated 32 times below (8 times vertically, 4 times for each of those vertically)

            sum += texture2D(bgl_RenderedTexture, texcoord);
            sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(-1, -1)*width));
            sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(1, -1)*width));
            sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(1, 1)*width));
            sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(-1, 1)*width));

            sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(-0.5, -0.5)*width));
            sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(0.5, -0.5)*width));
            sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(0.5, 0.5)*width));
            sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(-0.5, 0.5)*width));

            sum /= 9.0;

            float brightness = (0.2126*sum.r) + (0.7152*sum.g) + (0.0722*sum.b);

            float scanline;

            ivec2 size = textureSize(bgl_RenderedTexture, 0);

            if (mod(floor(texcoord.y * size.y), """ + str(float(pixelcount)) + """) < """ + str(float(scanwidth)) + """)
            {
                scanline = (""" + str(float(scandarkness)) + """ + (brightness) * """ + str(float(scancontrast)) + """);
                scanline = clamp(scanline, 0, 1);
            }
            else
                scanline = 1.0;


            gl_FragColor = center * scanline;
        }

    """

    return (scan)


def bloom(strength=1.0, width=1.0, height=1.0, sample_num_x=4, sample_num_y=4, threshold=.5):

    shader = """

        uniform sampler2D bgl_RenderedTexture;
        uniform sampler2D bgl_LuminanceTexture;

        /*float rand(vec2 co) // This used to have highp to indicate the highest quality precision in the variables, but
        {// wouldn't compile after I upgrade graphics card drivers. ?_?
        // Note that this also made the bloom look pretty tight, but I couldn't
        // get it to work with the luminance function... :(
            float a = 12.9898;
            float b = 78.233;
            float c = 43758.5453;
            float dt= dot(co.xy ,vec2(a,b));
            float sn= mod(dt,3.14);
            return fract(sin(sn) * c);
        }*/

        float luminance(vec4 color){

            //return max(max(color.r, color.b), color.g); // Original color-channel-blind luminance

            //return (max(max(color.r, color.b), color.g) + min(min(color.r, color.g), color.b)) / 2; // Newer
            // color-channel dependent luminance (takes the brightest and darkest colors, and averages them out)

            return (((color.r*2) + color.b + (color.g*3)) / 6);  // Luminance function taken from StackOverflow
        }

        void main()
        {

            vec4 sum = vec4(0);
            vec2 texcoord = vec2(gl_TexCoord[0]);

            vec4 center = texture2D(bgl_RenderedTexture, texcoord);

            int sample_num_x = """ + str(int(sample_num_x)) + """;
            int sample_num_y = """ + str(int(sample_num_y)) + """;

            float width = 0.01 * """ + str(float(width)) + """ / sample_num_x;	// width = how wide of a sample to use (is repeated 32 times below (8 times vertically, 4 times for each of those vertically)
            float height = 0.01 * """ + str(float(height)) + """ / sample_num_y;  // height = how tall of a sample to use

            vec2 tv;
            vec4 bloom_col;

            float threshold = """ + str(float(threshold)) + """;

            for (int i = -sample_num_x; i < sample_num_x; i++)
            {

                for (int j = -sample_num_y; j < sample_num_y; j++)
                {

                    tv.x = texcoord.x + ((i+0.5)*width);
                    tv.y = texcoord.y + ((j+0.5)*height);

                    //tv.x = texcoord.x;

                    bloom_col = texture2D(bgl_RenderedTexture, tv);

                    //bloom_col = texture2D(bgl_RenderedTexture, vec2(texcoord.x - i, texcoord.y - j));

                    // float l = texture2D(bgl_LuminanceTexture, tv).r;
                    // if (l >= threshold)  // Slower to look up a texture than to just run a function to check color values.
                    if (luminance(bloom_col) >= threshold)
                        sum += bloom_col;
                }
            }

            sum /= ((sample_num_x * 2) * (sample_num_y * 2));

            float str = """ + str(float(strength)) + """;

            vec4 bloom = sum * str;

            bloom.a = 1.0;

            gl_FragColor = center + (bloom);	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32

        }
    """

    return shader


def bloomcrossold(strength=1.0, width=1.0, shape=0, quality=0):
    """
    Cross-shaped Bloom filter. Derived from Bloom, which is adapted from Blender Foundation's Bloom filter

    Author: SolarLune, derived from Blender Foundation's Bloom filter
    Date Updated: 6/6/11

    strength = how strong the bloom affect appears
    width = how wide of an area to sample; note that I only use 16 samples in this filter (which isn't that much)
    shape = what shape the bloom should be in - 0 = X, 1 = +, 2 = * (X and + together)
    quality = quality of the filter; 0 = low quality (16 samples), 1 = medium quality (32 samples), 2 = high quality (64 samples)

    shape HAS TO BE NUMBERS, EITHER 0, 1, or 2 TO WORK

    Note that this is a more efficient, but less appealing bloom effect that uses if statements instead of
    for loops. It works well and is pretty efficient, though.
    """

    bclow = """

        // Name: Cross Bloom Screen Filter
        // Author: SolarLune
        // Date Updated: 2/21/11

        uniform sampler2D bgl_RenderedTexture;

        float samples[11];

        void main()
        {
            samples[0] = 0.0222244;
            samples[1] = 0.0378346;
            samples[2] = 0.0755906;
            samples[3] = 0.1309775;
            samples[4] = 0.1756663;
            samples[5] = 0.1974126;
            samples[6] = 0.1756663;
            samples[7] = 0.1309775;
            samples[8] = 0.0755906;
            samples[9] = 0.0378346;
            samples[10] = 0.0222244;

            vec4 sum = vec4(0);
            vec2 texcoord = vec2(gl_TexCoord[0]);

            vec4 center = texture2D(bgl_RenderedTexture, texcoord);

            float width = 0.002 * """ + str(float(width)) + """;	// width = how wide of a sample to use (is repeated 16 times below (4 times horizontally, 4 times for each of those vertically)
            // Usually 0.002, but as can be seen below, sum would USUALLY be calculated 8 * 8 times (absurd CPU drain); should probably be around 0.001

            int shape = """ + str(shape) + """;

            if ((shape == 0) || (shape == 2))

            {
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, -4)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, -3)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, -2)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, -1)*width) * samples[3];

                //sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 0)*width) * samples[4];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, 1)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 2)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, 3)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(4, 4)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 4)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, 3)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 2)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, 1)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, -1)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, -2)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, -3)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(4, -4)*width) * samples[8];
            }

            if ((shape == 1) || (shape == 2))
            {

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 0)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, 0)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 0)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, 0)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, 0)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 0)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, 0)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(4, 0)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 4)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 3)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 2)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 1)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -1)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -3)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -4)*width) * samples[8];

            }

            if (shape == 2)
                sum /= 1.5;

            vec4 bloom = sum*(""" + str(float(strength)) + """ / 1.5);

            bloom.a = 1.0;

            //gl_FragColor = sum*(""" + str(float(strength)) + """ / 1.5) + texture2D(bgl_RenderedTexture, texcoord);	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32

            gl_FragColor = center + bloom;	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32

        }"""

    bcmed = """

        // Name: Cross Bloom Screen Filter
        // Author: SolarLune
        // Date Updated: 2/21/11

        uniform sampler2D bgl_RenderedTexture;

        float samples[11];

        void main()
        {
            samples[0] = 0.0222244;
            samples[1] = 0.0378346;
            samples[2] = 0.0755906;
            samples[3] = 0.1309775;
            samples[4] = 0.1756663;
            samples[5] = 0.1974126;
            samples[6] = 0.1756663;
            samples[7] = 0.1309775;
            samples[8] = 0.0755906;
            samples[9] = 0.0378346;
            samples[10] = 0.0222244;

            vec4 sum = vec4(0);
            vec2 texcoord = vec2(gl_TexCoord[0]);

            vec4 center = texture2D(bgl_RenderedTexture, texcoord);

            float width = 0.002 * """ + str(float(width)) + """;	// width = how wide of a sample to use (is repeated 16 times below (4 times horizontally, 4 times for each of those vertically)
            // Usually 0.002, but as can be seen below, sum would USUALLY be calculated 8 * 8 times (absurd CPU drain); should probably be around 0.001

            int shape = """ + str(shape) + """;

            if ((shape == 0) || (shape == 2))

            {
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, -4)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, -3)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, -2)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, -1)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.5, -3.5)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.5, -2.5)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.5, -1.5)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.5, -0.5)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, 1)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 2)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, 3)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(4, 4)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.5, 0.5)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.5, 1.5)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.5, 2.5)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.5, 3.5)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 4)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, 3)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 2)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, 1)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.5, 3.5)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.5, 2.5)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.5, 1.5)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.5, 0.5)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, -1)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, -2)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, -3)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(4, -4)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.5, -0.5)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.5, -1.5)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.5, -2.5)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.5, -3.5)*width) * samples[8];
            }



            if ((shape == 1) || (shape == 2))
            {

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 0)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, 0)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 0)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, 0)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.5, 0)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.5, 0)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.5, 0)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.5, 0)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, 0)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 0)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, 0)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(4, 0)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.5, 0)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.5, 0)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.5, 0)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.5, 0)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 4)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 3)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 2)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 1)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 3.5)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 2.5)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 1.5)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 0.5)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -1)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -3)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -4)*width) * samples[8];

                //sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -0.5)*width) * samples[5];	// For some reason, these last samples don't work
                //sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -1.5)*width) * samples[6];
                //sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2.5)*width) * samples[7];
                //sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -3.5)*width) * samples[8];

            }

            if (shape == 2)
                sum /= 2.0;

            vec4 bloom = sum*(""" + str(float(strength)) + """ / 3.0);

            bloom.a = 1.0;

            //gl_FragColor = sum*(""" + str(float(strength)) + """ / 1.5) + texture2D(bgl_RenderedTexture, texcoord);	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32

            gl_FragColor = center + bloom;	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32

        }
        """

    bchigh = """

        // Name: Cross Bloom Screen Filter
        // Author: SolarLune
        // Date Updated: 2/21/11

        uniform sampler2D bgl_RenderedTexture;

        float samples[11];

        void main()
        {
            samples[0] = 0.0222244;
            samples[1] = 0.0378346;
            samples[2] = 0.0755906;
            samples[3] = 0.1309775;
            samples[4] = 0.1756663;
            samples[5] = 0.1974126;
            samples[6] = 0.1756663;
            samples[7] = 0.1309775;
            samples[8] = 0.0755906;
            samples[9] = 0.0378346;
            samples[10] = 0.0222244;

            vec4 sum = vec4(0);
            vec2 texcoord = vec2(gl_TexCoord[0]);

            vec4 center = texture2D(bgl_RenderedTexture, texcoord);

            float width = 0.002 * """ + str(float(width)) + """;	// width = how wide of a sample to use (is repeated 16 times below (4 times horizontally, 4 times for each of those vertically)
            // Usually 0.002, but as can be seen below, sum would USUALLY be calculated 8 * 8 times (absurd CPU drain); should probably be around 0.001

            int shape = """ + str(shape) + """;

            if ((shape == 0) || (shape == 2))
            {
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, -4)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, -3)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, -2)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, -1)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.75, -3.75)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.75, -2.75)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.75, -1.75)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.75, -0.75)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.5, -3.5)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.5, -2.5)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.5, -1.5)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.5, -0.5)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.25, -3.25)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.25, -2.25)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.25, -1.25)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.25, -0.25)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, 1)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 2)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, 3)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(4, 4)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.25, 0.25)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.25, 1.25)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.25, 2.25)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.25, 3.25)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.5, 0.5)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.5, 1.5)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.5, 2.5)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.5, 3.5)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.75, 0.75)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.75, 1.75)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.75, 2.75)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.75, 3.75)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 4)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, 3)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 2)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, 1)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.75, 3.75)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.75, 2.75)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.75, 1.75)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.75, 0.75)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.5, 3.5)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.5, 2.5)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.5, 1.5)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.5, 0.5)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.25, 3.25)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.25, 2.25)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.25, 1.25)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.25, 0.25)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, -1)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, -2)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, -3)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(4, -4)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.75, -0.75)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.75, -1.75)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.75, -2.75)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.75, -3.75)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.5, -0.5)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.5, -1.5)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.5, -2.5)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.5, -3.5)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.25, -0.25)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.25, -1.25)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.25, -2.25)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.25, -3.25)*width) * samples[8];
            }



            if ((shape == 1) || (shape == 2))
            {

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 0)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, 0)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 0)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, 0)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.75, 0)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.75, 0)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.75, 0)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.75, 0)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.5, 0)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.5, 0)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.5, 0)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.5, 0)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3.25, 0)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2.25, 0)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1.25, 0)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-0.25, 0)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.25, 0)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.25, 0)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.25, 0)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.25, 0)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.5, 0)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.5, 0)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.5, 0)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.5, 0)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0.75, 0)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1.75, 0)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2.75, 0)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3.75, 0)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, 0)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 0)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, 0)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(4, 0)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 3.25)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 2.25)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 1.25)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 0.25)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 4)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 3)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 2)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 1)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 3.5)*width) * samples[0];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 2.5)*width) * samples[1];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 1.5)*width) * samples[2];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 0.5)*width) * samples[3];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 3.75)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 2.75)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 1.75)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 0.75)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -0.25)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -1.25)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2.25)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -3.25)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -0.5)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -1.5)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2.5)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -3.5)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -0.75)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -1.75)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2.75)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -3.75)*width) * samples[8];

                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -1)*width) * samples[5];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2)*width) * samples[6];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -3)*width) * samples[7];
                sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -4)*width) * samples[8];

                //sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -0.5)*width) * samples[5];	// For some reason, these last samples don't work
                //sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -1.5)*width) * samples[6];
                //sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2.5)*width) * samples[7];
                //sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -3.5)*width) * samples[8];

            }

            if (shape == 2)
                sum /= 2.0;

            vec4 bloom = sum*(""" + str(float(strength)) + """ / 6.0);

            bloom.a = 1.0;

            //gl_FragColor = sum*(""" + str(float(strength)) + """ / 1.5) + texture2D(bgl_RenderedTexture, texcoord);	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32

            gl_FragColor = center + bloom;	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32

        }
        """

    if quality == 0:
        return bclow
    elif quality == 1:
        return bcmed
    else:
        return bchigh


def bloomcross(strength=1.0, width=1.0, height=1.0, shape=0, sample_num=4):
    forbloom = """

        uniform sampler2D bgl_RenderedTexture;

        void main()
        {
            int shape = """ + str(int(shape)) + """;

            vec4 sum = vec4(0);
            vec2 texcoord = vec2(gl_TexCoord[0]);

            vec4 center = texture2D(bgl_RenderedTexture, texcoord);

            float width = 0.002 * """ + str(float(width)) + """;	// width = how wide the sample distance is
            float height = 0.002 * """ + str(float(height)) + """;	// height = how high the sample distance is

            int sample_num = """ + str(int(sample_num)) + """;

            if ((shape == 0) || (shape == 2))
            {

                for (int i = -sample_num; i < sample_num; i += 1)
                {
                    sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(i * width, i * height)));
                    sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(-i * width, -i * height)));
                    sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(i * width, -i * height)));
                    sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(-i * width, i * height)));
                }

            }

            if ((shape == 1) || (shape == 2))
            {

                for (int i = -sample_num; i < sample_num; i += 1)
                {
                    sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(i * width, 0)));
                    sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(-i * width, 0)));
                    sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(0, -i * height)));
                    sum += texture2D(bgl_RenderedTexture, texcoord + (vec2(0, i * height)));
                }

            }

            if ((shape == 0) || (shape == 1))
                sum /= (sample_num * 2) * 4;
            else
                sum /= ((sample_num * 2) * 4) * 2;

            //float brightness = (max(sum.r, max(sum.g, sum.b)) + min(sum.r, min(sum.g, sum.b))) / 2.0;

            vec4 bloom = sum * (""" + str(float(strength)) + """);

            bloom.a = 1.0;

            gl_FragColor = center + (bloom); //* brightness);	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32
        }
    """

    return (forbloom)


def colorbleed(strength=1.0, width=1.0):
    """
    Attempt at a color bleeding filter.

    Author: SolarLune - Derived from Bloom
    Date Updated: 6/9/11

    strength = how strong the bleeding affect appears
    width = how wide of an area to sample; note that I only use 16 samples.
    """

    return ("""

    // Name: Hey Frankie-based 16-Sample Bloom Effect
    // Author: BGE Foundation, Readapted by SolarLune
    // For slower / less capable graphics cards (that can't handle for-loops)

    uniform sampler2D bgl_RenderedTexture;

    float samples[11];

    void main()
    {
        samples[0] = 0.0222244;
        samples[1] = 0.0378346;
        samples[2] = 0.0755906;
        samples[3] = 0.1309775;
        samples[4] = 0.1756663;
        samples[5] = 0.1974126;
        samples[6] = 0.1756663;
        samples[7] = 0.1309775;
        samples[8] = 0.0755906;
        samples[9] = 0.0378346;
        samples[10] = 0.0222244;

        vec4 sum = vec4(0);
        vec2 texcoord = vec2(gl_TexCoord[0]);
        float width = 0.002 * """ + str(float(width)) +
            """;	// width = how wide of a sample to use (is repeated 16 times below (4 times horizontally, 4 times for each of those vertically)
            // Usually 0.002, but as can be seen below, sum would USUALLY be calculated 8 * 8 times (absurd CPU drain); should probably be around 0.001

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, -4)*width) * samples[0];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, -4)*width) * samples[2];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -4)*width) * samples[4];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, -4)*width) * samples[6];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, -2)*width) * samples[0];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, -2)*width) * samples[2];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2)*width) * samples[4];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, -2)*width) * samples[6];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 0)*width) * samples[0];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 0)*width) * samples[2];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 0)*width) * samples[4];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 0)*width) * samples[6];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 2)*width) * samples[0];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 2)*width) * samples[2];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 2)*width) * samples[4];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 2)*width) * samples[6];
            //gl_FragColor = sum / 16.0;
            gl_FragColor = sum * (""" + str(float(strength)) + """ / 1.5) * texture2D(bgl_RenderedTexture, texcoord);	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32
    }
        """)


def colorbleed32(strength=1.0, width=1.0):
    """
    Attempt at a 32-sample color bleeding filter.

    Author: SolarLune - Derived from ColorBleed
    Date Updated: 6/9/11

    strength = how strong the bleeding affect appears
    width = how wide of an area to sample; note that I only use 16 samples.
    """

    return ("""

    // Name: Hey Frankie-based 32-Sample Bloom Effect
    // Author: BGE Foundation, Readapted by SolarLune
    // For slower / less capable graphics cards (that can't handle for-loops)
    // Date Updated: 6/9/11

    uniform sampler2D bgl_RenderedTexture;

    float samples[11];

    void main()
    {
        samples[0] = 0.0222244;
        samples[1] = 0.0378346;
        samples[2] = 0.0755906;
        samples[3] = 0.1309775;
        samples[4] = 0.1756663;
        samples[5] = 0.1974126;
        samples[6] = 0.1756663;
        samples[7] = 0.1309775;
        samples[8] = 0.0755906;
        samples[9] = 0.0378346;
        samples[10] = 0.0222244;

        vec4 sum = vec4(0);
        vec2 texcoord = vec2(gl_TexCoord[0]);
        float width = 0.004 * """ + str(float(width)) +
            """;	// width = how wide of a sample to use (is repeated 32 times below (8 times vertically, 4 times for each of those vertically)

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, -4)*width) * samples[0];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, -4)*width) * samples[2];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -4)*width) * samples[4];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, -4)*width) * samples[6];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, -3)*width) * samples[1];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, -3)*width) * samples[3];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, -3)*width) * samples[5];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, -3)*width) * samples[7];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, -2)*width) * samples[0];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, -2)*width) * samples[2];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, -2)*width) * samples[4];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, -2)*width) * samples[6];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, -1)*width) * samples[1];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, -1)*width) * samples[3];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, -1)*width) * samples[5];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, -1)*width) * samples[7];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 0)*width) * samples[0];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 0)*width) * samples[2];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 0)*width) * samples[4];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 0)*width) * samples[6];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, 1)*width) * samples[1];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, 1)*width) * samples[3];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, 1)*width) * samples[5];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, 1)*width) * samples[7];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-4, 2)*width) * samples[0];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-2, 2)*width) * samples[2];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(0, 2)*width) * samples[4];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(2, 2)*width) * samples[6];

            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-3, 3)*width) * samples[1];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(-1, 3)*width) * samples[3];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(1, 3)*width) * samples[5];
            sum += texture2D(bgl_RenderedTexture, texcoord + vec2(3, 3)*width) * samples[7];

            //for( i= -4 ;i < 4; i++)	// The sixteen sum instructions above replace these for loops
            //{
            //    for( j= -4 ;j < 4; j++)
            //    {
            //			sum += texture2D(bgl_RenderedTexture, texcoord + vec2(j, i)*0.004) * samples[j+4];
            //		}
            //	}

            sum.a = 1.0;

            gl_FragColor = sum*(""" + str(float(strength)) + """ / 3.0) * texture2D(bgl_RenderedTexture, texcoord);	// Usually sum*0.08; 0.08 < is how bright the bloom effect appears on the screen; should probably be around 0.32
    }
        """)


def contrast(strength=1.0):
    """
    Contrast filter.

    Author: SolarLune
    Date Updated: 6/6/11

    strength = how strong the contrast filter is.
    """

    return (
        """

            // Name: Contrast Filter
            // Author: SolarLune
            // Date Updated: 6/6/11

            uniform sampler2D bgl_RenderedTexture;

            void main(void)
            {
                float contrast = """ + str(float(strength)) + """;	// Multiplication value for contrast (high = more, 0 = none)
            vec4 color = texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y));
            float avg = dot(color.rgb, vec3(0.299, 0.587, 0.114));

            float diff = 1.0 + ((avg - 0.5) * contrast);

            color *= diff;

            gl_FragColor = color;
        }
        """
    )


def dynamic_contrast(strength=1.0):
    script = """

        uniform sampler2D bgl_RenderedTexture;

        float get_brightness(vec4 rgba){
            return max(max(rgba.r, rgba.g), rgba.b);
        }

        void main(void){

            vec4 color = texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st));

            float di = 0.2;
            float contrast_range = 3.0;
            float contrast_base = 1.0;

            float brightness = get_brightness(texture2D(bgl_RenderedTexture, vec2(0.5-di, 0.5-di)));
            brightness += get_brightness(texture2D(bgl_RenderedTexture, vec2(0.5-di, 0.5+di)));
            brightness += get_brightness(texture2D(bgl_RenderedTexture, vec2(0.5+di, 0.5+di)));
            brightness += get_brightness(texture2D(bgl_RenderedTexture, vec2(0.5+di, 0.5-di)));
            brightness += get_brightness(texture2D(bgl_RenderedTexture, vec2(0.5, 0.5)));

            brightness /= 5.0;

            float neg_br = 1.0 - brightness;

            float br = contrast_base + (neg_br * contrast_range);

            gl_FragColor = color * (br);

        }

    """

    return script


def default(return_type=0):
    ### Just a 2D filter without any changes, basically.
    ### 0 = Rendered texture (screen)
    ### 1 = Luminance texture
    ### 2 = Depth texture (will show up white; you (I) need to linearize it for it to be actually usable)

    if return_type == 0:

        filt = """

        uniform sampler2D bgl_RenderedTexture;

        void main(void)
        {
            vec4 color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);
            gl_FragColor = color;
        }
            """

    elif return_type == 1:

        filt = """

        uniform sampler2D bgl_LuminanceTexture;

        void main(void)
        {
            vec4 color = texture2D(bgl_LuminanceTexture, gl_TexCoord[0].st);
            gl_FragColor = color;
        }
            """

    else:

        cam = logic.getCurrentScene().active_camera

        filt = """

        uniform sampler2D bgl_DepthTexture;

        void main(void)
        {
            vec4 color = texture2D(bgl_DepthTexture, gl_TexCoord[0].st);
            gl_FragColor = color / """ + str(cam.far) + """;
        }
            """

    return filt


def desaturateuni(var='desatstr'):
    return ("""

        // Name: Desaturation Filter
        // Author: Printed in XNA Unleashed; Readapted for GLSL by SolarLune
        // Date Updated: 6/6/11

        uniform sampler2D bgl_RenderedTexture;
        uniform float """ + str(var) + """;

        void main(void)
        {
            vec4 color;
            color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

            float gray = dot(color.rgb, vec3(0.299, 0.587, 0.114));
            // The human eye is more sensitive to certain colors (like bright yellow) than others, so you need to use this specific color-formula to average them out to one monotone color (gray)

            vec4 desat = vec4(gray, gray, gray, color.a);

            gl_FragColor = mix(color, desat, """ + str(var) + """);
        }
        """)


def desaturate(percentage=1.0):
    return ("""

        // Name: Desaturation Filter
        // Author: Printed in XNA Unleashed; Readapted for GLSL by SolarLune
        // Date Updated: 6/6/11

        uniform sampler2D bgl_RenderedTexture;

        void main(void)
        {
            vec4 color;
            color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

            float gray = dot(color.rgb, vec3(0.299, 0.587, 0.114));
            // The human eye is more sensitive to certain colors (like bright yellow) than others, so you need to use this specific color-formula to average them out to one monotone color (gray)

            vec4 desat = vec4(gray, gray, gray, color.a);

            gl_FragColor = mix(color, desat, """ + str(float(percentage)) + """);
        }
        """)


def sepia(percentage=1.0):
    return ("""

        // Name: Sepia Filter
        // Author: Derived from Desaturate and Blender's source Sepia filter
        // Date Updated: 2/21/11

        uniform sampler2D bgl_RenderedTexture;

        void main(void)
        {
            vec4 color;
            color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

            float gray = dot(color.rgb, vec3(0.299, 0.587, 0.114));
            // The human eye is more sensitive to certain colors (like bright yellow) than others, so you need to use this specific color-formula to average them out to one monotone color (gray)

            vec4 desat = vec4(gray * vec3(1.2, 1.0, 0.8), color.a);

            gl_FragColor = mix(color, desat, """ + str(float(percentage)) + """);
        }
        """)


def harsh():
    return ("""

        // Name: Harsh Colors
        // Author: SolarLune
        // Date Updated: 2/21/11

        // This filter is actually quite like the Reduce filter, but uses if-statements
        // instead of rounding, achieving a more numerically correct version. Also, it's a bit
        // more difficult to deal with - customizing the bit filters is easy.

        uniform sampler2D bgl_RenderedTexture;

        void main(void)
        {
            vec4 color;

            color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

            if (color.r > 0.75)
                color.r = 1;
            else if (color.r > 0.5)
                color.r = 0.75;
            else if (color.r > 0.25)
                color.r = 0.5;
            else
                color.r = 0;

            if (color.g > 0.75)
                color.g = 1;
            else if (color.g > 0.5)
                color.g = 0.75;
            else if (color.g > 0.25)
                color.g = 0.5;
            else
                color.g = 0;

            if (color.b > 0.75)
                color.b = 1;
            else if (color.b > 0.5)
                color.b = 0.75;
            else if (color.b > 0.25)
                color.b = 0.5;
            else
                color.b = 0;

            gl_FragColor = color;

        }
        """)


def channel(color='r', percentage=1.0):
    """
    Color channeling. Because of the script's simplicity, the muting only works with a single channel - R, G, or B.
    color = a string ('r', 'g', or 'b') to mute all colors except that channel.
    percentage = desaturation amount; 1.0 = 100%

    Author: SolarLune
    Date Updated: 6/6/11
    """

    main = color.lower()
    subone = 'g'  # Defaults to muting Red
    subtwo = 'b'

    if main == 'g':
        subone = 'r'
        subtwo = 'b'
    elif main == 'b':
        subone = 'r'
        subtwo = 'g'

    return (

        """

        // Name: Color Channel
        // Author: SolarLune
        // Date Updated: 6/6/11

        uniform sampler2D bgl_RenderedTexture;

        void main(void)
        {
            vec4 color;
            color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

            float gray = dot(color.rgb, vec3(0.299, 0.587, 0.114));
            // The human eye is more sensitive to certain colors (like bright yellow) than others, so you need to use this specific color-formula to average them out to one monotone color (gray)

            vec4 desat;

            if ((color.""" + str(main) + """ < color.""" + str(subone) + """) || (color.""" + str(
            main) + """ < color.""" + str(subtwo) + """))
            desat = vec4(gray, gray, gray, color.a);
            // If red isn't the dominant color in the pixel (like the green cube or dark blue
            // background), gray it out
        else
            desat = color;
            // Otherwise, if red is a dominant color, display normally; note that red is a dominant color in purple, so the purple cube also shows up correctly.

        gl_FragColor = mix(color, desat, """ + str(float(percentage)) + """);

    }

    """
    )


def mute(color='r', percentage=1.0):
    """
    Color muting. The opposite of Channel - mute only a specific color channel.
    color = a string ('r', 'g', or 'b') to mute only the specified color channel.
    percentage = desaturation amount; 1.0 = 100%

    Author: SolarLune
    Date Updated: 6/6/11
    """

    main = color.lower()
    subone = 'g'  # Defaults to channeling Red
    subtwo = 'b'

    if main == 'g':
        subone = 'r'
        subtwo = 'b'
    elif main == 'b':
        subone = 'r'
        subtwo = 'g'

    return (

        """

        // Name: Color Mute
        // Author: SolarLune
        // Date Updated: 6/6/11

        // Notes: Color muting; this works, but some colors are (obviously)
        // made up of others; for example, purple is blue AND red, so if
        // you mute all colors but red, purple will still show up...

        uniform sampler2D bgl_RenderedTexture;

        void main(void)
        {
            vec4 color;
            color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

            float gray = dot(color.rgb, vec3(0.299, 0.587, 0.114));
            // The human eye is more sensitive to certain colors (like bright yellow) than others, so you need to use this specific color-formula to average them out to one monotone color (gray)

            vec4 desat;

            if ((color.""" + str(main) + """ > color.""" + str(subone) + """) && (color.""" + str(
            main) + """ > color.""" + str(subtwo) + """))
            desat = vec4(gray, gray, gray, color.a);
            // If red is the dominant color in the pixel (like the green cube or dark blue
            // background), gray it out
        else
            desat = color;
            // Otherwise, if red is a dominant color, display normally; note that red is a dominant color in purple, so the purple cube also shows up correctly.

        gl_FragColor = mix(color, desat, """ + str(float(percentage)) + """);

    }

    """
    )


def invert(percentage=1.0):
    """
    Color inversion filter.

    Author: Printed in XNA Unleashed - readpated for GLSL by SolarLune
    Date Updated: 6/6/11
    """

    return ("""

    // Name: Invert
    // Author: printed in XNA Unleashed, readapted by SolarLune
    // Date Updated: 6/6/11

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {
        vec4 invert = 1.0 - texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);
        vec4 color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);
        gl_FragColor = mix(color, invert, """ + str(float(percentage)) + """);
        gl_FragColor.a = 1.0;
    }
    """)


def blur(blur_width=1.0, blur_height=1.0, sample_num_x=4, sample_num_y=4):

    """
    Blur filter.
    distance = distance apart each sample is
    percentage = amount of blurring to apply
    sample_num_x = number of samples to apply on the X axis
    sample_num_y = number of samples to apply on the Y axis

    Author: SolarLune

    """

    return ("""

    // Name: Simple 16-Sample (Box?) Blur Effect
    // Author: SolarLune
    // Date Updated: 6/6/11

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {
        float blur_width = 0.002 * """ + str(blur_width) + """;
        float blur_height = 0.002 * """ + str(blur_height) + """;

        int sample_num_x = """ + str(sample_num_x) + """;
        int sample_num_y = """ + str(sample_num_y) + """;

        vec4 color;

        for (int i = -sample_num_x; i < sample_num_x; i++)
        {
            for (int j = -sample_num_y; j < sample_num_y; j++)
            {
                color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st) + vec2(i * blur_width, j * blur_height));
            }

        }

        gl_FragColor = color / (sample_num_x*sample_num_y*4);

    }
    """)


def blur_old(distance=1.0, percentage=1.0):
    """
    Blur filter.
    distance = distance apart each sample is
    percentage = amount of blurring to apply
    sample_num_x = number of samples to apply on the X axis
    sample_num_y = number of samples to apply on the Y axis

    Author: SolarLune

    """

    return ("""

    // Name: Simple 16-Sample (Box?) Blur Effect
    // Author: SolarLune
    // Date Updated: 6/6/11

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {
        float value = 0.0025 * """ + str(float(distance)) + """;

        vec4 color = texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.25, gl_TexCoord[0].st.y + value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.25, gl_TexCoord[0].st.y - value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.25, gl_TexCoord[0].st.y - value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.25, gl_TexCoord[0].st.y + value * 0.25));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.5, gl_TexCoord[0].st.y + value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.5, gl_TexCoord[0].st.y - value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.5, gl_TexCoord[0].st.y - value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.5, gl_TexCoord[0].st.y + value * 0.5));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.75, gl_TexCoord[0].st.y + value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.75, gl_TexCoord[0].st.y - value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.75, gl_TexCoord[0].st.y - value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.75, gl_TexCoord[0].st.y + value * 0.75));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y + value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y - value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y - value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y + value));
        color /= 16.0;
        vec4 origcolor = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

        gl_FragColor = origcolor + """ + str(float(percentage)) + """ * (color - origcolor);
    }
        """)


def blur32(distance=1.0, percentage=1.0):
    """
    32-sample Blur filter.
    distance = distance apart each sample is
    percentage = amount of blurring to apply

    Author: SolarLune
    Date Updated: 6/6/11
    """

    return ("""

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {
        float value = 0.0025 * """ + str(float(distance)) + """;

        vec4 color = texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.25, gl_TexCoord[0].st.y + value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.25, gl_TexCoord[0].st.y - value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.25, gl_TexCoord[0].st.y - value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.25, gl_TexCoord[0].st.y + value * 0.25));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y + value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y - value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.25, gl_TexCoord[0].st.y));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.25, gl_TexCoord[0].st.y));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.5, gl_TexCoord[0].st.y + value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.5, gl_TexCoord[0].st.y - value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.5, gl_TexCoord[0].st.y - value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.5, gl_TexCoord[0].st.y + value * 0.5));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y + value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y - value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.5, gl_TexCoord[0].st.y));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.5, gl_TexCoord[0].st.y));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.75, gl_TexCoord[0].st.y + value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.75, gl_TexCoord[0].st.y - value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.75, gl_TexCoord[0].st.y - value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.75, gl_TexCoord[0].st.y + value * 0.75));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y + value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y - value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.75, gl_TexCoord[0].st.y));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.75, gl_TexCoord[0].st.y));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y + value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y - value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y - value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y + value));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y + value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y - value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y));

        color /= 32.0;
        vec4 origcolor = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

        gl_FragColor = origcolor + """ + str(float(percentage)) + """ * (color - origcolor);
    }
        """)


def ink(thickness=1.0, edge=1.0, col=(0, 0, 0, 1)):
    """
    Ink filter. It doesn't use the depth texture, so it tries to create black edges around different colors.

    Author: SolarLune
    Date Updated: 6/6/11

    thickness = thickness of the lines
    edge = frequency of the lines
    colr, g, b, a = color of the lines

    With a function, users can easily customize the filter
    to return a 'custom-made' script that suits their purposes. Note that this works when calling the
    script, but don't call it every frame - that will kill your FPS. It's better to use a
    uniform variable if you want to alter variables while running the filter.

    thickness = Thickness of the lines (float)
    edge = Frequency of the lines; higher numbers equals more lines (float)
    col = color of the lines (list of float from 0 to 1); last defines how visible the ink effect is
    """

    return ("""

    // Name: Ink
    // Author: SolarLune
    // Date Updated: 6/6/11

    // Notes: Achieves an ink and paint or charcoal type of effect without use of a depth texture - it works on
    // the difference from one color to the next.

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {
        float value = 0.001 * """ +
            str(float(thickness)) + """;	// Value here controls how large the samples (and hence how thick the lines) are
        vec4 sample = texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y + value));
        sample += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y - value));
        sample += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y - value));
        sample += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y + value));
        sample /= 4.0;
        vec4 center = texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y));

        float edge = 0.1 / """ +
            str(float(edge)) + """;		// 'Edge' here controls how easy it is to get an outline on objects

        vec4 diff;
        diff = vec4(abs(sample.r - center.r), abs(sample.g - center.g), abs(sample.b- center.b), abs(sample.a - center.a));

        if ((diff.r > edge) || (diff.g > edge) || (diff.b > edge))
        {
            vec4 color = vec4(""" +
            str(float(col[0])) + """, """ +
            str(float(col[1])) + """, """ +
            str(float(col[2])) + """, 1.0);
            gl_FragColor = mix(center, color, """ + str(float(col[3])) +
            """);
        }
        else
            gl_FragColor = center;
        }
        """    )


def edgedetect(thickness=1.0, edge=1.0, col=(0, 0, 0, 1)):
    """
    Author: SolarLune
    Date Updated: 6/6/11

    thickness = Thickness of the lines (float)
    edge = Frequency of the lines; higher numbers equals more lines (float)
    col = color of the lines (list of floats from 0 to 1)
    """

    return ("""

    // Name: Edge Detect
    // Author: SolarLune
    // Date Updated: 6/6/11

    // Notes: Detects the edges in the screenshot and outputs the edge colors.

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {
        float value = 0.001 * """ +
            str(float(thickness)) + """;	// Value here controls how large the samples (and hence how thick the lines) are
        vec4 sample = texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y + value));
        sample += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y - value));
        sample += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y - value));
        sample += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y + value));
        sample /= 4.0;
        vec4 center = texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x, gl_TexCoord[0].st.y));

        float edge = 0.01 / """ +
            str(float(edge)) + """;		// 'Edge' here controls how easy it is to get an outline on objects

        vec4 diff;
        diff = vec4(abs(sample.r - center.r), abs(sample.g - center.g), abs(sample.b- center.b), abs(sample.a - center.a));

        if ((diff.r < edge) || (diff.g < edge) || (diff.b < edge))
        {
            vec4 color = vec4(""" +
            str(float(col[0])) + """, """ +
            str(float(col[1])) + """, """ +
            str(float(col[2])) + """, 1.0);
            gl_FragColor = mix(center, color, """ + str(float(col[3])) +
            """);
        }
        else
            gl_FragColor = center;
    }
        """    )


def pixellate(resolution_x=320, resolution_y=240):
    """
    A sharp pixellation filter.

    Author: SolarLune
    Date Updated: 6/6/11

    resolution_x = target resolution on the X axis. Defaults to 320.
    resolution_y = target resolution on the Y axis. Defaults to 240.

    A larger X-axis resolution would equal a less blocky picture. Note that the pixellation is locked to
    whole numbers, so there's no way to get "1.5x" pixellation, so to speak. You should probably choose
    a resolution that's both rather small as well as a resolution that is a whole division of what you're going
    to be running the game at most likely (i.e. 320x240 on a 1280x960 game window, not 600x500 on a 800x600 game window)

    """
    return ("""
    uniform sampler2D bgl_RenderedTexture;
    uniform float bgl_RenderedTextureWidth;
    uniform float bgl_RenderedTextureHeight;

    void main(void)
    {
        vec2 uv = gl_TexCoord[0].xy;
        vec2 pixel = vec2(1.0 / bgl_RenderedTextureWidth, 1.0 / bgl_RenderedTextureHeight);
        int target_x = int(ceil(bgl_RenderedTextureWidth / """ + str(float(resolution_x)) + """));
        int target_y = int(ceil(bgl_RenderedTextureHeight / """ + str(float(resolution_y)) + """));

        float dx = pixel.x * target_x;
        float dy = pixel.y * target_y;

        vec2 coord = vec2(dx * floor(uv.x / dx), dy * floor(uv.y / dy));

        coord += pixel * 0.5; // Add half a pixel distance so that it doesn't pull from the pixel's edges,
        // allowing for a nice, crisp pixellation effect

        coord.x = min(max(0.001, coord.x), 1.0);
        coord.y = min(max(0.001, coord.y), 1.0);

        gl_FragColor = texture2D(bgl_RenderedTexture, coord);
    }
    """)


def pixellate_factor(px_x=4, px_y=4):
    """
    A pixellation filter that uses factor values instead of resolution sizes.

    Author: SolarLune
    Date Updated: 6/6/11

    px_x = size of pixels on the x-axis
    px_y = size of pixels on the y-axis
    """

    return ("""
    uniform sampler2D bgl_RenderedTexture;
    uniform float bgl_RenderedTextureWidth;
    uniform float bgl_RenderedTextureHeight;

    void main(void)
    {
        vec2 uv = gl_TexCoord[0].xy;
        vec2 pixel = vec2(1.0 / bgl_RenderedTextureWidth, 1.0 / bgl_RenderedTextureHeight);

        int target_x = """ + str(px_x) + """;
        int target_y = """ + str(px_y) + """;

        float dx = pixel.x * target_x;
        float dy = pixel.y * target_y;

        vec2 coord = vec2(dx * floor(uv.x / dx), dy * floor(uv.y / dy));

        coord += pixel * 0.5; // Add half a pixel distance so that it doesn't pull from the pixel's edges,
        // allowing for a nice, crisp pixellation effect

        coord.x = min(max(0.001, coord.x), 1.0);
        coord.y = min(max(0.001, coord.y), 1.0);

        gl_FragColor = texture2D(bgl_RenderedTexture, coord);
    }
    """)


def radial_blur(blur_width=1.0, blur_height=1.0, sample_num_x=4, sample_num_y=4, center_area=0.0):

    """
    Blur filter.
    distance = distance apart each sample is
    percentage = amount of blurring to apply
    sample_num_x = number of samples to apply on the X axis
    sample_num_y = number of samples to apply on the Y axis
    center_area = what amount of the screen to leave unblurred, from the center outwards. 0.5 = entire screen

    Author: SolarLune

    """

    return ("""

    // Name: Simple 16-Sample (Box?) Blur Effect
    // Author: SolarLune
    // Date Updated: 6/6/11

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {

        vec2 xy = gl_TexCoord[0];

        float blur_width = 0.002 * """ + str(blur_width) + """;
        float blur_height = 0.002 * """ + str(blur_height) + """;

        int sample_num_x = """ + str(sample_num_x) + """;
        int sample_num_y = """ + str(sample_num_y) + """;

        vec4 color;

        float blurriness = max(abs(xy.x - 0.5), abs(xy.y - 0.5));
        blurriness -= """ + str(center_area) + """;
        blurriness = max(blurriness, 0.0);

        for (int i = -sample_num_x; i < sample_num_x; i++)
        {
            for (int j = -sample_num_y; j < sample_num_y; j++)
            {
                color += texture2D(bgl_RenderedTexture, vec2(xy) + vec2((i * blurriness) *
                blur_width, (j * blurriness) * blur_height));
            }

        }

        gl_FragColor = color / (sample_num_x*sample_num_y*4);

    }
    """)


def radial_blur_old(percentage=1.0, minimum=1.0):
    """
    Why a function? Look at Pixellate above this.
    percentage = amount of blurring to apply - can go above 1 to increase the effect even more so.
    minimum = minimum amount of area to blur; higher numbers equals less of the screen blurred.
    """
    return ("""

    // Name: 16-Sample Radial Blur
    // Author: SolarLune
    // Date Updated: 6/6/11
    //
    // Notes: Really, it's more of a diamond blur, but it's blurry enough for me not to care (LOL).

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {

        float x = gl_TexCoord[3].st.x;
        float y = gl_TexCoord[3].st.y;
        float value;
        float min = 0.1 * """ + str(float(minimum)) + """;

        value = ((abs(x - 0.5) - min) + (abs(y - 0.5) - min)) * """ + str(float(percentage)) + """;

        if (value < 0.0)
            value = 0.0;

        vec4 color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

        value /= 100.0;
        color = texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.25, gl_TexCoord[0].st.y + value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.25, gl_TexCoord[0].st.y - value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.25, gl_TexCoord[0].st.y - value * 0.25));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.25, gl_TexCoord[0].st.y + value * 0.25));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.5, gl_TexCoord[0].st.y + value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.5, gl_TexCoord[0].st.y - value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.5, gl_TexCoord[0].st.y - value * 0.5));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.5, gl_TexCoord[0].st.y + value * 0.5));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.75, gl_TexCoord[0].st.y + value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.75, gl_TexCoord[0].st.y - value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value * 0.75, gl_TexCoord[0].st.y - value * 0.75));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value * 0.75, gl_TexCoord[0].st.y + value * 0.75));

        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y + value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y - value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x + value, gl_TexCoord[0].st.y - value));
        color += texture2D(bgl_RenderedTexture, vec2(gl_TexCoord[0].st.x - value, gl_TexCoord[0].st.y + value));
        color /= 16.0;

        gl_FragColor = color;
    }
    """)


def radialdesaturate(percentage=1.0, minimum=1.0):
    """
    percentage = amount of blurring to apply - can go above 1 to increase the effect even more so.
    minimum = minimum amount of area to blur; lower numbers equals less of the screen blurred.
    """
    return ("""

    // Name: 16-Sample Radial Blur
    // Author: SolarLune
    // Date Updated: 6/6/11
    //
    // Notes: Really, it's more of a diamond blur, but it's blurry enough for me not to care (LOL).

    uniform sampler2D bgl_RenderedTexture;

    void main(void)
    {

        float x = gl_TexCoord[3].st.x;
        float y = gl_TexCoord[3].st.y;
        float value;
        float min = 0.1 * """ + str(float(minimum)) + """;

        value = ((abs(x - 0.5) - min) + (abs(y - 0.5) - min)) * """ + str(float(percentage)) + """;

        if (value < 0.0)
            value = 0.0;
        if (value > 1.0)
            value = 1.0;

        vec4 color = texture2D(bgl_RenderedTexture, gl_TexCoord[0].st);

        float gray = dot(color.rgb, vec3(0.299, 0.587, 0.114));
        // The human eye is more sensitive to certain colors (like bright yellow) than others, so you need to use this specific color-formula to average them out to one monotone color (gray)

        vec4 desat = vec4(gray, gray, gray, color.a);

        gl_FragColor = mix(color, desat, value);
    }
    """)
    #