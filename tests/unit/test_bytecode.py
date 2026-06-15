from simplylang.bytecode import Chunk, OpCode


def test_chunk_records_constants_and_instructions():
    chunk = Chunk()
    constant_index = chunk.add_constant(42)
    chunk.emit(OpCode.CONSTANT, constant_index, line=1)

    assert chunk.constants == [42]
    assert chunk.instructions[0].opcode is OpCode.CONSTANT
    assert chunk.instructions[0].operand == 0
