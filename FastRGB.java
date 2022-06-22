// No
import java.awt.image.BufferedImage;
import java.awt.image.DataBufferByte;
import javax.imageio;
import javax.imageio.ImageIO;
import java.io.*; 

public class FastRGB
{

    private int width;
    private int height;
    private boolean hasAlphaChannel;
    private int pixelLength;
    private byte[] pixels;

    public void FastRGBs(BufferedImage image)
    {

        pixels = ((DataBufferByte) image.getRaster().getDataBuffer()).getData();
        width = image.getWidth();
        height = image.getHeight();
        hasAlphaChannel = image.getAlphaRaster() != null;
        pixelLength = 3;
        if (hasAlphaChannel)
        {
            pixelLength = 4;
        }

    }

    int getRGB(int x, int y)
    {
        int pos = (y * pixelLength * width) + (x * pixelLength);

        int argb = -16777216; // 255 alpha
        if (hasAlphaChannel)
        {
            argb = (((int) pixels[pos++] & 0xff) << 24); // alpha
        }

        argb += ((int) pixels[pos++] & 0xff); // blue
        argb += (((int) pixels[pos++] & 0xff) << 8); // green
        argb += (((int) pixels[pos++] & 0xff) << 16); // red
        return argb;
    }
    public static void main(String[] args) throws IOException {
        BufferedImage imgBuffer = ImageIO.read(new File("/OwO.jpg"));

        FastRGB sd = new FastRGB();
        sd.FastRGBs(imgBuffer);
        System.out.println(sd.getRGB(120,52));
    }
}
