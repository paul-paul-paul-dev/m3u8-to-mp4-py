# m3u8-to-mp4-py

**m3u8-to-mp4-py** is a Python tool that allows you to download and convert M3U8 streaming videos to MP4 format using `ffmpeg`. It's straightforward to use and ideal for anyone who needs to convert M3U8 streams to MP4 files.

## Requirements

- Python 3.x
- `ffmpeg`
- Python packages listed in `requirements.txt`

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/paul-paul-paul-dev/m3u8-to-mp4-py
    cd m3u8-to-mp4-py
    ```

2. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:

    On macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

    On Windows:

    ```bash
    venv\Scripts\activate
    ```

4. Install the required Python packages:

    ```bash
    pip install --upgrade -r requirements.txt
    ```

## Usage

1. Update the `m3u8_url` and `output_file` variables in the script with your desired M3U8 stream URL and output file name:

    ```python
    m3u8_url = 'https://example.com/path/to/stream.m3u8'
    output_file = 'output.mp4'
    ```

2. Run the script:

    ```bash
    python main.py
    ```

3. The script will download and convert the M3U8 stream to the specified MP4 file.

## Example

Here's an example using a sample M3U8 URL:

```python
m3u8_url = 'https://f.media-amazon.com/images/S/vse-vms-transcoding-artifact-eu-west-1-prod/7661b9d4-255d-4eaf-9ca2-c0ff1fcbf99b/default.jobtemplate.hls.m3u8'
output_file = 'output.mp4'

download_m3u8_to_mp4(m3u8_url, output_file)
