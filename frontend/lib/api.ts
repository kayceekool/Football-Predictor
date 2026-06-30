const API_URL =
process.env.NEXT_PUBLIC_API_URL;

export async function getPredictions(){

    const response = await fetch(

        `${API_URL}/live/today`,

        {
            cache:"no-store"
        }

    );

    if(!response.ok){

        return [];

    }

    return response.json();

}