#
# PySNMP MIB module SYMMINTERFACEEXT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMINTERFACEEXT
# Produced by pysmi-0.3.4 at Tue Jul 30 11:34:24 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifEntry", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Bits, Counter32, iso, NotificationType, ObjectIdentity, Gauge32, ModuleIdentity, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Bits", "Counter32", "iso", "NotificationType", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibIdentifier", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
symmInterfaceExtension, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmInterfaceExtension")
symmInterfaceExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1))
symmInterfaceExt.setRevisions(('2011-02-24 17:47',))
if mibBuilder.loadTexts: symmInterfaceExt.setLastUpdated('201107181126Z')
if mibBuilder.loadTexts: symmInterfaceExt.setOrganization('Symmetricom')
class CLOCKDIRECTION(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("input", 1), ("output", 2), ("both", 3))

class DateAndTime(TextualConvention, OctetString):
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

interfaceExtTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1), )
if mibBuilder.loadTexts: interfaceExtTable.setStatus('current')
interfaceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1), )
ifEntry.registerAugmentions(("SYMMINTERFACEEXT", "interfaceExtEntry"))
interfaceExtEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: interfaceExtEntry.setStatus('current')
interfaceExtType = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceExtType.setStatus('current')
interfaceExtLayer = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceExtLayer.setStatus('current')
interfaceExtEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceExtEntityIndex.setStatus('current')
interfaceExtLocalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceExtLocalIndex.setStatus('current')
interfaceExtSignalDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 5), CLOCKDIRECTION()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceExtSignalDirection.setStatus('current')
interfaceExtConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2))
if mibBuilder.loadTexts: interfaceExtConformance.setStatus('current')
interfaceExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 1))
interfaceExtBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 1, 1)).setObjects(("SYMMINTERFACEEXT", "interfaceExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    interfaceExtBasicCompliance = interfaceExtBasicCompliance.setStatus('current')
interfaceExtUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 2))
interfaceExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 2, 1)).setObjects(("SYMMINTERFACEEXT", "interfaceExtType"), ("SYMMINTERFACEEXT", "interfaceExtLayer"), ("SYMMINTERFACEEXT", "interfaceExtEntityIndex"), ("SYMMINTERFACEEXT", "interfaceExtLocalIndex"), ("SYMMINTERFACEEXT", "interfaceExtSignalDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    interfaceExtGroup = interfaceExtGroup.setStatus('current')
mibBuilder.exportSymbols("SYMMINTERFACEEXT", CLOCKDIRECTION=CLOCKDIRECTION, DateAndTime=DateAndTime, interfaceExtLayer=interfaceExtLayer, interfaceExtCompliances=interfaceExtCompliances, interfaceExtConformance=interfaceExtConformance, interfaceExtLocalIndex=interfaceExtLocalIndex, interfaceExtEntry=interfaceExtEntry, interfaceExtSignalDirection=interfaceExtSignalDirection, TLatAndLon=TLatAndLon, TSsm=TSsm, interfaceExtGroup=interfaceExtGroup, TAntHeight=TAntHeight, interfaceExtTable=interfaceExtTable, PYSNMP_MODULE_ID=symmInterfaceExt, TLocalTimeOffset=TLocalTimeOffset, interfaceExtUocGroups=interfaceExtUocGroups, interfaceExtBasicCompliance=interfaceExtBasicCompliance, interfaceExtEntityIndex=interfaceExtEntityIndex, symmInterfaceExt=symmInterfaceExt, interfaceExtType=interfaceExtType)
