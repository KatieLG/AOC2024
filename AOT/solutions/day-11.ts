type Excuse<T> = new (excuse: T) => `${string & keyof T}: ${string & T[keyof T]}`;
