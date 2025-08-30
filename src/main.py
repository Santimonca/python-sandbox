import serial
import json
import time


def split_concatenated_json(data):
    """
    Separa múltiples JSONs concatenados en una sola línea.
    Ejemplo: '{"a":1}{"b":2}' -> ['{"a":1}', '{"b":2}']
    """
    json_strings = []
    if not data:
        return json_strings
    
    # Buscar patrones }{ para separar JSONs concatenados
    if '}{' in data:
        # Dividir por }{ y reconstruir los JSONs
        parts = data.split('}{')
        
        for i, part in enumerate(parts):
            if i == 0:
                # Primera parte: añadir } al final
                json_strings.append(part + '}')
            elif i == len(parts) - 1:
                # Última parte: añadir { al inicio
                json_strings.append('{' + part)
            else:
                # Partes del medio: añadir { al inicio y } al final
                json_strings.append('{' + part + '}')
    else:
        # Si no hay concatenación, devolver el string original
        json_strings.append(data)
    
    return json_strings


def main():
    # Configuración del puerto serial
    # Cambia '/dev/ttyUSB0' por el puerto correcto de tu Arduino
    # En macOS suele ser '/dev/tty.usbmodem*' o '/dev/tty.usbserial*'
    # En Windows sería 'COM3', 'COM4', etc.
    SERIAL_PORT = '/dev/tty.usbmodemF412FA65971C2'  # Ajusta según tu sistema
    BAUD_RATE = 115200  # Ajusta según la configuración de tu Arduino
    
    print("Iniciando lectura del puerto serial...")
    print(f"Puerto: {SERIAL_PORT}, Baudrate: {BAUD_RATE}")
    
    try:
        # Establecer conexión serial
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)  # Esperar a que se establezca la conexión
        
        print("Conexión establecida. Presiona Ctrl+C para salir.")
        print("-" * 50)
        
        while True:
            # Leer línea del puerto serial
            if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                
                if line:  # Si hay datos
                    # Separar múltiples JSONs concatenados
                    json_strings = split_concatenated_json(line)
                    
                    for json_str in json_strings:
                        if json_str:  # Si el string no está vacío
                            try:
                                # Convertir JSON a diccionario
                                data_dict = json.loads(json_str)
                                
                                # Imprimir el diccionario
                                print(f"Datos recibidos: {data_dict}")
                                
                                # También puedes acceder a campos específicos:
                                if 'sensor' in data_dict and 'voltage' in data_dict:
                                    sensor_type = data_dict['sensor']
                                    voltage_value = data_dict['voltage']
                                    print(f"Sensor: {sensor_type}, Voltaje: {voltage_value}V")
                                
                                print("-" * 30)
                                
                            except json.JSONDecodeError as e:
                                print(f"Error al parsear JSON: {e}")
                                print(f"Datos recibidos: {json_str}")
                        
            time.sleep(0.1)  # Pequeña pausa para no sobrecargar el CPU
            
    except serial.SerialException as e:
        print(f"Error de conexión serial: {e}")
        print("Verifica que el puerto sea correcto y que el Arduino esté conectado.")
        
    except KeyboardInterrupt:
        print("\nDeteniendo lectura...")
        
    except Exception as e:
        print(f"Error inesperado: {e}")
        
    finally:
        try:
            ser.close()
            print("Conexión serial cerrada.")
        except:
            pass


if __name__ == "__main__":
    main()