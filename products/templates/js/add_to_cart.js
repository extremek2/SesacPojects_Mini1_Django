const form = document.getElementById('myForm');
const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;

const jsonData_list =[];
console.dir(jsonData_list)

form.addEventListener('submit', async (event) => {
  event.preventDefault(); // 폼 제출 기본 동작 방지

  // // 이부분을 drop 이벤트로 가져가면 가능할지???
  // const formData = new FormData(form);
  // const jsonData = {};

  // // FormData 객체를 순회하며 JSON 객체로 변환
  // for (const [key, value] of formData.entries()) {
  //   if (!jsonData[key]) {
  //     jsonData[key] = [value];  // key에 해당하는 값이 없으면 새 배열로 초기화
  //   } else {
  //     jsonData[key].push(value);  // 이미 값이 있으면 배열에 추가
  //   }
  // }
  try {
    const response = await fetch('/products/cart/create/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken
      },
      body: JSON.stringify(jsonData_list)
    });

    if (response.ok) {
      const data = await response.json();
      console.log('성공:', data);

    } else {
      console.error('요청 실패:', response.status, response.statusText);

    }
  } catch (error) {
    console.error('오류 발생:', error);
  }
});


function allowDrop(event) {
  event.preventDefault();
}


function handleDragStart(event) {
    const target = event.currentTarget;
    const data = {
      id: target.dataset.id,
      name: target.dataset.name,
      price: target.dataset.price
    };
    event.dataTransfer.setData("text/plain", JSON.stringify(data));
  }

function handleDrop(event) {
  event.preventDefault();
  const data = JSON.parse(event.dataTransfer.getData("text/plain"));
  console.log(data.id, data.name, data.price)

  // 장바구니 리스트에 표시
  const cartList = document.getElementById("cart-items");
  const item = document.createElement("li");
  item.className = "list-group-item";
  item.textContent = `${data.name}`;
  

  // cartList.innerHTML = ""; // 하나만 담도록 초기화 (여러 개 담으려면 제거)
  cartList.appendChild(item);
  console.log(cartList);
  console.dir(cartList);

  // FormData 객체를 순회하며 JSON 객체로 변환
  const jsonData = {};
  const formData = new FormData(form);
  for (const [key, value] of formData.entries()) {
    if (!jsonData[key]) {
      jsonData[key] = [value];  // key에 해당하는 값이 없으면 새 배열로 초기화
    } else {
      jsonData[key].push(value);  // 이미 값이 있으면 배열에 추가
    }
  }

  
  if (jsonData_list[0] == "") {
    jsonData_list.slice(0,0,jsonData);
  } else {
    jsonData_list.push(jsonData);
  }
  console.log(jsonData_list.length);
  console.log(jsonData_list);
  console.dir(jsonData_list);

  // 폼에 값 채우기
  document.getElementById("cart-product-id").value = data.id;
  document.getElementById("cart-product-name").value = data.name;
  document.getElementById("cart-product-price").value = data.price;
  
}