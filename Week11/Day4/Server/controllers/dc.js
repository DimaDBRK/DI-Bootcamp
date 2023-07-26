//READ - GET get all products -> _ before it 
export const _getMessage = (req, res) => {
    const data = {msg: "Hello From Express"};
    try {
        res.json(data);
    } catch(e) {
        console.log(e);
        res.status(500).json({ msg: e.message }); // or e.message
    }
}

export const _anwserPostMessage = (req, res) => {
    try {
        const info = req.body;
        console.log(info);
        res.json(info);
    } catch(e) {
        console.log(e);
        res.status(500).json({ msg: e.message }); // or e.message
    }
}