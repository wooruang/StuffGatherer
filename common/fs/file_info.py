import re
import json

class DictParser:
    def toDict(self):
        return todict(self)

class JsonParser(DictParser):
    def toJson(self):
        return json.dumps(self.toDict(), ensure_ascii=False, allow_nan=False)

class Capabilities(JsonParser):
    def __init__(self, canDelete=False, canRename=False, canCopy=False, canEdit=False, canDownload=False, canListChildren=False, canAddChildren=False, canRemoveChildren=False):
        self.canDelete = canDelete
        self.canRename = canRename
        self.canCopy = canCopy
        self.canEdit = canEdit
        self.canDownload = canDownload
        self.canListChildren = canListChildren
        self.canAddChildren = canAddChildren
        self.canRemoveChildren = canRemoveChildren

    @staticmethod
    def RootCapabilities():
        return Capabilities(canListChildren=True, canAddChildren=True, canRemoveChildren=True)

    @staticmethod
    def CommonCapabities():
        return Capabilities(True, True, True, True, True, True, True, True)


class FileInfo(JsonParser):
    def __init__(self):
        self.id = None
        self.name = None
        self.createdTime = None
        self.modifiedTime = None
        self.capabilities = None
        self.type = None
        self.size = None
        self.parentId = None
        self.ancestors = []


def todict(obj, classkey=None):
    if isinstance(obj, dict):
        data = {}
        for (k, v) in obj.items():
            data[k] = todict(v, classkey)
        return data
    elif hasattr(obj, "_ast"):
        return todict(obj._ast())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    elif hasattr(obj, "__dict__"):
        data = dict([(key, todict(value, classkey)) 
            for key, value in obj.__dict__.items() 
            if not callable(value) and not key.startswith('_')])
        if classkey is not None and hasattr(obj, "__class__"):
            data[classkey] = obj.__class__.__name__
        return data
    else:
        return obj


if __name__ == "__main__":

    a = FileInfo()
    a.id = 'abc'
    a.ancestors.append(FileInfo())

    # print(convert_object_to_dict(a))
    print(todict(a))
    print(json.dumps(todict(a)))
    

# {
#     "id":"L01pc2M",
#     "name":"Misc",
#     "createdTime":"2020-10-04T20:13:44.428Z",
#     "modifiedTime":"2020-10-04T20:13:44.428Z",
#     "capabilities":
#         {
#             "canDelete":true,
#             "canRename":true,
#             "canCopy":true,
#             "canEdit":false,
#             "canDownload":false,
#             "canListChildren":true,
#             "canAddChildren":true,
#             "canRemoveChildren":true
#         },
#     "type":"dir",
#     "parentId":"Lw",
#     "ancestors":
#         [
#             {
#                 "id":"Lw",
#                 "name":"Customization area",
#                 "createdTime":"2020-10-20T13:15:30.218Z",
#                 "modifiedTime":"2020-10-20T13:15:30.218Z",
#                 "capabilities":
#                     {
#                         "canDelete":false,
#                         "canRename":false,
#                         "canCopy":false,
#                         "canEdit":false,
#                         "canDownload":false,
#                         "canListChildren":true,
#                         "canAddChildren":true,
#                         "canRemoveChildren":true
#                     },
#                 "type":"dir",
#                 "ancestors":[]
#             }
#         ]
# }