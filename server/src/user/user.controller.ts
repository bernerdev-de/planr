import {Controller, Get, Post, Body} from "@nestjs/common"
import { UserCreateDto, UserLoginDto } from "./user.dto"
import { IUser, UserService } from "./user.service"

@Controller("/user")
export class UserController {

    constructor(private readonly userService: UserService) {}

    @Post("/")
    async createUser(@Body() user: UserCreateDto): Promise<IUser> {
        return (await this.userService.newUser(user))
    }

    @Post("/login")
    async loginUser(@Body() user: UserLoginDto): Promise<IUser> {
        return (await this.userService.loginUser(user))
    }

}