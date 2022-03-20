import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { User } from 'src/entities/user.entity';
import { Repository } from 'typeorm';
import { UserCreateDto, UserLoginDto } from './user.dto';

export interface IUser {
  id: string;
  username: string;
  email: string;
}

export interface ITokenResponse {
  token: string;
}

@Injectable()
export class UserService {
  constructor(
    @InjectRepository(User) private readonly userRepository: Repository<User>,
  ) {}

  async newUser(user: UserCreateDto): Promise<IUser> {
    let dbUser = new User();
    dbUser.username = user.username;
    dbUser.email = user.email;
    dbUser.password = user.password;
    dbUser = await this.userRepository.save(dbUser);

    return {
      id: dbUser.id,
      username: dbUser.username,
      email: dbUser.email,
    };
  }

  async loginUser(user: UserLoginDto): Promise<ITokenResponse> {
    return;
  }

  async findOneByUsername(username: string): Promise<IUser> {
    const user = await this.userRepository.findOne({
      where: { username },
    });

    if (!user) {
      throw new Error('User not found');
    }

    return {
      id: user.id,
      username: user.username,
      email: user.email,
    };
  }

  async findOneByEmail(email: string): Promise<IUser> {
    const user = await this.userRepository.findOne({
      where: { email },
    });

    if (!user) {
      throw new Error('User not found');
    }

    return {
      id: user.id,
      username: user.username,
      email: user.email,
    };
  }
}
