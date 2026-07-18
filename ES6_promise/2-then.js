export default function handleResponseFromAPI(promise) {
    return promise
        .then(() => {
            return {
                status: 200,
                body: 'success'
            };
        })
        .catch(() => {
            return new Error();
        })
        .finally(() => {
            Console.log('Got a response from the API to the console');
        });
}