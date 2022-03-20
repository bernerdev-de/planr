export interface UserCreateDto {
    username: string;
    email: string;
    password: string;
}

export interface UserLoginDto {
    email: string;
    password: string;
}