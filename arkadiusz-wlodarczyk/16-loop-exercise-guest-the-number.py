# kita membuat program fun yang meminta user untuk menebak angka yang tepat.
# program akan terus berjalan sampai user bisa menebak angka tersebut.
# ketika berhasil program berhenti dan katakan "Selamat anda berhasil menebaknya"

secretNumber = 67
guessNumber = 0

while guessNumber != secretNumber :
    guessNumber = int(input("Ayo coba tebak, berapa angka yang benar: "))
    if secretNumber == guessNumber:
        print ("Sip, Anda berhasil menebaknya")
    else :
        print("Tebakan anda salah, ayo coba lagi!")
