#
# PySNMP MIB module SYMMINTERFACEEXT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/neermitt/Dev/kusanagi/mibs.snmplabs.com/asn1/SYMMINTERFACEEXT
# Produced by pysmi-0.3.4 at Tue Jul 30 11:35:04 2019
# On host NEERMITT-M-J0NV platform Darwin version 18.6.0 by user neermitt
# Using Python version 3.7.4 (default, Jul  9 2019, 18:13:23) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
entPhysicalIndex, = mibBuilder.importSymbols("ENTITY-MIB", "entPhysicalIndex")
ifNumber, ifEntry, ifIndex = mibBuilder.importSymbols("IF-MIB", "ifNumber", "ifEntry", "ifIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
TimeTicks, Gauge32, Unsigned32, ModuleIdentity, Integer32, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, ObjectIdentity, Bits, NotificationType, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Unsigned32", "ModuleIdentity", "Integer32", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "ObjectIdentity", "Bits", "NotificationType", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
symmInterfaceExtension, = mibBuilder.importSymbols("SYMM-COMMON-SMI", "symmInterfaceExtension")
symmInterfaceExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1))
symmInterfaceExt.setRevisions(('2011-02-24 17:47',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: symmInterfaceExt.setRevisionsDescriptions(('Symmetricom common interface extension MIB',))
if mibBuilder.loadTexts: symmInterfaceExt.setLastUpdated('201107181126Z')
if mibBuilder.loadTexts: symmInterfaceExt.setOrganization('Symmetricom')
if mibBuilder.loadTexts: symmInterfaceExt.setContactInfo('Symmetricom Technical Support 1-888-367-7966 toll free USA 1-408-428-7907 worldwide Support@symmetricom.com')
if mibBuilder.loadTexts: symmInterfaceExt.setDescription("Symmetricom Common interface extension MIB. This extension contains additional information for the interface entry in the public 'SNMP MIB-2 Interfaces.'")
class CLOCKDIRECTION(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("undefined", 0), ("input", 1), ("output", 2), ("both", 3))

class DateAndTime(TextualConvention, OctetString):
    description = "A date-time specification. field octets contents range ----- ------ -------- ----- 1 1-2 year* 0..65536 2 3 month 1..12 3 4 day 1..31 4 5 hour 0..23 5 6 minutes 0..59 6 7 seconds 0..60 (use 60 for leap-second) 7 8 deci-seconds 0..9 8 9 direction from UTC '+' / '-' 9 10 hours from UTC* 0..13 10 11 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - daylight saving time in New Zealand is +13 For example, Tuesday May 26, 1992 at 1:30:15 PM EDT would be displayed as: 1992-5-26,13:30:15.0,-4:0 Note that if only local time is known, then timezone information (fields 8-10) is not present."
    status = 'current'
    displayHint = '2d-1d-1d,1d:1d:1d.1d,1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(11, 11), )
class TLatAndLon(TextualConvention, OctetString):
    description = "antenna latitude and longitude specification. field octets contents range ----- ------ -------- ----- 1 1 +/-180 deg '+' / '-' 2 2 degree 0..180 3 3 minute 0..59 4 4 second 0..59 5 5 second fraction 0..99 +/- dd:mm:ss.ss "
    status = 'current'
    displayHint = '1a1d:1d:1d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class TAntHeight(TextualConvention, OctetString):
    description = "antenna height specification. field octets contents range ----- ------ -------- ----- 1 1 +/- '+' / '-' 2 2-3 meter 0..10000 3 4 meter fraction 0..99 +/- hh.hh "
    status = 'current'
    displayHint = '1a2d.1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class TLocalTimeOffset(TextualConvention, OctetString):
    description = "A local time offset specification. field octets contents range ----- ------ -------- ----- 1 1 direction from UTC '+' / '-' 2 2 hours from UTC* 0..13 3 3 minutes from UTC 0..59 * Notes: - the value of year is in network-byte order - The hours range is 0..13 For example, the -6 local time offset would be displayed as: -6:0 "
    status = 'current'
    displayHint = '1a1d:1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class TSsm(TextualConvention, Integer32):
    description = 'The ssm hex code'
    status = 'current'
    displayHint = 'x'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 255)

interfaceExtTable = MibTable((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1), )
if mibBuilder.loadTexts: interfaceExtTable.setStatus('current')
if mibBuilder.loadTexts: interfaceExtTable.setDescription('Common public interface extension table.')
interfaceExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1), )
ifEntry.registerAugmentions(("SYMMINTERFACEEXT", "interfaceExtEntry"))
interfaceExtEntry.setIndexNames(*ifEntry.getIndexNames())
if mibBuilder.loadTexts: interfaceExtEntry.setStatus('current')
if mibBuilder.loadTexts: interfaceExtEntry.setDescription('The entry of common interface extension table')
interfaceExtType = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceExtType.setStatus('current')
if mibBuilder.loadTexts: interfaceExtType.setDescription('Description about the interface type. Currently supported interface types include: E1, T1, DTI, IP, VLAN, PPS, PPS-TOD, 10M, Ethernet, GPS, and GNSS. ')
interfaceExtLayer = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceExtLayer.setStatus('current')
if mibBuilder.loadTexts: interfaceExtLayer.setDescription('Description of interface layer in protocol stack.')
interfaceExtEntityIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 3), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceExtEntityIndex.setStatus('current')
if mibBuilder.loadTexts: interfaceExtEntityIndex.setDescription('The entity index (module entPhysicalIndex) associated with the current interface. ')
interfaceExtLocalIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: interfaceExtLocalIndex.setStatus('current')
if mibBuilder.loadTexts: interfaceExtLocalIndex.setDescription('The local interface index for reference. ')
interfaceExtSignalDirection = MibTableColumn((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 1, 1, 5), CLOCKDIRECTION()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: interfaceExtSignalDirection.setStatus('current')
if mibBuilder.loadTexts: interfaceExtSignalDirection.setDescription("Interface clock signal direction. It can be input(1), output(2), both(3), or none(4). None means the interface is disabled. Only Ethernet and VLAN interfaces can be 'both.'")
interfaceExtConformance = ObjectIdentity((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2))
if mibBuilder.loadTexts: interfaceExtConformance.setStatus('current')
if mibBuilder.loadTexts: interfaceExtConformance.setDescription('This subtree contains conformance statements for the symmInterfaceExt MIB. ')
interfaceExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 1))
interfaceExtBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 1, 1)).setObjects(("SYMMINTERFACEEXT", "interfaceExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    interfaceExtBasicCompliance = interfaceExtBasicCompliance.setStatus('current')
if mibBuilder.loadTexts: interfaceExtBasicCompliance.setDescription('The compliance statement for SNMP entities which have interface extension.')
interfaceExtUocGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 2))
interfaceExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 6, 1, 2, 2, 1)).setObjects(("SYMMINTERFACEEXT", "interfaceExtType"), ("SYMMINTERFACEEXT", "interfaceExtLayer"), ("SYMMINTERFACEEXT", "interfaceExtEntityIndex"), ("SYMMINTERFACEEXT", "interfaceExtLocalIndex"), ("SYMMINTERFACEEXT", "interfaceExtSignalDirection"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    interfaceExtGroup = interfaceExtGroup.setStatus('current')
if mibBuilder.loadTexts: interfaceExtGroup.setDescription('A collection of objects providing information applicable to interface extension group.')
mibBuilder.exportSymbols("SYMMINTERFACEEXT", TLatAndLon=TLatAndLon, CLOCKDIRECTION=CLOCKDIRECTION, TSsm=TSsm, interfaceExtUocGroups=interfaceExtUocGroups, interfaceExtGroup=interfaceExtGroup, interfaceExtLocalIndex=interfaceExtLocalIndex, interfaceExtBasicCompliance=interfaceExtBasicCompliance, TAntHeight=TAntHeight, interfaceExtLayer=interfaceExtLayer, interfaceExtType=interfaceExtType, interfaceExtEntry=interfaceExtEntry, interfaceExtConformance=interfaceExtConformance, PYSNMP_MODULE_ID=symmInterfaceExt, interfaceExtSignalDirection=interfaceExtSignalDirection, DateAndTime=DateAndTime, TLocalTimeOffset=TLocalTimeOffset, interfaceExtCompliances=interfaceExtCompliances, symmInterfaceExt=symmInterfaceExt, interfaceExtEntityIndex=interfaceExtEntityIndex, interfaceExtTable=interfaceExtTable)
