#!/bin/bash
 
# array to hold list of IP blocks
ALL_IPS=()
NAME_SERVER='8.8.8.8'
txt_records=$(dig @${NAME_SERVER} _cloud-netblocks.googleusercontent.com txt +short)
txt_rr_only=$(echo $txt_records | grep -oP 'include:\S+' | sed 's/include://g')
[[ -z ${txt_rr_only} ]] && { echo 'No TXT dns record found.'; exit 1;}
## unpack txt records to get IPv4 ranges
for rr in ${txt_rr_only}; do
  new_ips=$(dig @${NAME_SERVER} $rr txt +short | grep -o -P '(\d+\.){3}\d+/\d+')
  for item in ${new_ips}; do
    # add space separator between ip blocks
    item=" ${item} "
    ALL_IPS+=${item}
  done
done
 
# sort IPs
echo ${ALL_IPS[@]} | sed 's/ /\n/g' | sort -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4
