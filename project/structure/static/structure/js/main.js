let canvas = document.getElementById("canvas");
let context = canvas.getContext("2d");

canvas.width = 1440;
canvas.height = 900;

let background_color = "#C6D0D7"

let canvas_width = canvas.width;
let canvas_height = canvas.height;

let ghost_blocks = {};
let dict_blocks = {};
let is_dragging = false;
let start_blockX;
let start_blockY;
let dragging_block;
let dragging_block_key;
let startX;
let startY;
let permission = false;

base_url = `${window.location.hostname}:${window.location.port}`
        const websocket = new WebSocket(`ws://${base_url}`)
        websocket.onopen = function (event) {
            websocket.send("Client sends Welcome")
            draw_all();
        }
        websocket.onmessage = function (event) {
            message = JSON.parse(event.data)
            let position = message.position
            permission = message.permission

            /* запись имён менеджеров в фигуры */
            dict_blocks = {50: {x: 130, y: 20, width: 180, height: 90, position: "Снятие /n с занимаемой /n должности", font: "16px"}};
            ghost_blocks = {};

            for(let key in alfa_dict_blocks) {
                check_is_manager = alfa_dict_blocks[key].is_manager
                // если блок менеджера, и для этой должности есть имя сотрудника, то записываем блок в словарь блоков
                // если имени нет, то блок попадает в словарь блоков призраков (должность без имени)
                // если блок не менеджера, то он сразу попадает в словарь блоков
                if (check_is_manager) {
                    if (key in position) {
                        dict_blocks[key] = {};
                        for (let k in alfa_dict_blocks[key]) {
                            dict_blocks[key][k] = alfa_dict_blocks[key][k]
                        }
                        dict_blocks[key].manager_name = position[key];
                    } else {
                        ghost_blocks[key] = {};
                        for (let k in alfa_dict_blocks[key]) {
                            ghost_blocks[key][k] = alfa_dict_blocks[key][k]
                        }
                        ghost_blocks[key].manager_name = " ";
                    }
                } else {
                    dict_blocks[key] = {};
                    for (let k in alfa_dict_blocks[key]) {
                        dict_blocks[key][k] = alfa_dict_blocks[key][k]
                    }
                    dict_blocks[key].manager_name = " ";
                }
            }
            draw_all();
        }

/* проверка, что указатель мыши находится в блоке */
let is_mouse_in_block = function (x, y, block) {
    let block_left = block.x;
    let block_right = block.x + block.width;
    let block_top = block.y;
    let block_bottom = block.y + block.height;
    if (x > block_left && x < block_right && y > block_top && y < block_bottom) {
        return true;
    }
    return false;
};

/* Функция для отображения текста блока и переноса строк текста */
function wrapText(context, block) {
        let lines = ""
        if (block.is_manager) lines = (block.position + "/n" + block.manager_name).split("/n")
        else lines = block.position.split("/n");
        let countLines = lines.length;
        context.textBaseline = "middle";
        if (countLines == 1) {
            context.fillText(block.position, block.x + block.width/2, block.y + block.height/2);
        }
        else {
            for (let n = 0; n < countLines; n++) {
                context.fillText(lines[n], block.x + block.width/2, block.y + block.height/2 - countLines * 20/2 + 6*countLines + n * 14);
            }
        }
    };

/* рисуем блоки */
let draw_blocks = function (event) {
    context.textAlign = "center";

    let rect = canvas.getBoundingClientRect();
    let block;

    if (event) {
        mouseX = event.clientX - rect.left;
        mouseY = event.clientY - rect.top;
    };

    for (let key in dict_blocks) {
        /* проверка что указатель мыши находится в блоке, исходя из этого выбираем цвет блока */
        block = dict_blocks[key]
        if (event) {
            if (is_mouse_in_block(mouseX, mouseY, block)) {
                if (block.is_manager) context.fillStyle = "#FFA24C"
                else context.fillStyle = "#FFF2E5"
            }
            else {
                if (block.is_manager) context.fillStyle = "#E67A17"
                else context.fillStyle = "#F9D5B0"
            }
        }
        else {
            if (block.is_manager) context.fillStyle = "#E67A17"
            else context.fillStyle = "#F9D5B0"
        }

        if (key==50) context.fillStyle = "#8B959B"

        context.fillRect(block.x, block.y, block.width, block.height);
        context.fillStyle = "black";
        context.strokeRect(block.x, block.y, block.width, block.height);
        context.font = block.font + " Arial";
        wrapText(context, block);
    }
};

/* рисуем линии */
let draw_lines = function () {
    context.beginPath();
    for (let line of lines) {
        context.moveTo(line.mt_x, line.mt_y);
        context.lineTo(line.lt_x, line.lt_y);
    };
    context.stroke();
};

/* рисуем стрелки */
/* берутся начальные координаты стрелки и в зависимости от длинны и направления рисуются стрелки */
let draw_arrows = function () {
    context.beginPath();
    let lt = [];
    for (let arrow of arrows) {
        if (arrow.rotate == 1) lt = [[arrow.arrow_length, 0], [-4, -4], [4, 4], [-4, 4]];
        else if (arrow.rotate == 2) lt = [[-arrow.arrow_length, 0], [4, -4], [-4, 4], [4, 4]];
        else lt = [[0, arrow.arrow_length], [-4, -4], [4, 4], [4, -4]];

        context.moveTo(arrow.mt_x, arrow.mt_y);
        let temp_ltx = arrow.mt_x;
        let temp_lty = arrow.mt_y;
        for (let m of lt) {
            temp_ltx += m[0];
            temp_lty += m[1];
            context.lineTo(temp_ltx, temp_lty);
        };
    };
    context.stroke();
};

/* рисуем блоки призраки */
let draw_ghost_blocks = function (event) {
    context.clearRect(0, 0, canvas_width, canvas_height);
    context.fillStyle = background_color;
    context.fillRect(0, 0, canvas_width, canvas_height);
    context.textAlign = "center";
    let ghost_block;

    for (let key in ghost_blocks) {
        ghost_block = ghost_blocks[key]
        context.fillStyle = "#8B959B"
        context.fillRect(ghost_block.x, ghost_block.y, ghost_block.width, ghost_block.height);
        context.fillStyle = "black";
        context.strokeRect(ghost_block.x, ghost_block.y, ghost_block.width, ghost_block.height);
        context.font = ghost_block.font + " Arial";
        wrapText(context, ghost_blocks[key]);
    }
}

let draw_all = function() {
    draw_ghost_blocks();
    draw_blocks(event);
    draw_arrows();
    draw_lines();
}

/* функция обработки нажатия клавиши мыши */
let mouse_down = function(event) {
    let rect = canvas.getBoundingClientRect();
    startX = event.clientX - rect.left;
    startY = event.clientY - rect.top;

    /* если нажатие клавиши было в блоке менеджера то сохраняются
        начальные координаты x и y для возврата блока на исходное место,
       если нажат был блок отдела, то происходит переход на соответствующую страницу */

    /* проверяется нажатие на блок, если блок в данный момент, не несётся */
    if (!is_dragging && event.which == 1)  {
        for (let key in dict_blocks) {
            if (is_mouse_in_block(startX, startY, dict_blocks[key])) {
                if (dict_blocks[key].is_manager  && permission) {
                    is_dragging = true;
                    start_blockX = dict_blocks[key].x;
                    start_blockY = dict_blocks[key].y;
                    dragging_block = dict_blocks[key];
                    dragging_block_key = key;
                    /* создаём блок призрак поднятого блока и записывем его в список ghost_blocks */
                    ghost_blocks[key] = {};
                    for (let k in dragging_block) {
                        ghost_blocks[key][k] = dragging_block[k]
                    }
                    ghost_blocks[key].manager_name = " "
                    break;    // если блок определился, происходит прерывание цикла поиска блока
                } else {
                    let num_key = key;
                    window.location = `/department/` + num_key + '/id/ascend';
                }
            };
        }
    }
};

/* функция обработки отпускания клавиши мыши */
let mouse_up = function(event) {
    /* если блок находится в зоне освобождения от занимаемой должности на сервер отправляется соответствующее сообщение */
    if (is_dragging) {
        let rect = canvas.getBoundingClientRect();
        let mouseX = event.clientX - rect.left;
        let mouseY = event.clientY - rect.top;

        // назначение менеджера
        for (let key in ghost_blocks) {
            if (is_mouse_in_block(mouseX, mouseY, ghost_blocks[key])) {
                is_dragging = false;
                text_data = {type_message: "appoint_manager", from_position_id: dragging_block_key, to_position_id: key};
                websocket.send(JSON.stringify(text_data));
                start_blockX = ghost_blocks[key].x;
                start_blockY = ghost_blocks[key].y;
                dragging_block.width = ghost_blocks[key].width
                dragging_block.height = ghost_blocks[key].height
                delete ghost_blocks[key]
                return
            }
        }

        // снятие с должности менеджера
        if (is_mouse_in_block(mouseX, mouseY, dict_blocks[50])) {
            is_dragging = false;
            confirm("Подтвердите снятие с должности!");
            text_data = {type_message: "remove_manager", from_position_id: dragging_block_key};
            websocket.send(JSON.stringify(text_data));
        } else {
            dragging_block.x = start_blockX;
            dragging_block.y = start_blockY;
            delete ghost_blocks[dragging_block_key]
        }
    }
    is_dragging = false;
}

/* обработка движения мыши */
let mouse_move = function(event) {
    if (!is_dragging) {
        draw_all();
    }
    else {
        /* вычисляем координаты смещения мыши с поднятым блоком и перемещаем блок на это смещение */
        let rect = canvas.getBoundingClientRect();
        let mouseX = event.clientX - rect.left;
        let mouseY = event.clientY - rect.top;

        let dx = mouseX - startX;
        let dy = mouseY - startY;
        dragging_block.x += dx;
        dragging_block.y += dy;

        startX = mouseX;
        startY = mouseY;

        draw_all();

        /* снова рисуем поднятый блок, чтобы он был сверху всех фигур */
        context.shadowBlur = 15;
        context.shadowOffsetX = 0;
        context.shadowColor = "#5D6468";
        context.fillStyle = "#FFA24C"
        context.fillRect(dragging_block.x, dragging_block.y, dragging_block.width, dragging_block.height);
        context.shadowBlur = 0;
        context.fillStyle = "black";
        context.strokeRect(dragging_block.x, dragging_block.y, dragging_block.width, dragging_block.height);
        context.font = dragging_block.font + " Arial";
        wrapText(context, dragging_block);

    }
}

/* если мышь с блоком выйдет за поле, блок вернётся на своё изначальное место */
let mouse_out = function(event) {
    if (is_dragging) {
        dragging_block.x = start_blockX;
        dragging_block.y = start_blockY;
    }
    is_dragging = false;
}

canvas.onmousemove = mouse_move;
canvas.onmousedown = mouse_down;
canvas.onmouseup = mouse_up;
canvas.onmouseout = mouse_out;
