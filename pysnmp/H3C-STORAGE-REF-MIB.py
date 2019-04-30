#
# PySNMP MIB module H3C-STORAGE-REF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-STORAGE-REF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:08:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
h3c, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3c")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, MibIdentifier, ModuleIdentity, IpAddress, ObjectIdentity, TimeTicks, Gauge32, Integer32, Bits, Unsigned32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "ModuleIdentity", "IpAddress", "ObjectIdentity", "TimeTicks", "Gauge32", "Integer32", "Bits", "Unsigned32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
h3cStorageRef = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 10))
if mibBuilder.loadTexts: h3cStorageRef.setLastUpdated('200709141452Z')
if mibBuilder.loadTexts: h3cStorageRef.setOrganization('H3C Technologies Co., Ltd.')
class H3cStorageCapableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("support", 1), ("notsupport", 2))

class H3cStorageEnableState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class H3cStorageActionType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("action", 1), ("invalid", 2))

class H3cStorageLedStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("off", 1), ("on", 2), ("blink", 3))

class H3cStorageOnlineState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("online", 1), ("offline", 2))

class H3cLvIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 20)

class H3cSessionIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 16)

class H3cWwpnListType(TextualConvention, OctetString):
    status = 'current'

class H3cStorageOwnerType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("spa", 1), ("spb", 2), ("none", 3))

class H3cExtendSelectPolicy(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("differentAdapter", 1), ("differentDrive", 2), ("anyDrive", 3), ("none", 4))

class H3cRaidIDType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(36, 71)

class H3cSoftwareInfoString(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(2, 64)

mibBuilder.exportSymbols("H3C-STORAGE-REF-MIB", h3cStorageRef=h3cStorageRef, H3cSoftwareInfoString=H3cSoftwareInfoString, H3cSessionIDType=H3cSessionIDType, H3cLvIDType=H3cLvIDType, H3cExtendSelectPolicy=H3cExtendSelectPolicy, H3cStorageOnlineState=H3cStorageOnlineState, H3cRaidIDType=H3cRaidIDType, H3cStorageLedStateType=H3cStorageLedStateType, H3cWwpnListType=H3cWwpnListType, PYSNMP_MODULE_ID=h3cStorageRef, H3cStorageCapableState=H3cStorageCapableState, H3cStorageActionType=H3cStorageActionType, H3cStorageOwnerType=H3cStorageOwnerType, H3cStorageEnableState=H3cStorageEnableState)
