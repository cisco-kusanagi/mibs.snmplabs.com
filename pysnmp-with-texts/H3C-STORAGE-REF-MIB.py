#
# PySNMP MIB module H3C-STORAGE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-STORAGE-REF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
h3c, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3c")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, ObjectIdentity, Gauge32, Counter64, MibIdentifier, ModuleIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32, IpAddress, iso, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "ObjectIdentity", "Gauge32", "Counter64", "MibIdentifier", "ModuleIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32", "IpAddress", "iso", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cStorageRef = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 10))
if mibBuilder.loadTexts: h3cStorageRef.setLastUpdated('200709141452Z')
if mibBuilder.loadTexts: h3cStorageRef.setOrganization('H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cStorageRef.setContactInfo('Platform Team H3C Technologies Co., Ltd. Hai-Dian District Beijing P.R. China Http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cStorageRef.setDescription('This MIB define the textual convention of storage.')
class H3cStorageCapableState(TextualConvention, Integer32):
    description = "An enumerated value which provides an indication of the capability state of a particular object. The value 'support' means the resource is enable to be managed, and the value 'notsupport' means not"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("support", 1), ("notsupport", 2))

class H3cStorageEnableState(TextualConvention, Integer32):
    description = 'An enumerated value which provides an indication of the ability state of a particular object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class H3cStorageActionType(TextualConvention, Integer32):
    description = 'A control variable used to trigger an operator events, when read, always returns a value of invalid.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

class H3cStorageLedStateType(TextualConvention, Integer32):
    description = "This object identifies the state of storage device's led. The value 'off' means the led is go out. The value 'on' means the led is on. The value 'blink' means the led is blinking."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("on", 2), ("blink", 3))

class H3cStorageOnlineState(TextualConvention, Integer32):
    description = 'An enumerated value means an resource is online or offline.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("online", 1), ("offline", 2))

class H3cLvIDType(TextualConvention, OctetString):
    description = 'A variable used to identifies the GUID(global universal identification) of the logic volume.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

class H3cSessionIDType(TextualConvention, OctetString):
    description = 'A hex string used to identifies the session between targets and initiators.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class H3cWwpnListType(TextualConvention, OctetString):
    description = 'This object describes the format of WWPN(World Wide Port Name) numbers. An WWPN is a 16-byte Hex value. Separate the WWPN by comma if more than one WWPN is specified. e.g. 13af35d2f4ea6fbc,13af35d2f4ea6fad.'
    status = 'current'

class H3cStorageOwnerType(TextualConvention, Integer32):
    description = "An enumerated value used in HA(High Availability) iSCSI target. The value 'spa' means the owner is the first storage processor, and 'spb' means another."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("spa", 1), ("spb", 2), ("none", 3))

class H3cExtendSelectPolicy(TextualConvention, Integer32):
    description = "This object describes how to assign the storage space. The value 'differentAdapter' means select drives from different adapter/channel, system will look for space on another array only if it is on a separate adapter/channel. The value 'differentDrive' means select different drive, system will look for space on another array. The value 'anyDrive' means select any available drive, system will look for space on any array, including the original. The value 'none' means the way to assign the storage space is not specified, in this case the system will allocate the storage with the default criteria in the following order: 1. the storage from different adapter 2. the storage from different drive 3. the storage from any drive"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("differentAdapter", 1), ("differentDrive", 2), ("anyDrive", 3), ("none", 4))

class H3cRaidIDType(TextualConvention, OctetString):
    description = "A string used to identifies the raid's UUID(unique universal identification). e.g. c0a800a8-0000-07f5-0057-386e145eda44."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(36, 71)

class H3cSoftwareInfoString(TextualConvention, OctetString):
    description = 'A string used to identifies the information which software provided. e.g. [TARGET,LVM,DM] or [Both] or [3].'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 64)

mibBuilder.exportSymbols("H3C-STORAGE-REF-MIB", H3cStorageCapableState=H3cStorageCapableState, H3cSessionIDType=H3cSessionIDType, H3cSoftwareInfoString=H3cSoftwareInfoString, H3cLvIDType=H3cLvIDType, H3cWwpnListType=H3cWwpnListType, H3cStorageOnlineState=H3cStorageOnlineState, H3cStorageOwnerType=H3cStorageOwnerType, H3cExtendSelectPolicy=H3cExtendSelectPolicy, H3cStorageLedStateType=H3cStorageLedStateType, h3cStorageRef=h3cStorageRef, H3cRaidIDType=H3cRaidIDType, H3cStorageEnableState=H3cStorageEnableState, H3cStorageActionType=H3cStorageActionType, PYSNMP_MODULE_ID=h3cStorageRef)
