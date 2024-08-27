import ffmpeg
import sys

def download_m3u8_to_mp4(m3u8_url, output_file):
    try:
        stream = ffmpeg.input(m3u8_url)
        stream = ffmpeg.output(stream, output_file, vcodec='libx264', acodec='aac')
        
        ffmpeg.run(stream)
        print(f"Successfully downloaded and converted to {output_file}")
    except ffmpeg.Error as e:
        print(f"An error occurred: {e.stderr.decode()}")
        sys.exit(1)

if __name__ == "__main__":
    
    m3u8_url = '''https://f.media-amazon.com/images/S/vse-vms-transcoding-artifact-eu-west-1-prod/7661b9d4-255d-4eaf-9ca2-c0ff1fcbf99b/default.jobtemplate.hls.m3u8'''
    output_file = "output.mp4"
    
    download_m3u8_to_mp4(m3u8_url, output_file)