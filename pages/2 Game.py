import streamlit as st
import time
import random   

tabA,tabB,tabC,tabD,tabF,tabE, tabG, tabH,tabI = st.tabs(["Game tung xúc sắc", "Game đoán số", "Kéo - Búa - Bao","Game tính toán nhanh","Game đuổi hình bắt chữ","🎯 Game Trắc Nghiệm", "Game quay số may mắn","Game quay số may mắn v2","Slot machine"])
with tabA:
    st.header("Game tung xúc sắc")
    st.image("https://thumb.ac-illust.com/11/11208a7f39207d32b1cff1a66d22dd75_t.jpeg")
    st.write("LUẬT CHƠI")
    st.write("Bấm Lắc xúc sắc để được một số ngẫu nhiên từ 1 đến 6")
    if st.button("Lắc xúc sắc"):
        roll = random.randint(1,6)
        st.success(f"bạn tung được số {roll}!!!!")
        if roll == 1:
            st.image(
            "http://www.clker.com/cliparts/m/v/m/J/4/V/dice-1-md.png"
        )
        if roll == 2:
            st.image(
            "https://www.clker.com/cliparts/a/Y/E/o/z/t/dice-2-md.png"
        )
        if roll == 3:
            st.image(
            "https://www.clker.com/cliparts/O/I/r/9/W/x/dice-3-md.png"
        )
        if roll == 4:
            st.image(
            "https://www.clker.com/cliparts/r/z/d/a/L/V/dice-4-md.png"
        )
        if roll == 5:
            st.image(
            "https://www.clker.com/cliparts/U/N/J/F/T/x/dice-5-md.png"
        )
        if roll == 6:
            st.image(
            "https://www.clker.com/cliparts/l/6/4/3/K/H/dice-6-md.png"
        )
with tabB:
    st.header("Game đoán số bí mật 1 - 100")
    st.image("https://m.media-amazon.com/images/I/71Agu95C-jL._AC_UF894,1000_QL80_.jpg")
    st.write("LUẬT CHƠI")
    st.write("Đoán một số bất kì từ 1 đến 100, nhập số để biết được số chính xác lớn hay bé hơn số đã nhập, cố đoán trong ít lần thử nhất có thể. Bấm chơi lại sau khi đoán đúng để được chơi lại")
    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 100)
        st.session_state.tries = 0
    guess = st.number_input("Nhập số dự đoán 1 - 100", min_value=1,max_value=100,step=1)
    if st.button("Đoán !!!!!"):
        st.session_state.tries += 1
        if guess < st.session_state.secret:
            st.warning("lớn hơn")
            st.image(
            "https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg"
        )
        elif guess > st.session_state.secret:
            st.warning("nhỏ hơn")
            st.image(
            "https://i.kym-cdn.com/editorials/icons/original/000/013/755/mon.jpg"
        )
        else:
            st.success(f"Chính xác! Bạn đoán đúng sau {st.session_state.tries} lần")
            st.image(
            "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR2pBfdCwgvKb7E8RBYkSluf3u3EdNxv54GuQ&s"
        )
    if st.button("Chơi lại"):
        st.session_state.secret = random.randint(1,100)
        st.session_state.tries = 0
with tabC:
    st.header("Kéo - Búa - Bao")
    st.image("https://static.tvtropes.org/trope_videos_transcoded/images/sd/q7uwxt.jpg")
    st.write("LUẬT CHƠI")
    st.write("Bấm nút để ra một trong kéo, búa hoặc bao. Hãy cố gắng thắng con bot nha!")
    st.write("Kéo thắng bao")
    st.write("Búa thắng kéo")
    st.write("Bao thắng búa")
    user = st.selectbox("Bạn chọn: ", ["Kéo", "Búa", "Bao"])
    bot = random.choice(["Kéo", "Búa", "Bao"])
    if st.button("Ra tay nào !!!!!!"):
        st.write(f"Bot chọn: {bot}")
        if user == bot:
            st.warning("Hoà!!!")
            st.image("https://i1.sndcdn.com/artworks-ecyyzfetWzmHLDpo-X7ICfQ-t500x500.jpg")
        elif(user == "Kéo" and bot == "Bao") or (user == "Bao" and bot == "Búa") or (user == "Búa" and bot == "Kéo"):
            st.success("Bạn thắng!!!!")
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1MBsQ9GnV0RNq9b_rJA63UN8m4e0Xq6HpGQ&s")
        else:
            st.error("Bạn thua!!!!")
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGlF-k_0Gsm39dJSSZCSEJUF-UsSkm_SAkHg&s")
with tabD:
    st.header("Game tính toán nhanh (+ - * /)")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ60myNa1QL0kJZoObUjDzto5UAyBokwUzLUg&s")
    st.write("LUẬT CHƠI")
    st.write("Nhập kết quả cho phép toán đã cho và bấm kiểm tra để biết đáp án đúng hay sai, bấm nút câu hỏi để được phép tính mới. Hãy trổ tài toán học của bạn nhé!")
    if "a" not in st.session_state:
        st.session_state.a = random.randint(1, 20)
        st.session_state.b = random.randint(1, 20)
        st.session_state.op = random.choice(["+", "-", "*", "/"])

    a = st.session_state.a
    b = st.session_state.b
    op = st.session_state.op
    st.session_state.answer = 0.0
    #tính kết quả đúng
    if op == "+":
        correct = a + b
    elif op == "-":
        correct = a - b
    elif op == "*":
        correct = a * b
    else:
        correct = round(a / b, 2)

    if st.button("Câu hỏi"):
        st.session_state.a = random.randint(1, 20)
        st.session_state.b = random.randint(1, 20)
        st.session_state.op = random.choice(["+", "-", "*", "/"])
        st.session_state.answer = 0.0

    a = st.session_state.a
    b = st.session_state.b
    op = st.session_state.op
    st.session_state.answer = 0.0
    if op == "/":
        st.write(f"tính {a} {op} {b} = ? (làm tròn 2 chữ số)")
    else:
        st.write(f"tính {a} {op} {b} = ?")

    answer = st.number_input("Nhập kết quả: ", step=1.0)

    if st.button ("Kiểm tra "):
        if correct == answer:
            st.success(" Chính xác")
            st.image("https://media.tenor.com/DtD4LZbctTIAAAAM/tamm-cat.gif")
        elif abs(answer - correct) < 0.005:
            st.success(" Chính xác")
            st.image("https://media.tenor.com/DtD4LZbctTIAAAAM/tamm-cat.gif")
        else:
            st.error(f"sai rùi, đáp án đúng là {correct} ")
            st.image("https://media.tenor.com/jXMsEpz30nIAAAAM/cat-cat-meme.gif")
with tabF:
    st.header("Game đuổi hình bắt chữ")
    sco = 0
    puzzles =  [
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469022597_dhbc.jpg",
            "answer": "thương tâm"
        },
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469011991_vai-tro.jpg",
            "answer": "vai trò"
        },
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469118011_tam-giac-can.jpg",
            "answer": "tam giác cân"
        },
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120784_kien-truc-su.jpg",
            "answer": "kiến trúc sư"
        },
        {
            "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1469120698_dan-bau.jpg",
            "answer": "đàn bầu"
        },
        {   "image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468933365_sau-sac.jpg",
            "answer": "sâu sắc"
            }  ,
            {"image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468933323_mat-bao.jpg",
            "answer": "mặt báo"
            },
            {"image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468932180_cao-hung.jpg",
            "answer": "cao hứng"
            },
            {"image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468811373_cao-nien.jpg",
            "answer": "cao niên"
            },
            {"image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468811344_cam-sung.jpg",
            "answer": "cắm sừng"
            },
            {"image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468386543_binh-chan-nhu-vai.jpg",
            "answer": "bình chân như vại"
            },
            {"image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468286389_ao-uoc.jpg",
            "answer": "ao ước"
            },
            {"image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468286072_vo-mong.jpg",
            "answer": "vỡ mộng"
            },
            {"image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468286022_thuong-hieu.jpg",
            "answer": "thương hiệu"
            },
            {"image": "https://cdn.lazi.vn/storage/uploads/dhbc/1468285782_thong-thoang.jpg",
            "answer": "thông thoáng"
        }
    ]
    if "dhbc_index" not in st.session_state:
        st.session_state.dhbc_index = random.randint(0,len(puzzles) - 1)
        st.session_state.start_time = time.time()
        st.session_state.duration = 45
        st.session_state.finished = False
        st.session_state.result = ""
        st.info(f"Bạn đang có {sco} điểm")
    puzzle = puzzles[st.session_state.dhbc_index]
    st.image(puzzle["image"], width=300)
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = st.session_state.duration - elapsed
    if remaining > 0 and not st.session_state.finished:
        st.warning(f"còn lại: {remaining} giây")
    else:
        st.session_state.finished = True
        st.error("Hết giờ")
    guess = st.text_input("Nhập đáp án: ", disabled=st.session_state.finished)
    if st.button("Kiểm tra") and not st.session_state.finished:
        if guess.lower().strip() == puzzle["answer"].lower():
            st.session_state.result = "correct"
            st.session_state.finished = True
        else:
            st.session_state.result = "wrong"
    if st.session_state.result == "correct":
        st.success("chính xác")
        sco+=10
        st.balloons()
    elif st.session_state.result == "wrong":
        st.error("Sai rồi, bạn nên thử lại !!!!")
        sco-=2
    if st.session_state.finished and remaining <=0:
        st.info(f"Đáp án đúng là: **{puzzle['answer']}**")
    if st.button("Vòng mới"):
        st.session_state.dhbc_index = random.randint(0,len(puzzles) - 1)
        st.session_state.start_time = time.time()
        st.session_state.finished = False
        st.session_state.result = ""
        st.info(f"Bạn đang có {sco} điểm")
        st.rerun()
with tabE:    
    st.header("🎯 Game Trắc Nghiệm")

    questions = [
        {
            "question": "Thủ đô của Việt Nam là gì?",
            "options": ["Hà Nội", "Huế", "Đà Nẵng", "Sài Gòn"],
            "answer": "Hà Nội"
            },
            {
            "question": "5 + 7 * 2 = ?",
            "options": ["24", "19", "17", "26"],
            "answer": "19"
            },
            {
            "question": "Ngôn ngữ dùng cho Streamlit?",
            "options": ["Java", "Python", "C++", "PHP"],
            "answer": "Python"
            },
            {
            "question": "Trái đất có bao nhiêu châu lục?",
            "options": ["5", "6", "7", "8"],
            "answer": "7"
            },
            {
            "question": "HTML là viết tắt của?",
            "options": ["HyperText Markup Language", "HighText Machine Language", "Hyper Tool Markup", "Home Tool Markup"],
            "answer": "HyperText Markup Language"
            }
        ]
        #Khởi tạo
    if "quiz_index" not in st.session_state:
        st.session_state.quiz_index = 0
        st.session_state.quiz_score = 0
        st.session_state.quiz_done = False
        st.session_state.quiz_feedback = ""
        st.session_state.quiz_checked = False
        st.session_state.start_time = time.time()
    TOTAL_TIME = 60
    elapsed = int(time.time() - st.session_state.start_time)
    remaining = max(TOTAL_TIME - elapsed,0)
    if remaining == 0:
        st.session_state.quiz_done = True
    st.progress(remaining/TOTAL_TIME)
    st.write(f"Thời gian còn lại: ** {remaining} giây")
    st.progress(st.session_state.quiz_index/len(questions))
    if st.session_state.quiz_done:
        st.success(f"Hoàn thành ! Điểm của bạn: {st.session_state.quiz_score}/ {len(questions)}")
        if st.button("Chơi lại!"):
            st.session_state.quiz_index = 0
            st.session_state.quiz_score = 0
            st.session_state.quiz_done = False
            st.session_state.quiz_feedback = ""
            st.session_state.quiz_checked = False
            st.session_state.start_time = time.time()
            st.rerun()
    else:
        q = questions[st.session_state.quiz_index]
        st.header(f"Câu {st.session_state.quiz_index+1}: {q['question']}")
        choice = st.radio(
            "Chọn đáp án",
            q['options'],
            key = f"quiz_{st.session_state.quiz_index}"
            )
        if st.button("Kiểm_tra"):
            if choice == q["answer"]:
                st.session_state.quiz_score += 1
                st.session_state.quiz_feedback = "correct"
                st.audio("https://www.soundjay.com/buttons/sounds/button-3.mp3")
            else:
                st.session_state.quiz_feedback = "wrong"
                st.audio("https://www.soundjay.com/buttons/sounds/button-10.mp3")
            #=====Hiển thị kết quả ========
        if st.session_state.quiz_feedback == "correct":
            st.success("Chính xác")
            st.balloons()
        elif st.session_state.quiz_feedback == "wrong":
            st.error(f"Sai rồi, đáp án đúng là : {q['answer']}")
            #====nút câu tiếp theo
        if st.session_state.quiz_feedback != "":
            if st.button("Câu tiếp theo"):
                st.session_state.quiz_index += 1
                st.session_state.quiz_feedback = ""
                st.session_state.quiz_checked = False
                if st.session_state.quiz_index >= len(questions):
                    st.session_state.quiz_done = True
                st.rerun()
with tabG:
    st.title("Game quay số may mắn")
    if "prizes" not in st.session_state:
        st.session_state.prizes = []
    new_prize = st.text_input("Nhập phần thưởng")
    if st.button("Thêm phần thưởng"):
        if new_prize:
            st.session_state.prizes.append(new_prize)
    st.write("Danh sách phần thưởng: ", st.session_state.prizes)
    if st.button("Quay số"):
        if st.session_state.prizes:
            result = random.choice(st.session_state.prizes)
            st.success(f"Bạn trúng {result}")
        else:
            st.warning("Chưa có phần thưởng")
    if st.button("Reset"):
        st.session_state.prizes = []
with tabH:
    if "new_prizes" not in st.session_state:
        st.session_state.new_prizes = []
    
    if "weights" not in st.session_state:
        st.session_state.weights = []
    
    st.subheader("Thêm phần thưởng")
    
    col1, col2 = st.columns(2)
    
    with col1:
        new_prize = st.text_input("Tên phần thưởng")
    
    with col2:
        weight = st.number_input("Tỷ lệ trúng (%)", min_value=1, max_value=100, value=1)
    
    if st.button("Thêm"):
        if new_prize:
            st.session_state.new_prizes.append(new_prize)
            st.session_state.weights.append(weight)
            st.success(f"Đã thêm {new_prize}")
    
    st.subheader("Danh sách phần thưởng")
    
    if st.session_state.new_prizes:
        for i, prize in enumerate(st.session_state.new_prizes):
            st.write(f"{i+1}. {prize} | tỷ lệ {st.session_state.weights[i]}%")
    else:
        st.info("Chưa có phần thưởng")
    
    st.subheader("Quay số")
    
    if st.button("Quay ngay"):
        if st.session_state.new_prizes:
    
            spin_placeholder = st.empty()
    
            for i in range(15):
                spin_placeholder.markdown(
                    f"## Đang quay... {random.choice(st.session_state.new_prizes)}"
                )
                time.sleep(0.1)
    
            result = random.choices(
                st.session_state.new_prizes,
                weights=st.session_state.weights,
                k=1
            )[0]
    
            spin_placeholder.empty()
    
            st.balloons()
            st.success(f"🎉 Chúc mừng bạn đã trúng: **{result}**")
    
        else:
            st.warning("Chưa có phần thưởng")
    
    if st.button("Reset game"):
        st.session_state.new_prizes = []
        st.session_state.weights = []
        st.success("Đã reset")
with tabI:
    st.title("🎰 High Stakes Slot Machine")

    symbols = ["🍒", "🍋", "💎", "7️⃣", "💀"]
    weights = [40, 30, 15, 4, 1]

    if "balance" not in st.session_state:
        st.session_state.balance = 1000
    if "last_spin" not in st.session_state:
        st.session_state.last_spin = ["❔", "❔", "❔"]
    if "history" not in st.session_state:
        st.session_state.history = []
    if "spins" not in st.session_state:
        st.session_state.spins = 0
    if "wins" not in st.session_state:
        st.session_state.wins = 0

    bet = st.selectbox("Choose your bet", [10, 20, 50, 100], index=2)

    balance_display = st.empty()
    stats_display = st.empty()
    balance_display.write(f"Balance: ${st.session_state.balance}")
    stats_display.write(f"Spins: {st.session_state.spins} | Wins: {st.session_state.wins}")
    slot_display = st.empty()
    slot_display.markdown(f"## {' | '.join(st.session_state.last_spin)}")

    spin = st.button(f"Spin ${bet}", disabled=st.session_state.balance < bet)

    if spin:
        st.session_state.balance -= bet
        st.session_state.spins += 1
        balance_display.write(f"Balance: ${st.session_state.balance}")
        stats_display.write(f"Spins: {st.session_state.spins} | Wins: {st.session_state.wins}")
        for _ in range(8):
            fake_result = random.choices(symbols, weights=weights, k=3)
            slot_display.markdown(f"## {' | '.join(fake_result)}")
            time.sleep(0.08)

        result = random.choices(symbols, weights=weights, k=3)
        st.session_state.last_spin = result
        st.session_state.history.insert(0, result)
        st.session_state.history = st.session_state.history[:5]
        slot_display.markdown(f"## {' | '.join(result)}")

        win = 0

        if result.count("💀") == 3:
            st.session_state.balance = 0
            st.error("💀💀💀 You lost everything!")
        elif result.count("💀") == 2:
            st.session_state.balance -= 200
            st.error("💀💀 You lost $200")
        elif result.count("💀") == 1:
            st.error("💀 You lost the spin!")

        elif result.count("7️⃣") == 3:
            win = bet * 100
            st.success(f"🎉 JACKPOT! +${win}")

        elif result.count("💎") == 3:
            win = bet * 20
            st.success(f"💎 Big win! +${win}")
        elif result.count("🍋") == 3:
            win = bet * 10
            st.success(f"🍋 Good win! +${win}")
        elif result.count("🍒") == 3:
            win = bet * 5
            st.success(f"🍒 Nice win! +${win}")

        elif result.count("7️⃣") == 2:
            win = bet * 10
            st.success(f"✨ Two 7s! +${win}")

        elif result.count("💎") == 2:
            win = bet * 3
            st.success(f"💎 Two diamonds! +${win}")
        elif result.count("🍋") == 2:
            win = bet 
            st.success(f"🍋 Two lemons! +${win}")
        elif result.count("🍒") == 2:
            win = bet//2
            st.success(f"🍒 Two cherries! +${win}")

        else:
            st.warning("You lost the spin.")

        if win > 0:
            st.session_state.balance += win
            st.session_state.wins += 1
        balance_display.write(f"Balance: ${st.session_state.balance}")
        stats_display.write(f"Total spins: {st.session_state.spins} | Wins: {st.session_state.wins}")
    if st.session_state.balance <= 0:
        st.error("Game Over!")

    st.subheader("Last 5 spins")
    if st.session_state.history:
        for h in st.session_state.history:
            st.write(" | ".join(h))
    else:
        st.info("No spins yet.")

    if st.button("Reset", key="reset_slot"):
        st.session_state.balance = 1000
        st.session_state.last_spin = ["❔", "❔", "❔"]
        st.session_state.history = []
        st.session_state.spins = 0
        st.session_state.wins = 0