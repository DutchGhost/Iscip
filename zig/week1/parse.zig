const std = @import("std");
const TypeId = @import("builtin").TypeId;

fn is_signed(comptime N: type) bool {
    switch (@typeInfo(N)) {
        TypeId.Int => |int| {
            return int.is_signed;
        },
        else => {
            @compileError("Is_signed is only available on integer types. Found `" ++ @typeName(N) ++ "`.");
        }
    }
}

fn bitcount(comptime N: type) u32 {
    switch (@typeInfo(N)) {
        TypeId.Int => |int| {
            return @intCast(u32, int.bits);
        },
        else => {
            @compileError("Bitcount only available on integer types. Found `" ++ @typeName(N) ++ "`.");
        }
    }
}

fn starts_with(buff: []const u8, needle: u8) bool {
    return buff[0] == needle;
}

fn is_negative(comptime N: type, num: N) bool {
    return n < 0;
}

pub fn digits10(comptime N: type, n: N) usize {
    
    if (comptime is_signed(N)) {

        const nbits = comptime bitcount(N);

        const unsigned_friend = @IntType(false, nbits);

        if (is_negative(N, n)) {
            return digits10(unsigned_friend, @intCast(unsigned_friend, n * -1));
        }
        else {
            return digits10(unsigned_friend, @intCast(unsigned_friend, n));
        }
    }

    comptime var digits = 1;
    comptime var check = 10;

    inline while (check <= @maxValue(N)) : ({check *= 10; digits += 1;}) {
        if (n < check) {
            return digits;
        }
    }

    return digits;
}

const ParseError = error {
    /// The input had a byte that was not a digit
    InvalidCharacter,

    /// The result cannot fit in the type specified
    Overflow,
};

/// Returns a slice containing all the multiple powers of 10 that fit in the integer type `N`.
pub fn pow10array(comptime N: type) []N {
    comptime var multiple_of_ten: N = 1;

    comptime var table_size = comptime digits10(N, @maxValue(N));
    comptime var counter = 0;

    inline while(counter + 1 < table_size): ({counter += 1;}) {
        multiple_of_ten *= 10;
    }

    // generate table
    comptime var table: [table_size] N = undefined;

    inline for(table) |*num| {
        num.* = multiple_of_ten;
        multiple_of_ten /= 10;
    }

    return table[0..];
}

/// Converts a byte-slice into the integer type `N`.
/// if the byte-slice contains a digit that is not valid, an error is returned.
/// An empty slice returns 0.
pub fn atoi(comptime N: type, buf: []const u8) ParseError!N {

    if (comptime is_signed(N)) {
        const nbits = comptime bitcount(N);

        const unsigned_friend = @IntType(false, nbits);

        if (starts_with(buf, '-')) {
            return -@intCast(N, try atoi(unsigned_friend, buf[1..]));
        }
        else {
            return @intCast(N, try atoi(unsigned_friend, buf));
        }
    }

    comptime var table = comptime pow10array(N);
    
    if (buf.len > table.len) {
        return ParseError.Overflow;
    }

    var bytes = buf;
    var result: N = 0;
    var len = buf.len;
    var idx = table.len - len;


    while (len >= 4) {
        comptime var UNROLL_IDX = 0;
        comptime var UNROLL_MAX = 4;

        // unroll
        inline while(UNROLL_IDX < UNROLL_MAX): ({UNROLL_IDX += 1;}) {

            const r1 = bytes[UNROLL_IDX] -% 48;
            if (r1 > 9) {
                return ParseError.InvalidCharacter;
            }
            //@NOTE: 30-10-2018
            // It doesn't matter using a partial_result array,
            // and then updating the result by 4 at a time. The assembly is the same with --release-fast,
            // and this is just easier to read.
            result = result +% r1 * table[idx + UNROLL_IDX];
        }

        len -= 4;
        idx += 4;

        bytes = bytes[4..];
    }

    for (bytes) |byte, offset| {
        const r = byte -% 48;
        if (r > 9) {
            return ParseError.InvalidCharacter;
        }

        const d = r * table[idx + offset];
        result = result +% d;
    }

    return result;
}

fn pow(base: usize, exp: usize) usize {
    var x: usize = base;
    var i: usize = 1;

    while (i < exp) : (i += 1) {
        x *= base;
    }
    return x;
}

pub fn itoa(comptime N: type, n: N, buff: []u8) void {
    comptime var UNROLL_MAX: usize = 4;
    comptime var DIV_CONST: usize = comptime pow(10, UNROLL_MAX);

    var num = n;
    var len = buff.len;

    while(len >= UNROLL_MAX): (num = @divTrunc(num, DIV_CONST)) {
        comptime var DIV10: N = 1;
        comptime var CURRENT: usize = 0;
        
        // Write digits backwards into the buffer
        inline while(CURRENT != UNROLL_MAX): ({CURRENT += 1; DIV10 *= 10;}) {
            var q = @divTrunc(num, DIV10);
            var r = @intCast(u8, @rem(q, 10)) + 48;
            buff[len - CURRENT - 1] = r;
        }

        len -= UNROLL_MAX;
    }

    // On an empty buffer, this will wrapparoo to 0xfffff
    len -%= 1;

    // Stops at 0xfffff
    while(len != @maxValue(usize)): (len -%= 1) {
        var q: N = @divTrunc(num, 10);
        var r: u8 = @intCast(u8, @rem(num, 10)) + 48;
        buff[len] = r;
        num = q;
    }
}
