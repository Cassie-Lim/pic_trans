let info = document.getElementById('info');
let op_elem = document.getElementById('trans_op');
let sw_butt = document.getElementById('sw_butt');
let preview = document.getElementById('image_preview');
let img_trans;
let basic_path;
let inimg_path;
//开启弹出层
function ShowDiv(bg_div){
    document.getElementById(bg_div).style.display='block' ;
    var bgdiv = document.getElementById(bg_div);
    bgdiv.style.width = document.body.scrollWidth;
};
//关闭弹出层
function CloseDiv(bg_div)
{
    document.getElementById(bg_div).style.display='none';
};
//初步判断是否为图片格式
function isAssetTypeAnImage(ext) {
    return [    
    'png', 'jpg', 'jpeg', 'bmp', 'gif', 'webp', 'psd', 'svg', 'tiff'].    
    indexOf(ext.toLowerCase()) !== -1;
}
//上传图片并显示
function upload(){
    inimg_path = document.getElementById("img_path").value;
    var type = inimg_path.substring(inimg_path.lastIndexOf(".")+1);
    // alert(type);
    alert(inimg_path);
    
    if(!inimg_path){
        alert("请输入图片绝对路径！");
        return;
    }
    else if(!isAssetTypeAnImage(type)){
        alert("请输入合法图片路径！");
        return;
    } 
    preview.setAttribute("src",inimg_path);
    sw_butt.disabled = "";
}



function trans(){
    ShowDiv("fade");

    var Shell = new ActiveXObject("WScript.Shell");
    try {
        //exe程序所在位置以及要传的参数
        var op = op_elem.selectedIndex + 1;
        var img_path;
        var exe_path;
        var save_path;
        basic_path = window.location.pathname;
        basic_path = basic_path.substring(1,basic_path.lastIndexOf("/")) +"/trans_src/dist/";
        exe_path = basic_path + "trans-pic.exe";
        save_path = basic_path + "out.jpg";
        img_path = inimg_path.replace(/\\/g,'\\\\');
        var inst = exe_path+" -op "+op+" -p "+ img_path+" -sp "+save_path;
        var dummy = Shell.Run(inst, 7, true);
        alert("转换完成！");
        save_path = save_path.replace(/\//g, '\\');
        img_trans = document.getElementById('image_trans');
        //生成随机数确保图片动态刷新
        img_trans.setAttribute("src",save_path+'?'+Math.random());
    }
    catch (e) {
        alert("默认可执行文件或图片不存在,请检查trans-pic.exe是否被移动以及图片路径");
    }
    CloseDiv("fade");
    let dl_butt = document.getElementById('dl_butt');
    dl_butt.disabled="";
}
function openFile(){
    try{ 
        var obj=new ActiveXObject("wscript.shell"); 
        if(obj){ 
            obj.Run("\""+basic_path+"\"", 1, false );
            obj=null; 
        } 
    }catch(e){ 
        alert("打开文件夹失败！"); 
    } 
}
// function save() {
//     var url = img_trans.src; // 获取图片地址
//     alert(url);
//     var a = document.createElement('a'); // 创建一个a节点插入的document
//     var event = new MouseEvent('click') // 模拟鼠标click点击事件
//     a.download = 'out' // 设置a节点的download属性值
//     a.href = url; // 将图片的src赋值给a节点的href
//     a.dispatchEvent(event)
// }

// let fileInput = document.getElementById('file');
// // 监听change事件:
// fileInput.addEventListener('change', function() {
//     // 清除背景图片:
//     preview.style.backgroundImage = '';
//     // if (!fileInput.value) {
//     //     info.innerHTML = '没有选择文件';
//     //     return;
//     // }
//     let file = fileInput.files[0];
//     let size = file.size;
//     // if (size >= 1 * 1024 * 1024) {
//     //     alert('文件大小超出限制');
//     //     info.innerHTML = '文件大小超出限制';
//     //     return false;
//     // }
    
//     // // 获取File信息:
//     // if (!['image/jpeg', 'image/png', 'image/gif'].includes(file.type)) {
//     //     alert('不是有效的图片文件!');
//     //     return;
//     // }
//     // // 读取文件:
//     // let reader = new FileReader();
//     // reader.onload = function(e) {
//     //     let data = e.target.result;
//     //     console.log(preview, 'a标签')
//     //     preview.src = data
//     // };
//     // // 以DataURL的形式读取文件:
//     // reader.readAsDataURL(file);
//     sw_butt.disabled = "";
// });