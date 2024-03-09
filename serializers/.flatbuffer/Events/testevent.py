# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Events

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class testevent(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = testevent()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAstestevent(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # testevent
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # testevent
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # testevent
    def Timestamp(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # testevent
    def Source(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # testevent
    def SerializerFormat(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(4)
def testeventStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def testeventAddName(builder, name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, name)
def AddTimestamp(builder, timestamp): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(timestamp), 0)
def testeventAddTimestamp(builder, timestamp):
    """This method is deprecated. Please switch to AddTimestamp."""
    return AddTimestamp(builder, timestamp)
def AddSource(builder, source): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(source), 0)
def testeventAddSource(builder, source):
    """This method is deprecated. Please switch to AddSource."""
    return AddSource(builder, source)
def AddSerializerFormat(builder, serializerFormat): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(serializerFormat), 0)
def testeventAddSerializerFormat(builder, serializerFormat):
    """This method is deprecated. Please switch to AddSerializerFormat."""
    return AddSerializerFormat(builder, serializerFormat)
def End(builder): return builder.EndObject()
def testeventEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)