from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.post('/run_code')
async def run_code(code: str):
    try:
        # Executa o código
        result = subprocess.check_output(['python', '-c', code], stderr=subprocess.STDOUT, timeout=10, universal_newlines=True)
        return {'output': result}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=400, detail=e.output)
    except subprocess.TimeoutExpired:
        raise HTTPException(status_code=400, detail='Tempo limite excedido')
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='localhost', port=8000)
