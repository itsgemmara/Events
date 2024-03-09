# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Events

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class testevent2(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = testevent2()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAstestevent2(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # testevent2
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # testevent2
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # testevent2
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # testevent2
    def Source(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # testevent2
    def SerializerFormat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(4)
def testevent2Start(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def testevent2AddName(builder, name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, name)
def AddTimestamp(builder, timestamp): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(timestamp), 0)
def testevent2AddTimestamp(builder, timestamp):
    """This method is deprecated. Please switch to AddTimestamp."""
    return AddTimestamp(builder, timestamp)
def AddSource(builder, source): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(source), 0)
def testevent2AddSource(builder, source):
    """This method is deprecated. Please switch to AddSource."""
    return AddSource(builder, source)
def AddSerializerFormat(builder, serializerFormat): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(serializerFormat), 0)
def testevent2AddSerializerFormat(builder, serializerFormat):
    """This method is deprecated. Please switch to AddSerializerFormat."""
    return AddSerializerFormat(builder, serializerFormat)
def End(builder): return builder.EndObject()
def testevent2End(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)