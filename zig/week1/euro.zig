const std = @import("std");
const builtin = @import("builtin");
const atoi = @import("parse.zig");

const io = std.io;
const File = std.os.File;
const Buffer = std.Buffer;
const mem = std.mem;
const warn = std.debug.warn;

const Value = struct {
    question: []const u8,
    value: f32
};

const QUESTIONS: []const Value = []const Value {
    Value { .question = "Voer het aantal 1 centen in:\n", .value = 0.01     },
    Value { .question = "Voer het aantal 2 centen in: \n", .value = 0.02    },
    Value { .question = "Voer het aantal 5 centen in: \n", .value = 0.05    },
    Value { .question = "Voer het aantal 10 centen in: \n", .value = 0.10   },
    Value { .question = "Voer het aantal 20 centen in: \n", .value = 0.20   },
    Value { .question = "Voer het aantal 50 centen in: \n", .value = 0.50   },
    Value { .question = "Voer het aantal 1 euro's in: \n", .value = 1.00    },
    Value { .question = "Voer het aantal 2 euro's in: \n", .value = 2.00    },
};


pub fn main() !void {
    var da = std.heap.DirectAllocator.init();
    const alloc = &da.allocator;

    errdefer da.deinit();

    const stdout: File = try io.getStdOut();
    defer stdout.close();

    const stdin = try io.getStdIn();
    defer stdin.close();

    var adapter = io.FileInStream.init(stdin);
    var stream = &adapter.stream;
    
    var buf = try Buffer.initSize(alloc, 24);
    defer buf.deinit();

    var ncoins: usize = 0;
    var total_value: f32 = 0.0;

    for(QUESTIONS) |question| {
        try stdout.write(question.question);
        try stream.readUntilDelimiterBuffer(&buf, '\r', 20);

        var slice = buf.toSlice();
        var n = try atoi.atoi(u64, slice[0..slice.len - 1]);

        ncoins += n;
        total_value += @intToFloat(f32, n) * question.value;
    }

    var ndigits = atoi.digits10(usize, ncoins);
    var buffer: [8]u8 = undefined; 

    _ = atoi.itoa(usize, ncoins, buffer[0..ndigits]);

    warn("You entered a total of {} coins\n", buffer[0..ndigits]);
    warn("You entered a total value of {.2}\n", total_value);
}