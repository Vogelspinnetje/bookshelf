from pyzbar.pyzbar import decode
from PIL import Image
import requests
import cv2

def get_barcode():
    cap = cv2.VideoCapture(1)

    last_code = None
    confidence = 0
    threshold = 5

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        barcodes = decode(frame)
        
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            barcode_data = barcode.data.decode("utf-8")
            barcode_type = barcode.type
            text = f"{barcode_data} ({barcode_type})"
            cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            if barcode_data == last_code:
                confidence += 1
            else:
                confidence = 1
                last_code = barcode_data

            if confidence >= threshold:
                cap.release()
                cv2.destroyAllWindows()
                return barcode_data

        cv2.imshow("Live Barcode Scanner", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

def lookup_isbn(isbn):
    url = f"https://openlibrary.org/api/books"
    params = {
        "bibkeys": f"ISBN:{isbn}",
        "jscmd": "details",
        "format": "json"
    }
    
    r = requests.get(url, params=params)
    data = r.json()
    key = f"ISBN:{isbn}"
    
    if key in data:
        details = data[key]["details"]
        return {
            "title": details.get("title"),
            "authors": ", ".join([a.get("name") for a in details.get("authors", [])]),
            "publish_date": details.get("publish_date"),
            "number_of_pages": details.get("number_of_pages"),
        }
        
    return None


if __name__ == "__main__":
    while True:
        isbn = get_barcode()
        info = lookup_isbn(isbn)
        if info == None:
            print("Boek niet gevonden.")   
        else:
            print(f'{info["title"]} - {info["authors"]}')
        if input("Nog een boek scannen? Typ dan Y") != "Y":
            break
