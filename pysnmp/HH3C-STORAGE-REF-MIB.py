#
# PySNMP MIB module HH3C-STORAGE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HH3C-STORAGE-REF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:13:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
hh3c, = mibBuilder.importSymbols("HH3C-OID-MIB", "hh3c")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Bits, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, ObjectIdentity, MibIdentifier, IpAddress, Counter32, ModuleIdentity, Integer32, TimeTicks, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Bits", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "ObjectIdentity", "MibIdentifier", "IpAddress", "Counter32", "ModuleIdentity", "Integer32", "TimeTicks", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
hh3cStorageRef = ModuleIdentity((1, 3, 6, 1, 4, 1, 25506, 10))
if mibBuilder.loadTexts: hh3cStorageRef.setLastUpdated('200709141452Z')
if mibBuilder.loadTexts: hh3cStorageRef.setOrganization('H3C Technologies Co., Ltd.')
class Hh3cStorageCapableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("support", 1), ("notsupport", 2))

class Hh3cStorageEnableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class Hh3cStorageActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

class Hh3cStorageLedStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("on", 2), ("blink", 3))

class Hh3cStorageOnlineState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("online", 1), ("offline", 2))

class Hh3cLvIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

class Hh3cSessionIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class Hh3cWwpnListType(TextualConvention, OctetString):
    status = 'current'

class Hh3cStorageOwnerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("spa", 1), ("spb", 2), ("none", 3))

class Hh3cExtendSelectPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("differentAdapter", 1), ("differentDrive", 2), ("anyDrive", 3), ("none", 4))

class Hh3cRaidIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(36, 71)

class Hh3cSoftwareInfoString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 64)

mibBuilder.exportSymbols("HH3C-STORAGE-REF-MIB", PYSNMP_MODULE_ID=hh3cStorageRef, Hh3cSessionIDType=Hh3cSessionIDType, Hh3cStorageEnableState=Hh3cStorageEnableState, Hh3cExtendSelectPolicy=Hh3cExtendSelectPolicy, Hh3cStorageActionType=Hh3cStorageActionType, Hh3cWwpnListType=Hh3cWwpnListType, Hh3cRaidIDType=Hh3cRaidIDType, Hh3cLvIDType=Hh3cLvIDType, Hh3cSoftwareInfoString=Hh3cSoftwareInfoString, Hh3cStorageOwnerType=Hh3cStorageOwnerType, hh3cStorageRef=hh3cStorageRef, Hh3cStorageOnlineState=Hh3cStorageOnlineState, Hh3cStorageLedStateType=Hh3cStorageLedStateType, Hh3cStorageCapableState=Hh3cStorageCapableState)
