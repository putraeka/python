import imageio
import os
import click

# os.path.abspath menampilkan absoluth path dari file sekarang
clip = os.path.abspath('test.mp4')

def gifMaker(inputPath,targetFormat):
    
    # os.path.splitext tugasnya split nama file dan extensi, disini kita mengambil 0 untuk nama file
    outputPath = os.path.splitext(inputPath)[0] + targetFormat
    
    print(f'Converting {inputPath} \n to {outputPath} ')
    reader = imageio.get_reader(inputPath)
    fps = reader.get_meta_data()['fps']

    writer = imageio.get_writer(outputPath, fps=fps)

    for frames in reader:
        writer.append_data(frames)
        # print(f'Frame {frames}')
    
    print('Done!')
    
    writer.close()

@click.command()
@click.argument('file')
@click.argument('converted')
def main(file,converted):
    gifMaker(file,converted)

if __name__ == "__main__":
    main()

