# 1. Mô tả tổng quan về hệ thống đồ họa:
**1. Giao diện đồ họa:**
> * Là một chuỗi những hình ảnh về trò chơi. 
> * Mỗi hình ảnh thể hiện trạng thái **(state)** mà người chơi quan sát được dưới góc nhìn cá nhân.
> * Nó được thiết kế dựa trên state, tức là biểu diễn các thông số của state dưới dạng hình ảnh trực quan để người chơi có thể theo dõi diễn biến trò chơi dễ dàng hơn.

**2. Về tương tác:**
> * Tại mỗi trạng thái mà người chơi sẽ nhận được những hành động **(action)** phù hợp để sử dụng. 
> * Khi lựa chọn một trong các hành động đó, giao diện đồ họa sẽ ghi nhận và chuyển sang trạng thái tương ứng tiếp theo.Ở trạng thái mới này lại có một dãy hành động phù hợp khác... Cứ như vậy đến khi kết thúc ván chơi.

--> Mọi trạng thái **(state)** cũng như hành động **(action)** mà người chơi sử dụng sẽ được lưu để quan sát lại khi một ván chơi kết thúc.
***

# 2. Thiết kế hệ thống đồ họa:
* Sử dụng template có sẵn theo hệ thống
* Sử dụng thư viện PIL để xử lý hình ảnh
## 1. Tạo file `_render_func.py` và xây dựng các hàm trong hệ thống:
1. Hàm `get_state_image`:
> * Input: state ( np.array 1D)
> * Output: Hình ảnh thể hiện state tương ứng

2. Hàm `get_description`:
> * Input: action ( float64)
> * Output: Xâu mô tả ý nghĩa của hành động đó ( String)

3. Hàm `get_env_components`:
> * Input: ( None)
> * Output: Một object `env_components` chứa tất cả các thành phần, thông tin về trạng thái của môi trường.

4. Hàm `get_main_player_state`:
> * Input: `env_components, list_agent, list_data, action = None`
> * Output: `win, state, new_env_components`
>    * win: Người chơi có chiến thắng hay không?
>    * state: Trạng thái tiếp theo của **người chơi chính ** nhận được
>    * new_env_components: chứa những thay đổi của các thành phần trong môi trường.

# Cách sử dụng Hệ thống đồ họa:
![huongdanDoHoa](https://github.com/tandat17z/ENV/assets/126872123/f9f02500-c57f-46e8-a0a9-905f0d4b47c3)

***

1. **Quan sát một ván đấu của Agent đã chơi:**

![hdDoHoa](https://github.com/tandat17z/ENV/assets/126872123/15e55747-eadd-4fb9-9de8-1daa7f0bcb54)

2. **Người sử dụng chơi trực tiếp:**
* Gán Agent = "human"

![image](https://github.com/tandat17z/ENV/assets/126872123/76ec52b7-67a9-4bbf-b484-75ed57abc465)
