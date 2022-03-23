#!/bin/bash

desktop=$USERPROFILE\\Desktop
dir_img=$desktop\\exif_img

cd $dir_img
find . -type f -name "*.jpg" -or -name "*.JPG" > img_list.txt

cat img_list.txt | while read img
do
  img_file_path="imgpath@${img},"
  echo -n $img_file_path | sed 's/.\///' > tmp.txt
  cmd //C $desktop\\ImageMagick\\identify -verbose $img | grep -a -e "Image Name" -e "Byline\[2" -e "City\[2" -e "State\[2" -e "Country\[2" -e "String\[2" -e "Colorspace" | sed 's/^[ \t]*//' | sed -E "s/\[.+\]//" | tr ':' '@' | tr '\n' ',' | sed 's/ //g' >> tmp.txt
  cmd //C $desktop\\ImageMagick\\identify -format 'width@%w,height@%h' $img >> tmp.txt
  charcode=$(file -i tmp.txt | sed -E "s/.+charset=(.+)/\1/")
  sjis="unknown-8bit"

  if [ $charcode = $sjis ]; then
    iconv -f SHIFT_JIS -t UTF-8 tmp.txt > tmp_utf8.txt
    rm tmp.txt
    mv tmp_utf8.txt tmp.txt
  fi

  cat tmp.txt >> exif.csv
  echo '' >> exif.csv

  rm tmp.txt
done

rm img_list.txt