font1_input = [[0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
               [0x04, 0x04, 0x04, 0x04, 0x04, 0x00, 0x04],
               [0x09, 0x09, 0x12, 0x00, 0x00, 0x00, 0x00],
               [0x0a, 0x0a, 0x1f, 0x0a, 0x1f, 0x0a, 0x0a],
               [0x04, 0x0f, 0x14, 0x0e, 0x05, 0x1e, 0x04],
               [0x19, 0x19, 0x02, 0x04, 0x08, 0x13, 0x13],
               [0x04, 0x0a, 0x0a, 0x0a, 0x15, 0x12, 0x0d],
               [0x04, 0x04, 0x08, 0x00, 0x00, 0x00, 0x00],
               [0x02, 0x04, 0x08, 0x08, 0x08, 0x04, 0x02],
               [0x08, 0x04, 0x02, 0x02, 0x02, 0x04, 0x08],
               [0x04, 0x15, 0x0e, 0x1f, 0x0e, 0x15, 0x04],
               [0x00, 0x04, 0x04, 0x1f, 0x04, 0x04, 0x00],
               [0x00, 0x00, 0x00, 0x00, 0x04, 0x04, 0x08],
               [0x00, 0x00, 0x00, 0x1f, 0x00, 0x00, 0x00],
               [0x00, 0x00, 0x00, 0x00, 0x00, 0x0c, 0x0c],
               [0x01, 0x01, 0x02, 0x04, 0x08, 0x10, 0x10],
               [0x0e, 0x11, 0x13, 0x15, 0x19, 0x11, 0x0e],
               [0x04, 0x0c, 0x04, 0x04, 0x04, 0x04, 0x0e],
               [0x0e, 0x11, 0x01, 0x02, 0x04, 0x08, 0x1f],
               [0x0e, 0x11, 0x01, 0x06, 0x01, 0x11, 0x0e],
               [0x02, 0x06, 0x0a, 0x12, 0x1f, 0x02, 0x02],
               [0x1f, 0x10, 0x1e, 0x01, 0x01, 0x11, 0x0e],
               [0x06, 0x08, 0x10, 0x1e, 0x11, 0x11, 0x0e],
               [0x1f, 0x01, 0x02, 0x04, 0x08, 0x08, 0x08],
               [0x0e, 0x11, 0x11, 0x0e, 0x11, 0x11, 0x0e],
               [0x0e, 0x11, 0x11, 0x0f, 0x01, 0x02, 0x0c],
               [0x00, 0x0c, 0x0c, 0x00, 0x0c, 0x0c, 0x00],
               [0x00, 0x0c, 0x0c, 0x00, 0x0c, 0x04, 0x08],
               [0x02, 0x04, 0x08, 0x10, 0x08, 0x04, 0x02],
               [0x00, 0x00, 0x1f, 0x00, 0x1f, 0x00, 0x00],
               [0x08, 0x04, 0x02, 0x01, 0x02, 0x04, 0x08],
               [0x0e, 0x11, 0x01, 0x02, 0x04, 0x00, 0x04]]

font1_output = [0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2a, 0x2b, 0x2c, 0x2d, 0x2e, 0x2f, 0x30,
                0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3a, 0x3b, 0x3c, 0x3d, 0x3e, 0x3f]   # son los asciis

font2_input = [[0x0e, 0x11, 0x17, 0x15, 0x17, 0x10, 0x0f],
               [0x04, 0x0a, 0x11, 0x11, 0x1f, 0x11, 0x11],
               [0x1e, 0x11, 0x11, 0x1e, 0x11, 0x11, 0x1e],
               [0x0e, 0x11, 0x10, 0x10, 0x10, 0x11, 0x0e],
               [0x1e, 0x09, 0x09, 0x09, 0x09, 0x09, 0x1e],
               [0x1f, 0x10, 0x10, 0x1c, 0x10, 0x10, 0x1f],
               [0x1f, 0x10, 0x10, 0x1f, 0x10, 0x10, 0x10],
               [0x0e, 0x11, 0x10, 0x10, 0x13, 0x11, 0x0f],
               [0x11, 0x11, 0x11, 0x1f, 0x11, 0x11, 0x11],
               [0x0e, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0e],
               [0x1f, 0x02, 0x02, 0x02, 0x02, 0x12, 0x0c],
               [0x11, 0x12, 0x14, 0x18, 0x14, 0x12, 0x11],
               [0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1f],
               [0x11, 0x1b, 0x15, 0x11, 0x11, 0x11, 0x11],
               [0x11, 0x11, 0x19, 0x15, 0x13, 0x11, 0x11],
               [0x0e, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0e],
               [0x1e, 0x11, 0x11, 0x1e, 0x10, 0x10, 0x10],
               [0x0e, 0x11, 0x11, 0x11, 0x15, 0x12, 0x0d],
               [0x1e, 0x11, 0x11, 0x1e, 0x14, 0x12, 0x11],
               [0x0e, 0x11, 0x10, 0x0e, 0x01, 0x11, 0x0e],
               [0x1f, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04],
               [0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0e],
               [0x11, 0x11, 0x11, 0x11, 0x11, 0x0a, 0x04],
               [0x11, 0x11, 0x11, 0x15, 0x15, 0x1b, 0x11],
               [0x11, 0x11, 0x0a, 0x04, 0x0a, 0x11, 0x11],
               [0x11, 0x11, 0x0a, 0x04, 0x04, 0x04, 0x04],
               [0x1f, 0x01, 0x02, 0x04, 0x08, 0x10, 0x1f],
               [0x0e, 0x08, 0x08, 0x08, 0x08, 0x08, 0x0e],
               [0x10, 0x10, 0x08, 0x04, 0x02, 0x01, 0x01],
               [0x0e, 0x02, 0x02, 0x02, 0x02, 0x02, 0x0e],
               [0x04, 0x0a, 0x11, 0x00, 0x00, 0x00, 0x00],
               [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1f]]

font2_output = [0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x37, 0x48, 0x49, 0x4a, 0x4b, 0x4c, 0x4d, 0x4e, 0x4f, 0x50,
                0x51, 0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5a, 0x5b, 0x5c, 0x5d, 0x5e, 0x5f]

font3_input = [[0x04, 0x04, 0x02, 0x00, 0x00, 0x00, 0x00],
               [0x00, 0x0e, 0x01, 0x0d, 0x13, 0x13, 0x0d],
               [0x10, 0x10, 0x10, 0x1c, 0x12, 0x12, 0x1c],
               [0x00, 0x00, 0x00, 0x0e, 0x10, 0x10, 0x0e],
               [0x01, 0x01, 0x01, 0x07, 0x09, 0x09, 0x07],
               [0x00, 0x00, 0x0e, 0x11, 0x1f, 0x10, 0x0f],
               [0x06, 0x09, 0x08, 0x1c, 0x08, 0x08, 0x08],
               [0x0e, 0x11, 0x13, 0x0d, 0x01, 0x01, 0x0e],
               [0x10, 0x10, 0x10, 0x16, 0x19, 0x11, 0x11],
               [0x00, 0x04, 0x00, 0x0c, 0x04, 0x04, 0x0e],
               [0x02, 0x00, 0x06, 0x02, 0x02, 0x12, 0x0c],
               [0x10, 0x10, 0x12, 0x14, 0x18, 0x14, 0x12],
               [0x0c, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04],
               [0x00, 0x00, 0x0a, 0x15, 0x15, 0x11, 0x11],
               [0x00, 0x00, 0x16, 0x19, 0x11, 0x11, 0x11],
               [0x00, 0x00, 0x0e, 0x11, 0x11, 0x11, 0x0e],
               [0x00, 0x1c, 0x12, 0x12, 0x1c, 0x10, 0x10],
               [0x00, 0x07, 0x09, 0x09, 0x07, 0x01, 0x01],
               [0x00, 0x00, 0x16, 0x19, 0x10, 0x10, 0x10],
               [0x00, 0x00, 0x0f, 0x10, 0x0e, 0x01, 0x1e],
               [0x08, 0x08, 0x1c, 0x08, 0x08, 0x09, 0x06],
               [0x00, 0x00, 0x11, 0x11, 0x11, 0x13, 0x0d],
               [0x00, 0x00, 0x11, 0x11, 0x11, 0x0a, 0x04],
               [0x00, 0x00, 0x11, 0x11, 0x15, 0x15, 0x0a],
               [0x00, 0x00, 0x11, 0x0a, 0x04, 0x0a, 0x11],
               [0x00, 0x11, 0x11, 0x0f, 0x01, 0x11, 0x0e],
               [0x00, 0x00, 0x1f, 0x02, 0x04, 0x08, 0x1f],
               [0x06, 0x08, 0x08, 0x10, 0x08, 0x08, 0x06],
               [0x04, 0x04, 0x04, 0x00, 0x04, 0x04, 0x04],
               [0x0c, 0x02, 0x02, 0x01, 0x02, 0x02, 0x0c],
               [0x08, 0x15, 0x02, 0x00, 0x00, 0x00, 0x00],
               [0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f, 0x1f]]

font3_output = [0x60, 0x61, 0x62, 0x63, 0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6a, 0x6b, 0x6c, 0x6d, 0x6e, 0x6f, 0x70,
                0x71, 0x72, 0x73, 0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7a, 0x7b, 0x7c, 0x7d, 0x7e, 0x7f]


def get_input():
    return font1_input


def get_output():
    return font1_output
